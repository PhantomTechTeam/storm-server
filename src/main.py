from dotenv import load_dotenv
from fastapi import FastAPI
from models.topic import TopicInput
from routes import create_article
load_dotenv()  # Load environment variables from .env file

app = FastAPI()

@app.post("/create-wiki-article")
def create_wiki_article(topic_input: TopicInput):
    create_article.create_article(topic_input)
