"""이동 속도를 Parameter로 설정하는 Publisher 실습입니다."""

from geometry_msgs.msg import Twist  # noqa: F401
import rclpy
from rclpy.node import Node


class CmdVelParameterPublisher(Node):
    """Parameter 값을 사용해 거북이 속도를 발행하는 노드입니다."""

    def __init__(self):
        super().__init__('lesson4_1_cmd_vel_parameters')

        # 실습 1: linear_speed와 angular_speed Parameter를 선언하세요.

        # 실습 2: /turtle1/cmd_vel Publisher와 0.1초 Timer를 만드세요.
        # self.publisher =
        # self.timer =

    def publish_velocity(self):
        """현재 Parameter 값으로 속도를 발행합니다."""
        # 실습 3: 두 Parameter를 읽어 Twist 메시지로 발행하세요.
        pass


def main(args=None):
    """노드를 실행합니다."""
    rclpy.init(args=args)
    node = CmdVelParameterPublisher()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
