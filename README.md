# Running-script-in-Docker-tutorial
This is a tutorial of Running script in Docker


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
install.packages("readr","dplyr","ggplot2","forcats")
``` 
Then, in the Dockerfile, we will add some commands:
```
RUN Rscript install_packages.R
```
Finally, we need to "tell" the new container image which scripts and data we need to use in the container, so we do "COPY" in the Dockerfile, which will copy the files to the new container image:
```
## copy Scripts and data
COPY myScript.R myScript.R
COPY us-500.csv us-500.csv
```
After these steps, we have finished the Dockerfile as below:
```
## Base image
FROM rocker/r-base:latest

## install R-packages
RUN Rscript install_packages.R

## copy Scripts and data
COPY myScript.R myScript.R
COPY us-500.csv us-500.csv
```
Remember to save these lines of command in file "Dockerfile".

Then, Docker build
```
docker build -t R/newimage .
```

Docker run
```
docker run -it --rm R/newimage
```

### 2.2 Python example






## 3. Run your script in your Docker container





## 4. Connect a widget to the container





## 5. Run the widget 

 We can use the “docker build” command to create a container from a Dockerfile, which is a container profile detailing which scripts and dependencies will be included in the container. For example, in order to run some python scripts inside the container, we will define the container python version in the Dockerfile by “FROM python:2.7” if we will use python2.7; to install dependencies of the python scripts, we will write “RUN pip install numpy pandas” in the Dockerfile to install “numpy” and “pandas” packages into the container we will build; “COPY Host_a.py Container_a.py” is to copy host python file “Host_a.py” to the container with name “Container_a.py”.
After configuring the dependencies and running scripts in the Dockerfile, we can use “docker build” command to build the container based on the Dockerfile.

## 6. Reference & Helpful link
https://www.r-bloggers.com/running-your-r-script-in-docker/
