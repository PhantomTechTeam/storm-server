from knowledge_storm import (
    STORMWikiRunnerArguments,
    STORMWikiRunner,
    STORMWikiLMConfigs,
)

# STORM is a LM system so different components can be powered by different models to reach a good balance between cost and quality.
# For a good practice, choose a cheaper/faster model for `conv_simulator_lm` which is used to split queries, synthesize answers in the conversation. Choose a more powerful model for `article_gen_lm` to generate verifiable text with citations.
lm_configs = STORMWikiLMConfigs()


def setup_storm_engine_args(args: dict[str, str], topic: str):
    output_dir_original = args.get("output_dir")

    # Check out the STORMWikiRunnerArguments class for more configurations.
    engine_args = STORMWikiRunnerArguments(
        output_dir=f"{output_dir_original}/{topic}",
        max_conv_turn=int(str(args.get("max_conv_turn"))),
        max_perspective=int(
            str(
                args.get("max_perspective"),
            )
        ),
        search_top_k=int(str(args.get("search_top_k"))),
        max_thread_num=int(str(args.get("max_thread_num"))),
    )
    return engine_args


def run_runner(topic: str, engine_args, rm):
    runner = STORMWikiRunner(engine_args, lm_configs, rm)
    runner.run(
        topic=topic,
        do_research=True,
        do_generate_outline=True,
        do_generate_article=True,
        do_polish_article=True,
    )
    
    runner.post_run()
    runner.summary()
    return runner.article_output_dir
