"""ROS 그래프 없이 수업 구성과 순수 로직을 검사합니다."""

import importlib
from pathlib import Path
import runpy
from types import SimpleNamespace
from unittest.mock import Mock, patch

import pytest

from turtle_robot.solutions.lesson_08_region_pen_client import color_for_region
from turtle_robot.solutions.lesson_08_region_pen_client import region_for_x
from turtle_robot.solutions.lesson_08_region_pen_client import RegionPenClient
from turtle_robot.solutions.lesson_12_distance_guard import distance_between
from turtle_robot.solutions.lesson_12_distance_guard import DistanceGuard
from turtle_robot.solutions.lesson_12_distance_guard import should_stop


LESSONS = [
    'pose_subscriber', 'color_subscriber', 'pose_color_subscriber',
    'pose_color_velocity_subscriber', 'cmd_vel_publisher', 'turtle_cmd_and_pose',
    'multi_thread', 'region_pen_client', 'teleport_client', 'spawn_client',
    'named_turtle_controller', 'distance_guard',
]
MODULES = [f'lesson_{i:02d}_{name}' for i, name in enumerate(LESSONS, 1)]


@pytest.mark.parametrize('module', MODULES)
def test_solution_import(module):
    """모든 완성 예제에 실행 함수가 있어야 합니다."""
    assert callable(importlib.import_module(f'turtle_robot.solutions.{module}').main)


@pytest.mark.parametrize('module', MODULES)
def test_starter(module):
    """미완성 실습은 한국어 안내로 종료하고 문법이 유효해야 합니다."""
    lesson = importlib.import_module(f'turtle_robot.exercises.{module}')
    source = Path(lesson.__file__).read_text()
    for number in range(1, 4):
        assert f'# 실습 {number}:' in source
    with pytest.raises(SystemExit, match='실습 1~3'):
        lesson.main()


def test_console_scripts():
    """24개 명령이 올바른 모듈로 연결되어야 합니다."""
    root = Path(__file__).resolve().parents[1]
    with patch('setuptools.setup') as setup:
        runpy.run_path(str(root / 'setup.py'))
    actual = setup.call_args.kwargs['entry_points']['console_scripts']
    expected = []
    for module in MODULES:
        expected.append(f'{module} = turtle_robot.exercises.{module}:main')
        expected.append(f'{module}_solution = turtle_robot.solutions.{module}:main')
    assert len(actual) == 24
    assert set(actual) == set(expected)
    for entry in actual:
        target = entry.split(' = ')[1].split(':')[0]
        assert callable(importlib.import_module(target).main)


@pytest.mark.parametrize('first,second,expected', [
    ((0, 0), (3, 4), 5), ((3, 4), (0, 0), 5),
    ((-1, -2), (-1, -2), 0), ((-3, -4), (0, 0), 5),
])
def test_distance(first, second, expected):
    """거리는 방향과 관계없이 음수가 아니어야 합니다."""
    a = SimpleNamespace(x=first[0], y=first[1])
    b = SimpleNamespace(x=second[0], y=second[1])
    assert distance_between(a, b) == pytest.approx(expected)


@pytest.mark.parametrize('x,color', [
    (0.0, (255, 255, 0)), (5.499, (255, 255, 0)),
    (5.5, (0, 255, 0)), (11.0, (0, 255, 0)),
])
def test_pen_color(x, color):
    """중앙 경계를 기준으로 노랑과 초록을 선택합니다."""
    assert color_for_region(region_for_x(x)) == color


@pytest.mark.parametrize('distance,expected', [(1.99, True), (2.0, False), (2.01, False)])
def test_stop_boundary(distance, expected):
    """안전거리 미만에서만 정지합니다."""
    assert should_stop(distance, 2.0) is expected


def test_pen_requests_only_on_region_change():
    """같은 영역과 대기 중에는 중복 요청을 보내지 않습니다."""
    node = SimpleNamespace(
        current_region=None, pending_region=None, pending_request=None,
        client=Mock(), on_result=Mock(), get_logger=Mock(),
    )
    node.client.service_is_ready.return_value = True
    RegionPenClient.on_pose(node, SimpleNamespace(x=1.0))
    node.client.call_async.assert_called_once()
    request = node.client.call_async.call_args.args[0]
    assert (request.r, request.g, request.b) == (255, 255, 0)
    RegionPenClient.on_pose(node, SimpleNamespace(x=8.0))
    node.client.call_async.assert_called_once()
    RegionPenClient.on_result(node, node.pending_request)
    RegionPenClient.on_pose(node, SimpleNamespace(x=1.0))
    node.client.call_async.assert_called_once()
    RegionPenClient.on_pose(node, SimpleNamespace(x=8.0))
    assert node.client.call_async.call_count == 2
    request = node.client.call_async.call_args.args[0]
    assert (request.r, request.g, request.b) == (0, 255, 0)


def test_guard_stops_and_resumes():
    """가까워지면 멈추고 안전해지면 이동 명령을 다시 보냅니다."""
    node = SimpleNamespace(
        turtle1_pose=SimpleNamespace(x=0.0, y=0.0),
        turtle2_pose=SimpleNamespace(x=1.0, y=0.0),
        safe_distance=2.0, was_stopped=None,
        turn_speed=0.4, next_turn_change=float('inf'),
        publisher=Mock(), get_logger=Mock(),
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
