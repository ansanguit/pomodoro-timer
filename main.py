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
reps = 0
clock  = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():

    window.after_cancel(clock)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer")
    check.config(text= "")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps

    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN*60)
        timer.config (text ="BREAK")
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN*60)
        timer.config(text="BREAK")
    else:
        count_down(WORK_MIN*60)
        timer.config(text="WORK")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    #print(count)
    #we have to format the seconds to 00:00
    #245 sec / 60 = 4 minutes
    #245 % 60 = seconds
    count_min = count // 60
    count_sec = count % 60 # This will give us a 0 instead of a 00 we need dynamic typing ie, changing the data type, just by assigning a value.This is quite unique to Python.
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global clock
        clock = window.after(1000, count_down, count-1)
    else:
        start_timer() # we need it in order to continue with the timer and breaks
       # to get a mark for every round of work
        mark = ""
        for _ in range (reps //2):
            mark += "✅"
        check.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx =100, pady= 50, bg= YELLOW)



#we have to create a canvas using Tkinter
canvas = Canvas(width = 220, height=230, bg = YELLOW, highlightthickness= 0)
tomato_img = PhotoImage(file = "tomato2.png") # This step is important to read the image
canvas.create_image(100,112, image = tomato_img )
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font= (FONT_NAME, 24, "bold"))
#we have assigned a variable to the text so that we can access it later to change it.
canvas.grid(column =1, row =1)

# now we create the labels and button

#timer
timer = Label(text= "Timer", font= (FONT_NAME, 35, "normal"), fg = GREEN, bg= YELLOW, highlightthickness= 0)
timer.grid(column =1, row =0)
timer.config(padx=10, pady=30)

#start
start = Button(text="Start", font =(FONT_NAME, 16, "normal"), fg= PINK, highlightthickness= 0, command = start_timer)
start.grid(column= 0, row=2)

#Reset
reset = Button(text="Reset", font =(FONT_NAME, 16, "normal"), fg= PINK, highlightthickness= 0, command =reset_timer)
reset.grid(column=2, row= 2)

#checks
check = Label(font= FONT_NAME, bg= YELLOW, highlightthickness= 0)
check.grid(column= 1, row=2)
check.config(padx=10, pady=30)


window.mainloop() #this is checking constantly if anything happened in the GUI
