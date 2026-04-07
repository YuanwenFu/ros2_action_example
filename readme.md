ros action使用案例，使用自定义的action消息，见`fibonacci_action_interfaces/action/Fibonacci.action`


编译命令
```bash
colcon build --packages-up-to fibonacci_action_demo
```

运行命令，
终端1上执行，
```bash
source install/setup.bash
ros2 run fibonacci_action_demo action_server
```

终端2上执行，
```bash
source install/setup.bash
ros2 run fibonacci_action_demo action_client
```

结果，
终端1上的结果
```txt
[INFO] [1775551952.542445293] [fibonacci_server]: Goal received
[INFO] [1775551960.546879022] [fibonacci_server]: Goal success! result.sequence = array('i', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

```
终端2上的结果
```txt
[INFO] [1775551402.370078708] [fibonacci_client]: Goal accepted
[INFO] [1775551402.370658418] [fibonacci_client]: Feedback: array('i', [0, 1, 1])
[INFO] [1775551403.372196152] [fibonacci_client]: Feedback: array('i', [0, 1, 1, 2])
[INFO] [1775551404.372896117] [fibonacci_client]: Feedback: array('i', [0, 1, 1, 2, 3])
[INFO] [1775551405.373002642] [fibonacci_client]: Feedback: array('i', [0, 1, 1, 2, 3, 5])
[INFO] [1775551406.373329028] [fibonacci_client]: Feedback: array('i', [0, 1, 1, 2, 3, 5, 8])
[INFO] [1775551407.374117217] [fibonacci_client]: Feedback: array('i', [0, 1, 1, 2, 3, 5, 8, 13])
[INFO] [1775551408.374495306] [fibonacci_client]: Feedback: array('i', [0, 1, 1, 2, 3, 5, 8, 13, 21])
[INFO] [1775551409.375165236] [fibonacci_client]: Feedback: array('i', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
[INFO] [1775551410.377198726] [fibonacci_client]: Result: array('i', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
```