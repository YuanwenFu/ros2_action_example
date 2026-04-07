import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from fibonacci_action_interfaces.action import Fibonacci

class FibonacciClient(Node):
    def __init__(self):
        super().__init__("fibonacci_client")
        self.client = ActionClient(self, Fibonacci, "fibonacci")

    def send_goal(self):
        goal = Fibonacci.Goal()
        goal.order = 10 

        self.client.wait_for_server()

        self.future = self.client.send_goal_async(
            goal,
            feedback_callback=self.feedback_callback
        )
        self.future.add_done_callback(self.goal_response_callback)
    
    def goal_response_callback(self, future):
        goal_handle = future.result()

        if not goal_handle.accepted:
            self.get_logger().info("Goal rejected")
            return 
        self.get_logger().info("Goal accepted")
        result_future = goal_handle.get_result_async()
        result_future.add_done_callback(self.get_result_callback)
    
    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info(f"Feedback: {feedback.partial_sequence}")
    
    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info(f"Result: {result.sequence}")
        rclpy.shutdown()
    
def main():
    rclpy.init()
    client = FibonacciClient()
    client.send_goal()
    rclpy.spin(client)

if __name__ == "__main__":
    main()