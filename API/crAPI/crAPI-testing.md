# GOAL
To utilize Postman & Burpsuite Community Edition to showcase security vulnerabilities within the crAPI application.

# Requirements
## Workstation
[mitmproxy](https://mitmproxy.org/)  
[mitmweb](https://mitmproxy.org/)  
[mitmdump](https://mitmproxy.org/)  
[mitmproxy2swagger]()
[foxyproxy](https://addons.mozilla.org/en-US/firefox/addon/foxyproxy-standard/)  
[Postman](https://www.postman.com/downloads/)  
[Postman vsCode Extension](https://marketplace.visualstudio.com/items?itemName=Postman.postman-for-vscode)  
[Burpsuite Community Edition](https://portswigger.net/burp/releases/community/latest)  
Swagger Editor
ZAProxy? Maybe later  
## Docker Standalone Server
crAPI Application Remotely Accessible  

# Installation Prep
I [downloaded](https://mitmproxy.org/), installed mitmproxy suite, and added them to my systems environmental path.  
```Bash
# when in download directory
sudo tar -xvzf mitmproxy-11.0.2-linux-x86_64.tar.gz -C /usr/local/bin
# then ran mitmweb gui. default address is 127.0.0.1:8081
mitmweb
```
After which I installed the [foxyproxy](https://addons.mozilla.org/en-US/firefox/addon/foxyproxy-standard/) firefox add-on.  Then configured it to use 127.0.0.1:8080

Then configured mitmweb, http://127.0.0.1:8081/#/flows, to capture traffic at 127.0.0.1:8080.

Then installed [Postman](https://www.postman.com/downloads/)/[Postman vsCode Extension](https://marketplace.visualstudio.com/items?itemName=Postman.postman-for-vscode) after downloading the binaries and enabling it within vsCode.
```Bash
# within the download directory
sudo tar -xvzf postman-linux-x64.tar.gz -C /opt # to extract the downloaded application
sudo ln -s /opt/Postman/Postman /usr/bin/postman # to be able to open the app via commandline usijng 'Postman'
postman # to open the app
```
Then installed [Burpsuite Community Edition](https://portswigger.net/burp/releases/community/latest)  
```Bash
chmod +x burpsuite_community_linux_v2024_10_3.sh # to make the script executable
sudo ./burpsuite_community_linux_v2024_10_3.sh # to run the script to open the interactive installer
```

# Process
## Step 1
Run mitmweb and foxyproxy while interacting with the crAPI applications in it's various use cases to capture traffic.  
### Details


## Step 2
Export traffic capture by mitmweb to import it into Postman  
### Details
After interacting with the crAPI I saved the overall traffic. Then used the folowing command to create the yaml to import into Postman.
```Bash
# -i to specify flows file, -o to specify the output file, -p for the path to the API, -f for type of input
mitmproxy2swagger -i flows -o spec.yml -p http://localhost:8888/ -f flow
```
The goal is to sift through the ignore comments within the yml file to find the API endpoints.
?All paths without files at the end?

## Step 3
Burpsuite?  
### Details
