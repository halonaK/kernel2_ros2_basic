"""상대 토픽 이름을 사용하는 거북이 제어 예제입니다."""

from geometry_msgs.msg import Twist
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose


class NamedTurtleController(Node):
    """namespace 아래의 pose와 cmd_vel을 사용합니다."""

    def __init__(self):
        super().__init__('lesson_11_named_turtle_controller')
        # 실습 1: 상대 발행 토픽 이름을 채웁니다.
        # 설명: 아래는 완성된 코드입니다.
        # 함께 작성할 코드:
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        # 실습 2: 상대 구독 토픽 이름을 채웁니다.
        # 설명: 아래는 완성된 코드입니다.
        # 함께 작성할 코드:
        self.subscription = self.create_subscription(
            Pose, 'pose', self.on_pose, 10
        )
        # 실습 3: 속도 타이머를 만듭니다.
        # 설명: 아래는 완성된 코드입니다.
        # 함께 작성할 코드:
        self.timer = self.create_timer(0.1, self.publish_velocity)

    def publish_velocity(self):
        """현재 namespace의 거북이를 전진시킵니다."""
        message = Twist()
        message.linear.x = 1.0
        self.publisher.publish(message)

    def on_pose(self, message):
        """현재 거북이 위치를 출력합니다."""
        self.get_logger().info(
            f'위치 x={message.x:.2f}, y={message.y:.2f}'
        )


def main(args=None):
    """노드를 실행합니다."""
    rclpy.init(args=args)
    node = NamedTurtleController()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        if rclpy.ok():
            node.publisher.publish(Twist())
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
