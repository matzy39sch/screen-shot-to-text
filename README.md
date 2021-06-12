# screen-shot-to-text

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


## Todo:
- [ ] get the google sheets URL from an entry and print the text there, lines new rows
- [ ] coordinate input limits to screen size