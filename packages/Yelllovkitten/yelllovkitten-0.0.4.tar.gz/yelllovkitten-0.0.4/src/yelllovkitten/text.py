from datetime import datetime, timezone

def color(text: str,color: str=None):
    if color == None:
        command = "0m"
    elif color == "red":
        command = "31m"
    elif color == "green":
        command = "32m"
    elif color == "yellow":
        command = "33m"
    elif color == "blue":
        command = "34m"
    elif color == "magenta":
        command = "35m"
    elif color == "cyan":
        command = "36m"
    elif color == "gray":
        command = "90m"
    elif color == "white":
        command = "97m"

    else:
        command = "0m"
    return f"\033[{command}{text}\033[m"

def info(text):
    return out(color(str(text),'green'))
def warn(text):
    return out(color(str(text),'yellow'))
def error(text):
    return out(color(str(text),'red'))


def out(text):
    textout = "\n" + str(datetime.now(timezone.utc))[:19] + " | " + str(text)
    print(textout,end="")
    return textout