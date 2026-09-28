"""10 Hz로 전진 속도를 발행하는 완성 예제입니다."""

from geometry_msgs.msg import Twist
import rclpy
from rclpy.node import Node


class CmdVelPublisher(Node):
    """거북이를 직진시키는 속도 발행자입니다."""

    def __init__(self):
        super().__init__('lesson_05_cmd_vel_publisher')
        # 실습 1: 속도 메시지 타입을 선택합니다.
        # 설명: 아래는 완성된 코드입니다.
        # 함께 작성할 코드:
        self.publisher = self.create_publisher(
            Twist, '/turtle1/cmd_vel', 10
        )
        # 실습 2: 10 Hz 타이머를 만듭니다.
        # 설명: 아래는 완성된 코드입니다.
        # 함께 작성할 코드:
        self.timer = self.create_timer(0.1, self.publish_velocity)

    def publish_velocity(self):
        """전진 속도를 발행합니다."""
        message = Twist()
        # 실습 3: 전진 속도를 설정합니다.
        # 설명: 아래는 완성된 코드입니다.
        # 함께 작성할 코드:
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
        if rclpy.ok():
            node.publisher.publish(Twist())
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
