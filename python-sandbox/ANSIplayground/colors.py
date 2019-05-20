class bcolors:
    
    # <DECORATION> : Decoration
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    REVERSED = '\033[7m'
    BLINK = '\033[5m'
    
    # <COLOR> : Color
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # B<COLOR> : Bright Color
    BBLACK = '\033[30;1m'
    BRED = '\033[31;1m'
    BGREEN = '\033[32;1m'
    BYELLOW = '\033[33;1m'
    BBLUE = '\033[34;1m'
    BMAGENTA = '\033[35;1m'
    BCYAN = '\033[36;1m'
    BWHITE = '\033[37;1m'

    # BG<COLOR> : BackGround Color
    BGBLACK = '\033[40m'
    BGRED = '\033[41m'
    BGGREEN = '\033[42m'
    BGYELLOW = '\033[43m'
    BGBLUE = '\033[44m'
    BGMAGENTA = '\033[45m'
    BGCYAN = '\033[46m'
    BGWHITE = '\033[47m'
    
    # BGB<COLOR> :  BackGround Bright Color
    BGBBLACK = '\033[40;1m'
    BGBRED = '\033[41;1m'
    BGBGREEN = '\033[42;1m'
    BGBYELLOG = '\033[43;1m'
    BGBBLUE = '\033[44;1m'
    BGBMAGENTA = '\033[45;1m'
    BGBCYAN = '\033[46;1m'
    BGBWHITE = '\033[47;1m'

    # Reset to default
    RESET = '\033[0m'
    
def printcolor(text="", color="BLUE"):
    str = text + "{RESET}"
    print(str.format(**bcolors.__dict__))


for color in bcolors.__dict__:
    printcolor("{"+ color +"}"+color)
