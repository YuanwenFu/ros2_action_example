import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from fibonacci_action_interfaces.action import Fibonacci
import time

class FibonacciServer(Node):
    def __init__(self):
        super().__init__("fibonacci_server")

        self.server = ActionServer(
            self,
            Fibonacci,
            "fibonacci",
            self.execute_callback
        )

    async def execute_callback(self, goal_handle):
        self.get_logger().info("Goal received")

        feedback = Fibonacci.Feedback()
        sequence = [0, 1]

        for i in range(2, goal_handle.request.order):
            sequence.append(sequence[-1] + sequence[-2])
            feedback.partial_sequence = sequence 
            goal_handle.publish_feedback(feedback)
            time.sleep(1)
        goal_handle.succeed()

        result = Fibonacci.Result()
        result.sequence = sequence 
        self.get_logger().info(f"Goal success! result.sequence = {result.sequence}")
        return result 

def main():
    rclpy.init()
    node = FibonacciServer()
    rclpy.spin(node)

if __name__ == "__main__":
    main()
