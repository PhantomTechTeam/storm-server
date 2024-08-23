from os import environ
from fastapi import FastAPI
from models.topic import TopicInput
from models.topic_sse import TopicInputSSE
from models.pdf import PdfInput
from models.topic_serper import SerperInput
from routes import create_article, upload_pdf
from fastapi.responses import JSONResponse, StreamingResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = str(environ.get("ORIGINS")).split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/create-wiki-article/chatgpt35")
def create_wiki_article(topic_input: TopicInput):
    json_contents = create_article.create_article(
        topic=topic_input.topic, ai_model=topic_input.ai_model, retriever_model=topic_input.retriever_model
    )
    return JSONResponse(content=json_contents)


@app.post("/create-wiki-article/serper")
def create_wiki_article(topic_input: SerperInput):
    json_contents = create_article.create_article_serper(
        topic=topic_input.topic,
        query_params=topic_input.query_params,
        ai_model=topic_input.ai_model,
    )
    return JSONResponse(content=json_contents)


@app.post("/create-wiki-article/sse/serper")
def create_wiki_article(topic_input: SerperInput):
    json_contents = create_article.create_article_sse_serper(
        topic=topic_input.topic,
        query_params=topic_input.query_params,
        ai_model=topic_input.ai_model,
    )
    return StreamingResponse(json_contents, media_type="text/event-stream")

@app.post("/create-wiki-article/sse")
def create_wiki_article(topic_input: TopicInputSSE):
    json_contents = create_article.create_article_sse(
        topic=topic_input.topic,
        retriever_model=topic_input.retriever_model,
        ai_model=topic_input.ai_model,
        user_id=topic_input.user_id
    )
    return StreamingResponse(json_contents, media_type="text/event-stream")


@app.post("/create-pdf")
def create_pdf(pdf_input: PdfInput):
    pdf_data = upload_pdf.upload_pdf(
        content=pdf_input.content, user_id=pdf_input.user_id, topic=pdf_input.topic
    )

    return JSONResponse(content=pdf_data)
