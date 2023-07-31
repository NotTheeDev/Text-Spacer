import time
import pyperclip
import getpass
import winreg

from google_trans_new import google_translator  

translator = google_translator()
neco = getpass.getuser()

texts = {
    "zadejjmeno": "Zadejte vaše jméno",
    "jses": "Jseš",
    "ipziskani": "Uplně získávám IP adresu",
    "trackuju": "Trackuju",
    "terminuji": "Terminuji",
    "pouziti": "Děkujeme za použtít random programu 420",
    "zpravu": "Zadejte zprávů",
    "konec": "Zprává byla automaticky zkopírovaná, teď stačí jen použít Ctrl+V pro vložení.",
    "jmenodatabaze": "Vaše jméno bylo nalezen v databázi, jestli že chcete jméno změnit použíjte příkaz '_name_'",
}

"""
Skill issue část

try:
    keys = texts.keys()
    count = 0
    for v in texts:
        texts[keys[count]] = translator.translate(v, dest="en").text
        count += 1
except:
    print("Translation failed ...")"""

def SetName(jmeno: str):
    soft = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, r"SOFTWARE\\")
    key = winreg.CreateKey(soft, "NOTTHEE_APPLICATIONS")

    winreg.SetValueEx(key, "username", 0, winreg.REG_SZ, jmeno)

try:
    soft = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, r"SOFTWARE\\NOTTHEE_APPLICATIONS\\")
    value = winreg.QueryValueEx(soft, "username")

    if value:
        neco = value[0]

    ano = "ano"
except:
    ano = input(texts["jses"] + " " + neco +"? : ").lower()

if ano == "ano" or ano == "jj" or ano == "j" or ano == "yes" or ano == "vůbec":
    print(texts["jmenodatabaze"])
else:
    jmeno = input(texts["zadejjmeno"] + ": ")
    neco = jmeno

    SetName(jmeno)

    print("\n" + texts["ipziskani"] + " ...")
    time.sleep(.5)
    print(texts["trackuju"] + " ...")
    time.sleep(.25)
    print(texts["terminuji"] + " ...")
    time.sleep(1)
    print(texts["pouziti"])

while True:
    text = input("\n" + texts["zpravu"] + " " + neco + " : ")
    
    if text == "_cancel_":
        break
    elif text == "_name_":
        jmeno = input(texts["zadejjmeno"] + ": ")
        SetName(jmeno)
        neco = jmeno
        continue
    
    new = ""

    for a in text:
        new += a + " "

    pyperclip.copy(new)
    print("\n" + texts["konec"])
    print("-----------------------------------------------------------------------------")