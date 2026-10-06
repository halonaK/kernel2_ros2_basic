"""ROS 그래프 없이 수업 구성과 순수 로직을 검사합니다."""

import importlib
from pathlib import Path
import runpy
from types import SimpleNamespace
from unittest.mock import Mock, patch

import pytest

from turtle_robot.solutions.lesson_06_turtle_cmd_and_pose import (
    is_near_wall,
)
from turtle_robot.solutions.lesson_10_region_pen_client import (
    color_for_region,
    region_for_x,
    RegionPenClient,
)
from turtle_robot.solutions.lesson_12_distance_guard import (
    distance_between,
    DistanceGuard,
    should_stop,
)


EXERCISE_LESSONS = [
    'lesson_01_pose_subscriber',
    'lesson_02_color_subscriber',
    'lesson_03_pose_color_subscriber',
    'lesson_04_pose_color_velocity_subscriber',
    'lesson_05_cmd_vel_publisher',
    'lesson_06_turtle_cmd_and_pose',
    'lesson_07_multi_thread',
    'lesson_08_region_pen_client',
    'lesson_09_teleport_client',
    'lesson_10_spawn_client',
    'lesson_11_named_turtle_controller',
    'lesson_12_distance_guard',
]

SOLUTION_LESSONS = [
    'lesson_01_pose_subscriber',
    'lesson_02_color_subscriber',
    'lesson_03_pose_color_subscriber',
    'lesson_04_pose_color_velocity_subscriber',
    'lesson_05_cmd_vel_publisher',
    'lesson_05_growing_circle',
    'lesson_06_turtle_cmd_and_pose',
    'lesson_07_multi_thread',
    'lesson_08_teleport_client',
    'lesson_09_spawn_client',
    'lesson_10_region_pen_client',
    'lesson_11_named_turtle_controller',
    'lesson_12_distance_guard',
]


@pytest.mark.parametrize('module', SOLUTION_LESSONS)
def test_solution_import(module):
    """모든 완성 예제에 실행 함수가 있어야 합니다."""
    target = f'turtle_robot.solutions.{module}'
    assert callable(importlib.import_module(target).main)


@pytest.mark.parametrize('module', EXERCISE_LESSONS)
def test_starter(module):
    """미완성 실습은 한국어 안내로 종료하고 문법이 유효해야 합니다."""
    lesson = importlib.import_module(f'turtle_robot.exercises.{module}')
    source = Path(lesson.__file__).read_text()
    for number in range(1, 4):
        assert f'# 실습 {number}:' in source
    with pytest.raises(SystemExit, match='실습 1~3'):
        lesson.main()


def test_console_scripts():
    """학생용과 완성용 실행 명령이 올바른 모듈로 연결되어야 합니다."""
    root = Path(__file__).resolve().parents[1]
    with patch('setuptools.setup') as setup:
        runpy.run_path(str(root / 'setup.py'))

    actual = setup.call_args.kwargs['entry_points']['console_scripts']
    expected = [
        f'{module} = turtle_robot.exercises.{module}:main'
        for module in EXERCISE_LESSONS
    ] + [
        f'{module}_solution = turtle_robot.solutions.{module}:main'
        for module in SOLUTION_LESSONS
    ]

    assert len(actual) == 25
    assert set(actual) == set(expected)

    for entry in actual:
        target = entry.split(' = ')[1].split(':')[0]
        assert callable(importlib.import_module(target).main)


@pytest.mark.parametrize('x,y,expected', [
    (0.9, 5.0, True),
    (10.1, 5.0, True),
    (5.0, 0.9, True),
    (5.0, 10.1, True),
    (5.0, 5.0, False),
])
def test_wall_boundary(x, y, expected):
    """화면 가장자리에서는 회전해야 합니다."""
    pose = SimpleNamespace(x=x, y=y)
    assert is_near_wall(pose) is expected


@pytest.mark.parametrize('first,second,expected', [
    ((0, 0), (3, 4), 5),
    ((3, 4), (0, 0), 5),
    ((-1, -2), (-1, -2), 0),
    ((-3, -4), (0, 0), 5),
])
def test_distance(first, second, expected):
    """거리는 방향과 관계없이 음수가 아니어야 합니다."""
    first_pose = SimpleNamespace(x=first[0], y=first[1])
    second_pose = SimpleNamespace(x=second[0], y=second[1])
    assert distance_between(first_pose, second_pose) == pytest.approx(expected)


@pytest.mark.parametrize('x,color', [
    (0.0, (255, 255, 0)),
    (5.499, (255, 255, 0)),
    (5.5, (0, 255, 0)),
    (11.0, (0, 255, 0)),
])
def test_pen_color(x, color):
    """중앙 경계를 기준으로 노랑과 초록을 선택합니다."""
    assert color_for_region(region_for_x(x)) == color


def test_pen_requests_only_on_region_change():
    """영역이 바뀔 때만 펜 색상 요청을 보냅니다."""
    node = SimpleNamespace(
        current_region=None,
        client=Mock(),
        get_logger=Mock(),
    )
    node.client.service_is_ready.return_value = True

    RegionPenClient.on_pose(node, SimpleNamespace(x=1.0))
    node.client.call_async.assert_called_once()

    RegionPenClient.on_pose(node, SimpleNamespace(x=2.0))
    node.client.call_async.assert_called_once()

    RegionPenClient.on_pose(node, SimpleNamespace(x=8.0))
    assert node.client.call_async.call_count == 2


@pytest.mark.parametrize(
    'distance,expected',
    [(1.99, True), (2.0, False), (2.01, False)],
)
def test_stop_boundary(distance, expected):
    """안전거리 미만에서만 정지합니다."""
    assert should_stop(distance) is expected


def test_guard_stops_and_resumes():
    """가까워지면 멈추고 안전해지면 이동 명령을 다시 보냅니다."""
    node = SimpleNamespace(
        turtle1_pose=SimpleNamespace(x=0.0, y=0.0),
        turtle2_pose=SimpleNamespace(x=1.0, y=0.0),
        safe_distance=2.0,
        was_stopped=None,
        turn_speed=0.4,
        next_turn_change=float('inf'),
        publisher=Mock(),
        get_logger=Mock(),
    )

    DistanceGuard.control_turtle2(node)
    message = node.publisher.publish.call_args.args[0]
    assert message.linear.x == 0.0
    assert message.angular.z == 0.0

    node.turtle2_pose.x = 3.0
    DistanceGuard.control_turtle2(node)
    message = node.publisher.publish.call_args.args[0]
    assert message.linear.x > 0.0
    assert message.angular.z == 0.4
