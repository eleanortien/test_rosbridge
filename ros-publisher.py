import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class TestPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, '/my_topic', 10)


def main(args=None):
    rclpy.init(args=args)

    testpublisher = TestPublisher()

    rclpy.spin(testpublisher)
    msg = String()
    msg.data = 'PM: 112.123'
    testpublisher.publisher_.publish(msg)


    testpublisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()