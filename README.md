# Nao-Robot-Motion-record-and-repeat
The motion manually executed in one Nao robot is followed by another Nao.

In the RArm Path Tracking file, the motion of only the arm(s) of the first Nao (leader) is recorded as a list of joint positions and saved. 
This list is then executed by the second Nao (follower).

In the Real time control, the joint positions are not saved as a list. Instead at each time interval, the follower moves to the current joint positions of the leader.
