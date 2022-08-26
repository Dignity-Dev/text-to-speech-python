import pyttsx3


def onStart():
    print('starting')


def onWord(name, location, length):
    print('word', name, location, length)


def onEnd(name, completed):
    print('finishing', name, completed)


engine = pyttsx3.init()

# engine.connect('started-utterance', onStart)
# engine.connect('started-word', onWord)
# engine.connect('finished-utterance', onEnd)

sen = """
This section comprises an analysis of the data collected from the questionnaire administered 
to the respondents. This study employed statistical techniques to determine the reliability and 
normality of the data on student perception of impact of guidance and counselling service on career 
choice of secondary school students..
"""

engine.say(sen)
engine.runAndWait()