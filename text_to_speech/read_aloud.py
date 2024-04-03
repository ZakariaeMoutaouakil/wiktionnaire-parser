import pyttsx3


def read_text_aloud(text: str):
    engine = pyttsx3.init()
    engine.setProperty('voice', 'french')
    engine.say(text)
    engine.runAndWait()


if __name__ == '__main__':
    string = "Bonjour, je m'appelle Jean"
    read_text_aloud(string)
