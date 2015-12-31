import re

response = {
    ".*always.*" : "Why do you think this happens so frequently?",
    ".*lonely.*" : "I'm sorry you feel that way.",
    ".*Argh.*" : "Please be patient with me. I'm trying my best!",
    ".*What do you think?" : "Hm, good question. Can you give me some more details?",
    "The end" : "Go on."
}

substitution = {
    "me" : "you",
    "my" : "your",
    "I'm" : "you are",
    "I" : "You",
    "am" : "are",
    "was" : "were"
}

punctuation = {
    "?": ".",
    "!": "."
}
def conversation():
    print ("It's really nice to meet you! What's your name?")
    name = input("* ").capitalize()
    print ("How are you, " + name + "?")

    while True:
        statement = input("* ")
        print (formulate_response(statement))
        if statement == "goodbye":
            print ("Take care, my friend!")
            break

def formulate_response(statement):
    statement = fix_punctuation(statement)
    for key, value in response.items():
        if re.match(key, statement, re.IGNORECASE):
            return (response[key])
    tokens = statement.split()
    for word in tokens:
        if word in substitution:
            statement = re.sub(word, substitution[word], statement)
    return statement

def fix_punctuation(statement):
    changed_statement = []
    for character in statement:
        if character in punctuation:
            character = punctuation[character]
        changed_statement.append(character)
    statement = "".join(changed_statement)
    return (statement)

conversation()
