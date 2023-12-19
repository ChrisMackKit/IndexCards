import json


# 'cards.json'
def openJSON(jsonFile):
    with open(jsonFile) as f:
        content = json.load(f)
    return content


# jsonFile is the name of the file to overwrite or create, content is the json (dic) that is to be saved
def saveJSON(jsonFile, content):
    with open(jsonFile, 'w') as f:
        json.dump(content, f, indent=4)


def showTopics(content):
    topics = []
    for i in content["topics"]:
        topics.append(i["topicName"])
    return topics


def showCards(content, topic, box):
    questions = []
    for i in content['topics']:
        if i["topicName"] == topic:
            for n in range(len(i[box])):
                questions.append(i['cardsBox1'][n]["question"])
    return questions


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


def addCardToTopic(content, topic, question, answer):
    newDic = {"question": question, "answer": answer, "stats": []}
    for i in content['topics']:
        if i["topicName"] == topic:
            i["cardsBox1"].append(newDic)
    return content

content = openJSON("cards.json")
# addCardToTopic(content, "capitals", "Was ist die Hauptstadt von Iran?", "Teheran")
# print(content)
# saveJSON("cards2.json", content)
# print(showCards(content, "rivers", "cardsBox1"))
