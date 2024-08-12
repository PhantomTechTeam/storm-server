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

Create an env using this structure if using the OpenAI + you.com route:
```bash
OPENAI_API_KEY=<OPENAI_KEY>
YDC_API_KEY=<YOUCOM_KEY>
MAX_THREAD_NUM=3
MAX_CONV_TURN=3
MAX_PERSPECTIVE=3
SEARCH_TOP_K=3
OUTPUT_DIR=/opt/results
PDF_STORAGE=/opt/pdf
SUPABASE_URL=<SUPABASE_URL>
SUPABASE_KEY=<SUPABASE_SUBSCRIPTION_KEY>
SUPABASE_BUCKET=<SUPABASE_PUBLIC_BUCKET>
```

Create an env using this structure if using the Anthropic + Serper route: 
```bash
OUTPUT_DIR=/opt/results
PDF_STORAGE=/opt/pdf
SUPABASE_URL=<SUPABASE_URL>
SUPABASE_KEY=<SUPABASE_SUBSCRIPTION_KEY>
SUPABASE_BUCKET=<SUPABASE_PUBLIC_BUCKET>
ANTHROPIC_API_KEY=<ANTHROPIC_API_KEY>
ANTHROPIC_SIMULATOR_LM=claude-3-haiku-20240307
ANTHROPIC_ASKER_LM=claude-3-sonnet-20240229
ANTHROPIC_GEN_LM=claude-3-opus-20240229
ANTHROPIC_ARTICLE_GEN_LM=claude-3-opus-20240229
ANTHROPIC_POLISH_LM=claude-3-opus-20240229
SERPER_API_KEY=<SERPER_API_KEY>
```


Run the following command:
```sh
docker compose -f dev_docker_compose.yaml up --build
```

This will spin up the server, and will listen to your localhost instance on port 8000.

Navigate to localhost:8000/docs to see the routes. 

Run /create-wiki-article to create an article based off a topic, currently this uses chatgpt 3.5-turbo but will be updated in the future.

Run /create-pdf using the content portion of the previous api call to create a pdf that will be updated to supabase storage.


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
Let it finish setting up the cluster, and importing the images + helm chart. Once done, you can run kubectl get pods to see the api server running successfully.

## Where it is being used
[buildbuzz.ai](https://buildbuzz.ai)
## Citations
```bibtex
@inproceedings{shao2024assisting,
      title={{Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models}}, 
      author={Yijia Shao and Yucheng Jiang and Theodore A. Kanell and Peter Xu and Omar Khattab and Monica S. Lam},
      year={2024},
      booktitle={Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers)}
}
```

