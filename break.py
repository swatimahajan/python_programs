import time
import webbrowser
i =0
print("this program started on" + time.ctime())
while i <=3:
    time.sleep(5)
    webbrowser.open("https://www.google.com")
    i=i+1
