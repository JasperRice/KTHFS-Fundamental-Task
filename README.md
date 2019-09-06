# KTH Formula Student - Exercises
## [Exercise 1 - Network](/kthfsdv/src/exc1)
> Enviroment: Ubuntu 18.04 + Python 2.7 + ROS Melodic Morenia
### Function
- Create **nodeA** to publish specific message to topic **/Jiang** at rate of 20 Hz.
- Create **nodeB** to subscribe the message from topic **/Jiang** and published the divided message (by 0.15) to topic **/kthfs/result**.
### Setup
- In the first *Terminal*: run `roscore`.
- In the second *Terminal*: run `rosrun receiver subscriber.py`
- In the third *Terminal*: run `broadcast publisher.py`
### Test & Result
- Run `rostopic echo /Jiang` and `rostopic echo /kthfs/result` to check the messages.
- Run `rqt_plot` to visualize the messages.
<p align="center">
    <img src="/kthfsdv/src/rosplot.png" alt>
</p>

- Run `rqt_graph` to visualize the nodes and topics.
<p align="center">
    <img src="/kthfsdv/src/rosgraph.png" alt>
</p>

## [Exercise 2 - Visualization](/exc2)
> Enviroment: Ubuntu 18.04 + Python 2.7 (matplotlib, numpy, Tkinter)
> - Unable to update plot by `FuncAnimation` if using the object function from `class`. Two ways:
>   - [x]
### Function
### Setup
### Test & Result
