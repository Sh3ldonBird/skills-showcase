# Overview
The goal of this exercise is to showcase my skill in:
- Coding in python. [network-traffic.py](skills-showcase/python/network-traffic-simulation/network-traffic.py)
- Creating a Docker image for python development. [network-traffic-dockerfile.test](skills-showcase/python/network-traffic-simulation/network-traffic-dockerfile.test)
- Setting up a docker container from that image. 
- Analyzing the code ran within the image.

# This will be done by: 
## Step 1
Creating or editing pre-built code in python that has the specific use case of simulating network traffic that is being blocked by firewall code. 
[network-traffic.py](skills-showcase/python/network-traffic-simulation/network-traffic.py)
## Step 2:
Then creating dockerfile to copy the code into a docker image. 
[network-traffic-dockerfile.test](skills-showcase/python/network-traffic-simulation/network-traffic-dockerfile.test)
## Step 3:
To then building the custom docker image to then run as a development container that showcases the running code.
### Building the custom docker image
```Bash
docker build -t network-traffic:test -f network-traffic-dockerfile.test .
```
'docker' 'image build command' 'arguement? -t' 'image name to be' 'arguement -f?' 'docker file to use to build image' '. is the same directory to ??'
### Image Check
The command line will tell you if there is an error during the build though you can check additional details with
```Bash
docker images
```
### Run The Image
To finally run the image, use
```Bash
docker run -it network-traffic:test
```
'docker' 
'run command starts the container with the specified image'
'the '-it' argument shows and interactive shell to allow you to view the code ran at the start of the docker container.'
'specifies the image name'
## Step 4:
Code review to showcase what's happening on screen [code-review.md](python-firewall/traffic-simulation/code-review.md)
```Bash
IP: 192.168.1.3, Action: allow, Random: 9503
IP: 192.168.1.12, Action: allow, Random: 2391
IP: 192.168.1.8, Action: allow, Random: 4941
IP: 192.168.1.18, Action: allow, Random: 2367
IP: 192.168.1.12, Action: allow, Random: 8592
IP: 192.168.1.4, Action: block, Random: 8616
IP: 192.168.1.12, Action: allow, Random: 7708
IP: 192.168.1.9, Action: block, Random: 6352
IP: 192.168.1.18, Action: allow, Random: 2456
IP: 192.168.1.2, Action: allow, Random: 2404
IP: 192.168.1.16, Action: block, Random: 5907
IP: 192.168.1.5, Action: allow, Random: 4527
```
