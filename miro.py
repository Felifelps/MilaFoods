import webbrowser
url = 'https://miro.com/app/board/uXjVMdtC0A8=/'
chrome_path = '"C:\Program Files\Google\Chrome\Application\chrome.exe" %s --incognito'
webbrowser.get(chrome_path).open_new(url)