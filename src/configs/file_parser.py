import json
from collections import OrderedDict
from os import rmdir, environ, getcwd
def parse_file(topic: str):
    print(getcwd())
    content = []
    updated_topic = topic.replace(" ", "_").replace("-", "_").lower()
    folder_path = f"{environ.get('OUTPUT_DIR')}/{updated_topic}"
    print(folder_path)
    with open(f"{folder_path}/storm_gen_article_polished.txt", "r+") as f:
        content.append(str(f.read()))
    escapable_str_with_comma = "\",\""
    escapable_str_without_comma = "\""
    double_escapes = "\n\n"
    final_results = "".join(content).replace(escapable_str_with_comma, "").replace(double_escapes, "\n").replace(escapable_str_without_comma, "")

    with open(f"{folder_path}/url_to_info.json", 'r+') as f:
        data = json.load(f)
    url_unified_index = data.get("url_to_unified_index")

    urls_to_unified_indexes = {}

    for url, unified_index in url_unified_index.items():
        if(unified_index not in urls_to_unified_indexes.keys()):
            urls_to_unified_indexes[unified_index] = url
    result = {
        "content": final_results,
        "urls_to_unified_index": OrderedDict(sorted(urls_to_unified_indexes.items()))
    }
    print(result)
    # rmdir(folder_path)
    return result
