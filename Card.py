class Card:
    
    def __init__(self, question, answer, stats):
        self._question = question
        self._answer = answer
        self._stats = stats
        
    def getQuestion(self):
        return self._question
    
    def getAnswer(self):
        return self._answer
    
    def getStats(self):
        return self._stats
        
    def changeCard(self, question, answer):
        self._question = question
        self._answer = answer
        
    def updateStats(self, correctAnswerGiven):
        self._stats.append(correctAnswerGiven)
        
    def checkIfStatsTooBig(self):
        if (len(self._stats) > 30):
            self._stats.pop(0)