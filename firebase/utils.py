import base64, os

def encode_image(image_path):
    """
    Transforms an image to a string
    
    image_path: path to the image
    
    returns [image_type, encoded string]
    """
    
    with open(image_path, "rb") as file:
        return [image_path.split("\\")[-1].split(".")[-1], base64.b64encode(file.read())]

def decode_image(string, image_name, dir):
    """
    Transforms a string to an image
    
    string: encoded string
    image_name: the name of the image file
    dir: path to the image local
    
    returns None
    """
    with open(os.path.join(dir, image_name), "wb") as file:
        file.write(base64.b64decode(string))


#from gmail import AuthenticationMail

#AuthenticationMail().send_code_email("felipefelipe23456@gmail.com")