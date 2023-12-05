import main

main.glogger.error("Crazy")


input = input("Number")
try:
    input = input("Number")
    print("done")
except TypeError:
    print("can't")