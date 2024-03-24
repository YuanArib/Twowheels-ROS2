from rclpy.node import Node
from geometry_msgs.msg import Twist
try:
    from my_robot_controller.motor_controller import MotorController
except ImportError as e:
    print(e)
    from my_robot_controller.fake_controller import MotorController

class TwowheelsController(Node):
    def __init__(self):
        super().init("minimal_publisher")
        self._cmd_vel_sub = self.create_subscription(
            Twist, "/cmd_vel", self.on_cmd_vel_msg, 10
        )
        self._controller = MotorController()
        self.get_logger().info("Twowheels Initiated.")

    def on_cmd_vel_msg(self, msg= Twist):
        self.get_logger().info(f"Got msg: {msg}")

        linear_left = linear_right = msg.linear.x / 2
        # Angular z is -1.0 for a right turn, 1.0 for a left turn
        angular_right = msg.angular.z / 4
        angular_left = -angular_right

        left = linear_left + angular_left
        right = linear_right + angular_right
        self.get_logger().info(f"left: {left}, right: {right}")

        # Send speeds to motors
        self._controller.set_motors(left, right)