import curses
from curses import wrapper
import time



def main(stdscr):

    curses.start_color()
    curses.curs_set(0)
    stdscr.clear()

    curses.init_pair(1, 233, curses.COLOR_BLACK)
    text = "Benthesda Studios Presents"
    title = ["`7MM\"\"\"Yb.     .g8\"\"8q.   `7MM\"\"\"Mq.  `7MMF' `YMM'",
             "  MM    `Yb. .dP'    `YM.   MM   `MM.   MM   .M'",
             "  MM     `Yb dP'      `YM   MM   `MM.   MM   .M' ",
             "  MM      MM MM        MM   MMmmdM9     MMMMM.   ",
             "  MM     ,MP MM.      ,MP   MM  YM.     MM  VMA ",
             "  MM    ,dP' `Mb.    ,dP'   MM   `Mb.   MM   `MM.",
             ".JMMmmmdP'     `\"bmmd\"'   .JMML. .JMM..JMML.   MMb.",
             " ",
             "              ESCAPE FROM TERROR CAVE             "]
                 

    for i in range(0, 21):
        curses.init_pair(1, 233+i, curses.COLOR_BLACK)
        stdscr.addstr(int(curses.LINES/2-1), int((curses.COLS/2)-(len(text)/2)), text, curses.color_pair(1))
        stdscr.refresh()
        time.sleep(0.2)
        
    for i in range(0, 21):
        curses.init_pair(1, 254-i, curses.COLOR_BLACK)
        stdscr.addstr(int(curses.LINES/2-1), int((curses.COLS/2)-(len(text)/2)), text, curses.color_pair(1))
        stdscr.refresh()
        time.sleep(0.2)

        stdscr.clear()
    lines = 9
    for i in range(0, 21):
        curses.init_pair(1, 233+i, curses.COLOR_BLACK)
        for j in range(0, lines):
            stdscr.addstr(int((curses.LINES/2)+(j%lines)-4), int((curses.COLS/2)-(25)),title[j%lines], curses.color_pair(1))
        
        stdscr.refresh()
        time.sleep(0.2)
        
    for i in range(0, 21):
        curses.init_pair(1, 254-i, curses.COLOR_BLACK)
        for j in range(0, lines):
            stdscr.addstr(int((curses.LINES/2)+(j%lines)-4), int((curses.COLS/2)-(25)),title[j%lines], curses.color_pair(1))
        
        stdscr.refresh()
        time.sleep(0.2)

    curses.endwin()

#wrapper(main)
