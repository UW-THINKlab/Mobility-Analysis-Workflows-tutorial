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

### 2.2 Python example






## 3. Run your script in your Docker container





## 4. Connect a widget to the container





## 5. Run the widget 





 We can use the “docker build” command to create a container from a Dockerfile, which is a container profile detailing which scripts and dependencies will be included in the container. For example, in order to run some python scripts inside the container, we will define the container python version in the Dockerfile by “FROM python:2.7” if we will use python2.7; to install dependencies of the python scripts, we will write “RUN pip install numpy pandas” in the Dockerfile to install “numpy” and “pandas” packages into the container we will build; “COPY Host_a.py Container_a.py” is to copy host python file “Host_a.py” to the container with name “Container_a.py”.
After configuring the dependencies and running scripts in the Dockerfile, we can use “docker build” command to build the container based on the Dockerfile.
