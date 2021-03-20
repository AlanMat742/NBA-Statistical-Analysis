import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *







LARGE_FONT = ("Verdana", 12)


class nbaGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, *kwargs)

        tk.Tk.iconbitmap(self, default="iconfinder_NBA_Live_60646 (1).ico")

        tk.Tk.wm_title(self, "NBA Statistics")

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (HomePage, Mavericks, Nuggets, GoldenState, Rockets, Clippers, Lakers, Grizzlies, Timberwolves, Pelicans,
                  Thunder, Suns, TrailBlazers, Kings, SanAntonioSpurs, Jazz, Hawks, Celtics, Nets, Hornets, Bulls, Cavaliers, Pistons, Pacers, Heat,
                  Bucks, Knicks, Magic, Philadelphia, Raptors, Wizards):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


def qf(param):
    print(param)


class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Home Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)






        photo = PhotoImage(file = "233480-small.png")
        Button(self, text = "NBA Logo", image = photo).pack(side = TOP)

        mainloop()





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


        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()




class Nuggets(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Denver Nuggets", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()


class GoldenState(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Golden State Warriors", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()


class Rockets(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Houston Rockets", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()

        button0 = ttk.Button(self, text="James Harden", command=lambda: controller.show_frame(PageName))
        button0.pack()
        button1 = ttk.Button(self, text="Kevin Porter", command=lambda: controller.show_frame(PageName))
        button1.pack()
        button2 = ttk.Button(self, text="Victor Oladipo", command=lambda: controller.show_frame(PageName))
        button2.pack()
        button3 = ttk.Button(self, text="John Wall", command=lambda: controller.show_frame(PageName))
        button3.pack()
        button4 = ttk.Button(self, text="Christian Wood", command=lambda: controller.show_frame(PageName))
        button4.pack()
        button5 = ttk.Button(self, text="P.J. Tucker", command=lambda: controller.show_frame(PageName))
        button5.pack()
        button6 = ttk.Button(self, text="Eric Gordon", command=lambda: controller.show_frame(PageName))
        button6.pack()
        button7 = ttk.Button(self, text="Jae'Sean Tate", command=lambda: controller.show_frame(PageName))
        button7.pack()
        button8 = ttk.Button(self, text="Danuel House", command=lambda: controller.show_frame(PageName))
        button8.pack()
        button9 = ttk.Button(self, text="Sterling Brown", command=lambda: controller.show_frame(PageName))
        button9.pack()
        button10 = ttk.Button(self, text="David Nwaba", command=lambda: controller.show_frame(PageName))
        button10.pack()
        button11 = ttk.Button(self, text="Justin Patton", command=lambda: controller.show_frame(PageName))
        button11.pack()
        button12 = ttk.Button(self, text="DeMarcus Cousins", command=lambda: controller.show_frame(PageName))
        button12.pack()
        button13 = ttk.Button(self, text="Anthony Lamb", command=lambda: controller.show_frame(PageName))
        button13.pack()
        button14 = ttk.Button(self, text="Kenyon Martin", command=lambda: controller.show_frame(PageName))
        button14.pack()
        button15 = ttk.Button(self, text="Ben McLemore", command=lambda: controller.show_frame(PageName))
        button15.pack()
        button16 = ttk.Button(self, text="Mason Jones", command=lambda: controller.show_frame(PageName))
        button16.pack()
        button17 = ttk.Button(self, text="Ray Spalding", command=lambda: controller.show_frame(PageName))
        button17.pack()
        button18 = ttk.Button(self, text="Rodions Kurucs", command=lambda: controller.show_frame(PageName))
        button18.pack()
        button19 = ttk.Button(self, text="Brodric Thomas", command=lambda: controller.show_frame(PageName))
        button19.pack()
        button20 = ttk.Button(self, text="Bruno Caboclo", command=lambda: controller.show_frame(PageName))
        button20.pack()


class Clippers(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Los Angeles Clippers", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()

        button0 = ttk.Button(self, text="Kawhi Leonard", command=lambda: controller.show_frame(PageName))
        button0.pack()
        button1 = ttk.Button(self, text="Paul George", command=lambda: controller.show_frame(PageName))
        button1.pack()
        button2 = ttk.Button(self, text="Nicolas Batum", command=lambda: controller.show_frame(PageName))
        button2.pack()
        button3 = ttk.Button(self, text="Marcus Morris", command=lambda: controller.show_frame(PageName))
        button3.pack()
        button4 = ttk.Button(self, text="Patrick Beverley", command=lambda: controller.show_frame(PageName))
        button4.pack()
        button5 = ttk.Button(self, text="Serge Ibaka", command=lambda: controller.show_frame(PageName))
        button5.pack()
        button6 = ttk.Button(self, text="Lou Williams", command=lambda: controller.show_frame(PageName))
        button6.pack()
        button7 = ttk.Button(self, text="Reggie Jackson", command=lambda: controller.show_frame(PageName))
        button7.pack()
        button8 = ttk.Button(self, text="Ivica Zubac", command=lambda: controller.show_frame(PageName))
        button8.pack()
        button9 = ttk.Button(self, text="Luke Kennard", command=lambda: controller.show_frame(PageName))
        button9.pack()
        button10 = ttk.Button(self, text="Terance Mann", command=lambda: controller.show_frame(PageName))
        button10.pack()
        button11 = ttk.Button(self, text="Patrick Patterson", command=lambda: controller.show_frame(PageName))
        button11.pack()
        button12 = ttk.Button(self, text="Amir Coffey", command=lambda: controller.show_frame(PageName))
        button12.pack()
        button13 = ttk.Button(self, text="Daniel Oturu", command=lambda: controller.show_frame(PageName))
        button13.pack()
        button14 = ttk.Button(self, text="Mfiondu Kabengele", command=lambda: controller.show_frame(PageName))
        button14.pack()



class Lakers(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Los Angeles Lakers", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()

        button0 = ttk.Button(self, text="LeBron James", command=lambda: controller.show_frame(PageName))
        button0.pack()
        button1 = ttk.Button(self, text="Anthony Davis", command=lambda: controller.show_frame(PageName))
        button1.pack()
        button2 = ttk.Button(self, text="Dennis Schroder", command=lambda: controller.show_frame(PageName))
        button2.pack()
        button3 = ttk.Button(self, text="Kentavious Caldwell-Pope", command=lambda: controller.show_frame(PageName))
        button3.pack()
        button4 = ttk.Button(self, text="Kyle Kuzma", command=lambda: controller.show_frame(PageName))
        button4.pack()
        button5 = ttk.Button(self, text="Montrezl Harrell", command=lambda: controller.show_frame(PageName))
        button5.pack()
        button6 = ttk.Button(self, text="Wesley Matthews", command=lambda: controller.show_frame(PageName))
        button6.pack()
        button7 = ttk.Button(self, text="Marc Gasol", command=lambda: controller.show_frame(PageName))
        button7.pack()
        button8 = ttk.Button(self, text="Alex Caruso", command=lambda: controller.show_frame(PageName))
        button8.pack()
        button9 = ttk.Button(self, text="Talen Horton-Tucker", command=lambda: controller.show_frame(PageName))
        button9.pack()
        button10 = ttk.Button(self, text="Markieff Morris", command=lambda: controller.show_frame(PageName))
        button10.pack()
        button11 = ttk.Button(self, text="Damian Jones", command=lambda: controller.show_frame(PageName))
        button11.pack()
        button12 = ttk.Button(self, text="Jared Dudley", command=lambda: controller.show_frame(PageName))
        button12.pack()
        button13 = ttk.Button(self, text="Kostas Antetokounmpo", command=lambda: controller.show_frame(PageName))
        button13.pack()
        button14 = ttk.Button(self, text="Alfonzo McKinnie", command=lambda: controller.show_frame(PageName))
        button14.pack()
        button15 = ttk.Button(self, text="Devontae Cacok", command=lambda: controller.show_frame(PageName))
        button15.pack()
        button16 = ttk.Button(self, text="Quinn Cook", command=lambda: controller.show_frame(PageName))
        button16.pack()



class Grizzlies(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Memphis Grizzlies", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()


class Timberwolves(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Minnesota Timberwolves", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()


class Pelicans(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="New Orleans Pelicans", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()

        button0 = ttk.Button(self, text="Brandon Ingram", command=lambda: controller.show_frame(PageName))
        button0.pack()
        button1 = ttk.Button(self, text="Zion Williamson", command=lambda: controller.show_frame(PageName))
        button1.pack()
        button2 = ttk.Button(self, text="Lonzo Ball", command=lambda: controller.show_frame(PageName))
        button2.pack()
        button3 = ttk.Button(self, text="Eric Bledsoe", command=lambda: controller.show_frame(PageName))
        button3.pack()
        button4 = ttk.Button(self, text="Josh Hart", command=lambda: controller.show_frame(PageName))
        button4.pack()
        button5 = ttk.Button(self, text="Steven Adams", command=lambda: controller.show_frame(PageName))
        button5.pack()
        button6 = ttk.Button(self, text="J.J. Redick", command=lambda: controller.show_frame(PageName))
        button6.pack()
        button7 = ttk.Button(self, text="Nickeil Alexander-Walker", command=lambda: controller.show_frame(PageName))
        button7.pack()
        button8 = ttk.Button(self, text="Willy Hernangomez", command=lambda: controller.show_frame(PageName))
        button8.pack()
        button9 = ttk.Button(self, text="Kira Lewis", command=lambda: controller.show_frame(PageName))
        button9.pack()
        button10 = ttk.Button(self, text="Jaxson Hayes", command=lambda: controller.show_frame(PageName))
        button10.pack()
        button11 = ttk.Button(self, text="Nicolo Melli", command=lambda: controller.show_frame(PageName))
        button11.pack()
        button12 = ttk.Button(self, text="Sindarius Thornwell", command=lambda: controller.show_frame(PageName))
        button12.pack()
        button13 = ttk.Button(self, text="Wenyen Gabriel", command=lambda: controller.show_frame(PageName))
        button13.pack()
        button14 = ttk.Button(self, text="Naji Marshall", command=lambda: controller.show_frame(PageName))
        button14.pack()


class Thunder(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Oklahoma City Thunder", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()

        button0 = ttk.Button(self, text="Shai Gilgeous-Alexander", command=lambda: controller.show_frame(PageName))
        button0.pack()
        button1 = ttk.Button(self, text="Darius Bazley", command=lambda: controller.show_frame(PageName))
        button1.pack()
        button2 = ttk.Button(self, text="Luguentz Dort", command=lambda: controller.show_frame(PageName))
        button2.pack()
        button3 = ttk.Button(self, text="Al Horford", command=lambda: controller.show_frame(PageName))
        button3.pack()
        button4 = ttk.Button(self, text="Ty Jerome", command=lambda: controller.show_frame(PageName))
        button4.pack()
        button5 = ttk.Button(self, text="George Hill", command=lambda: controller.show_frame(PageName))
        button5.pack()
        button6 = ttk.Button(self, text="Th�o Maledon", command=lambda: controller.show_frame(PageName))
        button6.pack()
        button7 = ttk.Button(self, text="Hamidou Diallo", command=lambda: controller.show_frame(PageName))
        button7.pack()
        button8 = ttk.Button(self, text="Isaiah Roby", command=lambda: controller.show_frame(PageName))
        button8.pack()
        button9 = ttk.Button(self, text="Aleksej Pokusevski", command=lambda: controller.show_frame(PageName))
        button9.pack()
        button10 = ttk.Button(self, text="Kenrich Williams", command=lambda: controller.show_frame(PageName))
        button10.pack()
        button11 = ttk.Button(self, text="Mike Muscala", command=lambda: controller.show_frame(PageName))
        button11.pack()
        button12 = ttk.Button(self, text="Justin Jackson", command=lambda: controller.show_frame(PageName))
        button12.pack()
        button13 = ttk.Button(self, text="Moses Brown", command=lambda: controller.show_frame(PageName))
        button13.pack()
        button14 = ttk.Button(self, text="Darius Miller", command=lambda: controller.show_frame(PageName))
        button14.pack()
        button15 = ttk.Button(self, text="Josh Hall", command=lambda: controller.show_frame(PageName))
        button15.pack()



class Suns(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Phoenix Suns", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()


class TrailBlazers(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Portland Trail Blazers", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()


class Kings(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Sacramento Kings", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()

        button0 = ttk.Button(self, text="Harrison Barnes", command=lambda: controller.show_frame(PageName))
        button0.pack()
        button1 = ttk.Button(self, text="Buddy Hield", command=lambda: controller.show_frame(PageName))
        button1.pack()
        button2 = ttk.Button(self, text="De'Aaron Fox", command=lambda: controller.show_frame(PageName))
        button2.pack()
        button3 = ttk.Button(self, text="Richaun Holmes", command=lambda: controller.show_frame(PageName))
        button3.pack()
        button4 = ttk.Button(self, text="Tyrese Haliburton", command=lambda: controller.show_frame(PageName))
        button4.pack()
        button5 = ttk.Button(self, text="Marvin Bagley", command=lambda: controller.show_frame(PageName))
        button5.pack()
        button6 = ttk.Button(self, text="Cory Joseph", command=lambda: controller.show_frame(PageName))
        button6.pack()
        button7 = ttk.Button(self, text="Nemanja Bjelica", command=lambda: controller.show_frame(PageName))
        button7.pack()
        button8 = ttk.Button(self, text="Glenn Robinson", command=lambda: controller.show_frame(PageName))
        button8.pack()
        button9 = ttk.Button(self, text="Hassan Whiteside", command=lambda: controller.show_frame(PageName))
        button9.pack()
        button10 = ttk.Button(self, text="DaQuan Jeffries", command=lambda: controller.show_frame(PageName))
        button10.pack()
        button11 = ttk.Button(self, text="Jabari Parker", command=lambda: controller.show_frame(PageName))
        button11.pack()
        button12 = ttk.Button(self, text="Kyle Guy", command=lambda: controller.show_frame(PageName))
        button12.pack()
        button13 = ttk.Button(self, text="Chimezie Metu", command=lambda: controller.show_frame(PageName))
        button13.pack()
        button14 = ttk.Button(self, text="Justin James", command=lambda: controller.show_frame(PageName))
        button14.pack()
        button15 = ttk.Button(self, text="Norvel Pelle", command=lambda: controller.show_frame(PageName))
        button15.pack()
        button16 = ttk.Button(self, text="Jahmi'us Ramsey", command=lambda: controller.show_frame(PageName))
        button16.pack()
        button17 = ttk.Button(self, text="Robert Woodard", command=lambda: controller.show_frame(PageName))
        button17.pack()


class SanAntonioSpurs(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="San Antonio Spurs", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()


class Jazz(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Utah Jazz", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()


class Hawks(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Atlanta Hawks", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()


class Celtics(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Boston Celtics", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()

        button0 = ttk.Button(self, text="Jayson Tatum", command=lambda: controller.show_frame(PageName))
        button0.pack()
        button1 = ttk.Button(self, text="Jaylen Brown", command=lambda: controller.show_frame(PageName))
        button1.pack()
        button2 = ttk.Button(self, text="Marcus Smart", command=lambda: controller.show_frame(PageName))
        button2.pack()
        button3 = ttk.Button(self, text="Kemba Walker", command=lambda: controller.show_frame(PageName))
        button3.pack()
        button4 = ttk.Button(self, text="Daniel Theis", command=lambda: controller.show_frame(PageName))
        button4.pack()
        button5 = ttk.Button(self, text="Tristan Thompson", command=lambda: controller.show_frame(PageName))
        button5.pack()
        button6 = ttk.Button(self, text="Payton Pritchard", command=lambda: controller.show_frame(PageName))
        button6.pack()
        button7 = ttk.Button(self, text="Semi Ojeleye", command=lambda: controller.show_frame(PageName))
        button7.pack()
        button8 = ttk.Button(self, text="Grant Williams", command=lambda: controller.show_frame(PageName))
        button8.pack()
        button9 = ttk.Button(self, text="Jeff Teague", command=lambda: controller.show_frame(PageName))
        button9.pack()
        button10 = ttk.Button(self, text="Robert Williams", command=lambda: controller.show_frame(PageName))
        button10.pack()
        button11 = ttk.Button(self, text="Aaron Nesmith", command=lambda: controller.show_frame(PageName))
        button11.pack()
        button12 = ttk.Button(self, text="Javonte Green", command=lambda: controller.show_frame(PageName))
        button12.pack()
        button13 = ttk.Button(self, text="Carsen Edwards", command=lambda: controller.show_frame(PageName))
        button13.pack()
        button14 = ttk.Button(self, text="Tremont Waters", command=lambda: controller.show_frame(PageName))
        button14.pack()
        button15 = ttk.Button(self, text="Tacko Fall", command=lambda: controller.show_frame(PageName))
        button15.pack()


class Nets(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Brooklyn Nets", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()

        button0 = ttk.Button(self, text="James Harden", command=lambda: controller.show_frame(PageName))
        button0.pack()
        button1 = ttk.Button(self, text="Kevin Durant", command=lambda: controller.show_frame(PageName))
        button1.pack()
        button2 = ttk.Button(self, text="Kyrie Irving", command=lambda: controller.show_frame(PageName))
        button2.pack()
        button3 = ttk.Button(self, text="Joe Harris", command=lambda: controller.show_frame(PageName))
        button3.pack()
        button4 = ttk.Button(self, text="Caris LeVert", command=lambda: controller.show_frame(PageName))
        button4.pack()
        button5 = ttk.Button(self, text="Jeff Green", command=lambda: controller.show_frame(PageName))
        button5.pack()
        button6 = ttk.Button(self, text="Jarrett Allen", command=lambda: controller.show_frame(PageName))
        button6.pack()
        button7 = ttk.Button(self, text="DeAndre Jordan", command=lambda: controller.show_frame(PageName))
        button7.pack()
        button8 = ttk.Button(self, text="Spencer Dinwiddie", command=lambda: controller.show_frame(PageName))
        button8.pack()
        button9 = ttk.Button(self, text="Bruce Brown", command=lambda: controller.show_frame(PageName))
        button9.pack()
        button10 = ttk.Button(self, text="Landry Shamet", command=lambda: controller.show_frame(PageName))
        button10.pack()
        button11 = ttk.Button(self, text="Timothe Luwawu-Cabarrot", command=lambda: controller.show_frame(PageName))
        button11.pack()
        button12 = ttk.Button(self, text="Taurean Prince", command=lambda: controller.show_frame(PageName))
        button12.pack()
        button13 = ttk.Button(self, text="Nicolas Claxton", command=lambda: controller.show_frame(PageName))
        button13.pack()
        button14 = ttk.Button(self, text="Tyler Johnson", command=lambda: controller.show_frame(PageName))
        button14.pack()
        button15 = ttk.Button(self, text="Andre Roberson", command=lambda: controller.show_frame(PageName))
        button15.pack()
        button16 = ttk.Button(self, text="Reggie Perry", command=lambda: controller.show_frame(PageName))
        button16.pack()
        button17 = ttk.Button(self, text="Norvel Pelle", command=lambda: controller.show_frame(PageName))
        button17.pack()
        button18 = ttk.Button(self, text="Chris Chiozza", command=lambda: controller.show_frame(PageName))
        button18.pack()
        button19 = ttk.Button(self, text="Iman Shumpert", command=lambda: controller.show_frame(PageName))
        button19.pack()
        button20 = ttk.Button(self, text="Tyler Cook", command=lambda: controller.show_frame(PageName))
        button20.pack()
        button21 = ttk.Button(self, text="Rodions Kurucs", command=lambda: controller.show_frame(PageName))
        button21.pack()
        button22 = ttk.Button(self, text="Noah Vonleh", command=lambda: controller.show_frame(PageName))
        button22.pack()




class Hornets(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Charlotte Hornets", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()

        button0 = ttk.Button(self, text="Gordon Hayward", command=lambda: controller.show_frame(PageName))
        button0.pack()
        button1 = ttk.Button(self, text="Terry Rozier", command=lambda: controller.show_frame(PageName))
        button1.pack()
        button2 = ttk.Button(self, text="Devonte' Graham", command=lambda: controller.show_frame(PageName))
        button2.pack()
        button3 = ttk.Button(self, text="P.J. Washington", command=lambda: controller.show_frame(PageName))
        button3.pack()
        button4 = ttk.Button(self, text="LaMelo Ball", command=lambda: controller.show_frame(PageName))
        button4.pack()
        button5 = ttk.Button(self, text="Miles Bridges", command=lambda: controller.show_frame(PageName))
        button5.pack()
        button6 = ttk.Button(self, text="Cody Zeller", command=lambda: controller.show_frame(PageName))
        button6.pack()
        button7 = ttk.Button(self, text="Bismack Biyombo", command=lambda: controller.show_frame(PageName))
        button7.pack()
        button8 = ttk.Button(self, text="Malik Monk", command=lambda: controller.show_frame(PageName))
        button8.pack()
        button9 = ttk.Button(self, text="Caleb Martin", command=lambda: controller.show_frame(PageName))
        button9.pack()
        button10 = ttk.Button(self, text="Cody Martin", command=lambda: controller.show_frame(PageName))
        button10.pack()
        button11 = ttk.Button(self, text="Jalen McDaniels", command=lambda: controller.show_frame(PageName))
        button11.pack()
        button12 = ttk.Button(self, text="Nate Darling", command=lambda: controller.show_frame(PageName))
        button12.pack()
        button13 = ttk.Button(self, text="Vernon Carey", command=lambda: controller.show_frame(PageName))
        button13.pack()
        button14 = ttk.Button(self, text="Nick Richards", command=lambda: controller.show_frame(PageName))
        button14.pack()


class Bulls(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Chicago Bulls", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()

        button0 = ttk.Button(self, text="Zach LaVine", command=lambda: controller.show_frame(PageName))
        button0.pack()
        button1 = ttk.Button(self, text="Coby White", command=lambda: controller.show_frame(PageName))
        button1.pack()
        button2 = ttk.Button(self, text="Lauri Markkanen", command=lambda: controller.show_frame(PageName))
        button2.pack()
        button3 = ttk.Button(self, text="Patrick Williams", command=lambda: controller.show_frame(PageName))
        button3.pack()
        button4 = ttk.Button(self, text="Garrett Temple", command=lambda: controller.show_frame(PageName))
        button4.pack()
        button5 = ttk.Button(self, text="Wendell Carter", command=lambda: controller.show_frame(PageName))
        button5.pack()
        button6 = ttk.Button(self, text="Thaddeus Young", command=lambda: controller.show_frame(PageName))
        button6.pack()
        button7 = ttk.Button(self, text="Otto Porter", command=lambda: controller.show_frame(PageName))
        button7.pack()
        button8 = ttk.Button(self, text="Tom Satoransky", command=lambda: controller.show_frame(PageName))
        button8.pack()
        button9 = ttk.Button(self, text="Denzel Valentine", command=lambda: controller.show_frame(PageName))
        button9.pack()
        button10 = ttk.Button(self, text="Daniel Gafford", command=lambda: controller.show_frame(PageName))
        button10.pack()
        button11 = ttk.Button(self, text="Ryan Arcidiacono", command=lambda: controller.show_frame(PageName))
        button11.pack()
        button12 = ttk.Button(self, text="Devon Dotson", command=lambda: controller.show_frame(PageName))
        button12.pack()
        button13 = ttk.Button(self, text="Chandler Hutchison", command=lambda: controller.show_frame(PageName))
        button13.pack()
        button14 = ttk.Button(self, text="Luke Kornet", command=lambda: controller.show_frame(PageName))
        button14.pack()
        button15 = ttk.Button(self, text="Cristiano Felicio", command=lambda: controller.show_frame(PageName))
        button15.pack()
        button16 = ttk.Button(self, text="Adam Mokoka", command=lambda: controller.show_frame(PageName))
        button16.pack()


class Cavaliers(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Cleveland Cavaliers", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()

        button0 = ttk.Button(self, text="Collin Sexton", command=lambda: controller.show_frame(PageName))
        button0.pack()
        button1 = ttk.Button(self, text="Larry Nance", command=lambda: controller.show_frame(PageName))
        button1.pack()
        button2 = ttk.Button(self, text="Darius Garland", command=lambda: controller.show_frame(PageName))
        button2.pack()
        button3 = ttk.Button(self, text="Isaac Okoro", command=lambda: controller.show_frame(PageName))
        button3.pack()
        button4 = ttk.Button(self, text="Andre Drummond", command=lambda: controller.show_frame(PageName))
        button4.pack()
        button5 = ttk.Button(self, text="Jarrett Allen", command=lambda: controller.show_frame(PageName))
        button5.pack()
        button6 = ttk.Button(self, text="Cedi Osman", command=lambda: controller.show_frame(PageName))
        button6.pack()
        button7 = ttk.Button(self, text="Taurean Prince", command=lambda: controller.show_frame(PageName))
        button7.pack()
        button8 = ttk.Button(self, text="Yogi Ferrell", command=lambda: controller.show_frame(PageName))
        button8.pack()
        button9 = ttk.Button(self, text="Dante Exum", command=lambda: controller.show_frame(PageName))
        button9.pack()
        button10 = ttk.Button(self, text="Damyean Dotson", command=lambda: controller.show_frame(PageName))
        button10.pack()
        button11 = ttk.Button(self, text="Dylan Windler", command=lambda: controller.show_frame(PageName))
        button11.pack()
        button12 = ttk.Button(self, text="JaVale McGee", command=lambda: controller.show_frame(PageName))
        button12.pack()
        button13 = ttk.Button(self, text="Kevin Love", command=lambda: controller.show_frame(PageName))
        button13.pack()
        button14 = ttk.Button(self, text="Lamar Stevens", command=lambda: controller.show_frame(PageName))
        button14.pack()
        button15 = ttk.Button(self, text="Quinn Cook", command=lambda: controller.show_frame(PageName))
        button15.pack()
        button16 = ttk.Button(self, text="Dean Wade", command=lambda: controller.show_frame(PageName))
        button16.pack()
        button17 = ttk.Button(self, text="Thon Maker", command=lambda: controller.show_frame(PageName))
        button17.pack()
        button18 = ttk.Button(self, text="Brodric Thomas", command=lambda: controller.show_frame(PageName))
        button18.pack()
        button19 = ttk.Button(self, text="Marques Bolden", command=lambda: controller.show_frame(PageName))
        button19.pack()


class Pistons(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Detroit Pistons", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()

        button0 = ttk.Button(self, text="Jerami Grant", command=lambda: controller.show_frame(PageName))
        button0.pack()
        button1 = ttk.Button(self, text="Blake Griffin", command=lambda: controller.show_frame(PageName))
        button1.pack()
        button2 = ttk.Button(self, text="Delon Wright", command=lambda: controller.show_frame(PageName))
        button2.pack()
        button3 = ttk.Button(self, text="Mason Plumlee", command=lambda: controller.show_frame(PageName))
        button3.pack()
        button4 = ttk.Button(self, text="Josh Jackson", command=lambda: controller.show_frame(PageName))
        button4.pack()
        button5 = ttk.Button(self, text="Saddiq Bey", command=lambda: controller.show_frame(PageName))
        button5.pack()
        button6 = ttk.Button(self, text="Wayne Ellington", command=lambda: controller.show_frame(PageName))
        button6.pack()
        button7 = ttk.Button(self, text="Derrick Rose", command=lambda: controller.show_frame(PageName))
        button7.pack()
        button8 = ttk.Button(self, text="Killian Hayes", command=lambda: controller.show_frame(PageName))
        button8.pack()
        button9 = ttk.Button(self, text="Dennis Smith", command=lambda: controller.show_frame(PageName))
        button9.pack()
        button10 = ttk.Button(self, text="Isaiah Stewart", command=lambda: controller.show_frame(PageName))
        button10.pack()
        button11 = ttk.Button(self, text="Sviatoslav Mykhailiuk", command=lambda: controller.show_frame(PageName))
        button11.pack()
        button12 = ttk.Button(self, text="Saben Lee", command=lambda: controller.show_frame(PageName))
        button12.pack()
        button13 = ttk.Button(self, text="Sekou Doumbouya", command=lambda: controller.show_frame(PageName))
        button13.pack()
        button14 = ttk.Button(self, text="Rodney McGruder", command=lambda: controller.show_frame(PageName))
        button14.pack()
        button15 = ttk.Button(self, text="Jahlil Okafor", command=lambda: controller.show_frame(PageName))
        button15.pack()
        button16 = ttk.Button(self, text="Frank Jackson", command=lambda: controller.show_frame(PageName))
        button16.pack()
        button17 = ttk.Button(self, text="Deividas Sirvydis", command=lambda: controller.show_frame(PageName))
        button17.pack()


class Pacers(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Indiana Pacers", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()

        button0 = ttk.Button(self, text="Domantas Sabonis", command=lambda: controller.show_frame(PageName))
        button0.pack()
        button1 = ttk.Button(self, text="Malcolm Brogdon", command=lambda: controller.show_frame(PageName))
        button1.pack()
        button2 = ttk.Button(self, text="Victor Oladipo", command=lambda: controller.show_frame(PageName))
        button2.pack()
        button3 = ttk.Button(self, text="Justin Holiday", command=lambda: controller.show_frame(PageName))
        button3.pack()
        button4 = ttk.Button(self, text="Myles Turner", command=lambda: controller.show_frame(PageName))
        button4.pack()
        button5 = ttk.Button(self, text="Caris LeVert", command=lambda: controller.show_frame(PageName))
        button5.pack()
        button6 = ttk.Button(self, text="T.J. Warren", command=lambda: controller.show_frame(PageName))
        button6.pack()
        button7 = ttk.Button(self, text="Doug McDermott", command=lambda: controller.show_frame(PageName))
        button7.pack()
        button8 = ttk.Button(self, text="T.J. McConnell", command=lambda: controller.show_frame(PageName))
        button8.pack()
        button9 = ttk.Button(self, text="Jeremy Lamb", command=lambda: controller.show_frame(PageName))
        button9.pack()
        button10 = ttk.Button(self, text="Aaron Holiday", command=lambda: controller.show_frame(PageName))
        button10.pack()
        button11 = ttk.Button(self, text="Edmond Sumner", command=lambda: controller.show_frame(PageName))
        button11.pack()
        button12 = ttk.Button(self, text="Goga Bitadze", command=lambda: controller.show_frame(PageName))
        button12.pack()
        button13 = ttk.Button(self, text="JaKarr Sampson", command=lambda: controller.show_frame(PageName))
        button13.pack()
        button14 = ttk.Button(self, text="Kelan Martin", command=lambda: controller.show_frame(PageName))
        button14.pack()
        button15 = ttk.Button(self, text="Brian Bowen", command=lambda: controller.show_frame(PageName))
        button15.pack()
        button16 = ttk.Button(self, text="Jalen Lecque", command=lambda: controller.show_frame(PageName))
        button16.pack()
        button17 = ttk.Button(self, text="Cassius Stanley", command=lambda: controller.show_frame(PageName))
        button17.pack()


class Heat(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Miami Heat", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()


class Bucks(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Milwaukee Bucks", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()

        button0 = ttk.Button(self, text="Giannis Antetokounmpo", command=lambda: controller.show_frame(PageName))
        button0.pack()
        button1 = ttk.Button(self, text="Khris Middleton", command=lambda: controller.show_frame(PageName))
        button1.pack()
        button2 = ttk.Button(self, text="Jrue Holiday", command=lambda: controller.show_frame(PageName))
        button2.pack()
        button3 = ttk.Button(self, text="Brook Lopez", command=lambda: controller.show_frame(PageName))
        button3.pack()
        button4 = ttk.Button(self, text="Donte DiVincenzo", command=lambda: controller.show_frame(PageName))
        button4.pack()
        button5 = ttk.Button(self, text="Pat Connaughton", command=lambda: controller.show_frame(PageName))
        button5.pack()
        button6 = ttk.Button(self, text="Bobby Portis", command=lambda: controller.show_frame(PageName))
        button6.pack()
        button7 = ttk.Button(self, text="D.J. Augustin", command=lambda: controller.show_frame(PageName))
        button7.pack()
        button8 = ttk.Button(self, text="Bryn Forbes", command=lambda: controller.show_frame(PageName))
        button8.pack()
        button9 = ttk.Button(self, text="Torrey Craig", command=lambda: controller.show_frame(PageName))
        button9.pack()
        button10 = ttk.Button(self, text="D.J. Wilson", command=lambda: controller.show_frame(PageName))
        button10.pack()
        button11 = ttk.Button(self, text="Thanasis Antetokounmpo", command=lambda: controller.show_frame(PageName))
        button11.pack()
        button12 = ttk.Button(self, text="Jordan Nwora", command=lambda: controller.show_frame(PageName))
        button12.pack()
        button13 = ttk.Button(self, text="Sam Merrill", command=lambda: controller.show_frame(PageName))
        button13.pack()
        button14 = ttk.Button(self, text="Mamadi Diakite", command=lambda: controller.show_frame(PageName))
        button14.pack()
        button15 = ttk.Button(self, text="Jaylen Adams", command=lambda: controller.show_frame(PageName))
        button15.pack()


class Knicks(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="New York Knicks", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()

        button0 = ttk.Button(self, text="Julius Randle", command=lambda: controller.show_frame(PageName))
        button0.pack()
        button1 = ttk.Button(self, text="RJ Barrett", command=lambda: controller.show_frame(PageName))
        button1.pack()
        button2 = ttk.Button(self, text="Mitchell Robinson", command=lambda: controller.show_frame(PageName))
        button2.pack()
        button3 = ttk.Button(self, text="Elfrid Payton", command=lambda: controller.show_frame(PageName))
        button3.pack()
        button4 = ttk.Button(self, text="Reggie Bullock", command=lambda: controller.show_frame(PageName))
        button4.pack()
        button5 = ttk.Button(self, text="Alec Burks", command=lambda: controller.show_frame(PageName))
        button5.pack()
        button6 = ttk.Button(self, text="Derrick Rose", command=lambda: controller.show_frame(PageName))
        button6.pack()
        button7 = ttk.Button(self, text="Nerlens Noel", command=lambda: controller.show_frame(PageName))
        button7.pack()
        button8 = ttk.Button(self, text="Austin Rivers", command=lambda: controller.show_frame(PageName))
        button8.pack()
        button9 = ttk.Button(self, text="Immanuel Quickley", command=lambda: controller.show_frame(PageName))
        button9.pack()
        button10 = ttk.Button(self, text="Taj Gibson", command=lambda: controller.show_frame(PageName))
        button10.pack()
        button11 = ttk.Button(self, text="Kevin Knox", command=lambda: controller.show_frame(PageName))
        button11.pack()
        button12 = ttk.Button(self, text="Frank Ntilikina", command=lambda: controller.show_frame(PageName))
        button12.pack()
        button13 = ttk.Button(self, text="Obi Toppin", command=lambda: controller.show_frame(PageName))
        button13.pack()
        button14 = ttk.Button(self, text="Dennis Smith", command=lambda: controller.show_frame(PageName))
        button14.pack()
        button15 = ttk.Button(self, text="Jared Harper", command=lambda: controller.show_frame(PageName))
        button15.pack()
        button16 = ttk.Button(self, text="Theo Pinson", command=lambda: controller.show_frame(PageName))
        button16.pack()
        button17 = ttk.Button(self, text="Ignas Brazdeikis", command=lambda: controller.show_frame(PageName))
        button17.pack()


class Magic(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Orlando Magic", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()


class Philadelphia(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Philadelphia 76ers", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()

        button0 = ttk.Button(self, text="Ben Simmons", command=lambda: controller.show_frame(PageName))
        button0.pack()
        button1 = ttk.Button(self, text="Tobias Harris", command=lambda: controller.show_frame(PageName))
        button1.pack()
        button2 = ttk.Button(self, text="Joel Embiid", command=lambda: controller.show_frame(PageName))
        button2.pack()
        button3 = ttk.Button(self, text="Seth Curry", command=lambda: controller.show_frame(PageName))
        button3.pack()
        button4 = ttk.Button(self, text="Danny Green", command=lambda: controller.show_frame(PageName))
        button4.pack()
        button5 = ttk.Button(self, text="Shake Milton", command=lambda: controller.show_frame(PageName))
        button5.pack()
        button6 = ttk.Button(self, text="Furkan Korkmaz", command=lambda: controller.show_frame(PageName))
        button6.pack()
        button7 = ttk.Button(self, text="Matisse Thybulle", command=lambda: controller.show_frame(PageName))
        button7.pack()
        button8 = ttk.Button(self, text="Dwight Howard", command=lambda: controller.show_frame(PageName))
        button8.pack()
        button9 = ttk.Button(self, text="Mike Scott", command=lambda: controller.show_frame(PageName))
        button9.pack()
        button10 = ttk.Button(self, text="Dakota Mathias", command=lambda: controller.show_frame(PageName))
        button10.pack()
        button11 = ttk.Button(self, text="Tyrese Maxey", command=lambda: controller.show_frame(PageName))
        button11.pack()
        button12 = ttk.Button(self, text="Tony Bradley", command=lambda: controller.show_frame(PageName))
        button12.pack()
        button13 = ttk.Button(self, text="Isaiah Joe", command=lambda: controller.show_frame(PageName))
        button13.pack()
        button14 = ttk.Button(self, text="Paul Reed", command=lambda: controller.show_frame(PageName))
        button14.pack()
        button15 = ttk.Button(self, text="Vincent Poirier", command=lambda: controller.show_frame(PageName))
        button15.pack()
        button16 = ttk.Button(self, text="Terrance Ferguson", command=lambda: controller.show_frame(PageName))
        button16.pack()



class Raptors(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Toronto Raptors", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()

        button0 = ttk.Button(self, text="Fred VanVleet", command=lambda: controller.show_frame(PageName))
        button0.pack()
        button1 = ttk.Button(self, text="Pascal Siakam", command=lambda: controller.show_frame(PageName))
        button1.pack()
        button2 = ttk.Button(self, text="Kyle Lowry", command=lambda: controller.show_frame(PageName))
        button2.pack()
        button3 = ttk.Button(self, text="OG Anunoby", command=lambda: controller.show_frame(PageName))
        button3.pack()
        button4 = ttk.Button(self, text="Norman Powell", command=lambda: controller.show_frame(PageName))
        button4.pack()
        button5 = ttk.Button(self, text="Chris Boucher", command=lambda: controller.show_frame(PageName))
        button5.pack()
        button6 = ttk.Button(self, text="Aron Baynes", command=lambda: controller.show_frame(PageName))
        button6.pack()
        button7 = ttk.Button(self, text="Henry Ellenson", command=lambda: controller.show_frame(PageName))
        button7.pack()
        button8 = ttk.Button(self, text="DeAndre' Bembry", command=lambda: controller.show_frame(PageName))
        button8.pack()
        button9 = ttk.Button(self, text="Terence Davis", command=lambda: controller.show_frame(PageName))
        button9.pack()
        button10 = ttk.Button(self, text="Stanley Johnson", command=lambda: controller.show_frame(PageName))
        button10.pack()
        button11 = ttk.Button(self, text="Yuta Watanabe", command=lambda: controller.show_frame(PageName))
        button11.pack()
        button12 = ttk.Button(self, text="Alex Len", command=lambda: controller.show_frame(PageName))
        button12.pack()
        button13 = ttk.Button(self, text="Paul Watson", command=lambda: controller.show_frame(PageName))
        button13.pack()
        button14 = ttk.Button(self, text="Malachi Flynn", command=lambda: controller.show_frame(PageName))
        button14.pack()
        button15 = ttk.Button(self, text="Matt Thomas", command=lambda: controller.show_frame(PageName))
        button15.pack()
        button16 = ttk.Button(self, text="Patrick McCaw", command=lambda: controller.show_frame(PageName))
        button16.pack()
        button17 = ttk.Button(self, text="Jalen Harris", command=lambda: controller.show_frame(PageName))
        button17.pack()


class Wizards(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Washington Wizards", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        #button to go back to home
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button.pack()


app = nbaGUI()
app.mainloop()
