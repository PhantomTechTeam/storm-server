from dotenv import load_dotenv
from fastapi import FastAPI
from models.topic import TopicInput
from models.pdf import PdfInput
from routes import create_article, upload_pdf
from fastapi.responses import JSONResponse
load_dotenv()  # Load environment variables from .env file

app = FastAPI()

@app.post("/create-wiki-article")
def create_wiki_article(topic_input: TopicInput):
     json_contents  = create_article.create_article(topic=topic_input.topic)
     return JSONResponse(content=json_contents)

@app.post("/create-pdf")
def create_pdf(pdf_input: PdfInput):
    pdf_data = upload_pdf.upload_pdf(content=pdf_input.content, user_id=pdf_input.user_id, topic=pdf_input.topic)
    return JSONResponse(content=pdf_data)
