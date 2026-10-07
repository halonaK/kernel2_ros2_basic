"""위치를 확인하며 벽을 피하는 실습입니다."""

from geometry_msgs.msg import Twist  # noqa: F401
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose  # noqa: F401


class TurtleCmdAndPose(Node):
    """속도를 발행하고 위치를 구독하는 노드입니다."""

    def __init__(self):
        super().__init__('lesson2_3_turtle_cmd_and_pose')
        self.pose = None

        # 실습 1: /turtle1/cmd_vel에 Twist를 발행하세요.
        # self.publisher =

        # 실습 2: /turtle1/pose를 구독하세요.
        # self.subscription =

        # 실습 3: publish_velocity를 0.1초마다 실행하세요.
        # self.timer =

    def on_pose(self, message):
        """최근 위치를 저장합니다."""
        # 실습 4: 받은 메시지를 self.pose에 저장하세요.
        pass

    def publish_velocity(self):
        """벽을 피하는 속도를 발행합니다."""
        # 실습 5: 벽 근처에서는 회전하고, 아니면 직진하도록 작성하세요.
        pass


def main(args=None):
    """노드를 실행합니다."""
    rclpy.init(args=args)
    node = TurtleCmdAndPose()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
