import os
import subprocess
from tkinter import filedialog
from pathlib import Path

def make_dir(self, singer_name):
        self.path = filedialog.askdirectory()
        print(self.path)
        try: # creating directory for downloading musics in there
            os.mkdir(Path(f'{self.path}/{singer_name}'))
        except FileExistsError:
            pass

def open_dir(self, path):
        if self.plt == 'Windows': # if the os is windwos
            os.startfile(path)
        else:
            subprocess.run(['xdg-open', path])