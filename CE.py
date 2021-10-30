from pyautogui import press, typewrite, hotkey, hold
import time
import mne
# press('a')
# typewrite('quick brown fox')
# hotkey('ctrl', 'w')
RawData = mne.datasets.sample.data_path()
print(RawData)
input("Press Enter to continue...")
while True:
    time.sleep(1)
    with hold('up'):
        time.sleep(1)
