import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class KeyListener(Node):
    def __init__(self):
        super().__init__('key_listener')
        self.subscription = self.create_subscription(
            String,
            'keypress',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        self.get_logger().info(f'Recibido: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = KeyListener()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
