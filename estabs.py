from db import DB

ESTABS = DB.collection("estabs")

def new_estab(name, email, password, contact, description):
    """Creates a new estab object in the database"""
    new = ESTABS.document(email)
    new.set({
        "name": name,
        "email": email,
        "password": password,
        "contact": contact,
        "description": description
    })
    new.collection("Cardápio")
    new.collection("Posts")

def update_estab(email, data):
    """Updates a estab object of the database"""
    ESTABS.document(email).update(data)
    
def delete_estab(email):
    """Deletes a estab object of the database"""
    ESTABS.document(email).delete()
    
def get_estab(email):
    """Gets all the data of a client object of the database"""
    return ESTABS.document(email).get().to_dict()

delete_estab("apagar")