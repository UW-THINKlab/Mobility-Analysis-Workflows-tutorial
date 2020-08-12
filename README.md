# Running-script-in-Docker-tutorial
This is a tutorial of running our own scripts in Docker container and building widgets and workflows using Biodepot-workflow-builder(Bwb). In this tutorial, we will use *App_data repository* as an example to give a step-bystep guide of building containers, later widgets, and workflows. Finially, we will reproduce the workflow in the paper: XXX
## 1. Try our AWS
You can quickly try our built workflow through AWS: XXX

*fig of DCI workflow*

You can simply click XXX module(widget) and click "start", then the workflow will run and you will have result like this:

*fig of result*

If you want to learn more about the workflow and widget, please read on or refer to: https://github.com/BioDepot/BioDepot-workflow-builder

## 2. Download eveything to run in your own PC ...
App_data repository is the code to handle mobility data(cellular and GPS data).
In order to continue further steps, please download the repository by:
```
git clone https://github.com/UW-THINKlab/app-data
```
## 3. Build Docker container / (modifiy the widget/workflow.. param..)
### 3.1. Install Docker
Install Docker Desktop following instruction: https://docs.docker.com/get-docker/ \
After installation and running Docker Desktop, you can test in the terminal with:
```
docker help 
```
or
```
sudo docker help
```
If the help information is returned, then it's good to move to the next step.

*fig of docker command help info*
### 3.2. Build your Docker container 
Dockerfile is a container profile detailing which scripts and dependencies will be included in the container. We will give a step by step guide to create a Docker container which can provide running environment for App_data code. You can also skip this step by pull our Docker container directly using below commands, then you can move on to section 3.3: 
```
docker pull biodepot/thinklab:workflow_v1
docker pull biodepot/thinklab:vis_v1
```
First we show the Dockerfile, it should be included in App_data repository:
```
# the base container image we will ues
FROM python:2.7

RUN pip install numpy psutil func_timeout

WORKDIR /

COPY AddressOscillation.py AddressOscillation.py
COPY class_cluster.py class_cluster.py
COPY CombineExtractedStays.py CombineExtractedStays.py
COPY distance.py distance.py
COPY incremental_clustering.py incremental_clustering.py
COPY IncrementalClustering.py IncrementalClustering.py
COPY oscillation_type1.py oscillation_type1.py
COPY ReadAndPartition.py ReadAndPartition.py
COPY TraceSegmentationClustering.py TraceSegmentationClustering.py
COPY UpdateStayDuration.py UpdateStayDuration.py
COPY WriteCSVFile.py WriteCSVFile.py
COPY util_func.py util_func.py
```
pull python base image:
```
docker pull python:2.7
```
then, in the directory where you downloaded the App_data code, run below command to build your container image:
```
docker build -t biodepot/thinklab:workflow_v1 .
```
*fig of built container image*

### 3.3. Run the scripts in your Docker container
After you have the container image, run below command to test your container image:
```
docker run -i --rm biodepot/thinklab:workflow_v1 python ReadAndPartition.py
```

*fig of returned result*

## 4. Run Biodepot-workflow-builder(Bwb).  DIY your own workflow
Pull Bwb repository:
```
git clone https://github.com/BioDepot/BioDepot-workflow-builder
```
then run:
```
docker run --rm   -p 6080:6080 \
    -v  ${PWD}/:/data  \
    -v  /var/run/docker.sock:/var/run/docker.sock \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    --privileged --group-add root \
    biodepot/bwb
```
After the Bwb container is launched, go to link: http://localhost:6080/. (This is a visualizable platform of Bwb.)

*fig of Bwb*

## 5. Build widgets and workflow in Bwb
*fig of DCI*

Shown as the figure above, our DCI workflow consists of 7 different widgets: “ReadAndPartition” widget, read the trip data and partition the data into two subsets; “IncrementalClustering”, perform incremental clustering on cellular data; “UpdateStayDuration”, update duration information; “AddressOscillation”, address oscillation problem; “CombineExtractedStays”, combine extracted cellular and GPS data, “WriteCSVFile”, write the result into CSV file; “TraceSegmentationClustering”, conduct trace segmentation clustering. 

From the left side of the figure to the right side, the workflow will run the widgets sequentially along the dot line arrow between each two widgets. The dot lines denote the workflow running direction and which parameters of one widget are passed to the others.

In this section, we will give a step-by-step guide to build these widgets and finally connect them together to have a complete workflow: follow our video tutorial: *link*

Also, if you would like to skip this step, you can download our workflow directly: *link* XXXX.

## 6. Run your workflow
After building the workflow, click "ReadAndPartition" widget and click "start", your workflow will run!

*fig of result*
