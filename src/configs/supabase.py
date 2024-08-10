import os
from supabase import create_client, Client
import shutil
import uuid
from datetime import datetime

class Supabase:
    def __init__(self):
        self.url: str = str(os.environ.get("SUPABASE_URL"))
        self.key: str = str(os.environ.get("SUPABASE_KEY"))
        self.supabase_bucket: str = str(os.environ.get("SUPABASE_BUCKET"))
        self.supabase_client: Client = create_client(self.url, self.key)

    def create_pdf(self, pdf_filepath, user_id, pdf_name, folder_path):
        with open(f"{pdf_filepath}.pdf", "rb") as f:
            self.supabase_client.storage.from_(self.supabase_bucket).upload(
                file=f,
                path=f"{user_id}/{pdf_name}",
                file_options={"content-type": "application/pdf"},
            )

        shutil.rmtree(folder_path)
        public_url = self.supabase_client.storage.from_(
            self.supabase_bucket
        ).get_public_url(f"{user_id}/{pdf_name}")
        return public_url
    def create_article(self, content, topic, user_id, urls_to_unified_index):
        self.supabase_client.from_("articles").insert(
            {
                "content": content,
                "title": topic,
                "user_id": user_id,
                "url_to_unified_index": urls_to_unified_index,
                "id": uuid.uuid4(),
                "pdf_url": "",
                "created_at": datetime.now().isoformat(),
                "user_id": user_id
            }
        )


