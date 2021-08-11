from tkinter import *
import warnings
warnings.filterwarnings("ignore")
import wikipedia
from webbrowser import *
import wikipedia 
import bs4
# color chart used - http://www.science.smith.edu/dftwiki/images/3/3d/TkInterColorCharts.png
todo_list = []
BG_GRAY = "coral4"
BG_COLOR = "coral1"
TEXT_COLOR = "black"

FONT = "Helvetica 17"
FONT_BOLD = "Helvetica 13 bold"

class ChatApplication:
    # Basic defining of the Tkinter window. Template by PythonEngineer youtube channel
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()
    #Making the chatbot run forever in the bachground
    def run(self):
        self.window.mainloop()
    #Basic design of the Window
    def _setup_main_window(self):
        self.window.title("Chat")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=1000, height=550, bg=BG_COLOR)
        
        # head label Says Stay Ahead the name of the app
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                           text="Stay Ahead", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)
        
        # tiny divider - Used to keep the head label mentioned above
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)
        
        # text widget - This is where all the text goes
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)
        
        # scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)
        
        # bottom label
        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)
        
        # message entry box
        self.msg_entry = Entry(bottom_label, bg="khaki", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)
        
        # send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, "Hi, for getting to know the commands please type -help- and I will be there for you\n\n\n\n_________________________\n")
        self.text_widget.configure(state=DISABLED)
        
        self.text_widget.see(END)
     
    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")
        
    def _insert_message(self, msg, sender):
        def get_answer(question):
            question = question.lower()
            if(question.find("hi")!=-1):
                return "Hi, for getting to know the commands please type -help- and I will be there for you\n\n_________________________________\n"
            if(question.find("features")!=-1 or question.find("what can you do")!=-1 or question.find("help")!=-1):
                return "This is a student helper\n These are the following ways in which it can help you:\n 1. Inorder to save  a hw in the virtual todo list please type -add todo + task name-\n 2. If you want to check what all is on your todo list, please type mytodo\n 3. If you want me to remove an item from your todo please type -remove todo +task to remove-\n 6.If you want me to open a website for you please type -open webpage + name of webpage-\n 7. If you want me to give wikipedia gists please type -research- and the rest steps will come on its own\n 8. If you ever have any problems with any command please type -help-\n I am Always there to help you!\n\n\n\n\n\n_______________________________________________________\n"
            if(question.find("add todo")!=-1):
                mainy_noy = question.replace("add todo ","")
                todo_list.append(mainy_noy)
                return "Added "+mainy_noy+" to your todo list\n\n\n___________________________________\n"
            if(question.find("mytodo")!=-1):
                answer = ""
                counter = 1
                if(len(todo_list)==0):
                    return "No tasks in the todo list #winning\n\n\n_____________________________\n"
                for item in todo_list:
                    answer+=str(counter)+". "
                    counter+=1
                    answer=answer+item;
                    answer+="\n"
                return answer+"\n\n\n____________________________________\n"
            if(question.find("remove todo")!=-1):
                mainy_boy = question.replace("remove todo ","")
                if(question in todo_list):
                    todo_list.remove(mainy_boy)
                    return "Successfully removed "+mainy_boy+"\n\n\n____________________________\n"
                else:
                    return "No task named "+mainy_boy+" there in the todo list please check for extra spaces or spelling mistakes\n\n\n__________________________\n"
            if(question.find("open webpage")!=-1):
                mainy_boy = question.replace("opened webpage If it has not opened on your computer please check if you have installed the necessary packages mentioned above and try again\n\n\n\n______________________\n","")
                webbrowser.open(mainy_boy, new=1)
            if(question.find("research")!=-1):
                mainy_boy = question.replace("research ","")
                try:
                    result = BeautifulSoup(html).find_all('li')
                except wikipedia.exceptions.DisambiguationError:
                    return "The words spelling is either wrong or wikipedia doesn't contain anything about that. There is also a probability of you downloading a corrupted package please reinstall the package\n\n\n\n\n_____________________________________\n"
                return result+"\n\n\n\n________________________________\n"
        if not msg:
            return
        
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        # The bots message is diplayed
        msg2 = get_answer(msg)
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        
        self.text_widget.see(END)
             
def run_main_app():
    splash_screen.destroy()
    app = ChatApplication()
    app.run()

splash_screen = Tk()
splash_screen.title("Stay Ahead!")
splash_screen.geometry("450x650")
splash_screen_bg = PhotoImage(file = "SpashBG .png")
background_paceholder = Label(splash_screen,image=splash_screen_bg)
background_paceholder.place(x=0,y=0,relwidth=1,relheight=1)
splash_screen.after(3000,run_main_app)
mainloop()