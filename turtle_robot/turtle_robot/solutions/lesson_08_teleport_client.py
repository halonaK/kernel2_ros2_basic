"""거북이를 지정한 위치로 순간이동시키는 예제입니다."""

import rclpy
from rclpy.node import Node
from turtlesim.srv import TeleportAbsolute


class TeleportClient(Node):
    """순간이동 서비스를 한 번 호출합니다."""

    def __init__(self):
        super().__init__('lesson_08_teleport_client')
        self.client = self.create_client(
            TeleportAbsolute, '/turtle1/teleport_absolute'
        )

    def send_request(self):
        """고정된 위치로 이동하는 요청을 보냅니다."""
        request = TeleportAbsolute.Request()
        request.x = 2.0
        request.y = 2.0
        request.theta = 0.0
        return self.client.call_async(request)


def main(args=None):
    """서비스를 호출하고 응답을 기다립니다."""
    rclpy.init(args=args)
    node = TeleportClient()
    node.client.wait_for_service()
    future = node.send_request()
    rclpy.spin_until_future_complete(node, future)
    future.result()
    node.get_logger().info('순간이동 완료')
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
