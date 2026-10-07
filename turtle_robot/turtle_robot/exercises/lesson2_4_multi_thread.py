"""기존 Publisher와 Subscriber를 함께 실행하는 실습입니다."""

import rclpy
from rclpy.executors import MultiThreadedExecutor  # noqa: F401

from turtle_robot.exercises.lesson1_1_pose_subscriber import PoseSubscriber
from turtle_robot.exercises.lesson2_1_cmd_vel_publisher import CmdVelPublisher


def main(args=None):
    """두 노드를 MultiThreadedExecutor로 실행합니다."""
    rclpy.init(args=args)

    # 실습 1: CmdVelPublisher와 PoseSubscriber 객체를 만드세요.
    # publisher =
    # subscriber =

    # 실습 2: 스레드가 2개인 MultiThreadedExecutor를 만드세요.
    # executor =

    # 실습 3: 두 노드를 executor에 추가하고 실행하세요.
    pass

    rclpy.try_shutdown()


if __name__ == '__main__':
    main()
