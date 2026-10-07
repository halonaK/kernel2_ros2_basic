"""시간이 지날수록 커지는 원을 그리는 Publisher 실습입니다."""

from geometry_msgs.msg import Twist  # noqa: F401
import rclpy
from rclpy.node import Node


class GrowingCirclePublisher(Node):
    """원의 반지름을 점차 키우는 노드입니다."""

    def __init__(self):
        super().__init__('lesson2_2_growing_circle')

        # 실습 1: /turtle1/cmd_vel Publisher를 만드세요.
        # self.publisher =

        # 실습 2: 선속도와 각속도를 저장하고 0.1초 Timer를 만드세요.
        # self.linear_speed =
        # self.angular_speed =
        # self.timer =

    def publish_velocity(self):
        """속도를 발행하고 다음 발행에 사용할 선속도를 증가시킵니다."""
        # 실습 3: Twist를 발행한 뒤 linear_speed를 조금 증가시키세요.
        pass


def main(args=None):
    """노드를 실행합니다."""
    rclpy.init(args=args)
    node = GrowingCirclePublisher()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
