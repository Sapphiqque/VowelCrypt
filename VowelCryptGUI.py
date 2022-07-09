from tkinter import *
from tkinter import filedialog
import os
import tempfile

win = Tk()
win.title("VowelCrypt")
# ---Creates a temporary transparent image file for window icon
ICON = (b'\x00\x00\x01\x00\x01\x00\x10\x10\x00\x00\x01\x00\x08\x00h\x05\x00\x00'
        b'\x16\x00\x00\x00(\x00\x00\x00\x10\x00\x00\x00 \x00\x00\x00\x01\x00'
        b'\x08\x00\x00\x00\x00\x00@\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x01\x00\x00\x00\x01') + b'\x00'*1282 + b'\xff'*64

_, ICON_PATH = tempfile.mkstemp()
with open(ICON_PATH, 'wb') as icon_file:
    icon_file.write(ICON)
# ---
win.iconbitmap(default=ICON_PATH)
win.resizable(False, False)
dsp1 = Entry(win, width = 18, borderwidth = 5)
dsp1.grid(row = 1, column = 1, columnspan = 2, padx = 10, pady = 5)

filename = "NULL"
def open_file():
    dsp1.delete(0, END)
    f = filedialog.askopenfile(mode = 'r', filetypes = [("Text Files", "*.txt")])
    global filename
    filename = f.name
    dsp1.insert(0, os.path.basename(f.name))
    print(filename)

def encrypt_file():
    if (filename != "NULL"):
        with open(filename, "r") as f1, open("encrypted.txt", "w") as f2:
            first_char_indicator = True
            end_of_sent = False
            first_char = "X"
            while 1:
                char = f1.read(1)
                if not char:
                    if (end_of_sent == False):
                        f2.write(first_char)
                    break
                if first_char_indicator:
                    first_char = char
                    first_char_indicator = False
                elif (char == "A"):
                    f2.write("Ye")
                elif (char == "a"):
                    f2.write("ye")
                elif (char == "E"):
                    f2.write("Ai")
                elif (char == "e"):
                    f2.write("ai")
                elif (char == "I"):
                    f2.write("Eo")
                elif (char == "i"):
                    f2.write("eo")
                elif (char == "O"):
                    f2.write("Iu")
                elif (char == "o"):
                    f2.write("iu")
                elif (char == "U"):
                    f2.write("Oy")
                elif (char == "u"):
                    f2.write("oy")
                elif (char == "Y"):
                    f2.write("Ua")
                elif (char == "y"):
                    f2.write("ua")
                elif (char == "."):
                    f2.write(first_char)
                    f2.write(".")
                    end_of_sent = True
                elif (char == "\n"):
                    if (end_of_sent == False):
                        f2.write(first_char)
                    f2.write(char)
                    first_char_indicator = True
                    end_of_sent = False
                elif ((char == " ") and (first_char_indicator == False) and (end_of_sent == False)):
                    f2.write(first_char)
                    f2.write(" ")
                    first_char_indicator = True
                elif ((char == " ") and (first_char_indicator == False) and (end_of_sent == True)):
                    f2.write(" ")
                    first_char_indicator = True
                    end_of_sent = False
                else:
                    f2.write(char)
    else:
        dsp1.delete(0, END)
        dsp1.insert(0, "No file selected")

def decrypt_file():
    num = 0
    # if (filename != "NULL"):
    #     with open(filename, "r") as f1, open("decrypted.txt", "w") as f2:
    #         first_char_indicator = True
    #         end_of_sent = False
    #         first_char = "X"
    #         while 1:
    #             char = f1.read(1)
    #             if not char:
    #                 if (end_of_sent == False):
    #                     f2.write(first_char)
    #                 break
    #             if first_char_indicator:
    #                 first_char = char
    #                 first_char_indicator = False
    #             elif (char == "A"):
    #                 f2.write("Ye")
    #             elif (char == "a"):
    #                 f2.write("ye")
    #             elif (char == "E"):
    #                 f2.write("Ai")
    #             elif (char == "e"):
    #                 f2.write("ai")
    #             elif (char == "I"):
    #                 f2.write("Eo")
    #             elif (char == "i"):
    #                 f2.write("eo")
    #             elif (char == "O"):
    #                 f2.write("Iu")
    #             elif (char == "o"):
    #                 f2.write("iu")
    #             elif (char == "U"):
    #                 f2.write("Oy")
    #             elif (char == "u"):
    #                 f2.write("oy")
    #             elif (char == "Y"):
    #                 f2.write("Ua")
    #             elif (char == "y"):
    #                 f2.write("ua")
    #             elif (char == "."):
    #                 f2.write(first_char)
    #                 f2.write(".")
    #                 end_of_sent = True
    #             elif (char == "\n"):
    #                 if (end_of_sent == False):
    #                     f2.write(first_char)
    #                 f2.write(char)
    #                 first_char_indicator = True
    #                 end_of_sent = False
    #             elif ((char == " ") and (first_char_indicator == False) and (end_of_sent == False)):
    #                 f2.write(first_char)
    #                 f2.write(" ")
    #                 first_char_indicator = True
    #             elif ((char == " ") and (first_char_indicator == False) and (end_of_sent == True)):
    #                 f2.write(" ")
    #                 first_char_indicator = True
    #                 end_of_sent = False
    #             else:
    #                 f2.write(char)
    # else:
    #     dsp1.delete(0, END)
    #     dsp1.insert(0, "No file selected")
    
lbl1 = Label(win, text = "Select File:").grid(row = 0, column = 0, padx = 10, pady = 10)
lbl2 = Label(win, text = "Selected File ->").grid(row = 1, column = 0, padx = 10, pady = 5)

btn_browse = Button(win, text = "Browse", command = open_file).grid(row = 0, column = 1, padx = 10, pady = 10)
btn_encrypt = Button(win, text = "Encrypt", command = encrypt_file).grid(row = 2, column = 0, padx = 10, pady = 10)
btn_decrypt = Button(win, text = "Decrypt", command = decrypt_file).grid(row = 2, column = 1, padx = 10, pady = 10)

win.mainloop()