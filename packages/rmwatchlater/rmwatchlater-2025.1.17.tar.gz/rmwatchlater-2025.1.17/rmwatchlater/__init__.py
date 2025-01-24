import pyautogui as gui
import webbrowser
import time
from mylocale.TR import tr
import locale
import os


def main():
    scriptpath = os.path.abspath(__file__)
    scriptpath = os.path.dirname(scriptpath)
    print(scriptpath)
    mylocale = locale.getlocale()[0].split("_")[0]
    url = "https://www.youtube.com/playlist?list=WL"
    trfile = f"{scriptpath}/localisation.csv"
    menue = f"{scriptpath}/imgs/menue.png"
    print(menue)
    promt = input(
        tr(csv_file=trfile, target_key="PROMT", langcode=mylocale).format(
            yes=tr(csv_file=trfile, target_key="YES"),
            no=tr(csv_file=trfile, target_key="NO"),
        )
    )
    webbrowser.open(url)
    if promt == tr(csv_file=trfile, target_key="YES", langcode=mylocale):
        time.sleep(5)
        gui.click(menue)
        print("ready")


if __name__ == "__main__":
    main()
