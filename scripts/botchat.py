import json

import aiml

with open("config.json", "r") as configFile:
    config = json.load(configFile)
chatBot = aiml.Kernel()
# Already have a brain - load it
chatBot.bootstrap(brainFile="scripts/brain.brn")
# Learned by this point - let's set our owner's name/gender
# Start the convo
chatBot.respond('Hello')


def respond(query: str):
    result = chatBot.respond(query.strip())
    print(result)
