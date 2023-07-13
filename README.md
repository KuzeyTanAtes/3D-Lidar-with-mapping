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
   Please extract the contents of the repo to the src folder. You should have the threeD_mapping pkg, a readme file, and the libgazebo plugin in the src folder.
5) In the tknls_ws folder run: (please don't run in the src folder)
   ```colcon build --symlink-install```
6) Add a source statement to ur .bashrc script
7) using nvidia settings set ur graphics card to **Performance Mode**
8) install slam_toolbox using ```sudo apt-get install ros-humble-slam-toolbox```
9) install pointcloud_to_laserscan ```sudo apt-get install-get ros-humble-pointcloud-to-laserscan```

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

