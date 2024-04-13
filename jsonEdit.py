import json


# 'cards.json'
def openJSON(jsonFile='cards.json'):
    with open(jsonFile) as f:
        content = json.load(f)
    return content


# jsonFile is the name of the file to overwrite or create, content is the json (dic) that is to be saved
def saveJSON(jsonFile='cards.json', content=openJSON("cards.json")):
    with open(jsonFile, 'w') as f:
        json.dump(content, f, indent=4)


def showTopics(content = openJSON("cards.json")):
    topics = []
    for i in content["topics"]:
        topics.append(i["topicName"])
    return topics


def showCards(topic, box = 'cardsBox1', content = openJSON("cards.json")):
    questions = []
    for i in content['topics']:
        if i["topicName"] == topic:
            for n in range(len(i[box])):
                questions.append(i['cardsBox1'][n]["question"])
    return questions

# with a given topic and box it returns a list of all the cards and every card is a list with 3 entries ['Question', 'Answer', [stats]]
def getListOfCards(topic, box = 'cardsBox1', content = openJSON("cards.json")):
    listOfCards = []
    for i in content['topics']:
        if i['topicName'] == topic:
            for n in range(len(i[box])):
                listOfCards.append([[i['cardsBox1'][n]["question"]], [i['cardsBox1'][n]["answer"]], [i['cardsBox1'][n]["stats"]]])
    return listOfCards

def convertBox(box):
    match box:
        case 1:
            return "cardsBox1"
        case 2:
            return "cardsBox2"
        case 3:
            return "cardsBox3"
        case 4:
            return "cardsBox4"
        case 5:
            return "cardsBox5"


def addCardToTopic(topic, question, answer, content = openJSON("cards.json")):
    newDic = {"question": question, "answer": answer, "stats": []}
    for i in content['topics']:
        if i["topicName"] == topic:
            i["cardsBox1"].append(newDic)
    return content

#type: 'dict'
content = openJSON("cards.json")

# addCardToTopic(content, "capitals", "Was ist die Hauptstadt von Iran?", "Teheran")
# print(content)
# saveJSON("cards2.json", content)
#print(getListOfCards("rivers", "cardsBox1"))
#saveJSON("cards.json", addCardToTopic('rivers', 'test frage', 'test antwort'))
