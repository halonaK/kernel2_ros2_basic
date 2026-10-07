"""turtlesim과 키보드 조종 노드를 함께 실행합니다."""

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
    teleop_node = Node(
        package='turtlesim',
        executable='turtle_teleop_key',
        name='teleop_turtle',
        prefix='gnome-terminal --wait --',
        output='screen',
    )

    return LaunchDescription([
        turtlesim_node,
        teleop_node,
    ])
