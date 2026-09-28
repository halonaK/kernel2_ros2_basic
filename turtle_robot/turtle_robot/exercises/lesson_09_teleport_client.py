"""거북이를 이동시키는 비동기 서비스 클라이언트입니다."""

import rclpy
from rclpy.node import Node
from turtlesim.srv import TeleportAbsolute  # noqa: F401


class TeleportClient(Node):
    """x, y, theta 파라미터로 순간이동합니다."""

    def __init__(self):
        super().__init__('lesson_09_teleport_client')
        # 실습 1: 순간이동 서비스를 선택합니다.
        # 설명: 빈칸을 채우고 아래 코드의 주석을 해제하세요.
        # 함께 작성할 코드:
        # self.client = self.create_client(
        #     ____, '____'
        # )
        pass
        self.declare_parameter('x', 2.0)
        self.declare_parameter('y', 2.0)
        self.declare_parameter('theta', 0.0)

    def send_request(self):
        """파라미터로 비동기 요청을 생성합니다."""
        request = None
        # 실습 2: 요청 메시지를 만듭니다.
        # 설명: 빈칸을 채우고 아래 코드의 주석을 해제하세요.
        # 함께 작성할 코드:
        # request = ____.Request()
        pass
        request.x = float(self.get_parameter('x').value)
        request.y = float(self.get_parameter('y').value)
        request.theta = float(self.get_parameter('theta').value)
        # 실습 3: 요청을 비동기로 보냅니다.
        # 설명: 빈칸을 채우고 아래 코드의 주석을 해제하세요.
        # 함께 작성할 코드:
        # return self.client.call_async(____)
        pass


def main(args=None):
    """서비스를 호출합니다."""
    # 실습을 모두 완성한 뒤 아래 안내 줄을 삭제하세요.
    raise SystemExit('실습 1~3을 완성하고 안내 줄을 삭제하세요.')
    rclpy.init(args=args)
    node = TeleportClient()
    try:
        if not node.client.wait_for_service(timeout_sec=3.0):
            raise RuntimeError('teleport_absolute 서비스를 찾지 못했습니다.')
        future = node.send_request()
        rclpy.spin_until_future_complete(node, future)
        future.result()
        node.get_logger().info('순간이동 완료')
    except (KeyboardInterrupt, RuntimeError) as error:
        node.get_logger().error(str(error))
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
