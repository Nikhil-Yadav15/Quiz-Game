from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition, WipeTransition
from kivy.clock import Clock
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
import mysql.connector
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.core.window import Window
kv = '''
<WindManager>:
    #btn_disable: btn_disable
    #life_lvl: life_lvl
    #inp_text: inp_text
    Screen:
        name: "Opening_scr"
        orientation: "horizontal"
        Label:
            id: opn_lbl_text_id
            text: root.opn_text
            color: 0,1,0.9,1
            font_size: 200
            pos_hint: {"x": 0.01, "y": 0.04}
            size_hint_y: 1
        ProgressBar:
            id: prg_bar
            color: 0.2,0.4,0.5,0.5
            max: 8
            min: 0
            value: root.prg_value
            pos_hint: {"x": 0, "top": 0}
            size_hint_y: 1

    Screen:
        name: "Main"
        FloatLayout:
            Label:
                text: "Quiz Game"
                font_weight: "bold"
                size_hint: 0.3, 0.4
                pos_hint: {"x": 0.35, "y":0.65}
                font_size: 100
            Button:
                background_color: 0,0,0,0
                background_normal: ""
                canvas.before:
                    Color:
                        rgba: 0.3,0.8,0.2,1
                    RoundedRectangle: 
                        pos: self.x+1.2, self.y-2
                        size: self.width+7, self.height+4
                        radius: root.radius_cnv
                    Color:
                        rgba: 11/255, 16/255, 88/255, 1
                    RoundedRectangle:
                        pos:self.x + 4, self.y
                        size: self.width, self.height
                        radius: root.radius_cnv
                text: "Play"
                pos_hint: {"x": 0.078 , "y":root.main_size_y}
                size_hint: root.main_size
                font_size: root.main_fnt
                font_weight: "bold"
                color: root.main_clr
                on_press:
                    root.strt_game()
                    root.strt_clock()
                


            Button:
                background_color: 0,0,0,0
                background_normal: ""
                canvas.before:
                    Color:
                        rgba: 0.3,0.8,0.2,1
                    RoundedRectangle: 
                        pos: self.x+1.2, self.y-2
                        size: self.width+7, self.height+4
                        radius: root.radius_cnv
                    Color:
                        rgba: 11/255, 16/255, 88/255, 1
                    RoundedRectangle:
                        pos:self.x + 4, self.y
                        size: self.width, self.height
                        radius: root.radius_cnv
                text: "Help"
                pos_hint: {"x": 0.388 , "y": root.main_size_y}
                size_hint: root.main_size
                font_size: root.main_fnt
                color: root.main_clr
                on_press: root.current = "help_wind"

            Button:
                background_color: 0,0,0,0
                background_normal: ""
                canvas.before:
                    Color:
                        rgba: 0.3,0.8,0.2,1
                    RoundedRectangle: 
                        pos: self.x+1.2, self.y-2
                        size: self.width+7, self.height+4
                        radius: root.radius_cnv
                    Color:
                        rgba: 11/255, 16/255, 88/255, 1
                    RoundedRectangle:
                        pos:self.x + 4, self.y
                        size: self.width, self.height
                        radius: root.radius_cnv
                text: "Quit"
                pos_hint: {"x": 0.688 , "y": root.main_size_y}
                size_hint: root.main_size
                font_size: root.main_fnt
                color: root.main_clr
                on_press: root.opn_quit_pop()

    GameWind:
        btn_disable: btn_disable
        life_lvl: life_lvl
        inp_text: inp_text
        name: "game_scr"
        FloatLayout:
            canvas.before:
                Color:
                    rgba: 5/255,8/255 , 62/255, 1
                Rectangle:
                    size: self.size
                    pos: self.pos
            # Home
            Button:
                background_color: 0,0,0,0
                    
                canvas.before:
                    Color:
                        rgba: 0.3,0.8,0.2,1
                    RoundedRectangle:
                        pos: self.x+1.2, self.y-2
                        size: self.width+3.5, self.height+2.5
                        radius: root.radius_cnv
                    Color:
                        rgba: 11/255, 16/255, 88/255, 1
                    RoundedRectangle:
                        pos: self.x+4.3, self.y+2
                        size: self.width-3, self.height-3
                        radius: root.radius_cnv
                bold: True
                font_size: 25
                text: "Home"
                size_hint_x: 0.12
                size_hint_y: None
                pos_hint: {"x": 0, "y": 0.85}
                on_press:
                    root.press_home()
            # Level
            Label:
                id: level_game
                canvas.before:
                    Color:
                        rgba: 0.1,0.8,0,1
                    RoundedRectangle:
                        pos: self.x-10, self.y+10
                        size: self.width+25, self.height-30
                        radius: root.radius_cnv_levl_lbl
                    Color:
                        rgba: 11/255, 16/255, 88/255, 1
                    RoundedRectangle:
                        pos: self.x-8, self.y+12.5
                        size: self.width+20, self.height-35
                        radius: root.radius_cnv_levl_lbl
                font_size: 25
                size_hint: None, None
                text: "Level: 1"
                pos_hint: {"x": 0.47, "y": 0.87}
            # Life
            Label:
                id: life_lvl
                canvas.before:
                    Color:
                        rgba: 0.3,0.8,0.2,1
                    RoundedRectangle:
                        pos: self.x-10, self.y+10
                        size: self.width+20, self.height-30
                        radius: root.radius_cnv_levl_lbl
                    Color:
                        rgba: 11/255, 16/255, 88/255, 1
                    RoundedRectangle:
                        pos: self.x-7.5, self.y+12.5
                        size: self.width+15, self.height-35
                        radius: root.radius_cnv_levl_lbl
                
                text: root.life
                font_size: 30
                size_hint: None, None
                pos_hint: {"x": 0.87, "y": 0.87}
            # Timer
            Label:
                id: timer_time
                font_size: 30
                timer_color: [0,1,0,1]
                size_hint: None,None
                canvas.before:
                    Color:
                        rgba: self.timer_color
                    Ellipse:
                        size: 100,100
                        pos: self.pos
                text: ""
                pos_hint: {"x": 0.13, "y": 0.5}
            # Questions
            Label:
                id: question_text_kv
                text_size: self.width - 20, None
                valign: "middle"
                halign: "center"
                size_hint_y: None
                size_hint_x: 0.3
                canvas.before:
                    Color:
                        rgba: 0.3,0.8,0.9,1
                    RoundedRectangle:
                        pos: self.x-10, self.y-10
                        size: self.width+25, self.height + 35
                        radius: root.radius_cnv_levl_lbl
                    Color:
                        rgba: 0.2,0.2,0.6,1
                    RoundedRectangle:
                        pos: self.x-5, self.y-5
                        size: self.width+15, self.height + 25
                        radius: root.radius_cnv_levl_lbl
                text: root.quest_text
                font_size: 20
                pos_hint: {"x": 0.35, "y": 0.47}
            # Text Input
            TextInput:
                id: inp_text
                canvas.before:
                    Color:
                        rgba: (0, 0.7, 0.7, 1)
                    Line:
                        width: 1.4
                        rectangle: self.pos[0], self.pos[1], self.width, self.height
                halign: "center"
                valign: "middle"
                cursor_color: (1,0,0,1)
                background_color: (0, 0, 0, 0)

                on_text_validate: root.on_check()
                hint_text: "Type Here"
                foreground_color: (1,1,1,1)
                font_size: 30
                size_hint: 0.15, 0.1
                multiline: False
                pos_hint: {"x": 0.41, "y": 0.22}
            # Check
            Button:
                id: check_btn
                font_size: 20
                background_color: 0,0,0,0
                canvas.before:
                    Color:
                        rgba: 0.3,0.8,0.2,1
                    RoundedRectangle: 
                        pos: self.x+1.2, self.y-2
                        size: self.width+7, self.height+4
                        radius: root.radius_cnv
                    Color:
                        rgba: 11/255, 16/255, 88/255, 1
                    RoundedRectangle:
                        pos:self.x + 4, self.y
                        size: self.width, self.height
                        radius: root.radius_cnv
                text: "Check"
                on_press: root.on_check()
                size_hint: 0.12, 0.1
                pos_hint: {"x": 0.425, "y": 0.1}
            
            # Answer
            Button:
                id: ans_btn
                font_size: 20
                background_color: 0,0,0,0
                background_normal: ""
                border_radius: [18]
                canvas.before:
                    Color:
                        rgba: 1,0,0,1
                    RoundedRectangle: 
                        pos: self.x, self.y
                        size: self.width, self.height
                        radius: self.border_radius
                            
                text: "Answer"
                on_press: root.on_ans()
                disabled: True
                size_hint: 0.12, 0.1
                pos_hint: {"x": 0.78, "y": 0.49}
            # Next
            Button:
                id: btn_disable
                font_size: 20
                background_color: 0,0,0,0
                background_normal: ""
                border_radius: [18]
                canvas.before:
                    Color:
                        rgba: 0.3,0.8,0.2,1
                    RoundedRectangle:
                        pos: self.x+1.2, self.y-2
                        size: self.width+3.5, self.height+2.5
                        radius: root.radius_cnv
                    Color:
                        rgba: 11/255, 16/255, 88/255, 1
                    RoundedRectangle:
                        pos: self.x+4.3, self.y+2
                        size: self.width-3, self.height-3
                        radius: root.radius_cnv
                            
                text: "Next"
                disabled: True
                on_press: 
                    root.on_next()
                    
                    root.strt_clock()
                size_hint: 0.12, 0.1
                pos_hint: {"x": 0.8, "y": 0.1}
    Screen:
        name: "help_wind"
        FloatLayout:
            border_radius: [18]
            canvas.before:
                Color:
                    rgba: 0.3,0.8,0.2,1
                RoundedRectangle:
                    pos: self.x+50.2, self.y+ 50.4
                    size: self.width - 100, self.height -100
                    radius: root.radius_cnv
                Color:
                    rgba: 11/255, 16/255, 88/255, 1
                RoundedRectangle:
                    pos: self.x + 60.4, self.y + 62.8
                    size: self.width -121, self.height -121
                    radius: root.radius_cnv
            Label:
                text: "Introduction"
                
                size_hint: 0.2, 0.2
                font_size: 60
                font_weight: "bold" 
                pos_hint:{"x": 0.4, "y":0.72}
            Label:
                size_hint: 0.2, 0.2
                font_size: 30
                text: "NyAs is an archetype of Hangman"
                pos_hint:{"x": 0.38, "y":0.61}
            Label:
                text_size: self.width, self.height
                size_hint: 0.8, 0.6
                pos_hint:{"x": 0.1, "y":0.42}
                font_size: 18
                text: "To play, click on the PLAY button, and you will be presented with a question that you may answer by typing your response in the Answer field. The questions are a mixture of riddles and 'Who am I' kind of questions. You will be given three lives for an overall game. Every wrong answer will result in the deduction of one of those lives. When you lose all three lives, the game will end, and you will be given your final score on the basis of how many questions you answered correctly in the given time."
            Label:
                size_hint: None, 0.2
                pos_hint:{"x": 0.42, "y":0.28}
                font_size: 20
                text: "Happy Playing!"
            Button:
                background_color: 0,0,0,0
                background_normal: ""
                canvas.before:
                    Color:
                        rgba: 14/255,238/255,29/255,1
                    RoundedRectangle: 
                        pos: self.x, self.y
                        size: self.width, self.height
                        radius: [18]
                size_hint: 0.1, 0.1
                pos_hint:{"x": 0.43, "y":0.14}
                text: "Back"
                font_size: 20
                font_weight: "bold"
                color: 12/255, 11/255,0,1
                on_press:
                    root.current = "Main"
'''

time = 30
key = 20
db = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'pass', database = 'questionAnswer')
global mycursor
mycursor = db.cursor()

quest_text = ''
Score = 0

class WindManager(ScreenManager):
    global sNo
    sNo = 1
    que_box_height = 25
    global time_timer
    time_timer = time
    ##############################################################################################
    mycursor.execute("SELECT questions FROM quiz WHERE quizID = {}".format(sNo))
    # for question
    for i in mycursor:
        quest = i
    var_quest = str(quest)
    var_quest_len = len(var_quest)
    sliced_quest_var = var_quest[2:var_quest_len - 3]
    quest_text = sliced_quest_var
    ##############################################################################################
    # for answer
    mycursor.execute("SELECT answer FROM quiz WHERE quizID = {}".format(sNo))
    for i in mycursor:
        ans_sq = i
    var_ans = str(ans_sq)
    var_ans_len = len(var_ans)
    sliced_ans_var = var_ans[2:var_ans_len - 3]

    global answer_text
    answer_text = sliced_ans_var
    ##############################################################################################
    global life_count
    life_count = 4
    life = "Life: {}".format(life_count)
    ##############################################################################################
    radius_cnv = [(40, 40), (40, 40), (40, 40), (40, 40)]
    radius_cnv_levl_lbl = [(30, 30), (30, 30), (30, 30), (30, 30)]
    ##############################################################################################
    opn_text = StringProperty("")
    
    prg_value = NumericProperty()
    # Button pos y
    main_size_y = NumericProperty("0.25")
    # Button Size
    main_size = (0.2, 0.3)
    # font of btn
    main_fnt = NumericProperty("30")

    # Button color
    main_clr = [0.9, 0, 0.2, 1]
    def strt_game(self):
        self.transition = SwapTransition()
        self.transition.duration = 1
        self.current = "game_scr"
        self.ids.inp_text.text = ""
        self.time_timer = time
        self.ids.timer_time.timer_color = [0,1,0,1]
        self.ids.check_btn.disabled = False
        self.ids.btn_disable.disabled = True
        self.ids.ans_btn.disabled = True
        self.ids.level_game.text = "Level: 1"
        global life_count
        life_count = 4
        self.ids.life_lvl.text = "Life: {}".format(life_count)
        self.ids.question_text_kv.text = self.quest_text
        global Score
        Score = 0
        mycursor.execute("SELECT answer FROM quiz WHERE quizID = {}".format(sNo))
        for i in mycursor:
            ans_sq = i
        var_ans = str(ans_sq)
        var_ans_len = len(var_ans)
        sliced_ans_var = var_ans[2:var_ans_len - 3]
        global answer_text
        answer_text = sliced_ans_var
    def strt_clock(self):
        self.ids.inp_text.focus = True
        self.ids.timer_time.text = str(self.time_timer)
        if self.time_timer>0:
            global event
            event = Clock.schedule_interval(lambda dt: self.dec_timer(), 1)


    def dec_timer(self):
        if self.ids.inp_text.focus == False:
            Window.set_system_cursor('arrow')
        else:
            Window.set_system_cursor('ibeam')
        if self.time_timer!=0:
            self.time_timer-=1
            if self.time_timer<20:
                self.ids.timer_time.timer_color[0] += 20/255
                self.ids.timer_time.timer_color[1] -= 20/255
        if self.time_timer==0:
            self.ids.ans_btn.disabled = False
        self.ids.timer_time.text = str(self.time_timer)
    def on_ans(self):
        Answer_pop()

    def opn_quit_pop(self):
        Quit_pop()

    def on_next(self):
        self.ids.timer_time.timer_color = [0,1,0,1]
        self.ids.check_btn.disabled = False
        self.time_timer = time
        self.ids.ans_btn.disabled = True
        self.ids.btn_disable.disabled = True
        self.ids.inp_text.text = ""
        global sNo
        if sNo!=key:
            sNo = sNo + 1
            self.ids.level_game.text = "Level: {}".format(sNo)
        else:
            self.ids.question_text_kv.font_size = 16
            self.ids.question_text_kv.valign = "middle"
            self.ids.question_text_kv.halign = "center"

        mycursor.execute("SELECT questions FROM quiz WHERE quizID = {}".format(sNo))
        for i in mycursor:
            quest = i
        global var_quest
        var_quest = str(quest)
        var_quest_len = len(var_quest)
        sliced_quest_var = var_quest[2:var_quest_len - 3]
        global quest_text
        replace_quest = quest_text[0:]
        replaced_quest = quest_text.replace(replace_quest, sliced_quest_var)
        quest_text = replaced_quest
        self.ids.question_text_kv.text = quest_text
        ##############################################################################################
        # for answer
        mycursor.execute("SELECT answer FROM quiz WHERE quizID = {}".format(sNo))
        for i in mycursor:
            ans_sq = i
        var_ans = str(ans_sq)
        var_ans_len = len(var_ans)
        sliced_ans_var = var_ans[2:var_ans_len - 3]
        global answer_text
        answer_text = sliced_ans_var


    def on_check(self):
        Window.set_system_cursor('arrow')
        global inputed_text, answer_text, life_count, event
        inputed_text = self.ids.inp_text.text
        if answer_text.lower() != inputed_text.lower():
            if life_count>1:
                life_count-=1
            else:
                Life_end_pop()
                self.current = "Main"
                global sNo
                Clock.unschedule(event)
                sNo = 1
                life_count = 4
            self.ids.life_lvl.text = "Life: {}".format(life_count)
        else:
            Clock.unschedule(event)
            if self.time_timer>0:
                if self.ids.check_btn.disabled != True:
                    global Score
                    Score+=100
            if answer_text.lower() == "yardstick":
                self.ids.btn_disable.on_press = self.current = "Main"
            self.ids.btn_disable.disabled = False
            self.ids.ans_btn.disabled = False
            self.ids.check_btn.disabled = True
        global title_p
        if sNo == key:
            title_p = "Result"
        else:
            title_p = "Check"
        Check_popup()
    def press_home(self):
        self.current = "Main"
        global sNo, event, life_count
        Clock.unschedule(event)
        sNo = 1
class Check_popup(Popup):
    def __init__(self, **kwargs):
        super(Check_popup, self).__init__(**kwargs)
        self.title = title_p
        self.size_hint = 0.5,0.5
        self.title_align = "center"
        self.title_size  = 20
        self.background = "btn_img.jfif"
        self.open()
        self.auto_dismiss = False
        self.separator_color = (1,0,0,1)
        self.flt = FloatLayout()
        global inputed_text, answer_text, Score
        if inputed_text.lower() == "yardstick":
            self.flt.lbl = Label(text = "Your total Score: {0}/{1}".format(Score, key*100),font_size = 30, size_hint = (0.3, 0.3), pos_hint = {"x": 0.4, "y": 0.6})
            self.flt.add_widget(self.flt.lbl)
            self.flt.lbl1 = Label(text = "", bold = True,font_size = 30, size_hint = (0.3, 0.3), pos_hint = {"x": 0.38, "y": 0.4})
            self.flt.add_widget(self.flt.lbl1)
            if Score==0:
                self.flt.lbl1.text = "Better Luck Next Time"
            elif Score < (key*100):
                self.flt.lbl1.text = "Well Done!"
            else:
                self.flt.lbl1.text = "Excelent!"
            self.flt.btn = Button(text = "OK", font_size = 20, size_hint = (0.2,0.2), pos_hint = {"x": 0.38, "y": 0.1}, on_press = lambda dt: self.dismiss(), background_color = (1,0.7,0,1))
            self.flt.add_widget(self.flt.btn)
        elif answer_text.lower() == inputed_text.lower():
            self.flt.img = Image(source = "correct_ans1.gif", allow_stretch = True, keep_ratio = False, size_hint = (1, 1), pos_hint = {"x": 0, "y": 0}, anim_loop = 3, anim_delay= 0.1)
            self.flt.add_widget(self.flt.img)
            Clock.schedule_once(lambda dt: self.chn_widget(), 2)


        else:
            self.auto_dismiss = True
            self.flt.img = Image(source="wrong_ans.gif", allow_stretch=True, keep_ratio=False, size_hint=(1, 1), pos_hint={"x": 0, "y": 0}, anim_loop=1, anim_delay=0.1)
            self.flt.add_widget(self.flt.img)
            Clock.schedule_once(lambda dt: self.chn_widget(), 3)
        self.content = self.flt
    def chn_widget(self):
        self.flt.img.size_hint = (0,0)
        global inputed_text, answer_text, Score
        if answer_text.lower() == inputed_text.lower():
            self.flt.lbl2 = Label(text = "Score: {}".format(Score), size_hint = (0.2,0.2), pos_hint = {"x": 0.4, "y": 0.6}, font_size = 40)
            self.flt.add_widget(self.flt.lbl2)
            self.flt.btn = Button(text = "OK", font_size = 20, size_hint = (0.2,0.2), pos_hint = {"x": 0.4, "y": 0.1}, on_press = lambda dt: self.dismiss(), background_color = (1,0.7,0,1))
            self.flt.add_widget(self.flt.btn)
        else:
            self.flt.lbl = Label(text = "Life-=1", size_hint = (0.2,0.2), pos_hint = {"x": 0.4, "y": 0.6}, font_size = 30)
            self.flt.add_widget(self.flt.lbl)
            self.flt.lbl2 = Label(text = "Score: {}".format(Score), size_hint = (0.2,0.2), pos_hint = {"x": 0.4, "y": 0.4}, font_size = 30)
            self.flt.add_widget(self.flt.lbl2)
            self.flt.btn = Button(text = "OK", font_size = 20, size_hint = (0.2,0.2), pos_hint = {"x": 0.4, "y": 0.1}, on_press = lambda dt: self.dismiss_pop(), background_color = (1,0.7,0,1))
            self.flt.add_widget(self.flt.btn)
    def dismiss_pop(self):
        self.dismiss()


class Life_end_pop(Popup):
    def __init__(self, **kwargs):
        super(Life_end_pop, self).__init__(**kwargs)
        self.title = "Result"
        self.title_align = "center"
        self.title_size  = 20
        self.background = "btn_img.jfif"
        self.open()
        self.size_hint = 0.5,0.5
        self.auto_dismiss = False
        self.separator_color = (1,0,0,1)
        self.flt = FloatLayout()
        self.flt.lbl = Label(text="Your total Score: {0}/{1}".format(Score, key*100), font_size=30, size_hint=(0.5, 0.5),pos_hint={"x": 0.25, "y": 0.6})
        self.flt.add_widget(self.flt.lbl)
        self.flt.lbl1 = Label(text = "", bold = True,font_size = 30, size_hint = (0.3, 0.3), pos_hint = {"x": 0.38, "y": 0.4})
        self.flt.add_widget(self.flt.lbl1)
        if Score==0:
            self.flt.lbl1.text = "Better Luck Next Time"
        elif Score < (key*100):
            self.flt.lbl1.text = "Well Done!"
        else:
            self.flt.lbl1.text = "Excelent!"

        self.flt.btn = Button(text = "OK",font_size = 20, size_hint = (0.2,0.2), pos_hint = {"x": 0.4, "y": 0.1}, on_press = lambda dt: self.dismiss_pop(), background_color = (1,0.7,0,1))
        self.flt.add_widget(self.flt.btn)
        self.content = self.flt
    def dismiss_pop(self):
        self.dismiss()

class Quit_pop(Popup):
    def __init__(self, **kwargs):
        super(Quit_pop, self).__init__(**kwargs)
        self.title = "Exit"
        self.title_align = "center"
        self.title_size  = 20
        self.background = "btn_img.jfif"
        self.open()
        self.size_hint = 0.5,0.4
        self.separator_color = (1,0,0,1)
        self.grd = GridLayout()
        self.grd.rows = 2
        self.grd.lbl = Label(text="Are you sure?", font_size=20)
        self.grd.add_widget(self.grd.lbl)
        self.grd.grd_in = GridLayout()
        self.grd.grd_in.cols = 2
        self.grd.grd_in.btn1 = Button(text="Yes", on_press=lambda dt: self.clicked_close(), background_color = (1,0.7,0,1))
        self.grd.grd_in.add_widget(self.grd.grd_in.btn1)
        self.grd.grd_in.btn2 = Button(text = "No", on_press = lambda dt: self.clicked_back(), background_color = (1,0.7,0,1))
        self.grd.grd_in.add_widget(self.grd.grd_in.btn2)
        self.grd.add_widget(self.grd.grd_in)
        self.content = self.grd
    def clicked_close(self):
        App.get_running_app().stop()
    def clicked_back(self):
        self.dismiss()




class Answer_pop(Popup):
    def __init__(self, **kwargs):
        super(Answer_pop, self).__init__(**kwargs)
        self.title = "Answer"
        self.background = "btn_img.jfif"
        self.title_align = "center"
        self.title_size  = 20
        self.open()
        self.size_hint = 0.5,0.4
        self.separator_color = (1,0,0,1)
        global answer_text, sNo
        mycursor.execute("SELECT answer FROM quiz WHERE quizID = {}".format(sNo))
        for i in mycursor:
            ans_sq = i
        var_ans = str(ans_sq)
        var_ans_len = len(var_ans)
        sliced_ans_var = var_ans[2:var_ans_len - 3]

        global answer_text
        answer_text = sliced_ans_var
        self.flt = FloatLayout()
        self.flt.lbl = Label(text = answer_text,size_hint = (0.2,0.3), font_size=30, pos_hint = {"x": 0.4, "y": 0.5})
        self.flt.add_widget(self.flt.lbl)
        self.flt.btn = Button(text = "OK", size_hint = (0.2,0.2),pos_hint = {"x": 0.4, "y": 0.2},background_color = (1,0.7,0,1), on_press = lambda dt: self.dismiss_ans_pop())
        self.flt.add_widget(self.flt.btn)
        self.content = self.flt
    def dismiss_ans_pop(self):
        self.dismiss()

class GameWind(Screen):
    pass


Builder.load_string(kv)

class Quiz_gm(App):
    def build(self):
        self.title = "Quiz Game"
        self.icon = 'quiz_gm.jpg'
        # Delaying
        # 3
        Clock.schedule_once(lambda dt: self.update_opn_text(), 3)
        # 4
        Clock.schedule_once(lambda dt: self.inc_val(), 4)
        # 9
        Clock.schedule_once(lambda dt: self.move_screen(), 9)
        # 0
        Clock.schedule_once(lambda dt: self.max_scr(), 0)
        return WindManager()
    def update_opn_text(self):
        self.root.opn_text  = "NyAs"
        self.root.ids.prg_bar.pos_hint = {"x": 0, "top": 0.7}
    def inc_val(self):
        Clock.schedule_interval(lambda dt: self.update_prg_value(), 1)
    def update_prg_value(self):
        self.root.prg_value+=2
        
    def max_scr(self):
        App.get_running_app().root_window.maximize()
    def move_screen(self):
        self.root.transition = WipeTransition()
        self.root.transition.duration = 1
        self.root.current = "Main"

if __name__ == '__main__':
    Quiz_gm().run()
