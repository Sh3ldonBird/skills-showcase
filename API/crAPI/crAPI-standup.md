# GOAL
The goal is to stand up a crAPI (completely ridiculous API) instance to showcase API, Python, & other skills.  

# Standup  
## Requirements  
crAPI requires the use of Docker compose < 1.27.0.  
I've stood up a standalone Ubuntu-Sever-LTS-24.04.1 server (192.168.1.15/24) for this use case and have installed Docker to the needed version.  
On the separate server I've created the directory API-testing to pull and edit the files within.  

Note: Because I've set up a separate VM already to use as a Docker host, I will not be using the option to create the VM with Vagrant.  
## Prep
```Bash 
cd / # root or wherever you want to create the directory.
mkdir API-testing
cd API-testing
docker-compose version # As long as docker-compose is 1.27.0 this will work.
docker compose up # in case docker isn't up and running already
```
```Bash
# Pulled from the crAPI README.md to pull the latest stable version.
curl -o docker-compose.yml https://raw.githubusercontent.com/OWASP/crAPI/main/deploy/docker/docker-compose.yml

docker-compose pull

docker-compose -f docker-compose.yml --compatibility up -d
```
The result should look similar to this.  
```Bash
doasbardsdo@docker-standalone:~/API-testing$ curl -o docker-compose.yml https://raw.githubusercontent.com/OWASP/crAPI/main/deploy/docker/docker-compose.yml

docker-compose pull

docker-compose -f docker-compose.yml --compatibility up -d
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  7512  100  7512    0     0  26434      0 --:--:-- --:--:-- --:--:-- 26357
Pulling postgresdb                  ... done
Pulling mongodb                     ... done
Pulling mailhog                     ... done
Pulling crapi-identity              ... done
Pulling crapi-community             ... done
Pulling crapi-workshop              ... done
Pulling crapi-web                   ... done
Pulling api.mypremiumdealership.com ... done
Creating network "api-testing_default" with the default driver
Creating volume "api-testing_mongodb-data" with default driver
Creating volume "api-testing_postgresql-data" with default driver
Creating mongodb                     ... done
Creating postgresdb                  ... done
Creating api.mypremiumdealership.com ... done
Creating mailhog                     ... done
Creating crapi-identity              ... done
Creating crapi-community             ... done
Creating crapi-workshop              ... done
Creating crapi-web                   ... done
```
I'm using the Docker management system "Portainer" alongside this to get a more visual representation as well. 
screenshot.todo

## Test
To test whether or not the download and standup was successful I visited http://192.168.1.15:8888.  
Connecting to http://192.168.1.15:8888 failed because the quickstart guide for docker assumes that the crAPI application is deployed locally, not to a remote server.  
To make it so the crAPI application can be accessed remotely from my workstation, I edited two entries within the docker-compose.yml file.  

The services section for "crapi-web" & "mailhog" needed to have it's "ports:" section edited.  
"crapi-web"  
- "${LISTEN_IP:-127.0.0.1}:8888:80"  
Changed to:  
- "${LISTEN_IP:-0.0.0.0}:8888:80"  
I left 443 alone for now as I haven't set up SSL/TLS just yet.  
#- "${LISTEN_IP:-127.0.0.1}:8443:443" # same treatment?  
"mailhog"  
- "${LISTEN_IP:-127.0.0.1}:8025:8025" # Mail ui  
Changed to:  
- "${LISTEN_IP:-0.0.0.0}:8025:8025"  

After making these changes I ran
`sudo docker compose -f docker-compose.yml --compatibility up -d'
to rebuild the applications containers with the updated networking.  
After, I was able to navigate to crAPI & mailhog services via http://192.168.1.15:8888 & http://192.168.1.15:8025  

## Process
I'm not sure if this is the full networking setup wi want to go with just yet. I haven't delved fully into the application yet to fully understand it's components and how they work together. 
While troubleshooting I was playing with the idea to create a custom Docker bridge network with the ip networking of 192.168.1.144/28 to allow the containers to have their own IP addresses on the same subnet
as the server rather than just port forwarding via NAT.  


 

