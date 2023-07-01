import base64, os

def encode_image(image_path):
    with open(image_path, "rb") as file:
        return [image_path.split("\\")[-1].split(".")[-1], base64.b64encode(file.read())]

def decode_image(string, image_name):
    with open(os.path.join('views', 'data', 'user_images', image_name), "wb") as file:
        file.write(base64.b64decode(string))

def user_image_was_loaded(username):
    for i in os.listdir(os.path.join('views', 'data', 'user_images')):
        if username in i:
            return i
    return 'account-circle.png'