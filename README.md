# robotics-solo-quadruped-robot

Solo 8 quadruped robot is open-sourced by the Open Dynamic Robot Initiative. See: https://open-dynamic-robot-initiative.github.io/.

This is the final project of the course:  ROS2 Control Framework by The Construct. See: the.construct.ai.

The goal is to move the legs of the robot in a specific way using ros2_control.

## Source of the urdf model
https://github.com/open-dynamic-robot-initiative/robot_properties_solo/tree/master

## How to run

### Build repository

```
cd robotics-solo-quadruped-robot
colcon build
source install/setup.bash
```

### Display in RViz
```
ros2 launch solo_description display.launch.py
```

### Run in gazebo
```
ros2 launch solo_description gazebo.launch.py
```

### Spin up controllers
There is `joint_trajectory_controller` (See: https://control.ros.org/humble/doc/ros2_controllers/joint_trajectory_controller/doc/userdoc.html) used to control the legs of the robot. Spin up the controller with:
```
ros2 launch solo_controller controllers.launch.py
```

## How to test
After spinning up controllers, there is `solo_controller` of type `joint_trajectory_controller`. It listens to the topic: `/solo_controller/joint_trajectory`. You can send `trajectory_msgs/msg/JointTrajectory` message, for example:

```
ros2 topic pub /solo_controller/joint_trajectory trajectory_msgs/msg/JointTrajectory "header:
  stamp:
    sec: 0
    nanosec: 0
  frame_id: ''
joint_names: ['FL_HFE', 'FL_KFE', 'FR_HFE', 'FR_KFE','HL_HFE','HL_KFE','HR_HFE','HR_KFE']
points: [{positions: [1.57, -3.14, 1.57, -3.14, -1.57, 3.14, -1.57, 3.14], time_from_start: {sec: 4}}]"  -1
```

```
ros2 topic pub /solo_controller/joint_trajectory trajectory_msgs/msg/JointTrajectory "header:
  stamp:
    sec: 0
    nanosec: 0
  frame_id: ''
joint_names: ['FL_HFE', 'FL_KFE', 'FR_HFE', 'FR_KFE','HL_HFE','HL_KFE','HR_HFE','HR_KFE']
points: [{positions: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], time_from_start: {sec: 4}}]"  -1
```