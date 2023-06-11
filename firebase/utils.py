import base64, os

def encode_image(image_path):
    with open(image_path, "rb") as file:
        return [image_path.split("\\")[-1].split(".")[-1], base64.b64encode(file.read())]

def decode_image(string, image_name, dir):
    with open(os.path.join(dir, image_name), "wb") as file:
        file.write(base64.b64decode(string))