# 3D-Lidar-with-mapping
3D mapping using a 3D Lidar

# Installation Instructions and First Time Setup

1) ```mkdir -p ~/Desktop/tknls_ws/src/```
   Note that since the paths are hardcoded, you need to change the /home/usame_aw/ to /home/usrname/ in the following places:
   a) launch files --> robot_state_publisher
   b) launch files --> threeD_lnchr
   c) launch files --> online_async
   d) launch files --> spawn turtlebot
3) For the sake of convience I already ran the cmake and make commands on the 3D lidar plugin. run ```sudo mv libgazebo_ros_velodyne_laser.so /opt/ros/humble/lib/```
4) In the tknls_ws folder run: (please don't run in the src folder)
   ```colcon build --symlink-install```
5) Add a source statement to ur .bashrc script
6) using nvidia settings set ur graphics card to **Performance Mode**

# Running the Demo
After sourcing: 
1) ```ros2 launch threeD_mapping threeD_lnchr.launch.py```
2) ```ros2 run turtlebot3_teleop teleop_keyboard```
3) ```ros2 launch threeD_mapping online_async_launch.py use_sim_time:=True```

# Visualizing current results
At the moment there is no occ_map or costmap map being generated, however the lidar data can still be visualized using rviz
run ```rviz2``` 
The frame should be set to map.
Click on Add by topic --> /map

all other stuff is optional. Possible things that can be visualized include the lidar data, the robot transformations and locations, the laserscan topic ....

# To-DO
[] ADD a NAV2 params list
