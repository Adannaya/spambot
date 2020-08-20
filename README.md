# spambot
Code for making a spambot with a console menu

When the script starts, it will allow you to choose which text to spam, then you have 5 seconds to get your cursor in place.
If you need to stop the script, move your mouse to the top-left corner of the screen to activate PyAutoGUI's failsafe.

PyAutoGUI needs to be installed for this to work, which can easily be done with `pip install pyautogui` from the command line or Windows Command Prompt.

Make sure all files are in the same folder/directory, or provide the exact file path to the text files if they are not in the same location as the Python script.

The `spamfiles` list contains the file names of the text files, minus the ".txt" extension, so you can change these to whatever you like or add your own. You can delete the endings list if you like, but make sure to also delete the
``` python
pyautogui.typewrite(endings[choice])
pyautogui.press("enter")
```
lines as well.

I've discovered that - at least on Windows - when running from the command line, you have to run the Python script from the same folder or directory as the script. Otherwise, an error will come up, saying `FileNotFoundError: [Errno 2] No such file or directory: 'rickroll.txt'` or something along those lines.

The executable file `spambot.exe` contains lyrics for the songs:
- The periodic table song by ASAPScience
- Waterloo Sunset by The Kinks
- Never Gonna Give You Up by Rick Astley
- 100 Digits of Pi by ASAPScience
- Bohemian Rhapsody by Queen
- Harvest Samba

If you want to run the executable, make sure all the text files are in the same directory as it.

However, if you would like to customise the song lyrics and make your own executable, in Windows CMD or Linux or macOS terminal type from the same directory as your script:
```
pip install pyinstaller
pyinstaller --onefile spambot.py
```
If you wish to have an icon for your executable, type `pyinstaller --onefile -i icon.ico spambot.py` instead.

I used [this](https://youtu.be/UZX5kH72Yx4) YouTube tutorial to help with making the EXE file.
