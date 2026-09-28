"""두 노드를 MultiThreadedExecutor로 실행하는 예제입니다."""

from geometry_msgs.msg import Twist
import rclpy
from rclpy.executors import MultiThreadedExecutor  # noqa: F401

from turtle_robot.solutions.lesson_01_pose_subscriber import PoseSubscriber
from turtle_robot.solutions.lesson_05_cmd_vel_publisher import CmdVelPublisher


def main(args=None):
    """두 노드를 멀티스레드 실행기로 실행합니다."""
    # 실습을 모두 완성한 뒤 아래 안내 줄을 삭제하세요.
    raise SystemExit('실습 1~3을 완성하고 안내 줄을 삭제하세요.')
    rclpy.init(args=args)
    publisher = CmdVelPublisher()
    subscriber = PoseSubscriber()
    executor = None
    # 실습 1: 멀티스레드 실행기를 만듭니다.
    # 설명: 빈칸을 채우고 아래 코드의 주석을 해제하세요.
    # 함께 작성할 코드:
    # executor = ____(num_threads=2)
    pass
    # 실습 2: 발행 노드를 추가합니다.
    # 설명: 빈칸을 채우고 아래 코드의 주석을 해제하세요.
    # 함께 작성할 코드:
    # executor.add_node(____)
    pass
    executor.add_node(subscriber)
    try:
        # 실습 3: 실행기를 실행합니다.
        # 설명: 빈칸을 채우고 아래 코드의 주석을 해제하세요.
        # 함께 작성할 코드:
        # ____.spin()
        pass
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
