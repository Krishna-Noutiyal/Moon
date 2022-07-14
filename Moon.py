import pyautogui as pg
import time
import random as r
import pyperclip


def SelectEmoji(lst=None):
    """Selects Emoji form the list randomly
    to use ur lst specificaly 
    """
    try:
        return r.choice(lst)
    except :
        EmojiLst = ["🤣","😘","😎","👌","😂"]
        Emoji = r.choice(EmojiLst)
        return Emoji

def Combination(Length=int,Rand=False,lst=None):
    """Copys the emoji to your clipboard
    Lenght - Defines how many emoji should me in 1 line
    Rand - Defines if the emoji in line should be random or not

    """
    if Rand==False:
        s = ""
        if s != "":
            pass
        else:
            SelectedEmoji = SelectEmoji(lst)
        for i in range(Length):
            s += f"{SelectedEmoji}"
        pyperclip.copy(s)

    elif Rand ==None:
        s = ""
        SelectedEmoji = SelectEmoji(lst)
        for i in range(Length):
            s += f"{SelectedEmoji}"
        pyperclip.copy(s)

    else:
        s = ""
        for i in range(Length):
            s += f"{SelectEmoji(lst)}"
        pyperclip.copy(s)


def PrintEmoji(Times=int,Length=int,Rand=False,lst=None):
    """
    Pasts Emoji and Hits Enter 😊😊
    """
    print("\n\n\n\t\tYou Have 5 sec click where you want to Enter Emojis !!!")

    time.sleep(5)
    for i in range(0,Times):
        Combination(Length,Rand,lst)
        pg.hotkey("ctrl","v")
        pg.press("enter")
        

if __name__ == "__main__":

    while True:

        
        def Times():
            try:
                
                Times = int(input("\n\nHow many time you want to print Emoji : "))
                if Times >= 1:
                    return Times
                raise ValueError
            except:
                return 10

        def No_Emoji_In_Line():
            """
            Asks user to Enter the no of Emoji's they want to 
            print in One line
            Returns the Number
            """
            try:
                no = int(input("How many Emoji's you want in one line : "))
                if no >= 1:
                    return no
                raise ValueError
            except:
                return 1

        def Rand_Or_Not():
            """
            Asks user to use Random emoji in line or Not
            Returns True or False 
            """

            s = """
                \n\nPress 0 to Use the same emoji in line
                \nPress 1 to use Random emoji in line
                \nPress 2 to use same emoji in line but diffrent emoji on the 2nd line
            """
            print(s)
            try:

                Rand = int(input("Type 0,1 or 2 respectivly : "))
                if Rand ==0:
                    return False
                elif Rand == 1:
                    return True
            except:
                return False

        def Custom_Emoji_Or_Not():
            st = """
                \nDo you want to use pre defined emojis or
                \nadd your own emoji's to use 
                \n\t1) Inbuilt Emojis
                \n\t2) Your Emojis
            """
            print(st)
            try:
                In = int(input("Choose from Option 1) and 2) : "))
                if In == 2:
                    return input("Enter Your Emoji with Spaces Betweeen Then : ").split()
            except:
                return None

        PrintEmoji(Times(),No_Emoji_In_Line(),Rand_Or_Not(),Custom_Emoji_Or_Not())

        c = input(" 'Y' to continue or 'Enter' to Exit : ")
        if c == "Y" or c == "y":
            continue
        else:
            break