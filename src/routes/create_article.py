from configs import storm
import os

def create_article(topic: str):
    from configs import argparser, you_com, file_parser, openai
    updated_topic = topic.replace(" ", "_").lower()
    
    open_ai_kwargs = openai.setup_openai_kwargs()

    openai.setup_gpt_3_5(open_ai_kwargs)

    print("Successfully set up openai!")
    
    engine_args = storm.setup_storm_engine_args(argparser.parser)
    print("Successfully retrieved engine_args!\n")

    rm = you_com.setup_you_rm(engine_args)

    print("Successfully got rm from you.com!\nRunning runner now!\n")

    output_dir = storm.run_runner(updated_topic, engine_args, rm)

    print("Finished running runner!\nParsing file now to send to frontend!\n")

    json_contents = file_parser.parse_file(output_dir)

    print("Fully parsed file, sending response back!\n")

    return json_contents


def create_article_serper(topic: str, query_params: dict[str, str]):
    from configs import argparser, serper, file_parser, anthropic
    
    anthropic.Anthropic(storm.lm_configs)

    print("Successfully set up claude!")

    engine_args = storm.setup_storm_engine_args(argparser.parser)

    serper_init = serper.Serper(query_params)

    print("Successfully retrieved engine_args!\n")

    print("Successfully got rm from serper.com!\nRunning runner now!\n")

    output_dir = storm.run_runner(topic, engine_args, serper_init.rm)
    files = os.listdir(output_dir)
    for file in files: 
        print(f"File: {file} in {output_dir}")
    print("Finished running runner!\nParsing file now to send to frontend!\n")

    json_contents = file_parser.parse_file(output_dir, topic, query_params.get("user_id"))

    print("Fully parsed file, sending response back!\n")

    return json_contents
