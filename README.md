# storm-server

# What is this project?
## Context
This project is a server based implementation of [storm](https://github.com/stanford-oval/storm) which provides a way to perform web searches to simulate the process of creating a paper of sorts that can be used in academia or on Wikipedia.

## Technologies
FastAPI - Server framework of choice, very simple to set up and getting systems set up.

Conda - Package manager utilized in data science, similar to pip.

Helm - Templating system to help create kubernetes manfiests

Docker - Technology that creates containers that can be deployed to servers or ran within docker-compose to create a isolated network environment.

DevContainers - Allows a docker image to be loaded, acting as an ethermal environment.
## Running
### Docker Compose
To run using Docker compose, make sure both [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/install/) are both installed and properly running.

Update dev_docker_compose.yaml environment variables with the various keys and variables needed.

Run the following command:
```sh
docker compose -f dev_docker_compose.yaml up --build
```

This will spin up the server, and will listen to your localhost instance on port 8000.

Navigate to localhost:8000/docs to see the routes

## Credits
This project wouldn't be possible without the [storm team](https://github.com/stanford-oval/storm) who created and maintain the python package.

### K8s
Using Visual Studio Code, open up the project. Ensure that docker is installed. 

A pop up should pop up letting you know that the folder containers a .devcontainer, select to open up Visual Studio Code using the DevContainer. 
Let it extract the docker image.

Once it has been set up, click on the bash terminal to open up an ohmyzash instance. From here, run the following command:
```bash
make create-cluster
```
Let it finish setting up the cluster, and importing the images + manifests. Once done, you can run kubectl get pods to see the api server running successfully.

