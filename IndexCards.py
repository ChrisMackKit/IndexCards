import json
# import Card


class Topic:
    def __init__(self, name, cards):
        self._name = name
        self._cards = cards

    def createTopic(self, name):
        self._name = name
        x = {"name": self._name,
             "cards": []}
        y = json.dumps(x)

    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name

    def getCards(self):
        return self._cards

    def setCards(self, cards):
        self._cards = cards

    def addCard(self, card):
        self._cards[0].append(card)

    def correctAnswer(self, card, indexOfCard):
        self._cards[indexOfCard].remove(card)
        self._cards[indexOfCard + 1].append()(card)


# objCard = Card.Card("What is the capital of Germany?", "Berlin", [False, True, True])
# objTopic = Topic('Name1', ['c1', 'c2', 'c2'])

# answer = input(objCard.getQuestion() + '\n')
# print(answer == objCard.getAnswer())
# objCard.updateStats(answer == objCard.getAnswer())
# print(*objCard.getStats())

# To name an object through input (new Topic) use dictonaries: https://stackoverflow.com/questions/53347379/how-to-use-input-as-a-name-for-object-in-python
# GUI mit tkinter lib?
# JSON und python: 'import JSON' und um von python dict zu json: y = json.dumps(x) und andersrum: y = json.loads(x)

"""
JSON structure: instead do one JSON
{ 
'topic': String,
'cards': {
    'box1': ['card'],
    'box2': ['card'],
    'box3': ['card'],
    'box4': ['card'],
    'box5': ['card']
}
}


Class Cards: ['Question', 'Answer', [bool, bool, bool, bool, bool, ...]]
Cards have Question, Answer and a list of booleans that tracks the last (maybe) 30 answers (correct/incorrect)

Functions:
Adding a topic: Create topic: give name and create empty stack of cards with 5 lists that represent the boxes

Add card to stack: Add a card with a topic, question and answer. It gets added to the topics stack and get placed in the 1. box and with a empty list of boolean

delete card: delete a card from a stack. Show whole stack of a topic and delete it in the list OR delete while you view the card

get asked: give topic and get random question. answer by checking the answer and tell program if correct or incorrect. 
    Also give option to only ask specefic boxes (like boxes 1-3 exclude 4+)
    random cards odds to get asked is based on the box. First box gets asked the most likly and so on
    
manually change box of card: show list of cards of a topic and change the index of one card

show stats: based on the boolean lists of the cards shows you stats. Is displayed ned to the question and answer?



topicDict = {
    "name": "capitols",
    "cards": []
}


"""
