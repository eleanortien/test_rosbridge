# Notes on Setup 

You might be tempted to look at the rosbridge documentation but I swear some of it is outdated or smth bc it sucks and lies to you. (Or I just had the wrong version) 


## Installation
1. sudo apt install ros-<ROS_DISTRO>-rosbridge-server -> replace ROS_DISTRO with foxy (or do echo $ROS_DISTRO and add what comes out of that)
2. source /opt/ros/<ROS_DISTRO>/setup.bash -> sourcing here and then sourcing your own workspace does not seem to have complications so far but I didn't test very far into it.


## Running Rosbridge
1. ros2 launch rosbridge_server rosbridge_websocket_launch.xml
- should give: [INFO] [1541100534.152110]: Rosbridge WebSocket server started on port 9090
 - -> you can make a custom .launch file and run ros2 launch newFile to choose which port to run

## Webserver Explanation
1. HTML Script uses roslibjs (could not figure out if python works for this, webdev confusing ;-;) -> requires two components:
    - a ros connection to the websocket ROSLIB.Ros(), turned on with .on()
    - ros services (subscriber used here) to communicate with rover using the standard topics

When webfile is run, you may need to reload the site to make sure it's connected to the websocket. Any topics your website should be connected to should be printed.
Example output:

[rosbridge_websocket-1] [INFO] [1732499776.558816503] [rosbridge_websocket]: Client connected. 1 clients total.
[rosbridge_websocket-1] [INFO] [1732499777.048354208] [rosbridge_websocket]: [Client 43de0117-af21-4fbf-af04-dc709ce901da] Subscribed to /my_topic


