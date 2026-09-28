"""두 노드를 MultiThreadedExecutor로 실행하는 예제입니다."""

from geometry_msgs.msg import Twist
import rclpy
from rclpy.executors import MultiThreadedExecutor

from turtle_robot.solutions.lesson_01_pose_subscriber import PoseSubscriber
from turtle_robot.solutions.lesson_05_cmd_vel_publisher import CmdVelPublisher


def main(args=None):
    """두 노드를 멀티스레드 실행기로 실행합니다."""
    rclpy.init(args=args)
    publisher = CmdVelPublisher()
    subscriber = PoseSubscriber()
    # 실습 1: 멀티스레드 실행기를 만듭니다.
    # 설명: 아래는 완성된 코드입니다.
    # 함께 작성할 코드:
    executor = MultiThreadedExecutor(num_threads=2)
    # 실습 2: 발행 노드를 추가합니다.
    # 설명: 아래는 완성된 코드입니다.
    # 함께 작성할 코드:
    executor.add_node(publisher)
    executor.add_node(subscriber)
    try:
        # 실습 3: 실행기를 실행합니다.
        # 설명: 아래는 완성된 코드입니다.
        # 함께 작성할 코드:
        executor.spin()
    except KeyboardInterrupt:
        pass
    finally:
        if rclpy.ok():
            publisher.publisher.publish(Twist())
        executor.shutdown()
        publisher.destroy_node()
        subscriber.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
