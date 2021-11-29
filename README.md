# Mobility-Analysis-Workflows-tutorial
Watch our video tutorial to learn how to work with MAW:https://www.youtube.com/watch?v=9emIszx2hgo

All commands in this tutorial should be executed on Mac/Linux terminal or Windows command-line interface. 

Before starting the tutorial, please navigate to the directory where you want all the downloaded tools and data to be stored, using the following command on the terminal/command-line interface.

Windows:\
`cd ${your directory path}` \
MAC / Linux: \
`cd /your directory path`

## 1. Prepare Docker containers
### 1.1. Install Docker
Install Docker Desktop following the instruction: https://docs.docker.com/get-docker/ 

You can test in the terminal with: 

`docker run hello-world`  

You will get the result from Docker: 

![alt text](https://github.com/UW-THINKlab/Mobility-Analysis-Workflows-tutorial/blob/master/figures/Docker%20group%20result.png)

This step is to work with Docker using your own PC.
### 1.2. Download Docker images 
A Docker image is a read-only template that contains a set of instructions for creating containers that can run on the Docker platform.
To work with MAW, we need to download the relevant Docker images by running: 
```
docker pull uwthinklab/maw_gui:v2
docker pull uwthinklab/maw_containers_1:v6
docker pull uwthinklab/maw_visualization:v1
docker pull uwthinklab/maw_visualization:gnumeric
```
## 2. Prepare workflows
### 2.1 Running MAW
First, we need "Git" tool to download code from Github. To download and install “Git” command line tool, following the instructions on: https://git-scm.com/downloads 

Then download our repository: 

`git clone https://github.com/UW-THINKlab/Mobility-Analysis-Workflows-tutorial`

**Then go to “/Mobility-Analysis-Workflows-tutorial” directory**. For Windows users, run:
```bash 
docker run --rm   -p 6080:6080 \
    -v  %cd%/:/data  \
    -v  /var/run/docker.sock:/var/run/docker.sock \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    --privileged --group-add root \
    uwthinklab/maw_gui:v1
```
For MAC/Linux Users, run:
```bash 
docker run --rm   -p 6080:6080 \
    -v  ${PWD}/:/data  \
    -v  /var/run/docker.sock:/var/run/docker.sock \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    --privileged --group-add root \
    uwthinklab/maw_gui:v1
```
Upon completion, the following information should be displayed on the terminal.

![alt text](https://github.com/UW-THINKlab/Mobility-Analysis-Workflows-tutorial/blob/master/figures/BWB%20start.png)

To launch MAW, go to link: http://localhost:6080/ using any web browser, which leads to the graphical interface of MAW.

![alt text](https://github.com/UW-THINKlab/Mobility-Analysis-Workflows-tutorial/blob/master/figures/MAW.png)

After testing the MAW, you can close it by pressing "Ctrl+C" in the terminal where you launched your MAW.

### 2.2 Download the test data 
You can download the synthetic test datasets via: 

http://dx.doi.org/10.17632/cb2r6hv72b.1

The two test datasets are named "input_case1_v2.csv" and "input_case2_v2.csv", respectively.

Then create a new directory, "/Mobility-Analysis-Workflows-tutorial/trans_data", and put the dataset files under this directory. 

### Dowload the two example workflows
The “MAW_case1” folder and the “MAW_case2” folder in this repository contain the two workflows for processing GPS data and cellular data, respectively. Each folder contains the configuration of a workflow including the information about which wigets are used in the workflow, how the widgets are connected, what are the default values of the change points, etc.

After you download the “MAW_case1” folder and “MAW_case2” folder to you computer, make sure they are in the directory "/Mobility-Analysis-Workflows-tutorial". 

## 3. Run example workflows
### 3.1 Workflow for processing GPS data
After launching MAW following section 2.1, click "File" in the menu bar, and click "Load workflow", move to the “/data” directory, choose the folder “MAW_case1” (do not enter the directory), and click the “Choose” button.
Then you should see the workflow as shown below.

![alt text](https://github.com/UW-THINKlab/Mobility-Analysis-Workflows-tutorial/blob/449c6b3c926e3bdf764adf473317c7223a645052/figures/workflow%206.png)

After loading the workflow, double-click the "Trace Segmentation Clustering" widget and click "Start", and the workflow will start running. If error occurs, see step 4 “Modify the workflow and widgets” to reconfigure the "Trace Segmentation Clustering" widget before start running it. After the workflow is completed, you will see the following output.

![alt text](https://github.com/UW-THINKlab/Mobility-Analysis-Workflows-tutorial/blob/0141b49382f10c606f55626ebd8b4bac7469c6a7/figures/workflow%206%20result.png)

### 3.2 Workflow for processing cellular data
Similarly as in section 3.1, you can load the workflow for processing cellular data by choosing the “MAW_case2” folder. 

![alt text](https://github.com/UW-THINKlab/Mobility-Analysis-Workflows-tutorial/blob/2e6e6f053ec672cf197f05350d9e723617cc4997/figures/workflow%202.png)

After loading the workflow, double-click the "Incremental Clustering" widget and click "Start", and your workflow will start running. If error occurs, see step 4 “Modify the workflow and widgets” to reconfigure the "Incremental Clustering" widget before start running it. After the workflow is completed, you will see the following output.

![alt text](https://github.com/UW-THINKlab/Mobility-Analysis-Workflows-tutorial/blob/0141b49382f10c606f55626ebd8b4bac7469c6a7/figures/workflow%202%20results.png)

## 4. Modify the workflow and widgets
### 4.1. Change input and output 
You can change the input and output files of a widget in the following steps: double-click the widget, and a widget configuration window will pop up. You can change the input and output files by simply clicking the folder icon next to the “Input” or “Output” textbox, and select the input file or type in the output file name in the pop-up file explorer.

In the workflow for processing GPS data, the default input file is "/Mobility-Analysis-Workflows-tutorial/trans_data/input_case1_v2.csv", which should be the Input for the first widget “Trace Segmentation Clustering” in the workflow.

In the workflow for processing cellular data, the default input file is /Mobility-Analysis-Workflows-tutorial/trans_data/input_case2_v2.csv, which should be the Input for the first widget “Incremental Clustering” in the workflow.

![alt text](https://github.com/UW-THINKlab/Mobility-Analysis-Workflows-tutorial/blob/master/figures/Change%20Param%20case%201.png)

### 4.2. Change parameters
Similarly, you can modify the change point values of a widget by typing in the values directly in the configuration window. For example, in the above screenshot of the workflow for processing GPS data, the widget “Trace Segmentation Clustering” has two change points, “Distance threshold” and “Duration threshold”, whose default values are sets as 0.2 km ans 300 seconds, respectively. Customized change point values can be typed in the corresponding textboxes.

### 4.3. Customize a workflow
There are numerous ways a workflow can be changed or customized. We give an example of how to skip the widget of “Oscillation Corrector” in the workflow for processing cellular data. 

First, the widget “Oscillation Corrector” and the subsequent widget “Stay Duration Calculator” need to be removed from the workflow. To do so, right-click on each widget, and click “Remove”. 

Then, a link needs to be drawn from the remaining “Stay Duration Calculator” widget to the “gnumeric” widget. To do so, left-click on the right edge of  “Stay Duration Calculator”, hold and drag to the left edge of “gnumeric”. Upon releasing your mouse, a link configuration window will pop up as shown in the following screenshot.

![alt text](https://github.com/UW-THINKlab/Mobility-Analysis-Workflows-tutorial/blob/master/figures/Add%20Link.png)

The link configuration window defines the functionality of the link. In the above screenshot, the link means the output of  “Stay Duration Calculator” serves as input to “gnumeric”, and should be kept this way. If the link needs to be configured differently, it can be adjusted by clicking the checkboxes. Then click “Ok” to confirm the configuration and close the pop-up window. The modified workflow looks as below.

![alt text](https://github.com/UW-THINKlab/Mobility-Analysis-Workflows-tutorial/blob/master/figures/Delete%20widget.png)

The modified workflow can be run similarly as the unmodified version. After the workflow is completed, the output should look as below.

![alt text](https://github.com/UW-THINKlab/Mobility-Analysis-Workflows-tutorial/blob/master/figures/Case%202%20result.png)

## Reference
Our work is built based on Bwb (https://github.com/BioDepot/BioDepot-workflow-builder)

Our MAW icons are made by <a href="https://www.flaticon.com/authors/flat-icons" title="Flat Icons">Flat Icons</a>, <a href="https://www.flaticon.com/authors/itim2101" title="itim2101">itim2101</a>, <a href="https://www.flaticon.com/authors/pixel-perfect" title="Pixel perfect">Pixel perfect</a>, <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a>, <a href="https://www.flaticon.com/authors/darius-dan" title="Darius Dan">Darius Dan</a>, <a href="https://www.flaticon.com/authors/smashicons" title="Smashicons">Smashicons</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a> 


