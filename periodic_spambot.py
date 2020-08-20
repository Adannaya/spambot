import pyautogui, time

spamfiles = ["periodic", "waterloo", "rickroll", "pi", "harvest", "borap", "dontstop"]
endings = ["Now you have no excuse for failing Chemistry.", "TAKE THAT LOLA", ".............", "Now you have no excuse for failing Maths.", "GOD THE FATHER", "Hmm?", "Sex machine?"]
print("""0: The periodic table song
1: Waterloo Sunset
2: Never Gonna Give You Up
3: 100 Digits of Pi
4: Harvest Samba
5: Bohemian Rhapsody
6: Don't Stop Me Now
""")
choice = int(input("Pick a number for a text to spam, which will start 5 seconds after you press enter: "))

time.sleep(5)
spamtext = open("C:\\Users\\blokk\\Desktop\\spambot\\" + spamfiles[choice] + ".txt", "r")
for line in spamtext:
    pyautogui.typewrite(line)
    pyautogui.press("enter")
pyautogui.typewrite(endings[choice])
pyautogui.press("enter")
spamtext.close()
