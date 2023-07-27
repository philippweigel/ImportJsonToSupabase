import os
from dotenv import load_dotenv
from supabase import create_client, Client
import json


load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(url, key)


json_file_path = "data/jsontoDB.json"

with open(json_file_path, "r") as json_file:
    json_data = json.load(json_file)


response = supabase.table("documents").select("jsonb_data").execute()


if not response.data:
    print("New data gets added!")
    data, count = (
        supabase.table("documents").insert({"jsonb_data": json_data}).execute()
    )
# entry already exists
else:
    print("The entry already exists")
