"""중앙 경계에서 펜 색상을 바꾸는 서비스 클라이언트입니다."""

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from turtlesim.srv import SetPen


def region_for_x(x):
    """가로 좌표를 왼쪽 또는 오른쪽 영역으로 바꿉니다."""
    return 'left' if x < 5.5 else 'right'


def color_for_region(region):
    """영역에 맞는 RGB 색상을 반환합니다."""
    return (255, 255, 0) if region == 'left' else (0, 255, 0)


class RegionPenClient(Node):
    """영역이 바뀔 때만 SetPen 서비스를 호출합니다."""

    def __init__(self):
        super().__init__('lesson_08_region_pen_client')
        # 실습 1: 펜 서비스 클라이언트를 만듭니다.
        # 설명: 아래는 완성된 코드입니다.
        # 함께 작성할 코드:
        self.client = self.create_client(SetPen, '/turtle1/set_pen')
        # 실습 2: 위치를 구독합니다.
        # 설명: 아래는 완성된 코드입니다.
        # 함께 작성할 코드:
        self.subscription = self.create_subscription(
            Pose, '/turtle1/pose', self.on_pose, 10
        )
        self.current_region = None
        self.pending_region = None
        self.pending_request = None

    def on_pose(self, message):
        """영역이 바뀌면 비동기 요청을 보냅니다."""
        region = region_for_x(message.x)
        if region == self.current_region or self.pending_request is not None:
            return
        if not self.client.service_is_ready():
            return
        request = SetPen.Request()
        request.r, request.g, request.b = color_for_region(region)
        request.width = 3
        request.off = 0
        self.pending_region = region
        # 실습 3: 색상 요청을 비동기로 보냅니다.
        # 설명: 아래는 완성된 코드입니다.
        # 함께 작성할 코드:
        self.pending_request = self.client.call_async(request)
        self.pending_request.add_done_callback(self.on_result)

    def on_result(self, future):
        """서비스 결과를 처리합니다."""
        try:
            future.result()
            self.current_region = self.pending_region
            self.get_logger().info(f'펜 색상 변경: {self.current_region}')
        except Exception as error:
            self.get_logger().error(f'펜 색상 변경 실패: {error}')
        finally:
            self.pending_region = None
            self.pending_request = None


def main(args=None):
    """노드를 실행합니다."""
    rclpy.init(args=args)
    node = RegionPenClient()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
