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
