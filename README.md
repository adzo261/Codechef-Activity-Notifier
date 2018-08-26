# Codechef Activity Notifier

Codechef Activity Notifier is a python script, which can be executed by setting a keyboard shortcut,
and we will get the recent submission of required users straight as a notification on Windows 10 OS.
### Screenshots

   ![Alt text](sshots1.png?raw=true "Optional Title") &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ![Alt text](sshots2.png?raw=true "Optional Title")

## Getting Started

Download ZIP of the project and follow the given instructions:

### Prerequisites

```
Windows 10 OS
```
```
Python 3.6
```
```
Beautiful Soup 4
```
```
lxml
```
```
PyQt5
```
```
win10toast
```
Refer [requirements.txt](https://github.com/adzo261/Codechef-Activity-Notifier/blob/master/requirements.txt)
### Installing
```
pip install beautifulsoup4
```
```
pip install lxml
```
```
pip install pyqt5
```
```
pip install win10toast
```
### Instructions

Change ```C:\Users\AdityaZope\Anaconda3\envs\WebScrapping\pythonw.exe``` in ```star.bat``` to ```YOUR pythonw.exe PATH```<br><br>
And ```C:\Users\AdityaZope\PycharmProjects\WebScrapping\CodechefActivity.py``` in ```star.bat``` to ```LOCATION OF CodechefActivity.py WHERE YOU EXTRACTED ZIP```<br><br>
Create desktop shortcut to ```start.vbs``` and ```stop.vbs``` and assign keyboard shortcuts.<br><br>
Use ```start.vbs``` to run and ```stop.vbs``` to stop a running script.<br><br>
Add the usernames of coders whom u want to track in ```usernames.txt``` file,one on each line.
## Acknowledgments

* [Jithu R Jacob](https://github.com/jithurjacob) for Python Windows 10 notification library.
* [Codechef](https://www.codechef.com/) for inspiration.
