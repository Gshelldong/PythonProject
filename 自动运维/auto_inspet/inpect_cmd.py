import pyautogui
import pyperclip
from time import sleep

class InspectCmd():
    def __init__(self):
        self.cmd_lists=["""ps -ef | grep hadoop""",
             r"""mt=`grep 'MemTotal:' /proc/meminfo |awk '{print $2}'`;ma=`grep 'Active:' /proc/meminfo|awk '{print $2}'`;mf=`expr $mt - $ma`;echo 'Memory:' `expr $mt / 1024`'M' all `expr $mf / 1024`'M' avail | awk  '{print $2,$4,"\033[1;31m" ($2-$4)/$2 "\033[0m"}'""",
             r"""sar -u 1 2 | sed '/^$/d' | awk '{print "\033[1;31m" "\t"$3 "\033[0m"}' """,
             """df -h""",
             """exit"""
                        ]

    def cmd_input(self):
        for i in self.cmd_lists:

            pyperclip.copy(i)
            pyperclip.paste()

            pyautogui.hotkey("ctrl","v")
            pyautogui.press("\n")
            sleep(0.4)
