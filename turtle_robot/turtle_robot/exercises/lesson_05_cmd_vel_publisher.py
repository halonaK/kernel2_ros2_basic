"""10 Hz로 전진 속도를 발행하는 실습입니다."""

from geometry_msgs.msg import Twist
import rclpy
from rclpy.node import Node


class CmdVelPublisher(Node):
    """거북이를 직진시키는 속도 발행자입니다."""

    def __init__(self):
        super().__init__('lesson_05_cmd_vel_publisher')
        # 실습 1: 속도 메시지 타입을 선택합니다.
        # 설명: 빈칸을 채우고 아래 코드의 주석을 해제하세요.
        # 함께 작성할 코드:
        # self.publisher = self.create_publisher(
        #     ____, '/turtle1/cmd_vel', 10
        # )
        pass
        # 실습 2: 10 Hz 타이머를 만듭니다.
        # 설명: 빈칸을 채우고 아래 코드의 주석을 해제하세요.
        # 함께 작성할 코드:
        # self.timer = self.create_timer(____, ____)
        pass

    # 확장: 전진과 회전을 함께 설정하여 완전한 원을 그려 보세요.
    # 한 바퀴 시간은 2π / |각속도|이며 자세한 조건은 docs/lessons.md를 보세요.

    def publish_velocity(self):
        """전진 속도를 발행합니다."""
        message = Twist()
        # 실습 3: 전진 속도를 설정합니다.
        # 설명: 빈칸을 채우고 아래 코드의 주석을 해제하세요.
        # 함께 작성할 코드:
        # message.linear.x = ____
        pass
        self.publisher.publish(message)


def main(args=None):
    """노드를 실행합니다."""
    # 실습을 모두 완성한 뒤 아래 안내 줄을 삭제하세요.
    raise SystemExit('실습 1~3을 완성하고 안내 줄을 삭제하세요.')
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
