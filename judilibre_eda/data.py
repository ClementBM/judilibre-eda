from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from tqdm import tqdm

import judilibre_client
from judilibre_client.rest import ApiException

ROOT = Path(__file__)

load_dotenv()


def save_df_as_jsonl(df, file_path: Path):
    if file_path.exists():
        file_path.unlink()

    with open(file_path, "ab") as json_file:
        df.apply(
            lambda x: json_file.write(f"{x.to_json()}\n".encode("utf-8")),
            axis=1,
        )


def get_summaries(results):
    return [result["summary"] for result in results["results"] if "summary" in result]


def main():
    api_instance = judilibre_client.DefaultApi()

    try:
        api_instance.healthcheck()

        page_size = 50
        query_text = "notaire"
        search_results = api_instance.search(
            query=query_text, page_size=page_size, page=0
        )

        all_results = search_results["results"]

        page_count = (search_results["total"] // page_size) - 1

        for i in tqdm(range(1, page_count)):
            search_results = api_instance.search(
                query=query_text, page_size=page_size, page=i
            )
            all_results += search_results["results"]

        df = pd.DataFrame(all_results)

        save_df_as_jsonl(df[df["summary"].notna()], ROOT.parent / "dataset.jsonl")

    except ApiException as e:
        print("Exception when calling DefaultApi ... %s\n" % e)
