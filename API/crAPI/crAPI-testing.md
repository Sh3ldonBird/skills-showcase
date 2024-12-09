# GOAL
To utilize Postman & Burpsuite Community Edition to showcase security vulnerabilities within the crAPI application.

# Requirements
## Workstation
[mitmproxy](https://mitmproxy.org/)  
[mitmweb](https://mitmproxy.org/)  
[mitmdump](https://mitmproxy.org/)  
[mitmproxy2swagger](https://github.com/alufers/mitmproxy2swagger)
[python3]()
[python3-pip]()
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
Python3 is already installed on my system globally, though I needed to install pip3 & python3-venv for python package management to install mitmproxy2swagger to a python virtual environment.  I may use the docker method later, for now this will work.   
```Bash
sudo apt install python3-pip # to install pip3
sudo apt install python3-venv # to install python virtual environments
cd /API/crAPI # to navigate to where the venv will be created to line up with the .gitignore file
python3 -m venv mitmproxy2swagger-venv # to create a python3 virtual environment for mitmproxy2swagger
source mitmproxy2swagger-venv/bin/activate # to activate the virtual environment
pip install mitmproxy2swagger # to install mitmproxy2swagger within the venv
```
# Process
## Step 1
Run mitmweb and foxyproxy while interacting with the crAPI applications in it's various use cases to capture traffic.  
### Notes Interacting With The crAPI App
Started mitmweb by running `mitmweb` and started foxy proxy by switching to the pre-configured proxy within the extension.  
Navigated to http://192.168.1.15:8080 for the crAPI app & http://192.168.1.15:8025 for the mailhog instance.  
Created username & password within the crAPI portal & confirmed the email within the mailhog instance.  
After logging in i selected to add a car after being prompted to do so. It requested a pin code & VIN number which were provided within the mailhog email.  
When entered I was shown that I'm the proud owner of a Lamborghini Aventador. Firefox also is detecting a MITM(Man-in-the-middle) attack because I haven't fully set up the mitmproxy certificate yet. I believe this is for the google map locator.  
I've also selected "Contact Mechanic." My Lambo's VIN (5PYLL95LVWY627034) is prepopulated, I've selected the mechanic "TRAC_JME," and have provided the Problem Description: "I wanted a teal Lambo not a black one." Not really a mechanic's issue, but this is a test.  
I've reset the password next by selecting the prompt in the top right and entering in my password twice. It accepted the same password as my first password without error.
I navigated to the "shop" in the top left. I bought the $Wheel, $10
After backing out of "past orders" I selected community in the top left to view crAPI's forum.
I selected the first post by Adam and commented "howdy."  
I navigated back to the dashboard and then logged out.

## Step 2
Export traffic capture by mitmweb to import it into Postman  
### Details
After interacting with the crAPI I saved the overall traffic to a "flows" file. Then used the folowing command to create the yaml to import into Postman.
```Bash
# -i to specify flows file, -o to specify the output file, -p for the path to the API, -f for type of input
mitmproxy2swagger -i flows -o spec.yml -p http://localhost:8888/ -f flow
```
The goal is to sift through the ignore comments within the yml file to find the API endpoints.
?All paths without files at the end?

## Step 3
Burpsuite?  
### Details
