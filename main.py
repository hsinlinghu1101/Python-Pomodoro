from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
gb_timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    start.config(state='active')
    global reps
    reps = 0
    window.after_cancel(gb_timer)
    canvas.itemconfig(timer, text="00:00")
    label.config(text="Timer")
    check.config(text='')
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    start.config(state='disabled')
    global reps
    reps += 1
    if reps % 2 == 1:
      count_down(WORK_MIN*60)
      label.config(text="Work", fg=GREEN)
    elif reps % 8 == 0:
      count_down(LONG_BREAK_MIN * 60)
      label.config(text="Break", fg=RED)
    else:
      count_down(SHORT_BREAK_MIN * 60)
      label.config(text="Break", fg=PINK)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global gb_timer
        gb_timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ''
        for num in range(math.floor(reps/2)):
            mark += '✔'
        check.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
tomato = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato)
timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(column=1, row=1)

label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
label.grid(column=1, row=0)

start = Button(text="Start", highlightthickness=0, activebackground="white", command=start_timer)
start.grid(column=0, row=2)
reset = Button(text="Reset", highlightthickness=0, activebackground="white", command=reset_timer)
reset.grid(column=2, row=2)
check = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 10, "bold"))
check.grid(column=1, row=3)
window.mainloop()