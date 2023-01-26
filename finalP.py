import tkinter as tk #Library tkinter (install --> pip install tk)
from tkinter import ttk
from tkinter import filedialog
import speech_recognition as sr #Library Speech Recognition (install --> pip install SpeechRecognition)
from pygame import mixer  #Library pygame (install --> pip install pygame)


r = sr.Recognizer()
mixer.init()

def recognize_file(): #memuat file audio dan mengkonversi ucapan menjadi bentuk text menggunaan recognize google
    f = select_file() 

    mixer.music.load(f) #memuat file audio untuk diputar
    mixer.music.play() #memulai pemutaran file audio

    #Open file audio
    with sr.AudioFile(f) as source:
        audio = r.record(source) #Listen data audio dan memuat data audio ke memori

        try:       
            text = r.recognize_google(audio, language='id') #mendeteksi audio dan mengkonversi ke dalam bentuk text
            text_widget.insert('0.0', text) #memasukan text yang dikonversi dengan waktu mulai 0.0 detik

        except sr.UnknownValueError: #kesalahan value yang tidak diketahui
            print('Audio tidak bisa dikenali')
        
        except sr.RequestError as e: #kesalahan lain
            print(e)

   
def save_file(): #menyimpan file text audio
    f = select_file()
    with open(f, 'w') as file: #open untuk membuka file dan w untuk menulis file
        file.write(text_widget.get('0.0', 'end')) #menulis file dengan  waktu mulai 0.0 detik


def select_file(): #memilih file penyimpanan
    file_path = filedialog.askopenfilename(title = "Pilih file")
    return file_path

root = tk.Tk() #membuat turunan frame tkinter
root.title("SPEECH TO TEXT : AUDIO")
root.resizable(0, 0) #mengubah ukuran window

 
text_widget = tk.Text(font=('Times New Roman', 14)) #mengatur jenis dan ukuran
text_widget.grid(column=0, row=0)

button_frame = tk.Frame() #membuat frame
button_frame.grid(column=0, row=1)

recognize_btn = ttk.Button(button_frame, text='Enter audio', command= recognize_file) #membuat button yang menginput file audio
save_btn = ttk.Button(button_frame, text='Save text', command=save_file) #membuat button yang menyimpan file konversi text audio

recognize_btn.grid(column=0, row=0)
save_btn.grid(column=1, row=0)

root.mainloop() #mengeksekusi aplikasi

