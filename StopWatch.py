##http://www.codeskulptor.org/#user39_2HGx53dVm5_0.py

# import
import simplegui
  
# initialize global variables used in your code here
timed = 0
tries = 0
win = 0
msec = 0

#define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(timed_var):
    global timed, msec
    minute = timed // 1000
    sec = (timed - minute * 1000) // 10
    msec = (timed - minute * 1000) % 10
    if sec < 10:
        return str(minute) + ":0" + str(sec) + "." + str(msec)
    else:
        return str(minute) + ":" + str(sec) + "." + str(msec)

# define event handlers for buttons; "Start", "Stop", "Reset"
def start_button():
    if not t.is_running():
        t.start()
        #print t.is_running()

def stop_button():
    global tries, win
    if t.is_running():
        t.stop()
        tries += 1
        if msec == 0:
            win += 1  
        
def reset_button():
    global timed, tries, win
    if t.is_running():
        t.stop()
        timed = 0
        tries = 0
        win = 0
        t.start()
    else :
        timed = 0
        tries = 0
        win = 0
        t.start()
        
#define timer handlers
def timer_hand():
    global timed
    timed += 1
    if timed - timed // 1000 * 1000 == 600:
        timed += 400

def draw(canvas):
    global timed, tries, wins
    score = str(win)+" / "+str(tries)
    timedisplay = format(timed)
    canvas.draw_text(score, [175,10], 12, "White")
    canvas.draw_text(timedisplay, [75,100], 18, "Red")    
    
# create frame
f=simplegui.create_frame("Stop Watch: ",200,200)

# register event handlers 
f.add_button("Start", start_button,200)
f.add_button("Stop", stop_button,200)
f.add_button("Reset", reset_button,200)
f.set_draw_handler(draw)
t = simplegui.create_timer(100, timer_hand)

# start frame
f.start()

# always remember to check your completed program against the grading rubric