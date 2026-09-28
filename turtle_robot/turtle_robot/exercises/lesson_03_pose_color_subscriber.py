"""위치와 색상을 함께 구독하는 실습입니다."""

import rclpy
from rclpy.node import Node
from turtlesim.msg import Color, Pose  # noqa: F401


class PoseColorSubscriber(Node):
    """위치와 색상을 1초마다 출력합니다."""

    def __init__(self):
        super().__init__('lesson_03_pose_color_subscriber')
        self.pose = None
        self.color = None
        # 실습 1: 위치 메시지 타입을 선택합니다.
        # 설명: 빈칸을 채우고 아래 코드의 주석을 해제하세요.
        # 함께 작성할 코드:
        # self.pose_subscription = self.create_subscription(
        #     ____, '/turtle1/pose', self.on_pose, 10
        # )
        pass
        # 실습 2: 색상 메시지 타입을 선택합니다.
        # 설명: 빈칸을 채우고 아래 코드의 주석을 해제하세요.
        # 함께 작성할 코드:
        # self.color_subscription = self.create_subscription(
        #     ____, '/turtlesim/color_sensor', self.on_color, 10
        # )
        pass
        # 실습 3: 출력 타이머를 만듭니다.
        # 설명: 빈칸을 채우고 아래 코드의 주석을 해제하세요.
        # 함께 작성할 코드:
        # self.timer = self.create_timer(____, ____)
        pass

    def on_pose(self, message):
        """최근 위치를 저장합니다."""
        self.pose = message

    def on_color(self, message):
        """최근 색상을 저장합니다."""
        self.color = message

    def print_values(self):
        """최근 위치와 색상을 출력합니다."""
        if self.pose is None or self.color is None:
            return
        self.get_logger().info(
            f'위치 x={self.pose.x:.2f}, y={self.pose.y:.2f} | '
            f'색상 R={self.color.r}, G={self.color.g}, B={self.color.b}'
        )


def main(args=None):
    """노드를 실행합니다."""
    # 실습을 모두 완성한 뒤 아래 안내 줄을 삭제하세요.
    raise SystemExit('실습 1~3을 완성하고 안내 줄을 삭제하세요.')
    rclpy.init(args=args)
    node = PoseColorSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
