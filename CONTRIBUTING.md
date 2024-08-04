# Where to begin?
Prerequisites:
- Visual Studio Code or Cursor.
- Docker.
- This repository cloned on your local machine.
- Pick up an issue on the issues board, feel free to ask follow up questions to the one who created the issue to begin requirement gathering.
  
After the prerequisites have been met, start up Visual Studio Code on your local machine. 
A prompt asking that a devcontainer is found in the folder will show up, click to allow it to be launched as a devcontainer.

It will take some time for the image to be pulled, after it has been completed ohmyzash will be installed and ready to be used.

The docker-compose file is provided for ease of development.

To utilize it, run this command:
```sh
docker-compose -f dev_docker_compose.yaml up --build
```
Upon the image being built, docker will now watch for the src directory to be changed then will make the appropriate updates. 
If env variables are updated or created, the docker process will have to be stopped with ctrl+z then re-ran with the docker-compose up command.

# Project structure
This project is a FastAPI based project that is contained in the src/ folder and is split into multiple parts.
| Folder name    | What it does |
| -------- | ------- |
| configs  | Contains all the config code that will be utilized, loads up the various rms + lms that will be used by storm.    |
| models | Models used to parse json payload provided by user, recommended to create new models to ensure consistency of paylod behavior.     |
| routes    | Contains all the various routes that will be called by the user.   |

# Expectations
This project is currently ongoing and growing as more features are suggested.
It is recommended in the config folder to focus on utilizing classes and object oriented principals.
Currently those portions are being rewritten to follow these standards.

It recommended to run the code through a code-formatter once work has been completed. 
Black has been provided in the requirements.txt, to utilize it use this command:
```
black format .
```
to format the current directory + sub directories.

# Contact
PhantomTech has a community discord for our open source projects here:
https://discord.gg/HqhSvX9Vsf
Feel free to join to put suggestions/features, as well as ask for guidance and suggestions.
