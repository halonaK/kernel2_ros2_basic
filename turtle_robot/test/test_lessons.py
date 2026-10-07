"""학생용 수업 파일과 실행 명령 구성을 검사합니다."""

import importlib
from pathlib import Path
import runpy
from unittest.mock import patch

import pytest


LESSONS = [
    'lesson1_1_pose_subscriber',
    'lesson1_2_color_subscriber',
    'lesson1_3_pose_color_subscriber',
    'lesson1_4_pose_color_velocity_subscriber',
    'lesson2_1_cmd_vel_publisher',
    'lesson2_2_growing_circle',
    'lesson2_3_turtle_cmd_and_pose',
    'lesson2_4_multi_thread',
    'lesson3_1_teleport_client',
    'lesson3_2_spawn_client',
    'lesson3_3_region_pen_client',
    'lesson4_1_cmd_vel_parameters',
]


@pytest.mark.parametrize('module', LESSONS)
def test_starter(module):
    """모든 학생용 파일은 오류 없이 import할 수 있어야 합니다."""
    lesson = importlib.import_module(f'turtle_robot.exercises.{module}')
    source = Path(lesson.__file__).read_text()

    for number in range(1, 4):
        assert f'# 실습 {number}:' in source

    compile(source, str(lesson.__file__), 'exec')
    assert 'raise SystemExit' not in source


def test_console_scripts():
    """학생용 실행 명령이 올바른 모듈로 연결되어야 합니다."""
    root = Path(__file__).resolve().parents[1]
    with patch('setuptools.setup') as setup:
        runpy.run_path(str(root / 'setup.py'))

    actual = setup.call_args.kwargs['entry_points']['console_scripts']
    expected = [
        f'{module} = turtle_robot.exercises.{module}:main'
        for module in LESSONS
    ]

    assert len(actual) == 12
    assert set(actual) == set(expected)

    for entry in actual:
        target = entry.split(' = ')[1].split(':')[0]
        assert callable(importlib.import_module(target).main)
