"""점점 커지는 원을 그리는 확장 예제입니다."""

from geometry_msgs.msg import Twist
import rclpy
from rclpy.node import Node


class GrowingCirclePublisher(Node):
    """전진 속도를 증가시켜 원의 반지름을 키웁니다."""

    def __init__(self):
        super().__init__('lesson2_2_growing_circle')
        self.publisher = self.create_publisher(
            Twist, '/turtle1/cmd_vel', 10
        )
        self.linear_speed = 0.2
        self.angular_speed = 1.0
        self.timer = self.create_timer(0.1, self.publish_velocity)

    def publish_velocity(self):
        """회전 속도는 유지하고 전진 속도를 증가시킵니다."""
        message = Twist()
        message.linear.x = self.linear_speed
        message.angular.z = self.angular_speed
        self.publisher.publish(message)
        self.linear_speed += 0.002


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
