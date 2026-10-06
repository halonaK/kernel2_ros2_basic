"""두 노드를 MultiThreadedExecutor로 실행하는 예제입니다."""

import rclpy
from rclpy.executors import MultiThreadedExecutor

from turtle_robot.solutions.lesson_01_pose_subscriber import PoseSubscriber
from turtle_robot.solutions.lesson_05_cmd_vel_publisher import CmdVelPublisher


def main(args=None):
    """두 노드를 멀티스레드 실행기로 실행합니다."""
    rclpy.init(args=args)
    publisher = CmdVelPublisher()
    subscriber = PoseSubscriber()
    executor = MultiThreadedExecutor(num_threads=2)
    executor.add_node(publisher)
    executor.add_node(subscriber)
    try:
        executor.spin()
    except KeyboardInterrupt:
        pass
    finally:
        executor.shutdown()
        publisher.destroy_node()
        subscriber.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
