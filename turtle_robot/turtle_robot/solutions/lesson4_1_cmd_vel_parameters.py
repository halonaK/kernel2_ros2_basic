"""Parameter로 거북이의 선속도와 각속도를 설정하는 예제입니다."""

from geometry_msgs.msg import Twist
import rclpy
from rclpy.node import Node


class CmdVelParameterPublisher(Node):
    """현재 Parameter 값을 사용해 속도를 발행합니다."""

    def __init__(self):
        super().__init__('lesson4_1_cmd_vel_parameters')
        self.declare_parameter('linear_speed', 1.0)
        self.declare_parameter('angular_speed', 0.0)
        self.publisher = self.create_publisher(
            Twist, '/turtle1/cmd_vel', 10
        )
        self.timer = self.create_timer(0.1, self.publish_velocity)

    def publish_velocity(self):
        """현재 설정된 속도를 읽어 발행합니다."""
        message = Twist()
        message.linear.x = self.get_parameter('linear_speed').value
        message.angular.z = self.get_parameter('angular_speed').value
        self.publisher.publish(message)


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
