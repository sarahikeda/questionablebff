import re
import string
import code
from random import randint

def randomize_response():
    possibilities = ["Interesting thought.", "I'll need to speculate further.", "What a peculiarity!", "Hm, good idea. Can you give me some more details?"]
    length = len(possibilities) - 1
    choice_index = randint(0,length)
    return possibilities[choice_index]

def answer_question(question):
    possibilities = ["Interesting question.", "You sure ask good questions!", "Question time is over.", "Hm, good question. Can you fill me in?", "What do you think the answer is?"]
    length = len(possibilities) - 1
    choice_index = randint(0,length)
    return possibilities[choice_index]

response = {
    ".*always.*" : "Why do you think this happens so frequently?",
    "(.*mom?(ther)?.*|.*father.*|.*dad.*)" : "Tell me more about your parent.",
    ".*argh.*" : "Please be patient with me. I'm trying my best!",
    ".*need (.*)" : "Are you sure you really need \g<1>?",
    ".*lonely.*" : "I'm sorry you feel that way.",
    "^the end$" : "Go on. We're making headway!"
}

punctuation = {
    "?": ".",
    "!": "."
}
def conversation():
    print ("It's really nice to meet you! What's your name?")
    name = input("* ").title()
    print ("How are you, " + name + "?")

    while True:
        statement = input("* ")
        type_response = check_type(statement)
        print (formulate_response(statement) + " | response type:\t" + type_response)
        if statement == "goodbye":
            print ("That will be $50 for this session, my friend.")
            break

def check_type(statement):
    if re.search(r'\?|^(how|where|why|who|what|when|are|is|can|which|have|would)\b', statement, re.IGNORECASE):
        return "question"
    else:
        return "statement"

def formulate_response(statement):
    type = check_type(statement)
    if type == "question":
        return answer_question(statement)
    else:
        statement = fix_punctuation(statement).lower()
        for regex in response.keys():
            if re.search(regex, statement):
                return re.sub(regex, response[regex], statement)
        return randomize_response()


def fix_punctuation(statement):
    changed_statement = []
    for character in statement:
        if character in punctuation:
            character = punctuation[character]
        changed_statement.append(character)
    statement = "".join(changed_statement)
    return statement

conversation()
