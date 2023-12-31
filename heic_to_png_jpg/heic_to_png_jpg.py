import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror
from tkinter import filedialog as fd
from PIL import Image
from pillow_heif import register_heif_opener
import os

class Applikacka(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Konvertor Heic to jpg or png")
        self.geometry('200x80')
        self.iconbitmap('znak_skoda.ico')
        self.resizable(False, False)

        # layout gaddets
        self.label = ttk.Label(self, text="HEIC to PNG or JPG convertor")        
        self.label.grid(row=0, column=0, columnspan=2,padx=20)
        self.button_png = ttk.Button(self, text="Konvertuj")
        self.button_png['command'] = self.button_convert
        self.button_png.grid(column=0, row=1,columnspan=2)
        self.moje_value = tk.StringVar()
        self.moje_value.set('jpg')
        self.radiobutton_jpg = ttk.Radiobutton(self, text='jpg',variable=self.moje_value, value='jpg')
        self.radiobutton_jpg.grid(column=0, row=2)
        self.radiobutton_png = ttk.Radiobutton(self, text='png',variable=self.moje_value, value='png')
        self.radiobutton_png.grid(column=1, row=2)
        self.cesta = 'C:/Users/jakub.vlasak/Desktop/'
        self.muj_error = 'Hou, hou, cekani na smrt je horsi nez smrt sama.'

    def button_convert(self):
            register_heif_opener()
            file_types = (
                ('HEIC files', '*.heic'),
                ('All files', '*.*')
            )
            heic_files = [photo for photo in os.listdir() if '.heic' in photo]
            self.counter = len(heic_files)
            konvert_value = self.moje_value.get()

            heic_files = fd.askopenfilenames(initialdir=self.cesta,
                                            filetypes=file_types)
            if heic_files == '':
                showerror(title='ERROR', message= self.muj_error + '\nNevlozil si soubor.')
            else:
                try:
                    for fotka in heic_files:
                        temp_img = Image.open(fotka)
                        if konvert_value == 'png':
                            konvert_fotka = fotka.replace('.heic','.png')
                            temp_img.save(konvert_fotka)
                        else:
                            konvert_fotka = fotka.replace('.heic','.jpg')
                            temp_img.save(konvert_fotka)

                    print(heic_files)
                    print("Konvertuji...")
                    showinfo(title='Info', message='Konvert je hotov.')
                except:
                    showerror(title='Convert ERROR', message= self.muj_error + '\nAn error occured while trying to ' \
                        'convert the selected images in file ' + str(self.counter) + '.')


if __name__ == "__main__":
    muj_konvertor = Applikacka()
    muj_konvertor.mainloop()