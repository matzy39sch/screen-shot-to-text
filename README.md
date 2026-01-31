# screen-shot-to-text
![alt text](https://github.com/matzy39sch/screen-shot-to-text/blob/master/screenshots/working.gif?raw=true)

start with the following command:

###  `python ui_screen_shot_to_text.py`

You'll see the following screen:
<br />
![alt text](https://github.com/matzy39sch/screen-shot-to-text/blob/master/screenshots/start.PNG?raw=true)

The first 4 inputs are the coordinates in your screen within the screenshot that will be taken.
The text area will contain the text. 
The buttons should be pressed. It performs under pressure. 

Once you pressed the button or F12 then you should be presented with something similar to the following screen, based on the captured image<br />
![alt text](https://github.com/matzy39sch/screen-shot-to-text/blob/master/screenshots/running.PNG?raw=true)


on the right side, there is a preview of the captured area, the textarea should contain your text.

If you press ESC the window will be closed. 

### `pyinstaller ui_screen_shot_to_text.py`
This will create an exe file on windows so you can run our script from your desktop. 
If you are not familiar with pyinstaller, please check the official documentation. https://www.pyinstaller.org/


###### To use google sheet, you'll have to get Google Drive API, credentials and a JSON file which you have to load later
###### I followed the first steps of the following post https://erikrood.com/Posts/py_gsheets.html


## Todo:
- [X] create dependency list and installation guide
- [X] get the google sheets name and the sevice account JSON file from an entry and print the text there, new lines to new rows
- [ ] coordinate input limits to screen size
- [ ] load image instead of the screenshot
- [ ] make the selecetion with a mouse instead of the boring coordinates
