import queue
import sounddevice as sd
import vosk
import json
import texts
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from skills import *
from tkinter import *



q = queue.Queue()
model = vosk.Model('vosk-model-small-ru-0.22')

device = sd.default.device = 0, 4                   # sd.default.device -1,3   /////input, output [1, 4]
samplerate = int(sd.query_devices(device[0], 'input')['default_samplerate'])  #48000


def callback(indata, frames, time, status):

    q.put(bytes(indata))


def recognize(data, vectorizer, clf):
    trg = texts.TRIGGERS.intersection(data.split())
    if not trg:
        return

    data.replace(list(trg)[0], '')
    text_vector = vectorizer.transform([data]).toarray()[0]
    answer = clf.predict([text_vector])[0]

    func_name = answer.split()[0]
    speaker(answer.replace(func_name, ''))
    exec(func_name + '()')


def main():
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(list(texts.data_set.keys()))

    clf = LogisticRegression()
    clf.fit(vectors, list(texts.data_set.values()))

    del texts.data_set

    with sd.RawInputStream(samplerate=samplerate, blocksize=16000, device=device[0],
                               dtype="int16", channels=1, callback=callback):

        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                data = json.loads(rec.Result())['text']
                recognize(data, vectorizer, clf)


visual = Tk()
visual.geometry('250x350')
visual.configure(bg = 'black')
visual.title('Пирожок')
visual.resizable(False, False)
visual.iconbitmap('icon.ico')

lb = Label(visual, text='Привет друг!')
lb.configure(bg='white')
lb.place(x = 25, y = 25, height=25, width=200)

but1 = Button(visual, text='Слушаю', command=main)
but1.configure(bd=1, font=('Castellat', 25),bg='white')
but1.place(x=50, y=160, height=50, width=150)
visual.update()
but2 = Button(visual, text='Выход', command=quit)
but2.configure(bd=1, font=('Castellat', 25),bg='white')
but2.place(x=50, y=220, height=50, width=150)

visual.mainloop()




if __name__ == "__main__":
    main()


