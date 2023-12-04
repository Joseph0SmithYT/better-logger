from time import time,ctime
import datetime

def printmsg(logtype, reason):
    local_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"{local_time}: {logtype.upper()} | {reason}")

class glogger():
    def error(reason):
        printmsg("ERROR", reason)
    def warning(reason):
        printmsg("WARNING", reason)
    def info(reason):
        printmsg("INFO", reason)
    def custom(reason, custommsg):
        printmsg(custommsg,reason)
if "__main__" == __name__:
    glogger.custom("cracker", "debug")