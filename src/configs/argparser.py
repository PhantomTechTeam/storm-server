from os import environ

parser = {
    "output_dir": environ.get("OUTPUT_DIR"),
    "max_thread_num": environ.get("MAX_THREAD_NUM"),
    "max_conv_turn": environ.get("MAX_CONV_TURN"),
    "max_perspective": environ.get("MAX_PERSPECTIVE"),
    "search_top_k": environ.get("SEARCH_TOP_K"),
}
