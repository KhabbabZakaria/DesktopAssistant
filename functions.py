def openFile(string):
    string=string.lower()
    import os

    repo = 'C:\\Users\\zakar\\OneDrive\\Desktop'
    arr = os.listdir(repo)
    arr2=[]
    for _ in range(len(arr)):
        f = arr.pop()
        f = f.lower()
        f=f.split('.')
        arr2.append(f[0])
    arr=arr2

    if string in arr:
        #return True
        string_ori = string
        string = os.path.join(repo, string)
        os.startfile(string)
        return 'Opening ' + string_ori
    else:
        return 'Sorry, I could not find ' + string


def openWebPage(voice):
    import webbrowser
    import urllib.request
    from googlesearch import search

    chrome_path = '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" %s'
    url = 'http://www.' + voice  + '.com/'

    try:
        urllib.request.urlopen(url).getcode()
        webbrowser.get(chrome_path).open(url)
    except:
        url = 'https://www.google.com/search?q=' + voice
        webbrowser.get(chrome_path).open(url)


def tellJoke():
    with open('jokes.txt') as f:
        lines = [line.rstrip() for line in f]
    from random import randrange
    randNum = randrange(len(lines))
    
    import pyttsx3
    engine = pyttsx3.init()
    engine.say(lines[randNum])
    engine.runAndWait()