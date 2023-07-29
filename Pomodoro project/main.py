from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer() :
    window.after_cancel(timer)
    null_element.grid_forget()
    start_button.grid(row=3,column=1)
    timer_text.config(text="TIMER")
    checkmark_text.config(text="")
    canvas.itemconfig(countdown_text, text="00:00")
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_countdown() :
    start_button.grid_forget()
    null_element.grid(row=3,column=1)

    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0 :
        countdown(long_break_sec)
        timer_text.config(text="BREAK",fg=RED)
    elif reps % 2 == 0 :
        countdown(short_break_sec)
        timer_text.config(text="BREAK",fg=PINK)
    else :
        countdown(work_sec)
        timer_text.config(text="WORK",fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count) :
    count_minute= count//60
    count_second= count % 60

    if count_second < 10 :
        count_second="0"+str(count_second)
    if count_minute < 10 :
        count_minute="0"+str(count_minute)

    canvas.itemconfig(countdown_text, text=f"{count_minute}:{count_second}")
    if count > 0 :
        global timer
        timer= window.after(1000,countdown,count-1)
    else :
        start_countdown()
        mark=""
        for _ in range(reps//2):
            mark += "✔"
        checkmark_text.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas=Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
countdown_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=2,column=2)

timer_text=Label(text="TIMER",bg=YELLOW,fg=GREEN,font=(FONT_NAME,35,"bold"))
timer_text.grid(row=1,column=2)

start_button=Button(text="START", highlightthickness=0, command=start_countdown)
start_button.grid(row=3,column=1)

reset_button=Button(text="RESET", highlightthickness=0, command=reset_timer)
reset_button.grid(row=3,column=3)

checkmark_text=Label(bg=YELLOW,fg=GREEN,font=(FONT_NAME,15,"bold"))
checkmark_text.grid(row=4,column=2)

null_element=Label(text=".START",bg=YELLOW,fg=YELLOW)

window.mainloop()