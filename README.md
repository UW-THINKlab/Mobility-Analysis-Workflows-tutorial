# Running-script-in-Docker-tutorial
This is a tutorial of running our own scripts in Docker container and building widgets and workflows using Biodepot-workflow-builder(Bwb). In this tutorial, we will use *App_data repository*(Link: XXX) as an example to give a step-bystep guide of building containers, widgets, and workflows. Finially, we will reproduce the workflow in the paper: XXX
## 1. Try our AWS
You can quickly try our built workflow through AWS: XXX

You will see our workflow like this:

![alt text](https://github.com/Ien001/Running-script-in-Docker-tutorial/blob/master/figures/DCI.png)

You can simply click "ReadAndPartition" widget and click "start", then the workflow will run and you will have result csv file like this:

(better put result in bwb)
![alt text](https://github.com/Ien001/Running-script-in-Docker-tutorial/blob/master/figures/DCI%20running%20result.png)

If you want to learn more about the workflow and widget, please read on or refer to: https://github.com/BioDepot/BioDepot-workflow-builder

## 2. Download & run workflow application on your own PC
### 2.1. Install Docker
Install Docker Desktop following instruction: https://docs.docker.com/get-docker/ 

After installation, add the current PC user to docker group:
```
sudo groupadd docker
sudo gpasswd -a $USER docker
newgrp docker
```
You can test in the terminal with:

```
docker run hello-world
```
You will get the result from Docker:
![alt text](https://github.com/Ien001/Running-script-in-Docker-tutorial/blob/master/figures/Docker%20group%20result.png)
### 2.2. Download Biodepot-workflow-builder(Bwb)
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
After the Bwb container is launched, go to link: http://localhost:6080/. (This is a visualizable platform of Bwb)

![alt text](https://github.com/Ien001/Running-script-in-Docker-tutorial/blob/master/figures/Bwb.png)

### 2.3. Download DCI container images and Workflow
To download DCI container image:
```
docker pull biodepot/thinklab:workflow_v1
docker pull biodepot/thinklab:vis_v1
```
DCI Workflow download link:

Then place the downloaded workflow under the Bwb folder, "/BioDepot-workflow-builder".

After downloading the DCI container image and Workflow, cilck "File" in the menu bar, and click "load workflow", then choose the downloaded workflow directory.
Then you should see the DCI workflow is loaded. You should see our DCI workflow.

### 2.4 Download test data
You can download our test data via: XXX

Then put the data file under the Bwb folder, "/BioDepot-workflow-builder". 

Click "ReadAndPartition" widget and click "start", then the workflow will run.

## 3. Modify the workflow and widgets
### 3.1. Change input & output 
You can Change input & output by clicking the widget you want modify, and you will see the config form. You can simply change the input & output by modify the corresponding text.
![alt text](https://github.com/Ien001/Running-script-in-Docker-tutorial/blob/master/figures/change%20param.png)
### 3.2. Change parameters
Similarly, you can change the parameters of any widget by modify the parameters directly in the config form.

## 4. Build your own workflow
### 4.1. Build your Docker container 
Please install Docker following section 2.1.

Dockerfile is a container profile detailing which scripts and dependencies will be included in the container. We will give a step by step guide to create a Docker container which can provide running environment for App_data code. 

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

After you have the container image, run below command to test your container image:
```
docker run -i --rm biodepot/thinklab:workflow_v1 python ReadAndPartition.py
```

*fig of returned result*

## 4.2. Run Biodepot-workflow-builder(Bwb)
Please follow section 2.2 to download BWb first.

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

## 4.3. Build widgets and workflow in Bwb
![alt text](https://github.com/Ien001/Running-script-in-Docker-tutorial/blob/master/figures/DCI.png)
Shown as the figure above, our DCI workflow consists of 7 different widgets: “ReadAndPartition” widget, read the trip data and partition the data into two subsets; “IncrementalClustering”, perform incremental clustering on cellular data; “UpdateStayDuration”, update duration information; “AddressOscillation”, address oscillation problem; “CombineExtractedStays”, combine extracted cellular and GPS data, “WriteCSVFile”, write the result into CSV file; “TraceSegmentationClustering”, conduct trace segmentation clustering. 

From the left side of the figure to the right side, the workflow will run the widgets sequentially along the dot line arrow between each two widgets. The dot lines denote the workflow running direction and which parameters of one widget are passed to the others.

In this section, we will give a step-by-step guide to build these widgets and finally connect them together to have a complete workflow: follow our video tutorial: *link*

## 4.4. Run your workflow
After building the workflow, click "ReadAndPartition" widget and click "start", your workflow will run!

*fig of result*
