"""두 번째 거북이를 생성하는 예제입니다."""

import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn


class SpawnClient(Node):
    """spawn 서비스를 한 번 호출합니다."""

    def __init__(self):
        super().__init__('lesson3_2_spawn_client')
        self.client = self.create_client(Spawn, '/spawn')

    def send_request(self):
        """turtle2 생성 요청을 보냅니다."""
        request = Spawn.Request()
        request.x = 8.0
        request.y = 8.0
        request.theta = 0.0
        request.name = 'turtle2'
        return self.client.call_async(request)


def main(args=None):
    """서비스를 호출하고 응답을 기다립니다."""
    rclpy.init(args=args)
    node = SpawnClient()
    node.client.wait_for_service()
    future = node.send_request()
    rclpy.spin_until_future_complete(node, future)
    response = future.result()
    node.get_logger().info(f'{response.name} 생성 완료')
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
