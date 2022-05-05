import uploadtoIPFS

def get_ipfs():
    path_input = input("Please enter the location of your file : ")
    ipfs_file_location = uploadtoIPFS.invoke_interaction(path_input)
    return ipfs_file_location


fl = get_ipfs()
print(fl)
