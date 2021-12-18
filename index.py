# pip install tk
# pip install tkinter-page
# pip install tkinter
import tkinter as tk
from tkinter import Message, Text
import tkinter.ttk as ttk
import tkinter.font as font

# pip install opencv-python
import cv2


# pip install shutil
# Fungsinya untuk mencopy file dengan directorynya secara otomatis
import shutil

# pip install csv
# Fungsinya untuk membaca file excel atau csv nya
import csv

# pip install Pillow
# Fungsinya untuk membuat kotakan deteksi wajah
from PIL import Image, ImageTk

# pip install numpy
# Fungsinya untuk membuat perhitungan atau aritmatika di python
import numpy as np

# pip install pandas
# Fungsinya untuk membuat inputan data kedalam suatu data yang diolah lebih lanjut
import pandas as pd

# Default dari instalasi Python
import os
# Untuk membaca directory atau isi dari sebuah directory
import datetime
# Untuk mengambil waktu dan tanggal dalam format date time
import time
# Untuk mengambil waktu yang berjalan sekarang dengan format time


# Membuat objek window yang dideklarasi dari package tkinter
window = tk.Tk()
# Membuat title dari object window
window.title("Face Checker")

# Membuat background warna dari GUI nya
window.configure(background='lightblue')

# Membuat grid dari window (GUI nya) defaultnya weight nya 1
window.grid_rowconfigure(0, weight=1)
# Row untuk baris dan dari windownya (GUI) defaultnya weight nya 1
window.grid_columnconfigure(0, weight=1)

# Membuat text message
# text nya diisi "Pendeteksi Wajah", Backgroundnya diubah lightgreen, Warna tulisannya "black" (Hitam)
message = tk.Label(window, text="Face Checker", bg="lightgreen", fg="black", width=50, height=3, font=('times new roman', 30, 'bold'))

# Meletakkan posisi message terhadap window (GUI)
message.place(x=200, y=20)

# Membuat text untuk Memasukkan ID Student
teksidstudent = tk.Label(window, text="Enter ID Student", width=20, height=2,
                fg="black", bg="lightyellow", font=('times', 15, 'bold'))
# Mengatur posisi teksidstudent terhadap window (GUI)
teksidstudent.place(x=400, y=200)

# Membuat input untuk memasukkan ID Student
inputidstudent = tk.Entry(window, width=20, bg="lightyellow", fg="black", font=('times', 15, 'bold'))
# Mengatur posisi inputidstudent terhadap window (GUI)
inputidstudent.place(x=700, y=215)

# Membuat text untuk memasukkan Name Student
teksnamestudent = tk.Label(window, text="Enter Student Name", width=20, fg="black", bg="lightyellow", height=2, font=('times', 15, 'bold'))
# Mengatur posisi teksnamestudent terhadap window (GUI)
teksnamestudent.place(x=400, y=300)

# Membuat input untuk memasukkan Student Name
inputstudentname = tk.Entry(window, width=20, bg="lightyellow", fg="black", font=('times', 15, 'bold'))
# Mengatur posisi inputstudentname terhadap window (GUI)
inputstudentname.place(x=700, y=315)

# Membuat teksnotifikasi untuk menampilkan informasi dari system
teksnotifikasi = tk.Label(window, text="Notification System : ", width=20, fg="black", bg="lightyellow", height=2, font=('times', 15, 'bold'))
# Mengatur posisi teksnotifikasi terhadap window (GUI)
teksnotifikasi.place(x=400, y=400)

# Membuat inputisinotifikasi untuk menampilkan informasi dari system
# teksnya diisi kosong karena untuk menampilkan output dari system jika terjadi aktivitas
message = tk.Label(window, text="", bg="lightyellow", fg="red", width=30,
                height=2, activebackground="yellow", font=('times', 15, 'bold'))
# Mengatur posisi inputisinotifikasi terhadap window (GUI)
message.place(x=700, y=400)

# Membuat label informasikehadiran untuk menampilkan informasi dari system
informasikehadiran = tk.Label(window, text="Attadance Information : ", width=20, fg="black",
                bg="lightyellow", height=2, font=('times', 15, 'bold'))
# Mengatur posisi informasikehadiran terhadap window (GUI)
informasikehadiran.place(x=400, y=650)

# Membuat label message2 untuk menampilkan informasi kehadiran mahasiswa jika sudah dideteksi
# teksnya diisi kosong karena untuk menampilkan output dari system jika mahasiswa melakukan aktivitas deteksi wajah
message2 = tk.Label(window, text="", fg="red", bg="lightyellow", activeforeground="green", width=30, height=2, font=('times', 15, 'bold'))
# Mengatur posisi message2 terhadap window (GUI)
message2.place(x=700, y=650)

# Membuat fungsi clear untuk membersihkan text yang diinput didalam field inputidstudent
def clear():
    # Menghapus isi dari inputidstudent dengan parameter 0 untuk menghapus isi inputnya
    inputidstudent.delete(0, 'end')
    res = ""
    # Mengoverride isi text dengan variabel res alias String kosong
    message.configure(text=res)

# Membuat fungsi clear2 untuk membersihkan text yang diinput didalam field inputstudentname
def clear2():
    # Menghapus isi dari inputstudentname dengan parameter 0 untuk menghapus isi inputnya
    inputstudentname.delete(0, 'end')
    res = ""
    # Mengoverride isi text dengan variabel res alias String kosong
    message.configure(text=res)

# Membuat fungsi is_number() 
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False


def TakeImages():
    # Mengambil value dari inputidstudent
    Id = (inputidstudent.get())
    # Mengambil value dari inputstudentname
    name = (inputstudentname.get())
    # Mengecek apakah value dari inputidstudent adalah number (angka)
    # Dan mengecek apakah value inputstudentname
    if(is_number(Id) and name.isalpha()):
        # membuat variabel cam yang berisikan VideoCapture(0)
        # Mangsudnya adalah untuk prepare dan koneksi dengan kamera perangkat
        cam = cv2.VideoCapture(0)
        # harcascadePath adalah nama file dari haarcascade_frontalface_default.xml
        # yang berisikan algoritma untuk mengenali bentuk wajah jika kamera dibuka
        harcascadePath = "haarcascade_frontalface_default.xml"
        # membuat variabel detector untuk mendeteksi apakah algoritma yang
        # ada pada file haarcascade_frontalface_default.xml terdapat pada kamera
        detector = cv2.CascadeClassifier(harcascadePath)
        # Membuat variable sampleNum yang digunakan untuk mencari
        sampleNum = 0
        # membuat parameter 
        while(True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
                # Menambahkan 
                sampleNum = sampleNum+1
                # Menuliskan dan membaca write 
                cv2.imwrite("TrainingImage\ "+name + "."+Id + '.' +
                            str(sampleNum) + ".jpg", gray[y:y+h, x:x+w])
                # menampilkan frame kamera dengan parameter img
                cv2.imshow('frame', img)
            # menunggu koneksi dengan parameter 100 (100 ms)
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # Jika sampleNum melebihi target (target kita 10 foto) maka break looping while nya
            elif sampleNum > 10:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Saved for ID : " + Id + " Name : " + name
        row = [Id, name]
        with open('StudentDetails\StudentDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        message.configure(text=res)
    else:
        # Jika input nama nya adalah number atau angka
        if(is_number(name)):
            messagenotifikasi = "Enter Alphabetical Name"
            # menampilkan variabel messagenotifikasi kedalam GUI (label notofikasi)
            message.configure(text=messagenotifikasi)
        # jika input namanya adalah alfabet atau selain angka
        if(Id.isalpha()):
            # membuat variabel messagenotifikasi dan mengisikan pesan bahwa id harrus number
            messagenotifikasi = "Enter Numeric Id"
            # menampilkan variabel messagenotifikasi kedalam GUI (label notofikasi)
            message.configure(text=messagenotifikasi)

def TrainImages():
    # Menggunakan salah satu method (bergantung pada perangkat yang digunakan)
    # recognizer = cv2.face.LBPHFaceRecognizer_create()
    # recognizer = cv2.createLBPHFaceRecognizer()
    recognizer = cv2.face_LBPHFaceRecognizer.create()
    # membuat variabel detector untuk mendeteksi apakah algoritma yang
    # ada pada file haarcascade_frontalface_default.xml terdapat pada kamera
    harcascadePath = "haarcascade_frontalface_default.xml"
    # membuat variabel detector untuk mendeteksi apakah algoritma yang
    # ada pada file haarcascade_frontalface_default.xml terdapat pada kamera
    detector = cv2.CascadeClassifier(harcascadePath)
    
    faces, Id = getImagesAndLabels("TrainingImage")

    recognizer.train(faces, np.array(Id))
    recognizer.save("TrainingImageLabel\Trainner.yml")
    res = "Image Trained"  # +",".join(str(f) for f in Id)
    message.configure(text=res)


def getImagesAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    # print(imagePaths)
    faces = []
    Ids = []
    for imagePath in imagePaths:
        pilImage = Image.open(imagePath).convert('L')
        imageNp = np.array(pilImage, 'uint8')
        Id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces.append(imageNp)
        Ids.append(Id)
    return faces, Ids


def TrackImages():
    # Membuat koneksi dengan kamera dari method face yang sudah di instansiasi face nya
    recognizer = cv2.face.LBPHFaceRecognizer_create() 
    # Membaca file trainer.yml untuk membuat kotak informasi pada wajah saat terdeteksi
    recognizer.read("TrainingImageLabel\Trainner.yml")
    # harcascadePath adalah nama file dari haarcascade_frontalface_default.xml
    # yang berisikan algoritma untuk mengenali bentuk wajah jika kamera dibuka
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath)
    df = pd.read_csv("StudentDetails\StudentDetails.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', 'Name', 'Date', 'Time']
    attendance = pd.DataFrame(columns=col_names)
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for(x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x+w, y+h), (225, 0, 0), 2)
            Id, conf = recognizer.predict(gray[y:y+h, x:x+w])
            if(conf < 50):
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(
                    ts).strftime('%H:%M:%S')
                aa = df.loc[df['Id'] == Id]['Name'].values
                tt = str(Id)+"-"+aa
                attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]

            else:
                Id = 'Unknown'
                tt = str(Id)
            if(conf > 75):
                noOfFile = len(os.listdir("ImagesUnknown"))+1
                cv2.imwrite("ImagesUnknown\Image"+str(noOfFile) +
                            ".jpg", im[y:y+h, x:x+w])
            cv2.putText(im, str(tt), (x, y+h), font, 1, (0, 0, 255), 2)
        attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
        cv2.imshow('im', im)
        if (cv2.waitKey(1) == ord('q')):
            break
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour, Minute, Second = timeStamp.split(":")
    fileName = "Attendance\Attendance_"+date+"_"+Hour+"-"+Minute+"-"+Second+".csv"
    attendance.to_csv(fileName, index=False)
    cam.release()
    cv2.destroyAllWindows()
    # print(attendance)
    res = attendance
    message2.configure(text=res)



# Membuat button clearButton untuk menghapus data yang ada pada ID Student
clearButton = tk.Button(window, text="Clear ID Student", command=clear, fg="red", bg="yellow", width=20, height=2, activebackground="#ff0000", font=('times', 15, ' bold '))
# Mengatur posisi clearButton terhadap window (GUI)
clearButton.place(x=950, y=200)

# Membuat button clearButton2 untuk menghapus data yang ada pada Name Student
clearButton2 = tk.Button(window, text="Clear Student Name", command=clear2, fg="red", bg="yellow",
                        width=20, height=2, activebackground="Red", font=('times', 15, ' bold '))
# Mengatur posisi clearButton2 terhadap window (GUI)
clearButton2.place(x=950, y=300)

# Membuat button takeImg untuk menjalankan fungsi TakeImages ketika di klik
takeImg = tk.Button(window, text="Take Images", command=TakeImages, fg="red", bg="yellow", width=20, height=3, activebackground="Red", font=('times', 15, ' bold '))
# Mengatur posisi takeImg terhadap window (GUI)
takeImg.place(x=200, y=500)

# Membuat button trainImg untuk menjalankan fungsi TakeImages ketika di klik
trainImg = tk.Button(window, text="Train Images", command=TrainImages, fg="red", bg="yellow", width=20, height=3, activebackground="Red", font=('times', 15, ' bold '))
# Mengatur posisi trainImg terhadap window (GUI)
trainImg.place(x=500, y=500)

# Membuat button trackImg untuk menjalankan fungsi TakeImages ketika di klik
trackImg = tk.Button(window, text="Track Images", command=TrackImages, fg="red", bg="yellow", width=20, height=3, activebackground="Red", font=('times', 15, ' bold '))
# Mengatur posisi trackImg terhadap window (GUI)
trackImg.place(x=800, y=500)

# Membuat button quitWindow untuk menjalankan fungsi quitWindow ketika di klik
quitWindow = tk.Button(window, text="Quit", command=window.destroy, fg="red", bg="yellow", width=20, height=3, activebackground="Red", font=('times', 15, ' bold '))
# Mengatur posisi quitWindow terhadap window (GUI)
quitWindow.place(x=1100, y=500)

# copyWrite untuk membuat text yang digunakan untuk footer dan deskripsi di akhir teks
copyWrite = tk.Text(window, background=window.cget("background"), borderwidth=0, font=('times', 30, 'italic bold underline'))
copyWrite.tag_configure("superscript", offset=10)
copyWrite.insert("insert", "Developed by Kelompok 4", "superscript")
copyWrite.configure(state="disabled", fg="red")
copyWrite.pack(side="left")
copyWrite.place(x=800, y=750)

# Menjalankan GUI nya dengan fungsi mainloop()
window.mainloop()
