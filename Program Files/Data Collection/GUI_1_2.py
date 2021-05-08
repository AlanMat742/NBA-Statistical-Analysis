import tkinter as tk
from tkinter import ttk
from tkinter import *
import pandas as pd
import datetime
from PIL import ImageTk,Image
from tkinter import filedialog




LARGE_FONT = ("Verdana", 18)







class nbaGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, *kwargs)

        tk.Tk.geometry(self, "800x800")

        tk.Tk.iconbitmap(self, default="iconfinder_NBA_Live_60646 (1).ico")

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
    newwindow=Toplevel()
    newwindow.geometry("800x800")
    lbl=Label(newwindow,text=name )
    lbl.pack()
    buton=Button(newwindow,text="Close Window",fg="red",command=lambda:newwindow.destroy()).pack()

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Home Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        #IMAGES for Buttons



        self.Mavericks = tk.PhotoImage(file='Maverickslogo3.png')
        button1 = ttk.Button(self, image = self.Mavericks, command=lambda: controller.show_frame(Mavericks))
        button1.place(x=25, y=75)

        self.Nuggets = tk.PhotoImage(file='Nuggetslogo.png')
        button2 = ttk.Button(self, image = self.Nuggets, command=lambda: controller.show_frame(Nuggets))
        button2.place(x=150,y=75)

        self.Warriors = tk.PhotoImage(file='GoldenStatelogo.png')
        button3 = ttk.Button(self, image =self.Warriors , command=lambda: controller.show_frame(GoldenState))
        button3.place(x=275,y=75)

        self.Rockets = tk.PhotoImage(file='Rocketslogo2.png')
        button4 = ttk.Button(self, image=self.Rockets, command=lambda: controller.show_frame(Rockets))
        button4.place(x=400,y=75)

        self.Clippers = tk.PhotoImage(file='Clipperslogo.png')
        button5 = ttk.Button(self, image =self.Clippers , command=lambda: controller.show_frame(Clippers))
        button5.place(x=525,y=75)

        self.Lakers = tk.PhotoImage(file='Lakerslogo.png')
        button6 = ttk.Button(self, image = self.Lakers, command=lambda: controller.show_frame(Lakers))
        button6.place(x=650,y=75)

        self.Grizzlies = tk.PhotoImage(file='Grizzlieslogo.png')
        button7 = ttk.Button(self, image = self.Grizzlies, command=lambda: controller.show_frame(Grizzlies))
        button7.place(x=25,y=200)

        self.Timberwolves = tk.PhotoImage(file='Timberwolveslogo2.png')
        button8 = ttk.Button(self, image= self.Timberwolves, command=lambda: controller.show_frame(Timberwolves))
        button8.place(x=150,y=200)

        self.Pelicans = tk.PhotoImage(file='Pelicanslogo2.png')
        button9 = ttk.Button(self, image=self.Pelicans, command=lambda: controller.show_frame(Pelicans))
        button9.place(x=275,y=200)

        self.Thunder = tk.PhotoImage(file='Thunderlogo2.png')
        button10 = ttk.Button(self, image=self.Thunder, command=lambda: controller.show_frame(Thunder))
        button10.place(x=400,y=200)

        self.Suns = tk.PhotoImage(file='Sunslogo2.png')
        button11 = ttk.Button(self, image=self.Suns, command=lambda: controller.show_frame(Suns))
        button11.place(x=525,y=200)

        self.TrailBlazers = tk.PhotoImage(file='TrailBlazerslogo3.png')
        button12 = ttk.Button(self, image=self.TrailBlazers, command=lambda: controller.show_frame(TrailBlazers))
        button12.place(x=650,y=200)

        self.Kings = tk.PhotoImage(file='Kingslogo.png')
        button13 = ttk.Button(self, image=self.Kings, command=lambda: controller.show_frame(Kings))
        button13.place(x=25,y=325)

        self.Spurs = tk.PhotoImage(file='Spurslogo2.png')
        button14 = ttk.Button(self, image=self.Spurs, command=lambda: controller.show_frame(SanAntonioSpurs))
        button14.place(x=150,y=325)

#here
        self.Jazz = tk.PhotoImage(file='Jazzlogo.png')
        button15 = ttk.Button(self, image=self.Jazz, command=lambda: controller.show_frame(Jazz))
        button15.place(x=275,y=325)

        self.Hawks = tk.PhotoImage(file='Hawkslogo.png')
        button16 = ttk.Button(self, image =self.Hawks, command=lambda: controller.show_frame(Hawks))
        button16.place(x=400,y=325)

        self.Celtics = tk.PhotoImage(file='Celticslogo.png')
        button17 = ttk.Button(self, image=self.Celtics, command=lambda: controller.show_frame(Celtics))
        button17.place(x=525,y=325)

        self.Nets = tk.PhotoImage(file='Netslogo.png')
        button18 = ttk.Button(self, image = self.Nets, command=lambda: controller.show_frame(Nets))
        button18.place(x=650,y=325)

        self.Hornets = tk.PhotoImage(file='Hornetslogo.png')
        button19 = ttk.Button(self, image = self.Hornets, command=lambda: controller.show_frame(Hornets))
        button19.place(x=25,y=450)

        self.Bulls = tk.PhotoImage(file='Bullslogo.png')
        button20 = ttk.Button(self, image = self.Bulls, command=lambda: controller.show_frame(Bulls))
        button20.place(x=150,y=450)

        self.Cavaliers = tk.PhotoImage(file='Cavalierslogo2.png')
        button21 = ttk.Button(self, image = self.Cavaliers, command=lambda: controller.show_frame(Cavaliers))
        button21.place(x=275,y=450)

        self.Pistons = tk.PhotoImage(file='Pistonslogo.png')
        button22 = ttk.Button(self, image=self.Pistons, command=lambda: controller.show_frame(Pistons))
        button22.place(x=400,y=450)

        self.Pacers = tk.PhotoImage(file='Pacerslogo.png')
        button23 = ttk.Button(self, image = self.Pacers, command=lambda: controller.show_frame(Pacers))
        button23.place(x=525,y=450)

        self.Heat = tk.PhotoImage(file='Heatlogo.png')
        button24 = ttk.Button(self, image = self.Heat, command=lambda: controller.show_frame(Heat))
        button24.place(x=650,y=450)

        self.Bucks = tk.PhotoImage(file='Buckslogo.png')
        button25 = ttk.Button(self, image = self.Bucks, command=lambda: controller.show_frame(Bucks))
        button25.place(x=25,y=575)

        self.Knicks = tk.PhotoImage(file='Knickslogo.png')
        button26 = ttk.Button(self, image = self.Knicks, command=lambda: controller.show_frame(Knicks))
        button26.place(x=150,y=575)

        self.Magic = tk.PhotoImage(file='Magiclogo.png')
        button27 = ttk.Button(self, image=self.Magic, command=lambda: controller.show_frame(Magic))
        button27.place(x=275,y=575)

        self.Sixers = tk.PhotoImage(file='Sixerslogo.png')
        button28 = ttk.Button(self, image = self.Sixers, command=lambda: controller.show_frame(Philadelphia))
        button28.place(x=400,y=575)

        self.Raptors = tk.PhotoImage(file='Raptorslogo.png')
        button29 = ttk.Button(self, image = self.Raptors, command=lambda: controller.show_frame(Raptors))
        button29.place(x=525,y=575)

        self.Wizards = tk.PhotoImage(file='Wizardslogo.png')
        button30 = ttk.Button(self, image = self.Wizards, command=lambda: controller.show_frame(Wizards))
        button30.place(x=650,y=575)

    


class Mavericks(tk.Frame):

   #used for most windows
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Dallas Mavericks", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        self.Mavericks = tk.PhotoImage(file = 'Maverickslogo3.png')
        Mavericks = tk.Label(self, image = self.Mavericks)
        Mavericks.pack(pady = 10, padx = 10)

        name="DAL"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])


        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()
        # button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()

class Nuggets(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Denver Nuggets", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        self.Nuggets = tk.PhotoImage(file='Nuggetslogo.png')
        Nuggets = tk.Label(self, image=self.Nuggets)
        Nuggets.pack(pady=10, padx=10)

        name="DEN"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()
        # button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()


class GoldenState(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Golden State Warriors", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        self.GoldenState = tk.PhotoImage(file='GoldenStatelogo.png')
        GoldenState = tk.Label(self, image=self.GoldenState)
        GoldenState.pack(pady=10, padx=10)

        name="GSW"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()
        # button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()

#fix layout
class Rockets(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Houston Rockets", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        self.Rockets = tk.PhotoImage(file='Rocketslogo2.png')
        Rockets = tk.Label(self, image=self.Rockets)
        Rockets.pack(pady=10, padx=10)

        name="HOU"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()
        # button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()


class Clippers(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Los Angeles Clippers", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        self.Clippers = tk.PhotoImage(file='Clipperslogo.png')
        Clippers = tk.Label(self, image=self.Clippers)
        Clippers.pack(pady=10, padx=10)

        name="LAC"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()
        # button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()



class Lakers(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Los Angeles Lakers", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        self.Lakers = tk.PhotoImage(file='Lakerslogo.png')
        Lakers = tk.Label(self, image=self.Lakers)
        Lakers.pack(pady=10, padx=10)

        name="LAL"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()
        # button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()


class Grizzlies(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Memphis Grizzlies", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        self.Grizzlies = tk.PhotoImage(file='Grizzlieslogo.png')
        Grizzlies = tk.Label(self, image=self.Grizzlies)
        Grizzlies.pack(pady=10, padx=10)

        name="MEM"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()
        # button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()

class Timberwolves(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Minnesota Timberwolves", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        self.Timberwolves = tk.PhotoImage(file='Timberwolveslogo2.png')
        Timberwolves = tk.Label(self, image=self.Timberwolves)
        Timberwolves.pack(pady=10, padx=10)

        name="MIN"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()
        # button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()


class Pelicans(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="New Orleans Pelicans", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        self.Pelicans = tk.PhotoImage(file='Pelicanslogo2.png')
        Pelicans = tk.Label(self, image=self.Pelicans)
        Pelicans.pack(pady=10, padx=10)

        name="NOP"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()
        # button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()



class Thunder(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Oklahoma City Thunder", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        self.Thunder = tk.PhotoImage(file='Thunderlogo2.png')
        Thunder = tk.Label(self, image=self.Thunder)
        Thunder.pack(pady=10, padx=10)

        name="OKC"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()
        # button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()

        



class Suns(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Phoenix Suns", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        self.Suns = tk.PhotoImage(file='Sunslogo2.png')
        Suns = tk.Label(self, image=self.Suns)
        Suns.pack(pady=10, padx=10)

        name="PHO"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()
        # button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()


class TrailBlazers(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Portland Trail Blazers", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        self.TrailBlazers = tk.PhotoImage(file='TrailBlazerslogo3.png')
        TrailBlazers = tk.Label(self, image=self.TrailBlazers)
        TrailBlazers.pack(pady=10, padx=10)

        name="POR"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()
        # button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()


class Kings(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Sacramento Kings", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        self.Kings = tk.PhotoImage(file='Kingslogo.png')
        Kings = tk.Label(self, image=self.Kings)
        Kings.pack(pady=10, padx=10)

        name="SAC"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()
        # button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()

       

#change name to Spurs
class SanAntonioSpurs(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="San Antonio Spurs", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        self.Spurs = tk.PhotoImage(file='Spurslogo2.png')
        Spurs = tk.Label(self, image=self.Spurs)
        Spurs.pack(pady=10, padx=10)

        name="SAS"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()
        # button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()


class Jazz(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Utah Jazz", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        self.Jazz = tk.PhotoImage(file='Jazzlogo.png')
        Jazz = tk.Label(self, image=self.Jazz)
        Jazz.pack(pady=10, padx=10)

        name="UTA"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()
        # button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()


class Hawks(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Atlanta Hawks", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        self.Hawks = tk.PhotoImage(file='Hawkslogo.png')
        Hawks = tk.Label(self, image=self.Hawks)
        Hawks.pack(pady=10, padx=10)

        name="ATL"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()
        # button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()


class Celtics(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Boston Celtics", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        self.Celtics = tk.PhotoImage(file='Celticslogo.png')
        Celtics = tk.Label(self, image=self.Celtics)
        Celtics.pack(pady=10, padx=10)

        name="BOS"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()
        # button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()

        


class Nets(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Brooklyn Nets", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        self.Celtics = tk.PhotoImage(file='Celticslogo.png')
        Celtics = tk.Label(self, image=self.Celtics)
        Celtics.pack(pady=10, padx=10)

        name="BRK"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()
        # button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()

class Hornets(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Charlotte Hornets", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        self.Hornets = tk.PhotoImage(file='Hornetslogo.png')
        Hornets = tk.Label(self, image=self.Hornets)
        Hornets.pack(pady=10, padx=10)

        name="CHO"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()
        # button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()

class Bulls(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Chicago Bulls", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        self.Bulls = tk.PhotoImage(file='Bullslogo.png')
        Bulls = tk.Label(self, image=self.Bulls)
        Bulls.pack(pady=10, padx=10)

        name="CHI"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()
        # button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()

class Cavaliers(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Cleveland Cavaliers", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        self.Cavaliers = tk.PhotoImage(file='Cavalierslogo2.png')
        Cavaliers = tk.Label(self, image=self.Cavaliers)
        Cavaliers.pack(pady=10, padx=10)

        name="CLE"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()
        # button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()
    
class Pistons(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Detroit Pistons", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        self.Pistons = tk.PhotoImage(file='Pistonslogo.png')
        Pistons = tk.Label(self, image=self.Pistons)
        Pistons.pack(pady=10, padx=10)

        name="DET"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()
        # button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()

class Pacers(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Indiana Pacers", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        self.Pacers = tk.PhotoImage(file='Pacerslogo.png')
        Pacers = tk.Label(self, image=self.Pacers)
        Pacers.pack(pady=10, padx=10)

        name="IND"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()
        # button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()

       


class Heat(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Miami Heat", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        self.Heat = tk.PhotoImage(file='Heatlogo.png')
        Heat = tk.Label(self, image=self.Heat)
        Heat.pack(pady=10, padx=10)

        name="MIA"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()
        # button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()


class Bucks(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Milwaukee Bucks", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        self.Bucks = tk.PhotoImage(file='Buckslogo.png')
        Bucks = tk.Label(self, image=self.Bucks)
        Bucks.pack(pady=10, padx=10)

        name="MIL"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()
        # button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()
       


class Knicks(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="New York Knicks", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        self.Knicks = tk.PhotoImage(file='Knickslogo.png')
        Knicks = tk.Label(self, image=self.Knicks)
        Knicks.pack(pady=10, padx=10)

        name="NYK"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()
        # button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()

        


class Magic(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Orlando Magic", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        self.Magic = tk.PhotoImage(file='Magiclogo.png')
        Magic = tk.Label(self, image=self.Magic)
        Magic.pack(pady=10, padx=10)

        name="ORL"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()
        # button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()

#change name to Sixers
class Philadelphia(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Philadelphia 76ers", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        self.Sixers = tk.PhotoImage(file='Sixerslogo.png')
        Sixers = tk.Label(self, image=self.Sixers)
        Sixers.pack(pady=10, padx=10)

        name="PHI"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()
        # button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()

        
class Raptors(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Toronto Raptors", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        self.Raptors = tk.PhotoImage(file='Raptorslogo.png')
        Raptors = tk.Label(self, image=self.Raptors)
        Raptors.pack(pady=10, padx=10)

        name="TOR"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()
        # button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()


class Wizards(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Washington Wizards", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        self.Wizards = tk.PhotoImage(file='Wizardslogo.png')
        Wizards = tk.Label(self, image=self.Wizards)
        Wizards.pack(pady=10, padx=10)

        name="WAS"
        year = datetime.date.today().year
        link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
        df=pd.read_html(link, match="Per Game")
        df=df[0]
        names=list(df["Unnamed: 1"])
        for name in names:
            button1 = ttk.Button(self, text=name, command=lambda name=name: Player_Window(name))
            button1.pack()
        # button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()




app = nbaGUI()
app.mainloop()

