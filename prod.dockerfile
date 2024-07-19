FROM  continuumio/miniconda3
RUN apt update

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY ./src $APP_HOME

RUN conda update --name base conda &&\
    conda env create --file storm_environment.yaml

RUN ["uvicorn", "main:app", "--host", "0.0.0.0"]
