from flask import Flask, request
import pyautogui
import socket
import subprocess
import sys
import tkinter as tk
#subprocess.call([sys.executable, "-m", "pip", "install", "flask"])
#subprocess.call([sys.executable, "-m", "pip", "install", "pyautogui"])



pyautogui.FAILSAFE = False
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
s.close()
oldx = oldy = 0

app = Flask(__name__)
app.debug = False
@app.route("/")
def main():
    global oldx, oldy
    action = request.args.get('action')
    
    if action == "move":
        x,y = (float(request.args.get('x')) * 2),(float(request.args.get('y')) * 2)
        pyautogui.moveRel(x, y, duration = 0.1)
        return ip
        
    if action == "write":
        string = request.args.get('string')
        pyautogui.typewrite(string)
        return ip
    
    if action == "leftclick":
        pyautogui.click()
        return ip
    if action == "rightclick":
        pyautogui.click(button='right')
        return ip
        
    if action == "scrolldown":
        pyautogui.scroll(-150)
        return ip
    if action == "scrollup":
        pyautogui.scroll(150)
        return ip
        
    if action == "scrolldownn":
        pyautogui.scroll(-800)
        return ip
    if action == "scrollupn":
        pyautogui.scroll(800)
        return ip

      
    if action == "closetab":  
        pyautogui.hotkey('ctrl','w')
        return ip
    if action == "switchtab":  
        pyautogui.hotkey('ctrl','tab')
        return ip
        
    if action == "ping":
        win = tk.Tk()
        win.geometry("500x100")
        win.title("TouchPad")
        win.iconbitmap("icon.ico")
        text = tk.Label(win, text = "Connected by IP: " + request.remote_addr)
        text.pack()
        win.mainloop()
        return ip
    
    else:
        return "error"

if __name__ == "__main__":
	app.run(host=ip, port=80)
