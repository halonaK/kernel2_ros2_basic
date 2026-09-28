"""거북이 위치 토픽을 구독하는 완성 예제입니다."""

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose


class PoseSubscriber(Node):
    """거북이 위치를 출력합니다."""

    def __init__(self):
        super().__init__('lesson_01_pose_subscriber')
        # 실습 1: 메시지 타입과 토픽 이름을 선택합니다.
        # 설명: 구독자를 생성합니다.
        # 함께 작성할 코드:
        self.subscription = self.create_subscription(
            Pose, '/turtle1/pose', self.on_pose, 10
        )

    def on_pose(self, message):
        """새 위치를 출력합니다."""
        # 실습 2: 메시지의 값을 출력합니다.
        # 설명: 받은 필드를 로그로 출력합니다.
        # 함께 작성할 코드:
        self.get_logger().info(
            f'위치 x={message.x:.2f}, y={message.y:.2f}, '
            f'방향={message.theta:.2f}'
        )


def main(args=None):
    """노드를 실행합니다."""
    rclpy.init(args=args)
    node = PoseSubscriber()
    try:
        # 실습 3: 콜백을 계속 처리합니다.
        # 설명: 일반 실행 함수에 노드를 전달합니다.
        # 함께 작성할 코드:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
