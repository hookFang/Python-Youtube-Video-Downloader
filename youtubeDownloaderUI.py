from pytube import YouTube
import PySimpleGUI as sg
from youtubeDownloader import youtubeDownload

sg.theme('DarkTeal6')   # Add a touch of color
# All the stuff inside your window.
layout = [ [sg.Text('Enter your youtube URL'), sg.InputText(key="youtube_url")],
           [sg.Text('Save Folder'),sg.Input(key="save_location"), sg.FolderBrowse()],
           [sg.Button('Download'), sg.Button('Cancel')]  ]

# Create the Window
window = sg.Window("Youtube Video Downloader", layout, size=(600,300))

while True:
    event, values = window.read()
    if event == 'Download':
        if(values["youtube_url"] == ""):
            sg.popup('Please provide a proper URL.', title="ERROR")
        elif(values["save_location"] == ""):
            sg.popup("Please browse your save location.", title="ERROR")
        else:
            if(youtubeDownload(values["youtube_url"], values["save_location"])):
                sg.popup_ok("Video Downloaded Successfully", title="Downloaded")
                window.FindElement('youtube_url').Update('')
                window.FindElement('save_location').Update('')
    elif event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
                break
                print('You entered ', values[0])

window.close()

