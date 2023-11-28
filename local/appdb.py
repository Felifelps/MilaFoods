from asyncio import sleep
import json

class Data:
    DATABASE = 'database.json'
    def __init__(self):
        with open(self.DATABASE, 'r') as file:
            self.__data = json.load(file)
        self.__open = False
        
    async def connect(self):
        while self.__open:
            await sleep(0.001)
        self.__open = True
        with open(self.DATABASE, 'r') as file:
            self.__data = json.load(file)
    
    async def commit_and_close(self):
        with open(self.DATABASE, 'w') as file:
            file.write(json.dumps(self.__data, indent=4))
        self.__open = False
    
    def __getitem__(self, key):
        return self.__data.get(key, None)
    
    @property
    def data(self):
        return self.__data
        
    def __setitem__(self, key, value):
        self.__data[key] = value

DATA = Data()

saved_cols = ['image', 'text', 'likes', 'timestamp', 'key']

async def save_username(username):
    await DATA.connect()
    DATA['user'].update({'username': username})
    await DATA.commit_and_close()

def get_username():
    return DATA.data['user']['username']

async def get_theme():
    return DATA.data['user']['theme']

async def alter_theme(theme):
    await DATA.connect()
    DATA['user'].update({'theme': theme})
    await DATA.commit_and_close()

async def back_to_default_user():
    await DATA.connect()
    DATA['user'].update({'username': '===NoUser==='})
    await DATA.commit_and_close()

async def local_save_post(post):
    await DATA.connect()
    DATA['posts'].update({f"{post['username']}-{post['id']}": post})
    await DATA.commit_and_close()
    
async def local_un_save_post(post_key):
    await DATA.connect()
    DATA['posts'].pop(post_key)
    await DATA.commit_and_close()

async def get_local_saved_posts():
    return DATA.data['posts']

async def erase_saved_data():
    await DATA.connect()
    DATA['posts'] = {}
    await DATA.commit_and_close()

