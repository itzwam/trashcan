import time, sys

def loading(size=25, text=None):
    text = text + '  ' if text else ''
    for i in range(0, size):
        time.sleep(0.05)
        width = (i + 1)
        bar = "[" + "#" * width + " " * (size - width) + "]"
        sys.stdout.write(u"\u001b[1000D" + text +  bar)
        sys.stdout.flush()
    print
    
loading(100, "Installing system ...")