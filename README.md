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
> Enviroment: Ubuntu 18.04 + Python 2.7
### Function
Using an object-oriented programming approach to generate plotting data, scales that visualise non-redundant information about the given function.

Outperforming features:
- [x] "Real-time'/live updated data visualisation.
- [ ] Graphical user interface (GUI):
    - [ ] adjusting axis with slider (zoom functionality);
    - [ ] manually adjusting the axis based on current min max values;
    - [x] adding a grid;
    - [x] add start, stop and reset button to reinitialise data collection;
    - [x] add an edit field to enter experiment name;
    - [x] add save button to store data as csv with date, time and edit field content.
- [ ] Tikz implementation, to allow export as LaTeX code with minimal adjustments.
### Setup
Run `python kthfsdv_exc2.py` in *Terminal*.
### Test & Result
<b>Start</b>
![img](https://github.com/JasperRice/KTHFS-DV/blob/master/exc2/start.gif)

<b>Stop & Reset</b>
![img](https://github.com/JasperRice/KTHFS-DV/blob/master/exc2/stop_reset.gif)

<b>Experiment Name & Save Data</b>
![img](https://github.com/JasperRice/KTHFS-DV/blob/master/exc2/name_save.gif)
