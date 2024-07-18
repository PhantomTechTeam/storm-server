from fastapi.responses import JSONResponse
from ..configs import openai, storm
from ..models.topic import TopicInput
def create_article(topic_input: TopicInput):
    # open_ai_kwargs = openai.setup_openai_kwargs()
    # openai.setup_gpt_3_5(open_ai_kwargs)
    # print("Successfully set up openai!")
    from ..configs import argparser, you_com, file_parser
    # engine_args = storm.setup_storm_engine_args(argparser.parser)
    # print("Successfully retrieved engine_args!\n")
    # rm = you_com.setup_you_rm(engine_args)
    # print("Successfully got rm from you.com!\nRunning runner now!\n")
    # storm.run_runner(topic_input.topic, engine_args, rm)
    print("Finished running runner!\nParsing file now to send to frontend!\n")
    json_contents = file_parser.parse_file(topic_input.topic)
    print("Fully parsed file, sending response back!\n")
    return JSONResponse(content=json_contents)
