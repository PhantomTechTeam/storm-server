import os
from supabase import create_client, Client

url: str = str(os.environ.get("SUPABASE_URL"))
key: str = str(os.environ.get("SUPABASE_KEY"))
supabase_bucket: str = str(os.environ.get("SUPABASE_BUCKET"))
supabase_client: Client = create_client(url, key)
