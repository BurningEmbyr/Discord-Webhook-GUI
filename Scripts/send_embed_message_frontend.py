import PySimpleGUI as sg
import threading
import send_embed_message_backend as backend

sg.theme('Dark Grey 11')

description_text = {
  'url': 'Webhook URL',
  'bot_name': 'Name for your bot',
  'embed_author': 'Embedded Author Name',
  'embed_icon_url': 'Embedded Article Icon URL',
  'embed_title': 'Embedded Article Title',
  'embed_body': 'Embedded Article Body'
}

# --- Helper Functions ---
def getDescriptionTextFromValues(values):
  text = ""
  for key in description_text:
    text += description_text[key] + ": " + values[key] + "\n"
  
  return text

# --- Layout ---
default_url = ""
default_bot_name = ""
default_embed_author = ""
default_icon_url = ""
default_embed_title = ""
default_embed_body = ""

width = 50
layout = [
  # URL
  [sg.Text("Webhook URL")],
  [sg.InputText(default_url, key='url', size=(width, 1))],

  # Author
  [sg.Text("Bot Name")],
  [sg.InputText(default_bot_name, key='bot_name', size=(width, 1))],
  [sg.Text('_'*(int)(width))],

  # Embed Author Name
  [sg.Text("Embedded Author Name")],
  [sg.InputText(default_embed_author, key='embed_author', size=(width, 1))],

  # Icon URL
  [sg.Text("Embedded Article Icon URL")],
  [sg.InputText(default_icon_url, key='embed_icon_url', size=(width, 1))],
  
  # Embed Title
  [sg.Text("Embedded Article Title")],
  [sg.InputText(default_embed_title, key='embed_title', size=(width, 1))],

  # Embed Body
  [sg.Text("Embedded Article Body")],
  [sg.Multiline(default_embed_body, key='embed_body', size=(width-2, 3))],
  [sg.Text('_'*(int)(width))],


  # Submit & Cancel Buttons
  [sg.Submit(tooltip='Click to begin scraping')],
]


window_title = 'GUI Test'
window = sg.Window(window_title, layout, default_element_size=(40, 1), grab_anywhere=False)

# Event loop
while(True):
  event, values = window.read()

  if event in (None, 'Exit'):
    break

  if event == 'Submit':
    # Check the data to make sure it's good, if not, throw error and continue loop
    url = values['url']
    bot_name = values['bot_name']
    embed_author = values['embed_author']
    embed_icon_url = values['embed_icon_url']
    embed_title = values['embed_title']
    embed_body = values['embed_body']

    # Data verification
    is_data_good = True
    for key in description_text:
      # If anything is empty, let the user know
      if values[key] == '':
        sg.popup(f"Make sure to add a(n) {description_text[key]}")
        is_data_good = False
        break

    if not is_data_good:
      continue


    # Open up the confirm window
    confirmed = sg.PopupYesNo("Here's the info you input: ", getDescriptionTextFromValues(values),"Are you sure you want to submit?", title="Confirm", )
    if confirmed == 'Yes':
      print("Beginning Program")

      threading.Thread(target=backend.sendMessage,
        args=(url, bot_name, embed_author, embed_icon_url, embed_title, embed_body), daemon=True).start()
