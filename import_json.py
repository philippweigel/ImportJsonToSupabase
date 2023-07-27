import os
from dotenv import load_dotenv
from supabase import create_client, Client
import json


def get_env_variable(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise Exception(f"{name} not found in environment variables")
    return value


def load_json_file(file_path: str) -> dict:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"No such file: {file_path}")
    with open(file_path, "r") as json_file:
        return json.load(json_file)


def main():
    load_dotenv()

    url = get_env_variable("SUPABASE_URL")
    key = get_env_variable("SUPABASE_KEY")

    supabase: Client = create_client(url, key)

    json_file_path = "data/jsontoDB.json"
    json_data = load_json_file(json_file_path)

    response = supabase.table("documents").select("jsonb_data").execute()

    if not response.data:
        data, count = (
            supabase.table("documents").insert({"jsonb_data": json_data}).execute()
        )
        print(f"Number of entries added: {count}")
    else:
        print("The entry already exists")


if __name__ == "__main__":
    main()
