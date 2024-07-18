import uuid
from os import environ, rmdir, mkdir
def create_markdown(content: str, filename_str: str):
    pass
def upload_pdf(content: str, user_id: str, topic: str):
    from ..configs.supabase import supabase_client, supabase_bucket
    import pymupdf4llm
    random_uuid = uuid.uuid4()
    topic_updated = topic.replace(" ", "_").lower()
    base_path = f"{environ.get('PDF_STORAGE')}/{user_id}"
    mkdir(base_path)
    md_text = pymupdf4llm.to_markdown(f"{base_path}/{topic_updated}_{random_uuid}.pdf")

    # now work with the markdown text, e.g. store as a UTF8-encoded file
    import pathlib
    pathlib.Path(f"{base_path}/{topic_updated}_{random_uuid}.md").write_bytes(md_text.encode())


    with open(f"{base_path}/{topic_updated}_{random_uuid}.pdf", 'rb') as f:
        supabase_client.storage.from_(supabase_bucket).upload(file=f,path=f"{user_id}/wikipedia-articles/", file_options={"content-type": "application/pdf"})

    # rmdir(f"{base_path}/{topic_updated}")
