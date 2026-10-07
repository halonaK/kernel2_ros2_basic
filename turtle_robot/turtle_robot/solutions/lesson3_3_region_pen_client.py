"""거북이 위치에 따라 펜 색상을 변경하는 예제입니다."""

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from turtlesim.srv import SetPen


def region_for_x(x):
    """X 좌표를 왼쪽 또는 오른쪽 영역으로 구분합니다."""
    return 'left' if x < 5.5 else 'right'


def color_for_region(region):
    """왼쪽은 노랑, 오른쪽은 초록을 반환합니다."""
    return (255, 255, 0) if region == 'left' else (0, 255, 0)


class RegionPenClient(Node):
    """영역이 바뀔 때 펜 색상 서비스를 호출합니다."""

    def __init__(self):
        super().__init__('lesson3_3_region_pen_client')
        self.client = self.create_client(SetPen, '/turtle1/set_pen')
        self.subscription = self.create_subscription(
            Pose, '/turtle1/pose', self.on_pose, 10
        )
        self.current_region = None

    def on_pose(self, message):
        """영역이 바뀌면 펜 색상을 변경합니다."""
        region = region_for_x(message.x)
        if region == self.current_region:
            return
        if not self.client.service_is_ready():
            return

        request = SetPen.Request()
        request.r, request.g, request.b = color_for_region(region)
        request.width = 3
        request.off = 0
        self.client.call_async(request)
        self.current_region = region
        self.get_logger().info(f'현재 영역: {region}')


def main(args=None):
    """위치를 계속 구독하며 서비스를 호출합니다."""
    rclpy.init(args=args)
    node = RegionPenClient()
    node.client.wait_for_service()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
