import requests
from bs4 import BeautifulSoup
import time
from win10toast import ToastNotifier

while True:

    request = requests.Session()
    url = "http://sahand.tehranpayment.com/Page/GRESchedule.aspx"
    soup_url = request.get(url)
    soup = BeautifulSoup(soup_url.content, "lxml")
    All_Hidden = soup.find_all("input", type="hidden")

    if not((str(soup).find("26 November") != -1 and str(soup).find("26 November")<str(soup).find("ORUMIYEH")) or \
           (str(soup).find("27 November") != -1 and str(soup).find("27 November")<str(soup).find("ORUMIYEH")) or \
           (str(soup).find("28 November") != -1 and str(soup).find("28 November")<str(soup).find("ORUMIYEH")) or \
           (str(soup).find("29 November") != -1 and str(soup).find("29 November")<str(soup).find("ORUMIYEH")) or \
           (str(soup).find("30 November") != -1 and str(soup).find("30 November")<str(soup).find("ORUMIYEH")) or \
           (str(soup).find("31 November") != -1 and str(soup).find("31 November")<str(soup).find("ORUMIYEH")) or \
           (str(soup).find("1 December") != -1 and str(soup).find("1 December")<str(soup).find("ORUMIYEH")) or \
           (str(soup).find(",2 December") != -1 and str(soup).find(",2 December")<str(soup).find("ORUMIYEH")) or \
           (str(soup).find("3 December") != -1 and str(soup).find("3 December")<str(soup).find("ORUMIYEH")) or \
           (str(soup).find("4 December") != -1 and str(soup).find("4 December")<str(soup).find("ORUMIYEH")) or \
           (str(soup).find("5 December") != -1 and str(soup).find("5 December")<str(soup).find("ORUMIYEH")) or \
           (str(soup).find("6 December") != -1 and str(soup).find("6 December")<str(soup).find("ORUMIYEH")) or \
           (str(soup).find("7 December") != -1 and str(soup).find("7 December")<str(soup).find("ORUMIYEH")) or \
           (str(soup).find(",8 December") != -1 and str(soup).find(",8 December")<str(soup).find("ORUMIYEH")) or \
           (str(soup).find("9 December") != -1 and str(soup).find("9 December")<str(soup).find("ORUMIYEH")) or \
           (str(soup).find("10 December") != -1 and str(soup).find("10 December")<str(soup).find("ORUMIYEH")) or \
           (str(soup).find("11 December") != -1 and str(soup).find("11 December")<str(soup).find("ORUMIYEH")) or \
           (str(soup).find("12 December") != -1 and str(soup).find("12 December")<str(soup).find("ORUMIYEH")) or \
           (str(soup).find("13 December") != -1 and str(soup).find("13 December")<str(soup).find("ORUMIYEH")) or \
           (str(soup).find("14 December") != -1 and str(soup).find("14 December")<str(soup).find("ORUMIYEH"))):
        print(time.time())
        time.sleep(8)
        continue

    else:
        print("Found!!")
        toaster = ToastNotifier()
        toaster.show_toast("Found GRE Place",
                           "Sign up now!!!",
                           duration=10)

