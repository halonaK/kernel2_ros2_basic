"""turtlesim과 직진 속도 Publisher를 함께 실행합니다."""

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    """수업용 두 노드를 반환합니다."""
    turtlesim_node = Node(
        package='turtlesim',
        executable='turtlesim_node',
        name='turtlesim',
        output='screen',
    )
    cmd_vel_node = Node(
        package='turtle_robot',
        executable='lesson2_1_cmd_vel_publisher_solution',
        name='lesson2_1_cmd_vel_publisher',
        output='screen',
    )

    return LaunchDescription([
        turtlesim_node,
        cmd_vel_node,
    ])
