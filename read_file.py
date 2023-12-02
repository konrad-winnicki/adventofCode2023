def read_file(file_name: str):
    with open(file_name, "r") as file:
        return file.readlines()


