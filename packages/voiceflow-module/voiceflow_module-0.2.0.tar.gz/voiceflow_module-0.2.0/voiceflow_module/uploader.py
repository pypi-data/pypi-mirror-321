import requests
import io
import json

def try_upload_text(text_name: str, text: str, token: str, metadata: dict = {}, chunk_size: int = 1000, overwrite: bool = True) -> tuple[bool, str]:
    if not token:
        raise ValueError("Invalid token field")

    txt_file = io.BytesIO(text.encode('utf-8-sig'))
    overwrite_param = 'true' if overwrite else 'false'

    url = f'https://api.voiceflow.com/v1/knowledge-base/docs/upload?overwrite={overwrite_param}&maxChunkSize={chunk_size}'
    headers = {
            "accept": "application/json",
            "Authorization": token
        }

    files = {
            "file": (f'{text_name}.txt', txt_file, "text/plain")
        }
    
    if metadata:
        metadata={
    'metadata': json.dumps(metadata)
}

    try:
        response = requests.post(url, headers=headers, files=files, data=metadata)
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        print(f"Error while trying to upload '{text_name}")
        raise
    finally:
        txt_file.close()
    
    return response.json()


def try_upload_table(table_name: str, items: list, token: str, searchable_fields: list, metadata_fields: list=[], overwrite=True):
    if not token:
        raise ValueError("Invalid token field")
    
    json_data = {
        "data": {
            "name": table_name,
            "schema": {
                "searchableFields": searchable_fields,
                "metadataFields": metadata_fields,
            },
            "items": items
        }
    }
        
    url = "https://api.voiceflow.com/v1/knowledge-base/docs/upload/table"
    if overwrite:
        url += "?overwrite=true"

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": token
    }

    try:
        response = requests.post(url, headers=headers, json=json_data)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"Error while trying to upload '{table_name}")
        raise

    return response.json()