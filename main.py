from dotenv import load_dotenv
from pathlib import Path
import logging

load_dotenv()

from src.pinata import upload_pinata


def accumulate_data():
    image_name = input('Enter image name: ')
    image_desc = input('Enter image description: ')
    image_path = input('Enter image path: ')
    image_location = input('Enter image location: ')
    image_photographer = input('Enter image photographer: ')

    return {
        "description": image_desc,
        "image_path": image_path,
        "name": image_name,
        "location" : image_location,
        "photographer" : image_photographer
    }


def nft_metadata_upload(input_data):
    with Path(input_data['image_path']).open("rb") as fp:
        file_binary = fp.read()
        uploadData = {
            "file_name": input_data['name'],
            "file_byte": file_binary
        }
        print('Image hashing in Progress...')
        image_hash = upload_pinata(1, uploadData)
        print('Image Uploaded at IPFS address : ',image_hash)
        input_data['image'] = image_hash
        del input_data['image_path']

        nft_metadata_hash = upload_pinata(2, input_data)
        return nft_metadata_hash


def main():
    try:
        input_data = accumulate_data()
        hash = nft_metadata_upload(input_data)

        print("NFT metadata location on IPFS : " , f"https://gateway.pinata.cloud/ipfs/{hash.split('/')[-1:][0]}")

    except Exception:
        logging.exception("An error occured while processing : ")
        

if __name__ == "__main__":
    main()