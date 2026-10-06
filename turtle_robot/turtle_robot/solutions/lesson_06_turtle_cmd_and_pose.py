"""위치를 확인하며 벽에 닿기 전에 회전하는 예제입니다."""

from geometry_msgs.msg import Twist
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose


def is_near_wall(pose):
    """거북이가 화면 가장자리와 가까운지 확인합니다."""
    return (
        pose.x < 1.0
        or pose.x > 10.0
        or pose.y < 1.0
        or pose.y > 10.0
    )


class TurtleCmdAndPose(Node):
    """거북이 위치를 구독하며 이동 명령을 보냅니다."""

    def __init__(self):
        super().__init__('lesson_06_turtle_cmd_and_pose')
        self.publisher = self.create_publisher(
            Twist, '/turtle1/cmd_vel', 10
        )
        self.subscription = self.create_subscription(
            Pose, '/turtle1/pose', self.on_pose, 10
        )
        self.pose = None
        self.timer = self.create_timer(0.1, self.publish_velocity)

    def on_pose(self, message):
        """현재 위치를 저장합니다."""
        self.pose = message

    def publish_velocity(self):
        """벽 근처에서는 회전하고 안전 영역에서는 직진합니다."""
        if self.pose is None:
            return

        message = Twist()
        if is_near_wall(self.pose):
            message.linear.x = 0.2
            message.angular.z = 1.5
        else:
            message.linear.x = 1.0
            message.angular.z = 0.0

        self.publisher.publish(message)


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
