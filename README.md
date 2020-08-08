# Running-script-in-Docker-tutorial
This is a tutorial of running our own scripts in Docker container and building widgets and workflows using Biodepot-workflow-builder(Bwb). In this tutorial, we will use *App_data repository* as an example to give a step-bystep guide of building containers, later widgets, and workflows. Finially, we will reproduce the workflow in the paper: XXX
## 1. Try our AWS
You can quickly try our built workflow through AWS: XXX

fig of Bwb portal

You can simply click XXX module(widget) and click "start", then the workflow will run and you will have result like this:

fig of result

If you want to learn more about the workflow and widget, please read on or refer to: https://github.com/BioDepot/BioDepot-workflow-builder

## 2. Download App_data code
App_data repository is the code to handle mobility data(cellular and GPS data).
In order to continue further steps, please download the repository by:
```
git clone https://github.com/UW-THINKlab/app-data
```
## 3. Build Docker container
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
### 3.2. Write Dockerfile and build your Docker container with the scripts / pull ours
### 3.3. Run the scripts in your Docker container

## 4. Run Bwb

## 5. build widgets
### 5.1 widget 1
### 5.2 widget 2

## 6. workflow / load ours






## 1. Install Docker
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
## 2. Write Dockerfile and build your Docker container with scripts (R/Python)
Dockerfile is a container profile detailing which scripts and dependencies will be included in the container.

### 2.1 R example
First, Pull a container image(Linux) which have R installed from the Rocker DockerHub repository. This image will serve as base image when we build the new container image.
```
docker pull rocker/r-base
```
In the Dockerfile, simply a text file named "Dockerfile" without any extension name, we will add some commands:
```
FROM rocker/r-base:latest
```
which means create a new container image from a base image. 

Second, we need to know which script we would like to be ran inside the container. 

In this example, under "R example" folder, we will run "myScript.R" inside the container.

Below are showing that, in "myScript.R", we need library "readr", "dplyr", "ggplot2", "forcats".
```
library(readr)
library(dplyr)
library(ggplot2)
library(forcats)
```
In order to "tell" the new container image to install these packages, we will have another Rscript, "install_packages.R". (Shown as below.)
```
install.packages("readr",repos = "http://cran.us.r-project.org")
install.packages("dplyr",repos = "http://cran.us.r-project.org")
install.packages("ggplot2",repos = "http://cran.us.r-project.org")
install.packages("forcats",repos = "http://cran.us.r-project.org")
``` 
Then, in the Dockerfile, we will add some commands:
```
RUN Rscript install_packages.R
```
Finally, we need to "tell" the new container image which scripts and data we need to use in the container, so we do "COPY" in the Dockerfile, which will copy the files to the new container image:
```
# Create new directory in th container image
RUN mkdir -p /output
## copy Scripts and data
COPY install_packages.R install_packages.R
COPY myScript.R myScript.R
COPY us-500.csv us-500.csv
```
After these steps, we have finished the Dockerfile as below:
```
## Base image
FROM rocker/r-base:latest

# Create new directory in th container image
RUN mkdir -p /output
## copy Scripts and data
COPY install_packages.R install_packages.R
COPY myScript.R myScript.R
COPY us-500.csv us-500.csv

## install R-packages
RUN Rscript install_packages.R
```
Remember to save these lines of command in file "Dockerfile".

Then, it's time build our container image!

Under directory "R_example", use command:
```
docker build -t r/newimage .
```
'-t' is giving a tag to the container image.

Test the container image:
```
docker run -it --rm r/newimage
```
This command will launch a container instance from the container image, then lead us to R interactive mode of the container image. At the end, the instance will be removed. 
### 2.2 Python example
## 3. Run your script in your Docker container
### 3.1 R example
Different from previous command, we add "-v" in the "docker run" command, which will map a host directory to a container directory. In the command below, we map current directory to "/output" directory of the container, then we will run "Rscript myScript.R" insider the container. Finally, in your current directory, the result from "myScript.R" will be generated.
```
docker run -i --rm -v ${PWD}:/output r/newimage Rscript myScript.R
```
### 3.2 Python example

## 4. Connect a widget to the container / Create a widget
### 4.1 Launch Biodepot-workflow-builder(Bwb)
Go to https://github.com/BioDepot/BioDepot-workflow-builder, and pull this repo to your computer, then run:
```
docker run --rm   -p 6080:6080 \
    -v  ${PWD}/:/data  \
    -v  /var/run/docker.sock:/var/run/docker.sock \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    --privileged --group-add root \
    biodepot/bwb
```
After the Bwb container is launched, go to link: http://localhost:6080/. (This is a visualizable platform of Bwb.)
### 4.2 Following video tutorial to create your first widget
Video link: https://www.youtube.com/watch?v=hqCr2Cs6EBQ. \
In this tutorial, you can learn how to create a widget with a container image, that is, to connect the container image to the widget you created. \
You can also learn to create a widget using python/R container image!

## 5. Reference & Helpful link
https://www.r-bloggers.com/running-your-r-script-in-docker/
https://www.youtube.com/watch?v=hqCr2Cs6EBQ

