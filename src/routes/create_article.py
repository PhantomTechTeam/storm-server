from configs import storm, argparser, file_parser
import os
import json


def create_article(topic: str, ai_model: str, retriever_model: str):
    match ai_model:
        case "gpt-3.5":
            from configs.llms import openai

            open_ai_kwargs = openai.setup_openai_kwargs()
            openai.setup_gpt_3_5(open_ai_kwargs)
            print("Successfully set up openai!")
        case "gpt-4-o":
            from configs.llms import openai

            openai.setup_gpt_4_o(open_ai_kwargs)
            print("Successfully set up openai!")
        case "mixed-openai":
            from configs.llms import openai

            openai.setup_mix_gpt(open_ai_kwargs)
            print("Successfully set up openai!")
        case "claude":
            from configs.llms import anthropic

            anthropic.Anthropic(storm.lm_configs)
            print("Successfully set up claude!")
        case "ollama":
            from configs.llms import ollama

            ollama_kwargs = {
                "model": os.getenv("OLLAMA_MODEL"),
                "port": os.getenv("OLLAMA_PORT"),
                "url": os.getenv("OLLAMA_URL"),
                "stop": ("\n\n---",),
            }
            ollama.Ollama(ollama_kwargs=ollama_kwargs)
        case _:
            raise ValueError(f"Invalid ai_model: {ai_model}")

    engine_args = storm.setup_storm_engine_args(argparser.parser)

    print("Successfully retrieved engine_args!\n")

    match retriever_model:
        case "brave":
            from configs.rms import brave

            rm = brave.Brave(engine_args).rm
            print("Successfully set up brave rm!\n")
        case "you":
            from configs.rms import you_com

            rm = you_com.You(engine_args).rm
            print("Successfully set up you rm!\n")
        case "searxng":
            from configs.rms import searxng

            rm = searxng.SearXNGRM(engine_args).rm
        case "duckduckgo":
            from configs.rms import duckduckgo

            rm = duckduckgo.DuckDuckGoSearch(engine_args).rm
        case _:
            print("Did not select any of the custom retrieval models!")

    print("Running runner now!")
    output_dir = storm.run_runner(topic, engine_args, rm)

    print("Finished running runner!\nParsing file now to send to frontend!\n")

    json_contents = file_parser.parse_file(output_dir)

    print("Fully parsed file, sending response back!\n")

    return json_contents


def create_article_serper(topic: str, query_params: dict[str, str], ai_model: str):
    from configs import argparser, serper, anthropic, openai, file_parser

    match ai_model:
        case "gpt-3.5":
            from configs.llms import openai

            open_ai_kwargs = openai.setup_openai_kwargs()
            openai.setup_gpt_3_5(open_ai_kwargs)
            print("Successfully set up openai!")
        case "gpt-4-o":
            from configs.llms import openai

            openai.setup_gpt_4_o(open_ai_kwargs)
            print("Successfully set up openai!")
        case "mixed-openai":
            from configs.llms import openai

            openai.setup_mix_gpt(open_ai_kwargs)
            print("Successfully set up openai!")
        case "claude":
            from configs.llms import anthropic

            anthropic.Anthropic(storm.lm_configs)
            print("Successfully set up claude!")
        case "ollama":
            from configs.llms import ollama

            ollama_kwargs = {
                "model": os.getenv("OLLAMA_MODEL"),
                "port": os.getenv("OLLAMA_PORT"),
                "url": os.getenv("OLLAMA_URL"),
                "stop": ("\n\n---",),
            }
            ollama.Ollama(ollama_kwargs=ollama_kwargs)
        case _:
            raise ValueError(f"Invalid ai_model: {ai_model}")

    engine_args = storm.setup_storm_engine_args(argparser.parser)

    serper_init = serper.Serper(query_params)

    print("Successfully retrieved engine_args!\n")

    print("Successfully got rm from serper.com!\nRunning runner now!\n")

    output_dir = storm.run_runner(topic, engine_args, serper_init.rm)
    files = os.listdir(output_dir)
    for file in files:
        print(f"File: {file} in {output_dir}")
    print("Finished running runner!\nParsing file now to send to frontend!\n")

    json_contents = file_parser.parse_file(output_dir)

    print("Fully parsed file, sending response back!\n")

    return json_contents


def create_article_sse_serper(topic: str, query_params: dict[str, str], ai_model: str):
    try:
        from configs import argparser
        from configs.rms import serper
        from shutil import rmtree
        from collections import OrderedDict
        import uuid
        from datetime import datetime
        from knowledge_storm import (
            STORMWikiRunner,
            STORMWikiLMConfigs,
            STORMWikiRunnerArguments,
        )
        from supabase import create_client, Client

        lm_configs = STORMWikiLMConfigs()
        match ai_model:
            case "gpt-3.5":
                from configs.llms import openai

                open_ai_kwargs = openai.setup_openai_kwargs()
                openai.setup_gpt_3_5(open_ai_kwargs)
                print("Successfully set up openai!")
            case "gpt-4-o":
                from configs.llms import openai

                openai.setup_gpt_4_o(open_ai_kwargs)
                print("Successfully set up openai!")
            case "mixed-openai":
                from configs.llms import openai

                openai.setup_mix_gpt(open_ai_kwargs)
                print("Successfully set up openai!")
            case "claude":
                from configs.llms import anthropic

                anthropic.Anthropic(storm.lm_configs)
                print("Successfully set up claude!")
            case "ollama":
                from configs.llms import ollama

                ollama_kwargs = {
                    "model": os.getenv("OLLAMA_MODEL"),
                    "port": os.getenv("OLLAMA_PORT"),
                    "url": os.getenv("OLLAMA_URL"),
                    "stop": ("\n\n---",),
                }
                ollama.Ollama(ollama_kwargs=ollama_kwargs)
            case _:
                raise ValueError(f"Invalid ai_model: {ai_model}")

        yield json.dumps(
            {
                "event_id": 1,
                "message": "Have successfully set up llm provider",
                "current_progress": "10",
                "is_done": False,
                "status_code": 200,
            }
        ) + "\n\n"
        output_dir_original = argparser.parser.get("output_dir")

        # Check out the STORMWikiRunnerArguments class for more configurations.
        engine_args = STORMWikiRunnerArguments(
            output_dir=f"{output_dir_original}",
            max_conv_turn=int(str(argparser.parser.get("max_conv_turn"))),
            max_perspective=int(
                str(
                    argparser.parser.get("max_perspective"),
                )
            ),
            search_top_k=int(str(argparser.parser.get("search_top_k"))),
            max_thread_num=int(str(argparser.parser.get("max_thread_num"))),
        )
        print("Successfully set up engine args")
        serper_init = serper.Serper(query_params)

        print("Successfully got rm from serper.com!\nRunning runner now!\n")
        yield json.dumps(
            {
                "event_id": 2,
                "message": "Have successfully set up search provider, running storm runner now",
                "current_progress": "20",
                "is_done": False,
                "status_code": 200,
            }
        ) + "\n\n"

        runner = STORMWikiRunner(engine_args, lm_configs, serper_init.rm)
        runner.run(
            topic=topic,
            do_research=True,
            do_generate_article=True,
            do_polish_article=True,
        )
        print("Have successfully finished the running process")
        runner.post_run()
        print("Have successfully finished the article generation process")
        yield json.dumps(
            {
                "event_id": 3,
                "message": "Have successfully finished the article generation process",
                "current_progress": "50",
                "status_code": 200,
                "is_done": False,
            }
        ) + "\n\n"
        runner.summary()

        directory = runner.article_output_dir
        print(directory)
        yield json.dumps(
            {
                "event_id": 4,
                "message": "Have finished summerizing article, beginning process to format article content",
                "current_progress": "80",
                "is_done": False,
                "status_code": 200,
            }
        ) + "\n\n"
        print("Finished running runner!\nParsing file now to send to frontend!\n")

        try:
            content = []

            with open(f"{directory}/storm_gen_article_polished.txt", "r+") as f:
                content.append(str(f.read()))

            escapable_str_with_comma = '","'

            escapable_str_without_comma = '"'

            double_escapes = "\n\n"

            final_results = (
                "".join(content)
                .replace(escapable_str_with_comma, "")
                .replace(double_escapes, "\n")
                .replace(escapable_str_without_comma, "")
            )

            with open(f"{directory}/url_to_info.json", "r+") as f:
                data = json.load(f)

            url_unified_index = data.get("url_to_unified_index")

            urls_to_unified_indexes = {}

            for url, unified_index in url_unified_index.items():
                if unified_index not in urls_to_unified_indexes.keys():
                    urls_to_unified_indexes[unified_index] = url

            rmtree(directory)
            if os.environ.get("PDF_STORAGE_SERVICE") == "supabase":
                yield json.dumps(
                    {
                        "event_id": 5,
                        "message": "Updating article in database",
                        "current_progress": "90",
                        "status_code": 200,
                        "is_done": False,
                    }
                ) + "\n\n"
                try:
                    url: str = os.environ.get("SUPABASE_URL")
                    key: str = os.environ.get("SUPABASE_KEY")
                    supabase_client: Client = create_client(url, key)
                    custom_uuid = uuid.uuid4()
                    supabase_client.table("storm_generation").insert(
                        {
                            "content": final_results,
                            "title": topic,
                            "user_id": query_params.get("user_id"),
                            "url_to_unified_index": OrderedDict(
                                sorted(urls_to_unified_indexes.items())
                            ),
                            "id": str(custom_uuid),
                            "pdf_url": "",
                            "created_at": datetime.now().isoformat(),
                        }
                    ).execute()
                    yield json.dumps(
                        {
                            "event_id": 6,
                            "message": "Have successfully uploaded to db, sending article content back",
                            "current_progress": "100",
                            "status_code": 200,
                            "is_done": True,
                            "id": str(custom_uuid),
                        }
                    ) + "\n\n"
                except Exception as e:
                    yield json.dumps(
                        {
                            "event_id": 6,
                            "message": f"Failed to upload article to database: {str(e)}",
                            "current_progress": "0",
                            "status_code": 500,
                            "is_done": False,
                        }
                    ) + "\n\n"
        except Exception as e:
            yield json.dumps(
                {
                    "event_id": 5,
                    "message": f"Failed parsing file, error is: {e}",
                    "current_progress": "0",
                    "status_code": 500,
                    "is_done": False,
                }
            ) + "\n\n"
        print("Fully parsed file, sending response back!\n")
    except Exception as e:
        print("Error in create_article_sse_serper: ", e)
        yield json.dumps(
            {
                "event_id": 1,
                "message": "Failed to create article",
                "current_progress": "0",
                "is_done": True,
                "status_code": 500,
            }
        ) + "\n\n"


def create_article_sse(topic: str, ai_model: str, retriever_model: str, user_id: str):
    try:
        from configs import argparser
        from shutil import rmtree
        from collections import OrderedDict
        import uuid
        from datetime import datetime
        from knowledge_storm import (
            STORMWikiRunner,
            STORMWikiLMConfigs,
            STORMWikiRunnerArguments,
        )
        from supabase import create_client, Client

        lm_configs = STORMWikiLMConfigs()
        match ai_model:
            case "gpt-3.5":
                from configs.llms import openai

                open_ai_kwargs = openai.setup_openai_kwargs()
                openai.setup_gpt_3_5(open_ai_kwargs)
                print("Successfully set up openai!")
            case "gpt-4-o":
                from configs.llms import openai

                openai.setup_gpt_4_o(open_ai_kwargs)
                print("Successfully set up openai!")
            case "mixed-openai":
                from configs.llms import openai

                openai.setup_mix_gpt(open_ai_kwargs)
                print("Successfully set up openai!")
            case "claude":
                from configs.llms import anthropic

                anthropic.Anthropic(storm.lm_configs)
                print("Successfully set up claude!")
            case "ollama":
                from configs.llms import ollama

                ollama_kwargs = {
                    "model": os.getenv("OLLAMA_MODEL"),
                    "port": os.getenv("OLLAMA_PORT"),
                    "url": os.getenv("OLLAMA_URL"),
                    "stop": ("\n\n---",),
                }
                ollama.Ollama(ollama_kwargs=ollama_kwargs)
            case _:
                raise ValueError(f"Invalid ai_model: {ai_model}")

        yield json.dumps(
            {
                "event_id": 1,
                "message": "Have successfully set up llm provider",
                "current_progress": "10",
                "is_done": False,
                "status_code": 200,
            }
        ) + "\n\n"
        output_dir_original = argparser.parser.get("output_dir")

        # Check out the STORMWikiRunnerArguments class for more configurations.
        engine_args = STORMWikiRunnerArguments(
            output_dir=f"{output_dir_original}",
            max_conv_turn=int(str(argparser.parser.get("max_conv_turn"))),
            max_perspective=int(
                str(
                    argparser.parser.get("max_perspective"),
                )
            ),
            search_top_k=int(str(argparser.parser.get("search_top_k"))),
            max_thread_num=int(str(argparser.parser.get("max_thread_num"))),
        )
        print("Successfully set up engine args")
        match retriever_model:
            case "brave":
                from configs.rms import brave

                rm = brave.Brave(engine_args).rm
                print("Successfully set up brave rm!\n")
            case "you":
                from configs.rms import you_com

                rm = you_com.You(engine_args).rm
                print("Successfully set up you rm!\n")
            case "searxng":
                from configs.rms import searxng

                rm = searxng.SearXNGRM(engine_args).rm
            case "duckduckgo":
                from configs.rms import duckduckgo

                rm = duckduckgo.DuckDuckGoSearch(engine_args).rm
            case _:
                print("Did not select any of the custom retrieval models!")
                exit()
        yield json.dumps(
            {
                "event_id": 2,
                "message": "Have successfully set up search provider, running storm runner now",
                "current_progress": "20",
                "is_done": False,
                "status_code": 200,
            }
        ) + "\n\n"

        runner = STORMWikiRunner(engine_args, lm_configs, rm)
        runner.run(
            topic=topic,
            do_research=True,
            do_generate_article=True,
            do_polish_article=True,
        )
        print("Have successfully finished the running process")
        runner.post_run()
        print("Have successfully finished the article generation process")
        yield json.dumps(
            {
                "event_id": 3,
                "message": "Have successfully finished the article generation process",
                "current_progress": "50",
                "status_code": 200,
                "is_done": False,
            }
        ) + "\n\n"
        runner.summary()

        directory = runner.article_output_dir
        print(directory)
        yield json.dumps(
            {
                "event_id": 4,
                "message": "Have finished summerizing article, beginning process to format article content",
                "current_progress": "80",
                "is_done": False,
                "status_code": 200,
            }
        ) + "\n\n"
        print("Finished running runner!\nParsing file now to send to frontend!\n")

        try:
            content = []

            with open(f"{directory}/storm_gen_article_polished.txt", "r+") as f:
                content.append(str(f.read()))

            escapable_str_with_comma = '","'

            escapable_str_without_comma = '"'

            double_escapes = "\n\n"

            final_results = (
                "".join(content)
                .replace(escapable_str_with_comma, "")
                .replace(double_escapes, "\n")
                .replace(escapable_str_without_comma, "")
            )

            with open(f"{directory}/url_to_info.json", "r+") as f:
                data = json.load(f)

            url_unified_index = data.get("url_to_unified_index")

            urls_to_unified_indexes = {}

            for url, unified_index in url_unified_index.items():
                if unified_index not in urls_to_unified_indexes.keys():
                    urls_to_unified_indexes[unified_index] = url

            rmtree(directory)
            if os.environ.get("PDF_STORAGE_SERVICE") == "supabase":
                yield json.dumps(
                    {
                        "event_id": 5,
                        "message": "Updating article in database",
                        "current_progress": "90",
                        "status_code": 200,
                        "is_done": False,
                    }
                ) + "\n\n"
                try:
                    url: str = os.environ.get("SUPABASE_URL")
                    key: str = os.environ.get("SUPABASE_KEY")
                    supabase_client: Client = create_client(url, key)
                    custom_uuid = uuid.uuid4()
                    supabase_client.table("storm_generation").insert(
                        {
                            "content": final_results,
                            "title": topic,
                            "user_id": user_id,
                            "url_to_unified_index": OrderedDict(
                                sorted(urls_to_unified_indexes.items())
                            ),
                            "id": str(custom_uuid),
                            "pdf_url": "",
                            "created_at": datetime.now().isoformat(),
                        }
                    ).execute()
                    yield json.dumps(
                        {
                            "event_id": 6,
                            "message": "Have successfully uploaded to db, sending article content back",
                            "current_progress": "100",
                            "status_code": 200,
                            "is_done": True,
                            "id": str(custom_uuid),
                        }
                    ) + "\n\n"
                except Exception as e:
                    yield json.dumps(
                        {
                            "event_id": 6,
                            "message": f"Failed to upload article to database: {str(e)}",
                            "current_progress": "0",
                            "status_code": 500,
                            "is_done": False,
                        }
                    ) + "\n\n"
        except Exception as e:
            yield json.dumps(
                {
                    "event_id": 5,
                    "message": f"Failed parsing file, error is: {e}",
                    "current_progress": "0",
                    "status_code": 500,
                    "is_done": False,
                }
            ) + "\n\n"
        print("Fully parsed file, sending response back!\n")
    except Exception as e:
        print("Error in create_article_sse_serper: ", e)
        yield json.dumps(
            {
                "event_id": 1,
                "message": "Failed to create article",
                "current_progress": "0",
                "is_done": True,
                "status_code": 500,
            }
        ) + "\n\n"
