import tkinter as tk
import jsonEdit as je


# Class for everything related to the interface

class GUI:
        #There will be one list with all the topics and a corresponding

        def __init__(self) -> None:
        
                self.jsonData = je.openJSON()
                
                self.cardsList = []
                
                self.question = "Choose a topic you want to learn"
                self.answer = " "
                
                self.box = 1
                self.stats = []
                self.topics = ['capitals', 'rivers']
                
                self.cardIndex = 0

                self.window = tk.Tk()
                self.window.geometry("800x400")
                self.window.title("Index Card Program")

                
                # Texts and labels
                self.questionLabel = tk.Label(self.window, text = self.question, font=('Arial', 18))
                self.questionLabel.pack(padx= 0, pady=20)

                self.answerText = tk.Text(self.window, height = 1)
                self.answerText.pack(padx = 0, pady = 10)

                self.answerLabel = tk.Label(self.window, text = "")
                self.answerLabel.pack(padx = 0, pady = 10)

                self.statsBox = tk.Label(self.window, text = self.stats, font=(14))
                self.statsBox.place(x = 300, y=240)
                
                # Button of the GUI
                self.showAnswer = tk.Button(self.window, text = "show answer", command = self.showAnswer, font=('Arial', 18))
                self.showAnswer.place(x= 90, y=120, height=30, width=200)
                
                self.correctAnswer = tk.Button(self.window, text = "correct answer", command = self.correctAnswer, font=('Arial', 18))
                self.correctAnswer.place(x= 300, y=120, height=30, width=200)
                
                self.wrongAnswer = tk.Button(self.window, text = "wrong answer", command = self.wrongAnswer, font=('Arial', 18))
                self.wrongAnswer.place(x= 510, y=120, height=30, width=200)
                
                self.addTopic = tk.Button(self.window, text = "add new topic", command = self.addTopic, font=('Arial', 18))
                self.addTopic.place(x= 90, y= 150, height=30, width=200)
                
                self.addCard = tk.Button(self.window, text = "add new card", command = self.addCard, font=('Arial', 18))
                self.addCard.place(x= 300, y= 150, height=30, width=200)

                # Drop down menu
                self.clicked = tk.StringVar()
                self.clicked.set('Choose Topic')
                self.clicked.trace_add('write', self.callback)
                self.topicMenu = tk.OptionMenu(self.window, self.clicked, *self.topics)
                self.topicMenu.config(font=('Arial', 14))
                self.topicMenu.place(x=80, y= 300)
                self.menu = self.window.nametowidget(self.topicMenu.menuname)
                self.menu.config(font=('Arial', 14))

                
                self.window.mainloop()

        def callback(self, *args):
                # if topic is changed, the list of cards changes
                listOfCards = je.getListOfCards(self.clicked.get(), 'cardsBox1')
                print('Topic: ' + self.clicked.get())
                print(listOfCards)
                self.cardsList = listOfCards
                self.questionLabel['text'] = listOfCards[0][0][0]
                self.answer = listOfCards[0][1][0]
                self.statsBox['text'] = listOfCards[0][2][0]
                

        def showAnswer(self):
                #answerLabel.configure(text = answer)
                #show the answer in the window
                print("okay")
                #self.answerLabel['text'] = self.answer
                self.answerLabel.destroy()
                self.answerLabel = tk.Label(self.window, text = self.answer, font=('Arial', 16))
                self.answerLabel.pack(padx = 0, pady = 100)
                #self.answerLabel.place(x = 350, y = 200)

        def correctAnswer(self):
                #updates stats and goes to next question
                print("correct")
                if self.clicked.get() == 'Choose Topic':
                        return None
                if len(self.stats) > 4:
                        self.stats.pop(0)
                self.stats.append(True)
                self.statsBox.destroy()
                self.statsBox = tk.Label(self.window, text = self.stats, font=(14))
                self.statsBox.place(x = 300, y=240)
                self.nextQuestion()

        def wrongAnswer(self):
                #updates stats and goes to next question
                print("wrong")
                if self.clicked.get() == 'Choose Topic':
                        return None
                if len(self.stats) > 4:
                        self.stats.pop(0)
                self.stats.append(False)
                self.statsBox.destroy()
                self.statsBox = tk.Label(self.window, text = self.stats, font=(14))
                self.statsBox.place(x = 300, y=240)
                self.nextQuestion()
        

        def nextQuestion(self):
                #self.answerLabel['text'] = ''
                self.cardIndex += 1
                if self.cardIndex >= len(self.cardsList):
                        self.cardIndex = 0
                self.questionLabel['text'] = self.cardsList[self.cardIndex][0][0]
                self.answer = self.cardsList[self.cardIndex][1][0]
                self.statsBox['text'] = self.cardsList[self.cardIndex][2][0]
                self.answerLabel['text'] = ''


        def addTopic(self):
                #adds new topic to the JSON
                print("new topic created")
                self.addTopicWindow = tk.Toplevel(self.window)
                self.addTopicWindow.title('Add New Topic')
                self.addTopicWindow.geometry('500x150')
                
                
                self.addTopicText = tk.Label(self.addTopicWindow, text ='Enter the name for the new topic: ')
                self.addTopicText.pack()
                self.addTopicButton = tk.Button(self.addTopicWindow, text = "add topic", command = self.addTopic2, font=('Arial', 18))
                self.addTopicButton.place(x= 150, y=100, height=30, width=200)
                self.topicText = tk.Text(self.addTopicWindow, height = 1)
                self.topicText.pack(padx = 0, pady = 10)
            
        def addTopic2(self):
                topicName = self.topicText.get('1.0', 'end -1c')
                print('topic added: ' + topicName)


        def addCard(self):
                #adds new card to a topic
                print("new card created")
                self.addCardWindow = tk.Toplevel(self.window)
                self.addCardWindow.title('Add New Card')
                self.addCardWindow.geometry('500x180')
                
                
                self.addCardLabel = tk.Label(self.addCardWindow, text ='Enter the question of the card: ')
                self.addCardLabel.pack()
                self.cardQuestion = tk.Text(self.addCardWindow, height = 1)
                self.cardQuestion.pack(padx = 0, pady = 10)
                self.addCardAnswerLabel = tk.Label(self.addCardWindow, text ='Enter the anwser of the card: ')
                self.addCardAnswerLabel.pack()
                self.cardAnswer = tk.Text(self.addCardWindow, height = 1)
                self.cardAnswer.pack(padx = 0, pady = 10)
                self.clicked2 = tk.StringVar()
                self.clicked2.set('Choose Topic')
                self.topicMenu2 = tk.OptionMenu(self.addCardWindow, self.clicked2, *self.topics)
                self.topicMenu2.place(x=20, y= 130)
                self.addTopicButton = tk.Button(self.addCardWindow, text = "add topic", command = self.addCard2, font=('Arial', 18))
                self.addTopicButton.place(x= 150, y=130, height=30, width=200)
            
        def addCard2(self):
                cardQuestion = self.cardQuestion.get('1.0', 'end -1c')
                cardAnswer = self.cardAnswer.get('1.0', 'end -1c')
                topicOfCard = self.clicked2.get()
                if topicOfCard == 'Choose Topic':
                        print('You have to pick a topic')
                else:
                        print('card added. Question: ' + cardQuestion + ' Answer: ' + cardAnswer + ' Topic: ' + topicOfCard)
                        self.jsonData = je.addCardToTopic(topicOfCard, cardQuestion, cardAnswer, self.jsonData)
                        je.saveJSON("cards.json", self.jsonData)
        
GUI()