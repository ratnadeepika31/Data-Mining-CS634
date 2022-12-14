### Transfer Learning for Custom Datasets in the Small-Data Regime for Basement

# Milestone 1: Environment Preparation
First step is to install a data anotation tool CVAT locally in our laptop.The document below cointains instruction for insalling on MAC OS with following system specifictions :
|  |   |
|--|--|
| Processer | 6-Core Intel i7  |
|Processer Speed|2.6 Ghz|
|Memory|16GB|
|System Version|macOS 12.4|
|Kernal Version|Darwin 21.5.0|


## Quick installation guide
### Install and run Docker Desktop on Mac

 1. Downloaded `Docker.dmg` from this [link](https://desktop.docker.com/mac/main/amd64/Docker.dmg?utm_source=docker&utm_medium=webreferral&utm_campaign=docs-driven-download-mac-amd64)
 2. Double-click  `Docker.dmg`  to open the installer, then drag the Docker icon to the Applications folder.
 3. Double-click  `Docker.app`  in the  **Applications**  folder to start Docker.
 4. The Docker menu (![whale menu](https://docs.docker.com/desktop/install/images/whale-x.svg)) displays the Docker Subscription Service Agreement window. Select **Accept** to continue. 
 5. Docker Desktop starts after you accept the terms.

### Install Git
For me I already had `git` installed. If you don’t have it installed already you can find instructions  [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

### Download and install Google Chrome
Google Chrome is the only browser which is supported by CVAT.

 1. Go to [Download Chrome](https://www.google.com/chrome/)
 2. Click Download Chrome.
 3. Double-click  `GoogleChrome.dmg`  to open the installer, then drag the Google Chrome icon to the Applications folder.
 4. Double-click  `GoogleChrome.app`  in the  **Applications**  folder to start Google Chrome.

### Installing CVAT

 1. Open a terminl Window.
 2. Clone  _CVAT_  source code from the  [GitHub repository](https://github.com/opencv/cvat)  with Git. The following command will clone the latest develop branch:
  ```shell
git clone https://github.com/opencv/cvat
```
3. Move into _CVAT_ folder .
```shell
cd cvat
```
4. Run docker containers. It will take some time to download the latest CVAT release and other required images like postgres, redis, etc. from DockerHub and create containers.
 ```shell
    docker-compose up -d
   ```
5. You can register a user but by default it will not have rights even to view list of tasks. Thus you should create a superuser. A superuser can use an admin panel to assign correct groups to other users. Please use the command below:
```shell
docker exec -it cvat_server bash -ic 'python3 ~/manage.py createsuperuser'
```
6. Choose a username and a password for your admin account.
7. Open the installed Google Chrome browser and go to [localhost:8080](http://localhost:8080/). Type your login/password for the superuser on the login page and press the _Login_ button. Now you should be able to create a new annotation task.
#### Login Page
<p align="center">
  <img src="https://i.ibb.co/sC4QpPf/bfcb2be8-f9d6-4cd8-bad5-df1a83dbd076.jpg" />
</p>

#### Home Page
<p align="center">
  <img src="https://i.ibb.co/VBTNJNH/ac3e0527-e58f-4928-bec7-69b0da1ab52b.jpg" />
</p>