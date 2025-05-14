import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/daniel/ros2_ws_v2/src/ros2_keypress/install/key_comm'
