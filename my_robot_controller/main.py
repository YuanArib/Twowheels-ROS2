import rclpy

from my_robot_controller.twowheels_controller import TwowheelsController


def main(args=None):
    rclpy.init(args=args)
    twowheels_controller = TwowheelsController()
    rclpy.spin(twowheels_controller)
    twowheels_controller.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()