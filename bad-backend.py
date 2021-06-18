import requests as r
import sys
import json

if(len(sys.argv) > 1 and sys.argv[1] == "-debug"):
    #My server
    print("Using debug options!")
    url = "" #debug hook goes here
elif(len(sys.argv) > 2 and sys.argv[1] == "-custom"):
    #Generic server
    print("Using custom webhook!")
    url = sys.argv[2]
else:
    print("Using default")
    url = "" #default hook goes here

while(1):
    botName = input("Enter message author name: ")
    authorName = ""
    authorName = input("Enter embed author name: ")

    message = {'username':f'{botname}'}
    #message['content'] = 'words'
    message['embeds'] = [{}]
    message['embeds'][0]['author'] = {}
    if(authorName != ""):
        message['embeds'][0]['author']['name'] = authorName
    icon_url = ""
    icon_url = input("Enter profile image url: ")
    if(icon_url != ""):
        message['embeds'][0]['author']['icon_url'] = icon_url

    title = input("Enter an embed title: ")
    subtitle = input("Enter an embed body: ")
    subtitle = subtitle.replace('\\n', '\n')
    
    message['embeds'][0]['title'] = title
    message['embeds'][0]['description'] = f"{subtitle}"
    #message['embeds'][0]['color'] = 4767906

    #    {'title':'News Headline', 'color': }


    print(message)


    result = r.post(url, json = message)

    print(result)
    print(result.text)