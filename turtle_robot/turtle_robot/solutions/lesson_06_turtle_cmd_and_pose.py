"""속도 발행과 위치 구독을 한 노드에서 수행하는 예제입니다."""

from geometry_msgs.msg import Twist
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose


class TurtleCmdAndPose(Node):
    """전진 명령을 보내고 위치를 출력합니다."""

    def __init__(self):
        super().__init__('lesson_06_turtle_cmd_and_pose')
        # 실습 1: 발행 메시지 타입을 선택합니다.
        # 설명: 아래는 완성된 코드입니다.
        # 함께 작성할 코드:
        self.publisher = self.create_publisher(
            Twist, '/turtle1/cmd_vel', 10
        )
        # 실습 2: 구독 메시지 타입을 선택합니다.
        # 설명: 아래는 완성된 코드입니다.
        # 함께 작성할 코드:
        self.subscription = self.create_subscription(
            Pose, '/turtle1/pose', self.on_pose, 10
        )
        # 실습 3: 속도 타이머를 만듭니다.
        # 설명: 아래는 완성된 코드입니다.
        # 함께 작성할 코드:
        self.timer = self.create_timer(0.1, self.publish_velocity)

    def publish_velocity(self):
        """전진 속도를 발행합니다."""
        message = Twist()
        message.linear.x = 1.0
        self.publisher.publish(message)

    def on_pose(self, message):
        """위치를 출력합니다."""
        self.get_logger().info(
            f'위치 x={message.x:.2f}, y={message.y:.2f}'
        )


def main(args=None):
    """노드를 실행합니다."""
    rclpy.init(args=args)
    node = TurtleCmdAndPose()
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
