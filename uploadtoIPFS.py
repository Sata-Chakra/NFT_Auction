import ipfs_interact


def invoke_interaction(path_input):
    fpath = path_input
    get_file_uri = ipfs_interact.upload_to_pinata(fpath)
    print("Your file is Uploaded at : ",get_file_uri)
    return get_file_uri