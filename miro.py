import webbrowser
url = 'https://miro.com/app/board/uXjVMdtC0A8=/'
chrome_path = 'C:\Users\Felipe\AppData\Local\Programs\Opera GX\launcher.exe %s --incognito'
webbrowser.get(chrome_path).open_new(url)