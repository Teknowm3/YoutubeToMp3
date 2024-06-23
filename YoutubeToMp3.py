# MIT License
#
# Copyright (c) 2024 Olcay Alkan
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import tkinter as tk
from tkinter import messagebox
from yt_dlp import YoutubeDL
import threading
import os

class Downloader:
    def __init__(self, url):
        self.url = url
        self.completed = 0
        self.total_size = 0
        self.title = ""
        self.download_thread = threading.Thread(target=self.download)
        self.download_thread.start()

    def download(self):
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            'noplaylist': True,
            'progress_hooks': [self.progress_hook]
        }
        try:
            with YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(self.url, download=False)
                self.title = info_dict.get('title', '')
                self.total_size = info_dict.get('filesize', 0)
                ydl.download([self.url])
        except Exception as e:
            self.show_error(str(e))

    def progress_hook(self, d):
        if d['status'] == 'downloading':
            self.completed = d.get('downloaded_bytes', 0)
            current_text = progress_text.get("1.0", tk.END)
            progress_text.delete("1.0", tk.END)
            progress_text.insert(tk.END, current_text + f"Downloading {self.title}... {self.get_progress()} ({self.get_size()} total, {self.total_size / (1024 * 1024):.2f} MB to be downloaded)\n")
            progress_text.see(tk.END)
        elif d['status'] == 'finished':
            self.completed = self.total_size
            current_text = progress_text.get("1.0", tk.END)
            progress_text.delete("1.0", tk.END)
            progress_text.insert(tk.END, current_text + f"Downloaded and converted to {self.title}.mp3 \n")
            progress_text.see(tk.END)
            self.convert_to_mp3()

    def convert_to_mp3(self):
        original_file = f"{self.title}.webm"
        converted_file = f"{self.title}.mp3"
        os.rename(original_file, converted_file)

    def get_progress(self):
        if self.total_size > 0:
            return f"{self.completed / self.total_size * 100:.2f}%"
        else:
            return "0.00%"

    def get_size(self):
        return f"{self.completed / (1024 * 1024):.2f} MB"

    def show_error(self, error_message):
        messagebox.showerror("Error", f"Failed to download video: {error_message}")

def download_and_convert():
    youtube_url = url_entry.get()
    if not youtube_url:
        messagebox.showerror("Error", "URL cannot be empty! \nPlease enter a valid URL!")
        return
    downloader = Downloader(youtube_url)

# GUI setup
root = tk.Tk()
root.title("YouTube Downloader")

blank_label = tk.Label(root, text="")
blank_label.pack()

url_label = tk.Label(root, text="YouTube URL:")
url_label.pack()

blank_label = tk.Label(root, text="")
blank_label.pack()

url_entry = tk.Entry(root, width=95)
url_entry.pack()

blank_label = tk.Label(root, text="")
blank_label.pack()

info_label = tk.Label(root, text="Information")
info_label.pack()

blank_label = tk.Label(root, text="")
blank_label.pack()

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

progress_text = tk.Text(root, height=12, width=95, yscrollcommand=scrollbar.set)
progress_text.pack()

scrollbar.config(command=progress_text.yview)

blank_label = tk.Label(root, text="")
blank_label.pack()

download_button = tk.Button(root, text="Download and Convert", command=download_and_convert)
download_button.pack()

blank_label = tk.Label(root, text="")
blank_label.pack()

progress_text.insert(tk.END, "The mp3 file to be downloaded will start processing within 15 seconds...\n")
progress_text.insert(tk.END, "The mp3 file to be downloaded will be added to the folder where the program file is located.\n")

root.mainloop()
