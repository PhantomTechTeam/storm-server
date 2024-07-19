# storm-server

# What is this project?
## Context
This project is a server based implementation of [storm](https://github.com/stanford-oval/storm) which provides a way to perform web searches to simulate the process of creating a paper of sorts that can be used in academia or on Wikipedia.

## Technologies
FastAPI - Server framework of choice, very simple to set up and getting systems set up.

Conda - Package manager utilized in data science, similar to pip.

Helm - Templating system to help create kubernetes manfiests

Docker - Technology that creates containers that can be deployed to servers or ran within docker-compose to create a isolated network environment.


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
