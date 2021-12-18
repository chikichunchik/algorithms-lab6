import numpy as np
from tkinter import *


class Pig:
    def __init__(self, bots_number, move_number, window):
        self.window = window
        self.bots_number = bots_number
        self.score = [0] * (bots_number + 1)
        self.move_number = move_number
        self.risk = np.random.choice([-0.02, -0.01, 0, 0.01, 0.02], size=bots_number, replace=False)

    def play(self):
        move_label = Label(self.window)
        move_label.grid(column=0, row=3)
        self.bot_move_labels = []
        bot_result_labels = []
        for i in range(self.bots_number):
            temp_label = Label(self.window, text='Bot' + str(i+1) + ' move result: ')
            temp_label.grid(column=0, row=(4 + i))
            self.bot_move_labels.append(temp_label)
            temp_label = Label(self.window, text='Bot' + str(i+1) + ' total result: ' + str(self.score[i]))
            temp_label.grid(column=1, row=(4 + i))
            bot_result_labels.append(temp_label)
        print(1)
        self.player_move_label = Label(self.window, text='Player move result: ')
        self.player_move_label.grid(column=0, row=(4+self.bots_number))
        player_result_label = Label(self.window, text='Player total result: ' + str(self.score[-1]))
        player_result_label.grid(column=1, row=(4+self.bots_number))
        for j in range(self.move_number):
            move_label.configure(text='Move' + str(j+1))
            for i in range(self.bots_number):
                self.bot_move_labels[i].configure(text='Bot' + str(i+1) + ' move result: 0')
                bot_gain = self.AI_move(i)
                self.score[i] += bot_gain
                self.bot_move_labels[i].configure(text=(self.bot_move_labels[i].cget('text') + ' = ' + str(bot_gain)))

            self.player_move_label.configure(text='Player move result: 0')
            player_gain = self.player_move()
            self.score[-1] += player_gain
            self.player_move_label.configure(text=self.player_move_label.cget('text') + ' = ' + str(player_gain))
            for i in range(self.bots_number):
                bot_result_labels[i].configure(text='Bot' + str(i+1) + ' total result: ' + str(self.score[i]))
            player_result_label.configure(text='Player total result: ' + str(self.score[-1]))

            go_next_move = IntVar()
            move_continue_button = Button(self.window, text='Next move', command=lambda: go_next_move.set(1))
            move_continue_button.grid(column=0, row=(6 + self.bots_number))
            self.window.wait_variable(go_next_move)

        print(self.risk)

    def AI_move(self, AI_index, current_move_score=0):
        if ((5 / 6) + self.risk[AI_index]) * 4 <= current_move_score * ((1 / 6) - self.risk[AI_index]):
            return current_move_score
        else:
            move_result = np.random.choice(range(1, 6))
            if move_result == 1:
                self.bot_move_labels[AI_index].configure(
                    text=(self.bot_move_labels[AI_index].cget('text') + ' - ' + str(current_move_score)))
                return 0
            else:
                self.bot_move_labels[AI_index].configure(
                    text=(self.bot_move_labels[AI_index].cget('text') + ' + ' + str(move_result)))
                return self.AI_move(AI_index, current_move_score=current_move_score + move_result)

    def player_move(self, current_move_score=0):
        player_decision = IntVar()
        continue_button = Button(self.window, text='Continue move', command=lambda: player_decision.set(1))
        continue_button.grid(column=0, row=(5+self.bots_number))
        stop_button = Button(self.window, text='Stop move', command=lambda: player_decision.set(0))
        stop_button.grid(column=1, row=(5 + self.bots_number))
        self.window.wait_variable(player_decision)
        if player_decision.get() == 0:
            return current_move_score
        elif player_decision.get() == 1:
            move_result = np.random.choice(range(1, 6))
            if move_result == 1:
                self.player_move_label.configure(
                    text=self.player_move_label.cget('text') + ' - ' + str(current_move_score))
                return 0
            else:
                self.player_move_label.configure(
                    text=self.player_move_label.cget('text') + ' + ' + str(move_result))
                return self.player_move(current_move_score + move_result)
        else:
            raise Exception('incorrect input')
