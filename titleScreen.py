import curses
from curses import wrapper
import time



def main(stdscr):

    curses.curs_set(0)
    stdscr.clear()

    curses.init_pair(1, 233,curses.COLOR_BLACK)
    text = "Benthesda Studios Presents"
    title = ["########   #######  ########  ##    ##",
             "##     ## ##     ## ##     ## ##   ## ",
             "##     ## ##     ## ##     ## ##  ##  ",
             "##     ## ##     ## ########  #####   ",
             "##     ## ##     ## ##   ##   ##  ##  ",
             "##     ## ##     ## ##    ##  ##   ## ",
             "########   #######  ##     ## ##    ##"]

    for i in range(0, 21):
        curses.init_pair(1, 233+i, curses.COLOR_BLACK)
        stdscr.addstr(int(curses.LINES/2), int((curses.COLS/2)-(len(text)/2)), text, curses.color_pair(1))
        stdscr.refresh()
        time.sleep(0.2)
        
    for i in range(0, 21):
        curses.init_pair(1, 254-i, curses.COLOR_BLACK)
        stdscr.addstr(int(curses.LINES/2), int((curses.COLS/2)-(len(text)/2)), text, curses.color_pair(1))
        stdscr.refresh()
        time.sleep(0.2)

        stdscr.clear()

    for i in range(0, 21):
        curses.init_pair(1, 233+i, curses.COLOR_BLACK)
        for j in range(0, 7):
            stdscr.addstr(int((curses.LINES/2)+(j%7)-4), int((curses.COLS/2)-(25)),title[j%7], curses.color_pair(1))
        
        stdscr.refresh()
        time.sleep(0.2)
        
    for i in range(0, 21):
        curses.init_pair(1, 254-i, curses.COLOR_BLACK)
        for j in range(0, 7):
            stdscr.addstr(int((curses.LINES/2)+(j%7)-4), int((curses.COLS/2)-(25)),title[j%7], curses.color_pair(1))
        
        stdscr.refresh()
        time.sleep(0.2)

wrapper(main)
