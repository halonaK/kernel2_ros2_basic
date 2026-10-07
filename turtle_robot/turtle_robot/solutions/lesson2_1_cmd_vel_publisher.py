"""10 Hz로 전진 속도를 발행하는 완성 예제입니다."""

from geometry_msgs.msg import Twist
import rclpy
from rclpy.node import Node


class CmdVelPublisher(Node):
    """거북이를 직진시키는 속도 발행자입니다."""

    def __init__(self):
        super().__init__('lesson2_1_cmd_vel_publisher')
        self.publisher = self.create_publisher(
            Twist, '/turtle1/cmd_vel', 10
        )
        self.timer = self.create_timer(0.1, self.publish_velocity)

    def publish_velocity(self):
        """전진 속도를 발행합니다."""
        message = Twist()
        message.linear.x = 1.0
        self.publisher.publish(message)


def main(args=None):
    """노드를 실행합니다."""
    rclpy.init(args=args)
    node = CmdVelPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
