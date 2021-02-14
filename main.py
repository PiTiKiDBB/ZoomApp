import PySimpleGUI as sg
import pyautogui
import time
import subprocess

sg.theme('DarkBrown4')

layout = [
    [sg.T("Enter your link:")], 
    [sg.In(key="thlink")], 
    [sg.T("Does this meeting require passord?"), sg.Radio("Yes", "RADIO1", default=True, key='pswy'), 
    sg.R("No", "RADIO1", default=False)], 
    [sg.B("Join Meeting", key="Join"), sg.Button("Cancel")]    
]
window = sg.Window('ZoomApp', layout ) 

while True:
    event, values = window.read(timeout=10) 

    if event in('Cancel', None): 
        break 
    
    if event in('Join'):
        
        print("Opening Zoom...")
        subprocess.Popen('zoom')
        print("Zoom opened...")
        time.sleep(4)
        print("Locating Join...")
        button = pyautogui.locateOnScreen('/home/pitikidbb/Desktop/code/zoomapp/snips/join.png')
        print("Join located...")
        pyautogui.click(button)
        print("Clicking button...")
        time.sleep(2)
        print("Locating linkb...")
        linkbox = pyautogui.locateOnScreen('/home/pitikidbb/Desktop/code/zoomapp/snips/linkb.png')
        print("Clicking Linkb...")
        pyautogui.click(linkbox)
        time.sleep(2)
        print("Writing link...")
        linkstr = (values['thlink'])
        pyautogui.typewrite(linkstr)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.typewrite("")
        

        pyautogui.press('enter')

window.close() 