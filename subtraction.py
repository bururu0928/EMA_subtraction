from os import times
from manim import *
from matplotlib.pyplot import pink
from calculate import borrow_list, calculate_str, calculate
from template import*
#from Substraction_text_output import text_output
import time

class Subtraction(Scene):
    def construct(self):
        # 輸入數字
        a=100
        b=7
        start_time = time.time()

        #產生詳解文本
        #text_output(a,b)
        
        # 計算各位數，並轉成整數、字串型態
        a_str_list, b_str_list, ans_str_list, borrow_str_list, max_len = calculate_str(a,b)
        
        # 計算答案
        Ans = a-b
        Ans_text = Text(f"答案是:{Ans}").to_corner(DR)

        # 寫題目
        question_text = Text(f"{a} - {b} = ?")
        question_text.to_corner(UP,buff=0.5)

        # 畫數線、題目做圖
        line_a = NumberLine(
            x_range=[0, a, a],
            color = BLUE,
            stroke_width = 4,
            length = 7,
        ).move_to((LEFT*3.5+UP*1.5), aligned_edge=LEFT)

        line_b = NumberLine(
            x_range=[0, b, b],
            color = YELLOW,
            stroke_width = 4,
            length = 7*b/a,
        ).move_to(line_a.get_left(), aligned_edge=LEFT)
        
        sub_line = DashedLine(
            [0,0,0],
            [7*Ans/a,0,0],
            color = WHITE
        ).move_to(line_b.get_right(),aligned_edge=LEFT)

        #number label
        a_number_label = Text(f"{a}").scale(0.5)
        a_number_label.next_to(line_a,DOWN)
        b_number_label = Text(f"{b}").scale(0.5)
        b_number_label.next_to(line_b,UP)

        #line label
        sub_label = Brace(sub_line,direction=UP)
        sub_text = sub_label.get_text("?")
    
        #位置表
        t0 = table_gen(a_str_list, b_str_list, ans_str_list, max_len)
    
        #將答案轉成轉成轉成Text()型態
        borrow_Text_list = []
        for i in range(len(borrow_str_list)):
            digit_borrow_list = []
            for j in range(len(borrow_str_list[i])):
                if j == len(borrow_str_list[i]):
                    digit_borrow_list.append(Text(borrow_str_list[i][j],color = YELLOW,stroke_width=0.2).scale(0.4).next_to(t0.get_cell((1,max_len+1-len(borrow_str_list[i])-i)),DR*0.5))
                else:
                    digit_borrow_list.append(Text(borrow_str_list[i][j],color = YELLOW,stroke_width=0.2).scale(0.4).next_to(t0.get_cell((1,max_len+1-i-j)),DR*0.5).shift(LEFT*0.5))
            digit_borrow_list.reverse()
            borrow_Text_list.append(digit_borrow_list)
    
        #關注位數
        attention = []
        for i in range(max_len):
            attention.append(t0.get_cell((4, max_len+1-i), color=RED))
     
        #影格

        #算式
        self.add(question_text)

        # 數線
        self.play(Create(line_a,lag_ratio=0.2),Write(a_number_label))
        self.play(Create(line_b,lag_ratio=0.2),Write(b_number_label))
        self.play(Create(sub_line,lag_ratio=0.2))
        self.play(Write(sub_label,lag_ratio=0.05),Write(sub_text,lag_ratio=0.1))
        self.wait(1)

        #位置表
        self.play(Create(t0))
        self.wait(1)
         
        #直式減法規則
        for i in range(max_len):
            self.play(Create(attention[i]))
            self.wait()
            '''if i < len(borrow_Text_list):
                for j in borrow_Text_list[i]:
                    self.play(Write(j))
                    self.wait(0.5)    '''     
            self.play(Write(t0.get_entries_without_labels()[-(i+1)].set_color(WHITE)))
            self.wait(1)
            self.play(Uncreate(attention[i]))
        
        # 寫答案
        self.play(AddTextLetterByLetter(Ans_text))
        self.wait(1)

        print("--- %s seconds ---" % (time.time() - start_time))
            
        '''
        for i in range(len(borrow_str_list)):
            digit_borrow_list = []
            for j in range(len(borrow_str_list[i])):
                if j == len(borrow_str_list[i]):
                    digit_borrow_list.append(Text(borrow_str_list[i][j],color = YELLOW,stroke_width=0.2).scale(0.4).next_to(t0.get_cell((1,max_len+1-len(borrow_str_list[i])-i),DR*0.5)))
                else:
                    digit_borrow_list.append(Text(borrow_str_list[i][j],color = YELLOW,stroke_width=0.2).scale(0.4).next_to(t0.get_cell((1,max_len+1-i-j),DR*0.5)).shift(LEFT*0.5))
            borrow_Text_list.append(digit_borrow_list)'''