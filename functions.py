def levenshteinDistance(str1, str2):
    E = [[0]*(len(str2)+1) for _ in range(len(str1)+1)]

    s1, s2 = [' '], [' ']
    s1.extend(list(str1))
    s2.extend(list(str2))

    for r in range(1,len(s1)):
        E[r][0] = E[r-1][0] + 1
    for c in range(1,len(s2)):
        E[0][c] = E[0][c-1] + 1
    
    for r in range(1, len(s1)):
        for c in range(1, len(s2)):
            if s1[r]==s2[c]:
                E[r][c]=E[r-1][c-1]
            else:
                E[r][c]=1+min(E[r-1][c-1], E[r][c-1], E[r-1][c])
    return E[-1][-1]

def openFile(string):
    string=string.lower()
    import os

    repo = 'C:\\Users\\zakar\\OneDrive\\Desktop'
    arr = os.listdir(repo)
    arr_ori = arr[::-1]
    arr2=[]
    for _ in range(len(arr)):
        f = arr.pop()
        f = f.lower()
        f=f.split('.')
        arr2.append(f[0])
    
    if string in arr2:
        #return True
        string_ori = string
        string = os.path.join(repo, arr_ori[arr2.index(string)])
        os.startfile(string)
        return 'Opening ' + string_ori
    else:
        string_ori = string
        for i in arr2:
            if levenshteinDistance(string,i)<=2:
                string = os.path.join(repo, arr_ori[arr2.index(i)])
                os.startfile(string)
                return 'Opening ' + i
        return 'Sorry, I could not find ' + string_ori


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