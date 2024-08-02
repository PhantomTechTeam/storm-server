from configs import openai, storm
def create_article_chatgpt35(topic: str):
    open_ai_kwargs = openai.setup_openai_kwargs()
    openai.setup_gpt_3_5(open_ai_kwargs)
    print("Successfully set up openai!")
    from configs import argparser, you_com, file_parser
    engine_args = storm.setup_storm_engine_args(argparser.parser, topic)
    print("Successfully retrieved engine_args!\n")
    rm = you_com.setup_you_rm(engine_args)
    print("Successfully got rm from you.com!\nRunning runner now!\n")
    storm.run_runner(topic, engine_args, rm)
    print("Finished running runner!\nParsing file now to send to frontend!\n")
    json_contents = file_parser.parse_file(topic)
    print("Fully parsed file, sending response back!\n")
    return json_contents

from configs import openai, storm, anthropic
def create_article_serper(topic: str):
    anthropic.setup_anthropic()
    print("Successfully set up openai and claude!")
    from configs import argparser, serper, file_parser
    engine_args = storm.setup_storm_engine_args(argparser.parser, topic)
    print("Successfully retrieved engine_args!\n")
    rm = serper.setup_serper_rm(engine_args)
    print("Successfully got rm from serper.com!\nRunning runner now!\n")
    storm.run_runner(topic, engine_args, rm)
    print("Finished running runner!\nParsing file now to send to frontend!\n")
    json_contents = file_parser.parse_file(topic)
    print("Fully parsed file, sending response back!\n")
    return json_contents
