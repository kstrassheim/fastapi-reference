# Fast-API Reference App
The app is creating a debugable combination between Fast-API and Vite (React). A preview can viewed on https://fast-api-reference.azurewebsites.net/ 
## Purpose detail
The app which fulfills the following requirements for a 
- Quick to initialize
- Debug with breakpoints of Frontend and Backend and just in time compiler
- Debug by starting F5 in VSCode (Starting chrome also)
- Deployment of a productive version with precompiled frontend server
- Deployment to Azure App Service Free Plan with Actions on Pull Request

## Prerequisites
1. The app requires python3 to be installed on the machine with venv. To install it on on Ubuntu (WSL) just type. On Windows just download the installer for python.
```
sudo apt update
sudo apt install python3 python3-venv python3-pip
```
2. Then clone the repository
3. Go into the backend folder `cd ./backend`
4. init venv by typing


## Azure Web App Setup

In Settings/Configuration your have to setup the Startup Command as
```
gunicorn --worker-class uvicorn.workers.UvicornWorker --timeout 600 --access-logfile '-' --error-logfile '-' main:app
```