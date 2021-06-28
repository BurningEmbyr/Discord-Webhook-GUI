import requests as r

def sendMessage(url, bot_name, embed_author, embed_icon_url, embed_title, embed_body):
  message = {'username': f'{bot_name}'}
  message['embeds'] = [{}]
  message['embeds'][0]['author'] = {}
  message['embeds'][0]['author']['name'] = embed_author
  message['embeds'][0]['author']['icon_url'] = embed_icon_url
  message['embeds'][0]['title'] = embed_title 
  message['embeds'][0]['description'] = f"{embed_body}"

  result = r.post(url, json=message)