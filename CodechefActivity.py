import bs4 as bs
from win10toast import ToastNotifier
import sys,os
from PyQt5.QtCore import QUrl,QEventLoop
from PyQt5.QtWidgets import QApplication,qApp
from PyQt5.QtWebEngineWidgets import QWebEnginePage


#Render a page to get dynamic source using PyQt5 ,create application once for multiple urls
def _render(url):

    class WebPage(QWebEnginePage):
        def __init__(self):
            super(WebPage, self).__init__()
            self.loadFinished.connect(self.handleLoadFinished)
            self.html = None

        def start(self, url):
            self._url = url
            self.load(QUrl(url))
            while self.html is None:
                qApp.processEvents(QEventLoop.ExcludeUserInputEvents
                                |QEventLoop.ExcludeSocketNotifiers |
                    QEventLoop.WaitForMoreEvents)
            qApp.quit()

        def processCurrentPage(self, data):
            url = self.url().toString()
            self.html = data

        def handleLoadFinished(self):
            self.toHtml(self.processCurrentPage)

    webpage = WebPage()
    webpage.start(url)
    return webpage.html

#Get data (star and recent data) for a given username
def getData(username):
    url='https://www.codechef.com/users/' + username
    print("Processing "+username)
    data=""
    index=0
    row=None
    while row==None:
        html = _render(url)
        soup = bs.BeautifulSoup(html, 'lxml')
        row=soup.find('table',{'class':'dataTable'}).tbody.tr

    star = soup.find('span', {'class': 'rating'})
    for d in row:
        if index==2:
            if d.span['title']=="":
                data += d.span.text+" "
            else:
                 data += d.span['title'] + " "
        else:
            data += d.string + " "
        index += 1
    return [star.text if star!=None else "d",data]

#Notify on windows10
def notify(username,data,icon_path):
    toaster = ToastNotifier()
    toaster.show_toast(username,data,icon_path,duration=30)



#########################################DRIVER CODE HERE###################################################

sys.stdout=open('log.txt','w') #Write console to log file
ICON_PATH = 'stars\\'          #Base path for icons
usernames=[s.rstrip("\n").strip(",") for s in open("usernames.txt","r").readlines()]#Read usernames from usernames.txt

index=0

if os.path.isfile("recent_data.txt"): #If file exists populate list with file data
    recent_data=[s.rstrip("\n").strip(",") for s in open("recent_data.txt","r").readlines()]
    print("File is full\n")
else:                                  #If file does not exist populate list with string "empty"
    recent_data=["empty" for i in range(len(usernames))]
    print("File is empty\n")

app = QApplication(sys.argv)#Create PyQt5 app once

for username,recent in list(zip(usernames,recent_data)):
    data = getData(username)
    if recent != data[1]:#If there is a new activity,then notify
        recent_data[index]=data[1]
        notify(username,data[1],ICON_PATH+data[0][0]+'.ico')
        index+=1

#Write scrapped activity back to recent_data file
f=open("recent_data.txt","w")
for data in recent_data:
    f.write(data + "\n")
    print("Wrote " + data + "\n")
    f.close()


##############################################THE END#####################################################
