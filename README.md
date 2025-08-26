### ROS2 Jazzy pkg ###
This package is a jazzy package to create a node which can transmitt keyboard commands via ros topic.

If you want to use this package, it is very simple.

First of all you gotta have ROS2 jazzy installed.
Simply clone this repo in your workspace, compile it with colcon.

This package is not meant to be used by it's own. Its so you can integrate the keyboard command node to your environment.

August 2025.

I originally posted this ros2 package some time ago, and recently I tried to use it for a small project, but I realized you could get trouble if you directly git clone this on your ROS2 workspace.
If you wanna get this working, you should just copy the nodes codes from the files (key_listener.py and key_publisher.py) and compile it in your own package, since the clone of this repo will create a workspace within your actual workspace and you wont't be able to build the ws.
I'll try to fix this as soon as i'm available, but for now, you can simply compile the source code.

Summary: this won't work if you directly clone it. You should copy the source code to your own package(python package) and then run the node.
For practical effects, the executables are called the same as the code files(as seen in the setup.py) so you can run it using the ros2 run tool.

Greetings!!
