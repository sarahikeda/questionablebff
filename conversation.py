import re

reversal = {
    "me" : "you",
    "my" : "your",
    "fun" : "enjoyment",
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
    # print ("It's really nice to meet you! What's your name?")
    # name = input("* ").capitalize()
    # print "How are you, " + name + "?"

    while True:
        statement = input("* ")
        print (formulate_response(statement))
        if statement == "goodbye":
            print ("Take care, my friend!")
            break

def formulate_response(statement):
    statement = fix_punctuation(statement)
    tokens = statement.split()
    for word in tokens:
        if word in reversal:
            statement = re.sub(word, reversal[word], statement)
    return statement

def fix_punctuation(statement):
    changed_statement = []
    for character in statement:
        if character in punctuation:
            character = punctuation[character]
        changed_statement.append(character)
    statement = "".join(changed_statement)
    return (statement)
    # if statement == "awesome":
    #     print "I'm glad to hear that :)"
    # elif re.search('my', statement):
    #     print re.sub('my', 'your', statement)
    # elif statement == "bad":
    #     print "Well shoot."
    # else:
    #     print "I don't quite understand, actually. Would you care to expand?"

# def search_pattern(statement):

conversation()
