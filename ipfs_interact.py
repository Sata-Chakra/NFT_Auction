from pathlib import Path
import requests
import logging

def upload_to_pinata(path):
    PINATA_BASE_URL = "https://api.pinata.cloud/"
    endpoint = "pinning/pinFileToIPFS"
    filepath = path
    filename = filepath.split("/")[-1:][0]
    headers = {
        "pinata_api_key": "eaec007f290d17de32fe",
        "pinata_secret_api_key": "79a8a224b4f0b435a82eae1ad5d8c6bf4f998a081c41912c947e6b0f22d0e273"
    }

    try:
        with Path(filepath).open("rb") as fp:
            file_binary = fp.read()
            response = requests.post(
                PINATA_BASE_URL + endpoint,
                files={"file": (filename, file_binary)},
                headers=headers,
            )
            ipfs_hash = response.json()["IpfsHash"]
            
            filename = filepath.split("/")[-1:][0]
            image_uri = f"ipfs://{ipfs_hash}?filename={filename}"

            print(f"Successfully uploaded {filename} to pinata.")
            print(response.json())
            return str(image_uri)

    except Exception:
        print("AN ERROR HAPPEND ! CHECK LOGS : ")
        logging(Exception)