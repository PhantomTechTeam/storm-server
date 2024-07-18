FROM  continuumio/miniconda3
LABEL Author, Amine HadjYoucef

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . $APP_HOME

# Prepare the environnement
RUN conda update --name base conda &&\
    conda env create --file environment.yaml
SHELL ["conda", "run", "--name", "app", "/bin/bash", "-c"]

ENTRYPOINT ["conda", "run", "--name", "app", "python", "main.py"]
