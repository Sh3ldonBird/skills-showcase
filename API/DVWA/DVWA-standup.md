# GOAL
The goal is to stand up the [DVWA](https://github.com/digininja/DVWA) via docker on my standalone(not swarm) Docker host with the IP of 192.168.1.15.  

# Standup
## Requirements
DVWA requires Docker compose version < ?. It just needs to be installed?  
clone of `git clone https://github.com/digininja/DVWA.git`  

## Prep

While connected to my remote Docker host from my workstation.
```Bash
# create directory to clone the DVWA application into
cd /
mkdir DVWA-testing
cd DVWA-testing
git clone https://github.com/digininja/DVWA.git # clones repo needed to build Docker images
cd DVWA # navigates the terminal into the DVWA directory
docker-compose version # makes sure Docker & Docker compose is intalled
```
Because I'm running the DVWA from a remote Docker host I will need to make changes to the compose.yml file & build policy.
I'm not sure if I need to change the build policy [options](https://github.com/compose-spec/compose-spec/blob/main/05-services.md#pull_policy).  
From
```YML
pull_policy: always
ports:
  - 127.0.0.1:4280:80
```
to
```YML
pull_policy: build
ports:
  - 0.0.0.0:4280:80
```
Then 
```Bash
docker compose up -d # runs Docker compose to build the Docker images
```
## Test
After changing the compose.yml and running the build comands I was able to navigate the DVWA at http://192.168.1.15:4280/login.php  


