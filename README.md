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

After testing the MAW, you can close it by typing "Ctrl+C" in the terminal where you launched your MAW.

### 2.2 Download the test data 
You can download our test data for Case study 1 via: 

https://drive.google.com/file/d/150etjTZ7EpF33l2Op1KC6xG29THicoo_/view?usp=sharing

You can download our test data for Case study 2 via: 

https://drive.google.com/file/d/1GzEfcTjlkVM2SpuKzAGIgKJAyKMsGrtz/view?usp=sharing

Then create a new directory, "/Mobility-Analysis-Workflows-tutorial/trans_data", and put the data file under this directory. 

### 2.3 Case study 1 workflow & Case study 2 workflow
The “MAW_case1” folder and the “MAW_case2” folder in this repo are the case study 1 workflow and case study 2 workflow implemented in our MAW paper, respectively.

They containes the configuration of a workflow including the information about how the workflow is connected, which wigets are used in the workflow and etc.

In this section, you don't need to type in any command. 

## 3. Run Case studies 1 & 2
### 3.1 Case study 1
After launching MAW following section 2.1, click "File" in the menu bar, and click "load workflow", move to the “/data” directory of MAW, then choose the downloaded workflow directory (do not enter the directory) and click “Choose”.
Then you should see our workflow for Case study 1 is loaded in MAW.

![alt text](https://github.com/UW-THINKlab/Mobility-Analysis-Workflows-tutorial/blob/master/figures/Case%201.png)

After loading the workflow, double-click "TraceSegmentationClustering" widget and click "start", your workflow will start to run! If error occurs, see step 4 “Modify the workflow and widgets” to reconfigure the "TraceSegmentationClustering" widget before start running it. After the workflow is completed, you will see the following output.

![alt text](https://github.com/UW-THINKlab/Mobility-Analysis-Workflows-tutorial/blob/master/figures/Case%201%20result.png)

### 3.2 Case study 2
Similarly, you can load the workflow for Case study 2 in MAW. 

![alt text](https://github.com/UW-THINKlab/Mobility-Analysis-Workflows-tutorial/blob/master/figures/Case%202.png)

After loading the workflow, double-click "CellIncrementalClustering" widget and click "start", your workflow will start to run! If error occurs, see step 4 “Modify the workflow and widgets” to reconfigure the "IncrementalClustering" widget before start running it. After the workflow is completed, you will see the following output.

![alt text](https://github.com/UW-THINKlab/Mobility-Analysis-Workflows-tutorial/blob/master/figures/Case%202%20result.png)

## 4. Modify the workflow and widgets
### 4.1. Change input and output 
You can change input and output file of one widget: double-click one widget, and a widget configuration form will pop up. You can simply change the input and output file by clicking the folder icon next to the “Input” or “Output” textbox, and select the input file or type in the output file name in the pop-up file explorer.

For case study 1, the default input file is /Mobility-Analysis-Workflows-tutorial/trans_data/input_case1.csv, which should be the Input for the first widget “TraceSegmentationClustering”.

For case study 2, the default input file is /Mobility-Analysis-Workflows-tutorial/trans_data/input_case2.csv, which should be the Input for the first widget “IncrementalClustering”.

![alt text](https://github.com/UW-THINKlab/Mobility-Analysis-Workflows-tutorial/blob/master/figures/Change%20Param%20case%201.png)

### 4.2. Change parameters
Similarly, you can change the parameters of a widget by typing in the parameters directly in the configuration form. For example, in the above screenshot for case study 1, the widget “TraceSegmentationClustering” has two parameters, “SpatialConstraint” and “DurationConstraint”, whose default values are sets as 0.2 ans 300, respectively. Customized parameter values can be typed in corresponding textboxes.

### 4.3. Customize a workflow
There are numerous ways a workflow can be changed and customized. We give an example of how to skip the widget of “Oscillation Corrector” in case study 2. 

First, the widget “Oscillation Corrector” and the subsequent widget “Stay Duration Calculator” need to be removed from the canvas. To do so, right-click on each widget, and click “Remove”. 

Then, a link needs to be drawn from the remaining “Stay Duration Calculator” widget to the “gnumeric” widget. To do so, click on the right edge of  “Stay Duration Calculator”, hold and drag to the left edge of “gnumeric”. Upon release the click, a link configuration window will pop up as shown in the following screenshot.

![alt text](https://github.com/UW-THINKlab/Mobility-Analysis-Workflows-tutorial/blob/master/figures/Add%20Link.png)

The link configuration window defines the functionality of the link. In the above screenshot, the link means the output of  “Stay Duration Calculator” serves as input to “gnumeric”, and should be kept this way. If the link is configured differently, it can be adjusted by clicking the checkboxes. Then click “OK” to confirm the configuration and close the pop-up window. The modified workflow looks as below.

![alt text](https://github.com/UW-THINKlab/Mobility-Analysis-Workflows-tutorial/blob/master/figures/Delete%20widget.png)

The modified workflow can be run similar as the unmodified version. After the workflow is completed, the output should look as below.

![alt text](https://github.com/UW-THINKlab/Mobility-Analysis-Workflows-tutorial/blob/master/figures/Case%202%20result.png)

## Reference
Our work is built based on Bwb (https://github.com/BioDepot/BioDepot-workflow-builder)

Our MAW icons are made by <a href="https://www.flaticon.com/authors/flat-icons" title="Flat Icons">Flat Icons</a>, <a href="https://www.flaticon.com/authors/itim2101" title="itim2101">itim2101</a>, <a href="https://www.flaticon.com/authors/pixel-perfect" title="Pixel perfect">Pixel perfect</a>, <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a>, <a href="https://www.flaticon.com/authors/darius-dan" title="Darius Dan">Darius Dan</a>, <a href="https://www.flaticon.com/authors/smashicons" title="Smashicons">Smashicons</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a> 


