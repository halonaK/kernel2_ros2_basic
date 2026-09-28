"""거북이 위치 토픽을 구독하는 실습입니다."""

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose  # noqa: F401


class PoseSubscriber(Node):
    """거북이 위치를 출력합니다."""

    def __init__(self):
        super().__init__('lesson_01_pose_subscriber')
        # 실습 1: 메시지 타입과 토픽 이름을 선택합니다.
        # 설명: 수업의 메시지를 받는 구독자를 만드세요.
        # 함께 작성할 코드:
        # self.subscription = self.create_subscription(
        #     ____, '____', self.on_pose, 10
        # )
        pass

    def on_pose(self, message):
        """새 위치를 출력합니다."""
        # 실습 2: 메시지의 값을 출력합니다.
        # 설명: 받은 메시지에서 x, y, theta 필드를 읽으세요.
        # 함께 작성할 코드:
        # self.get_logger().info(f'수신값: {____}')
        pass


def main(args=None):
    """노드를 실행합니다."""
    # 실습을 모두 완성한 뒤 아래 안내 줄을 삭제하세요.
    raise SystemExit('실습 1~3을 완성하고 안내 줄을 삭제하세요.')
    rclpy.init(args=args)
    node = PoseSubscriber()
    try:
        # 실습 3: 콜백을 계속 처리합니다.
        # 설명: 일반 실행 함수에 노드를 전달하세요.
        # 함께 작성할 코드:
        # rclpy.____(node)
        pass
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
