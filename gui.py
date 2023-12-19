import tkinter as tk


question = "Was ist die Hauptstadt von Deutschland?"
answer = "Berlin"
box = 1
stats = [True, False, False, True]

window = tk.Tk()
window.geometry("800x400")
window.title("Index Card Program")

questionLabel = tk.Label(window, text = question).pack(padx= 0, pady=20)

answerText = tk.Text(window, height = 1).pack(padx = 0, pady = 10)

answerLabel = tk.Label(window, text = "").pack(padx = 0, pady = 10)

def showAnswer():
    #answerLabel.configure(text = answer)
    print("okay")

showAswer = tk.Button(window, text = "show answer", command = showAnswer).pack(padx = 0, pady = 10)

statsBox = tk.Label(window, text = stats).pack(padx = 0, pady = 0)

    

window.mainloop()

