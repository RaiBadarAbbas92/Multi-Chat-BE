import os

def save_uploaded_file(file):
    file_location = f"data/uploads/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    return file_location

def split_document(file_path: str):
    # Logic to split document into manageable chunks
    return ["chunk1", "chunk2", "chunk3"]
