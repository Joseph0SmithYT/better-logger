from time import time, ctime
import datetime

logfile = False
bTimeStamp = False

def setup(logfile_option=False, timestamp_option=False):
    global logfile, bTimeStamp
    logfile = logfile_option
    bTimeStamp = timestamp_option

def printmsg(logtype, reason):
    print(bTimeStamp)
    if bTimeStamp is True:
        local_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"{local_time}: {logtype.upper()} | {reason}")
    else:
        print(f"{logtype.upper()} | {reason}")

def error(reason):
    printmsg("ERROR", reason)

def warning(reason):
    printmsg("WARNING", reason)

def info(reason):
    printmsg("INFO", reason)

def custom(reason, custommsg):
    printmsg(custommsg, reason)

if __name__ == "__main__":
    setup(logfile_option=True, timestamp_option=False)
    custom("cracker", "debug")
    setup(logfile_option=True)
