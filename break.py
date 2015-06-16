import time
import webbrowser
i =0
print("this program started on" + time.ctime())
#repeat this process 3 times
while i <=3:
#open google page after every 5 sec
    time.sleep(5)
    webbrowser.open("https://www.google.com")
    i=i+1
