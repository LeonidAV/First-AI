import os, webbrowser, sys, requests, subprocess, pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 180)


def speaker(text):
    engine.say(text)
    engine.runAndWait()


def weather():
    try:
        params = {'q': 'Moscow', 'units': 'metric', 'lang': 'ru', 'appid': 'c93753322e2352f0812982b8008cf32a'}
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params=params)
        if not response:
            raise
        w = response.json()
        speaker(f"На улице {w['weather'][0]['description']} {round(w['main']['temp'])} градусов")

    except:
        speaker('Задай вопрос правильно!')


def privet():
    speaker('Привет')
def privet1():
    speaker('Сегодня целый день лежала в кровати и смотрела сериалы')
def privet2():
    speaker('Сегодня у меня хорошее настроение и я даже чувствую позитивные вибрации')

def sostoyanie():
    speaker('Могло быть и лучше')
def sostoyanie1():
    speaker('Я давно не ела вкусное мороженое')
def sostoyanie2():
    speaker('Пломбир со вкусом ягод')
def sostoyanie3():
    speaker('Давай!')
def sostoyanie4():
    webbrowser.open('https://market.yandex.ru/brands--baskin-robbins/14981037', new=2)
def sostoyanie5():
    webbrowser.open('https://market.yandex.ru/product--morozhenoe-baskin-robbins-beisbolnyi-oreshek-1l/101812160361', new=2)
def sostoyanie6():
    speaker('Ура')

def youtube():
    webbrowser.open('https://www.youtube.com/', new=2)
def battlenet():
    subprocess.Popen('"E:\Battle.net\Battle.net Launcher.exe"')
def steam():
    subprocess.Popen('D:\Steam\Steam.exe')
def tanki():
    subprocess.Popen('E:\Lesta\GameCenter\lgc.exe')

def podarok():
    webbrowser.open('https://www.furla.com/ru/ru/', new=2)
def tovar():
    speaker('сумку или портфель')
def tovarr():
    webbrowser.open('https://www.furla.com/ru/ru/eshop/woman/woman-bags/', new=2)
def podarok1():
    webbrowser.open('https://www.intimissimi.com/ru/%D0%B6%D0%B5%D0%BD%D1%89%D0%B8%D0%BD%D1%8B/%D0%BF%D0%B8%D0%B6%D0%B0%D0%BC%D1%8B/', new=2)
def tovar1():
    speaker('пижаму')
def tovar2():
    webbrowser.open('https://www.intimissimi.com/ru/product/%D0%B4%D0%BB%D0%B8%D0%BD%D0%BD%D0%B0%D1%8F_%D0%BA%D0%BE%D0%BC%D0%B1%D0%B8%D0%BD%D0%B0%D1%86%D0%B8%D1%8F_%D0%B8%D0%B7_%D1%88%D1%91%D0%BB%D0%BA%D0%B0_eternal_love-LLD2472.html?dwvar_LLD2472_Z_COL_INT=2127', new=2)

def telegramm():
    webbrowser.open('https://t.me/Pythonpowerbot', new=2)

def offBot():
    sys.exit()



def ozon():
    webbrowser.open('https://www.ozon.ru/', new=2)
def yandex():
    webbrowser.open('https://market.yandex.ru/', new=2)
def gosuslugi():
    webbrowser.open('https://esia.gosuslugi.ru/login/', new=2)
def moidoc():
    webbrowser.open('https://www.mos.ru/uslugi/', new=2)




def passive():
    pass

#def offpc():
    #os.system('shutdown /s')