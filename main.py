import tkinter as tk
from tkinter import *


window = tk.Tk()
window.title("Typing Speed Test")
window.config(padx=80, pady=80)
timer = None

def generate_sample():
    sample_text = "horse foot cover great here large whole door final rain front real king always " \
                  "back next hold once drive go behind rest just moon"
    return sample_text




def count_down(time):
    if time < 10:
        time_label.config(text = f"00:0{time}")
    else:
        time_label.config(text = f"00:{time}")

    if time > 0:
        global timer
        timer = window.after(1000, count_down, time - 1)
    else:
        result_label.config(text = calculate_wpm())



def start_test():
    if timer:
        window.after_cancel(timer)
        count_down(59)
    else:
        count_down(59)

    sample_text = generate_sample()
    sample_label.config(text = sample_text)
    user_input.delete(0, 'end')


def calculate_wpm():
    user_text = user_input.get()
    user_words = user_text.split()
    word_count = len(user_words)
    return f"Nice job! You have {word_count} WPM."

sample_label = tk.Label(window, text="hello", wraplength=400)
user_input = tk.Entry(window, width=40)
start_button = tk.Button(window, text="Start Test", command = start_test)
result_label = tk.Label(window, text="")
time_label = tk.Label(window, text="01:00", bg='green', fg='white')

start_button.config(bg='green', fg='white')


sample_label.pack()
user_input.pack()
start_button.pack()
result_label.pack()
time_label.pack()











window.mainloop()