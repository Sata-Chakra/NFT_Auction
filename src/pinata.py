import os
import requests

pinata_base_url = os.getenv('PINATA_API_BASEURL') + "pinning/"
headers = {
    "pinata_api_key": os.getenv('PINATA_API_KEY'),
    "pinata_secret_api_key": os.getenv('PINATA_API_SECRET_KEY')
}


def upload_pinata(upload_type, payload):
    data = {}
    files = []
    if (upload_type == 1):
        files = [('file', (payload["file_name"], payload["file_byte"]))]
        pinata_url = pinata_base_url + 'pinFileToIPFS'
    else:
        data = payload
        pinata_url = pinata_base_url + 'pinJSONToIPFS'

    response = requests.post(
        pinata_url ,
        files=files,
        data=data,
        headers=headers,
    )

    ipfs_uri = ''
    if (response.status_code == 200):
        ipfs_hash = response.json()['IpfsHash']
        ipfs_uri = f"ipfs://{ipfs_hash}"

    return str(ipfs_uri)
