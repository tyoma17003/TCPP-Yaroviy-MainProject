import re


mytext = "red black yellow https://ru.wikipedia.org https://tproger.ru pink blue https://moodle.donnu.edu.ua green."

text = r'https\:\//([a-zA-Z0-9\.-_]+)'

allresults = re.findall(text,mytext)


for item in allresults:
    print(item)


