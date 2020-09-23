# Mobility Analysis Workflows tutorial
This is a tutorial of running our own scripts in Docker container and building widgets and workflows using Biodepot-workflow-builder(Bwb). In this tutorial, we will use **App_data repository**(Link: XXX) as an example to give a step-bystep guide of building containers, widgets, and workflows. Finially, we will reproduce the workflow in the paper: XXX


## 1. Prepare Docker containers
### 1.1. Download Docker
Install Docker Desktop following instruction: https://docs.docker.com/get-docker/ 

After installation, add the current user of your PC to docker group (for Unix System user):
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
### 1.2. Download Docker images 
To download MAW Docker images:
```
docker pull biodepot/thinklab:workflow_v1
docker pull biodepot/thinklab:vis_v1
```
## 2. Prepare workflows
## 2.1 Download Bwb
Download Biodepot-workflow-builder(Bwb) repository:
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
This command will take a while because it will pull the Bwb Docker image automatically.

After the Bwb container is launched, to test our Bwb, go to link: http://localhost:6080/. (This is a visualizable platform of Bwb)

![alt text](https://github.com/Ien001/Running-script-in-Docker-tutorial/blob/master/figures/Bwb.png)


## 2.2 Download the test data 
You can download our test data via: https://drive.google.com/file/d/1dHEI0voFOekZ9d7ZcfL7euOGJIyxKkcn/view?usp=sharing

Then create a new directory, "/Your Own Path/BioDepot-workflow-builder/trans_data", and put the data file under this directory. 

## 2.3 Download workflow for Case study 1
Case study 1 Workflow download link: XXX (in progress)

Then save the downloaded workflow under the Bwb folder, "/BioDepot-workflow-builder".

## 2.4 Download workflow for case study 2
Case study 2 Workflow download link: XXX (in progress)

Then save the downloaded workflow under the Bwb folder, "/BioDepot-workflow-builder".


## 3. Modify the workflow and widgets
### 3.1. Change input & output 
You can Change input & output by clicking the widget you want modify, and you will see the config form. You can simply change the input & output by modify the corresponding textbox.
![alt text](https://github.com/Ien001/Running-script-in-Docker-tutorial/blob/master/figures/change%20param.png)
### 3.2. Change parameters
Similarly, you can change the parameters of any widget by modify the parameters directly in the config form.


## 4. Run Case study 1 & 2
### 4.1 Case study 1
After downloading the workflow for Case study 1, cilck "File" in the menu bar, and click "load workflow", then choose the downloaded workflow directory.
Then you should see our workflow for Case study 1 is loaded in Bwb.

!case study 1 workflow

After building the workflow, click "ReadAndPartition" widget and click "start", your workflow will start to run!

!case study 1 workflow running result

### 4.2 Case study 2
Similarly, you can load our workflow for Case study 2 in Bwb. 

!case study 2 workflow

After building the workflow, click "ReadAndPartition" widget and click "start", your workflow will start to run!

!case study 2 workflow running result
