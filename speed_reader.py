import tkinter as tk
import datetime
from tkinter.filedialog import askopenfilename
import time 
from PyPDF2 import PdfReader

class PDFReader:
    def __init__(self, path):
        self.path = path

    def read(self):
        with open(self.path, 'rb') as f:
            pdf_reader = PdfReader(f)
            for page in pdf_reader.pages:
                text = page.extract_text()
                words = text.split()
                return [word for word in words]
            
class TextReaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Reader App")

        # Initialize variables
        self.inc_val = 1
        self.reading = False
        self.current_page_index = 0
        self.wpm = 150
        self.path = None
        self.pdf_reader = None
        self.update_list_pointer = self.root.after(0, self.list_pointer)

        # Create GUI components
        self.create_gui()

    def create_gui(self):
        # Create frames
        fr_buttons = tk.Frame(self.root)
        fr_play = tk.Frame(self.root)
        fr_book = tk.Frame(self.root)
        fr_wpm = tk.Frame(self.root)

        # Create buttons and labels
        btn_open = tk.Button(fr_buttons, text="Open", command=self.open_file)
        btn_save = tk.Button(fr_buttons, text="Save As...")  # Add functionality as needed

        btn_pause = tk.Button(fr_play, text='\u23F8', command=self.toggle_reading)
        btn_play = tk.Button(fr_play, text='\u25B6', command=self.toggle_reading)

        incc = tk.Button(fr_play, text='\u003E\u003E', command=self.increase_inc)

        btn_inc_wpm = tk.Button(fr_wpm, text="\u002B", command=self.inc_wpm)
        lbl_wpm = tk.Label(fr_wpm, text=self.wpm)
        btn_dec_wpm = tk.Button(fr_wpm, text='-', command=self.dec_wpm)
        btn_rst = tk.Button(fr_wpm, text='Reset', command=self.reset)

        # Create labels
        self.text_label = tk.Label(self.root, text='not started')
        self.lbl_wpm = tk.Label(fr_wpm, text=self.wpm)

        # Grid layout
        fr_buttons.grid(row=0, column=0, sticky="ns")
        fr_play.grid(row=1, column=0, sticky='ns')
        fr_book.grid(row=2, column=1)
        fr_wpm.grid(row=3, column=1)

        btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

        btn_inc_wpm = tk.Button(fr_wpm, text="+", command=self.inc_wpm)
        btn_inc_wpm.grid(row=0, column=0)

        self.lbl_wpm.grid(row=0, column=1)

        btn_dec_wpm.grid(row=0, column=2)
        btn_rst.grid(row=0, column=3)
        btn_save.grid(row=0, column=1, sticky="ew")
        
        btn_pause.grid(row=0, column=0)
        btn_play.grid(row=0, column=1)
        incc.grid(row=0, column=2)

        btn_inc_wpm.grid(row=0, column=0)
        lbl_wpm.grid(row=0, column=1)
        btn_dec_wpm.grid(row=0, column=2)
        btn_rst.grid(row=0, column=3)

        self.text_label.grid(row=0, column=1)

        # Other setup
        self.counting()
        self.clock()
    
    def list_pointer(self):
        if self.reading and self.pdf_reader:
            try:
                words_per_iteration = 1  # Adjust this value based on user preference
                for _ in range(words_per_iteration):
                    new_text = self.pdf_reader.read()[self.current_page_index]
                    self.text_label.config(text=new_text)
                    self.current_page_index += 1
            except IndexError:
                # End of the document, stop reading
                self.reading = False
        self.root.after(int(60000 / self.wpm), self.list_pointer)


    def update_list_pointer(self):
        if self.reading:
            self.current_page_index += self.inc_val
            self.list_pointer()

    def open_file(self):
        self.path = askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if self.path:
            self.pdf_reader = PDFReader(self.path)
            self.current_page_index = 0
            self.update_text_label()

    def pause(self):
        self.inc_val = 0

    def play(self):
        self.inc_val = 1
        self.text_label['text'] = self.inc_val

    def increase_inc(self):
        self.inc_val += 9
        self.text_label['text'] = self.inc_val

    def inc_wpm(self):
        self.wpm += 10
        self.lbl_wpm['text'] = self.wpm
        

    def dec_wpm(self):
        self.wpm -= 10
        self.lbl_wpm['text'] = self.wpm

    def counting(self):
        if self.inc_val and self.reading:
            self.current_page_index += self.inc_val
            self.update_text_label()
        self.root.after(1000, self.counting)

    def reset(self):
        self.current_page_index = 0

    def toggle_reading(self):
        self.reading = not self.reading

    def update_text_label(self):
        if self.reading and self.pdf_reader:
            try:
                new_text = self.pdf_reader.read()[self.current_page_index]
                self.text_label.config(text=new_text)
            except IndexError:
                # End of the document, stop reading
                self.reading = False

    def clock(self):
        time = datetime.datetime.now().strftime("Time: %H:%M:%S")
        self.root.title(time)
        self.root.after(1000, self.clock)

if __name__ == "__main__":
    root = tk.Tk()
    app = TextReaderApp(root)
    root.mainloop()
