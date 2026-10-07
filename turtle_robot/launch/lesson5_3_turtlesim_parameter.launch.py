"""turtlesim과 YAML Parameter Publisher를 함께 실행합니다."""

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    """YAML 설정을 사용하는 두 노드를 반환합니다."""
    config_file = os.path.join(
        get_package_share_directory('turtle_robot'),
        'config',
        'cmd_vel.yaml',
    )
    turtlesim_node = Node(
        package='turtlesim',
        executable='turtlesim_node',
        name='turtlesim',
        output='screen',
    )
    parameter_node = Node(
        package='turtle_robot',
        executable='lesson4_1_cmd_vel_parameters_solution',
        name='lesson4_1_cmd_vel_parameters',
        parameters=[config_file],
        output='screen',
    )

    return LaunchDescription([
        turtlesim_node,
        parameter_node,
    ])
