import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import sys
import termios
import tty

class KeyPublisher(Node):
    def __init__(self):
        super().__init__('key_publisher')
        self.publisher_ = self.create_publisher(String, 'keypress', 10)
        self.get_logger().info("Presiona teclas para enviarlas. Ctrl+C para salir.")
        self.read_keys()

    def read_keys(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            while True:
                ch = sys.stdin.read(1)
                msg = String()
                msg.data = ch
                self.publisher_.publish(msg)
                self.get_logger().info(f'Enviado: {ch}')
        except KeyboardInterrupt:
            pass
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def main(args=None):
    rclpy.init(args=args)
    node = KeyPublisher()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
