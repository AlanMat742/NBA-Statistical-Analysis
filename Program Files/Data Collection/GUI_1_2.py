import tkinter as tk
from tkinter import ttk
from tkinter import *
import pandas as pd
import datetime

LARGE_FONT = ("Verdana", 12)


class nbaGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, *kwargs)

        tk.Tk.wm_title(self, "NBA Statistics")

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {HomePage:HomePage(container,self), Mavericks:Mavericks(container,self), Nuggets:Nuggets(container,self), GoldenState:GoldenState(container,self), Rockets:Rockets(container,self),Clippers: Clippers(container,self),Lakers:Lakers(container,self), Grizzlies:Grizzlies(container,self), Timberwolves:Timberwolves(container,self), Pelicans:Pelicans(container,self),Thunder:Thunder(container,self), Suns:Suns(container,self), TrailBlazers:TrailBlazers(container,self), Kings:Kings(container,self), SanAntonioSpurs:SanAntonioSpurs(container,self), Jazz:Jazz(container,self), Hawks:Hawks(container,self), Celtics:Celtics(container,self),Nets:Nets(container,self),Hornets: Hornets(container,self), Bulls:Bulls(container,self),Cavaliers: Cavaliers(container,self), Pistons:Pistons(container,self), Pacers:Pacers(container,self), Heat:Heat(container,self),Bucks:Bucks(container,self), Knicks: Knicks(container,self),Magic: Magic(container,self),Philadelphia: Philadelphia(container,self), Raptors:Raptors(container,self), Wizards:Wizards(container,self)}
        self.frames[HomePage].grid(row=0, column=0, sticky='nsew')
        self.frames[Mavericks].grid(row=0, column=0, sticky='nsew')
        self.frames[Nuggets].grid(row=0, column=0, sticky='nsew')
        self.frames[GoldenState].grid(row=0, column=0, sticky='nsew')
        self.frames[Rockets].grid(row=0, column=0, sticky='nsew')
        self.frames[Clippers].grid(row=0, column=0, sticky='nsew')
        self.frames[Lakers].grid(row=0, column=0, sticky='nsew')
        self.frames[Grizzlies].grid(row=0, column=0, sticky='nsew')
        self.frames[Timberwolves].grid(row=0, column=0, sticky='nsew')
        self.frames[Pelicans].grid(row=0, column=0, sticky='nsew')
        self.frames[Thunder].grid(row=0, column=0, sticky='nsew')
        self.frames[Suns].grid(row=0, column=0, sticky='nsew')
        self.frames[TrailBlazers].grid(row=0, column=0, sticky='nsew')
        self.frames[Kings].grid(row=0, column=0, sticky='nsew')
        self.frames[SanAntonioSpurs].grid(row=0, column=0, sticky='nsew')
        self.frames[Jazz].grid(row=0, column=0, sticky='nsew')
        self.frames[Hawks].grid(row=0, column=0, sticky='nsew')
        self.frames[Celtics].grid(row=0, column=0, sticky='nsew')
        self.frames[Nets].grid(row=0, column=0, sticky='nsew')
        self.frames[Hornets].grid(row=0, column=0, sticky='nsew')
        self.frames[Bulls].grid(row=0, column=0, sticky='nsew')
        self.frames[Cavaliers].grid(row=0, column=0, sticky='nsew')
        self.frames[Pistons].grid(row=0, column=0, sticky='nsew')
        self.frames[Pacers].grid(row=0, column=0, sticky='nsew')
        self.frames[Heat].grid(row=0, column=0, sticky='nsew')
        self.frames[Bucks].grid(row=0, column=0, sticky='nsew')
        self.frames[Knicks].grid(row=0, column=0, sticky='nsew')
        self.frames[Magic].grid(row=0, column=0, sticky='nsew')
        self.frames[Philadelphia].grid(row=0, column=0, sticky='nsew')
        self.frames[Raptors].grid(row=0, column=0, sticky='nsew')
        self.frames[Wizards].grid(row=0, column=0, sticky='nsew')
        self.show_frame(HomePage)
        

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


def qf(param):
    print(param)

def Player_Window(name):
    root=Tk()
    newwindow=Toplevel(root)
    newwindow.geometry("500x500")
    lbl=Label(newwindow,text=name )
    lbl.pack()
class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Home Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Dallas Mavericks", command=lambda: controller.show_frame(Mavericks))
        button1.pack()

        button2 = ttk.Button(self, text="Denver Nuggets", command=lambda: controller.show_frame(Nuggets))
        button2.pack()

        button3 = ttk.Button(self, text="Golden State Warriors", command=lambda: controller.show_frame(GoldenState))
        button3.pack()

        button4 = ttk.Button(self, text="Houston Rockets", command=lambda: controller.show_frame(Rockets))
        button4.pack()

        button5 = ttk.Button(self, text="Los Angeles Clippers", command=lambda: controller.show_frame(Clippers))
        button5.pack()

        button6 = ttk.Button(self, text="Los Angeles Lakers", command=lambda: controller.show_frame(Lakers))
        button6.pack()

        button7 = ttk.Button(self, text="Memphis Grizzlies", command=lambda: controller.show_frame(Grizzlies))
        button7.pack()

        button8 = ttk.Button(self, text="Minnesota Timberwolves", command=lambda: controller.show_frame(Timberwolves))
        button8.pack()

        button9 = ttk.Button(self, text="New Orleans Pelicans", command=lambda: controller.show_frame(Pelicans))
        button9.pack()

        button10 = ttk.Button(self, text="Oklahoma City Thunder", command=lambda: controller.show_frame(Thunder))
        button10.pack()

        button11 = ttk.Button(self, text="Phoenix Suns", command=lambda: controller.show_frame(Suns))
        button11.pack()

        button12 = ttk.Button(self, text="Portland Trail Blazers", command=lambda: controller.show_frame(TrailBlazers))
        button12.pack()

        button13 = ttk.Button(self, text="Sacramento Kings", command=lambda: controller.show_frame(Kings))
        button13.pack()

        button14 = ttk.Button(self, text="San Antonio Spurs", command=lambda: controller.show_frame(SanAntonioSpurs))
        button14.pack()

        button15 = ttk.Button(self, text="Utah Jazz", command=lambda: controller.show_frame(Jazz))
        button15.pack()

        button16 = ttk.Button(self, text="Atlanta Hawks", command=lambda: controller.show_frame(Hawks))
        button16.pack()

        button17 = ttk.Button(self, text="Boston Celtics", command=lambda: controller.show_frame(Celtics))
        button17.pack()

        button18 = ttk.Button(self, text="Brooklyn Nets", command=lambda: controller.show_frame(Nets))
        button18.pack()

        button19 = ttk.Button(self, text="Charlotte Hornets", command=lambda: controller.show_frame(Hornets))
        button19.pack()

        button20 = ttk.Button(self, text="Chicago Bulls", command=lambda: controller.show_frame(Bulls))
        button20.pack()

        button21 = ttk.Button(self, text="Cleveland Cavaliers", command=lambda: controller.show_frame(Cavaliers))
        button21.pack()

        button22 = ttk.Button(self, text="Detroit Pistons", command=lambda: controller.show_frame(Pistons))
        button22.pack()

        button23 = ttk.Button(self, text="Indiana Pacers", command=lambda: controller.show_frame(Pacers))
        button23.pack()

        button24 = ttk.Button(self, text="Miami Heat", command=lambda: controller.show_frame(Heat))
        button24.pack()

        button25 = ttk.Button(self, text="Milwaukee Bucks", command=lambda: controller.show_frame(Bucks))
        button25.pack()

        button26 = ttk.Button(self, text="New York Knicks", command=lambda: controller.show_frame(Knicks))
        button26.pack()

        button27 = ttk.Button(self, text="Orlando Magic", command=lambda: controller.show_frame(Magic))
        button27.pack()

        button28 = ttk.Button(self, text="Philadelphia 76ers", command=lambda: controller.show_frame(Philadelphia))
        button28.pack()

        button29 = ttk.Button(self, text="Toronto Raptors", command=lambda: controller.show_frame(Raptors))
        button29.pack()

        button30 = ttk.Button(self, text="Washington Wizards", command=lambda: controller.show_frame(Wizards))
        button30.pack()

        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()

    


class Mavericks(tk.Frame):

   #used for most windows
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Dallas Mavericks", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        name="DAL"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()

class Nuggets(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Denver Nuggets", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        name="DEN"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()


class GoldenState(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Golden State Warriors", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        name="GSW"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()


class Rockets(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Houston Rockets", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        name="HOU"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()


class Clippers(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Los Angeles Clippers", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        name="LAC"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()



class Lakers(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Los Angeles Lakers", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        name="LAL"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()


class Grizzlies(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Memphis Grizzlies", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        name="MEM"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()

class Timberwolves(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Minnesota Timberwolves", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        name="MIN"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()


class Pelicans(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="New Orleans Pelicans", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        name="NOP"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()



class Thunder(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Oklahoma City Thunder", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        name="OKC"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()

        



class Suns(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Phoenix Suns", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        name="PHO"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()


class TrailBlazers(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Portland Trail Blazers", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        name="POR"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()


class Kings(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Sacramento Kings", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        name="SAC"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()

       


class SanAntonioSpurs(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="San Antonio Spurs", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        name="SAS"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()


class Jazz(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Utah Jazz", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        name="UTA"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()


class Hawks(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Atlanta Hawks", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        name="ATL"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()


class Celtics(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Boston Celtics", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        name="BOS"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()

        


class Nets(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Brooklyn Nets", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        name="BRK"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()

class Hornets(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Charlotte Hornets", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        name="CHO"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()

class Bulls(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Chicago Bulls", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        name="CHI"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()

class Cavaliers(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Cleveland Cavaliers", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        name="CLE"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()
    
class Pistons(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Detroit Pistons", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        name="DET"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()

class Pacers(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Indiana Pacers", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        name="IND"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()

       


class Heat(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Miami Heat", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        name="MIA"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()


class Bucks(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Milwaukee Bucks", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        name="MIL"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()

       


class Knicks(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="New York Knicks", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        name="NYK"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()

        


class Magic(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Orlando Magic", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        name="ORL"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()


class Philadelphia(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Philadelphia 76ers", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        name="PHI"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()

        
class Raptors(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Toronto Raptors", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        name="TOR"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()


class Wizards(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Washington Wizards", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        name="WAS"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()




app = nbaGUI()
app.mainloop()
