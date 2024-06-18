#  RAD DIFF CHECK BACKEND
### Github links
Backend code: https://github.com/rishabbahal9/RADPAIR_ASSIGNMENT_BE

## Overview
Backend code is written in python with Flask framework. Single API endpoint is made to accept template id in dynamic url and for the sake of this project as per instructions, irrespective of the template id, report template as given in assignment is returned as String literal.

Endpoint can be accessed: `http://localhost:<port>/get-report-template`

## How to run code

To run this code with frontend complete, use docker-compose.yaml that has been sent on email with Readme.md document for reference. It takes care of everything.

### To run this code individually via docker

 1. Clone this repository
 2. Create .env file and populate as per .env.example
 3. Make sure Docker is active on your computer. Create an image using:
 ```shell
 docker build --tag python-docker .
 ```
4. Create a container and run with following command:
```shell
docker run -d -p <OUT PORT>:<IN PORT> python-docker
```

### To run this code individually without docker
1. Clone this repository
2. Download python 3.
3. Run the following command on terminal to install the dependencies:
	 ```shell 
	 pip3 install requirements.txt
	 ```
4. Create .env file and populate as per .env.example
5. To run the application use following commands:
	```shell
	python3 app.py
	```
6. You should be able to access the endpoint on `http://localhost:<out port>/get-report-template`
