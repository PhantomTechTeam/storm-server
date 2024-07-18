from os import getenv
parser = {
    "output_dir": ".results/gpt",
    "max_thread_num": getenv("MAX_THREAD_NUM"),
    "max_conv_turn": getenv("MAX_CONV_TURN"),
    "max_perspective": getenv("MAX_PERSPECTIVE"),
    "search_top_k": getenv("SEARCH_TOP_K"),
}
