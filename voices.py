import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

for i, v in enumerate(voices):
    print(i)
    print("  id:", v.id)
    print("  name:", v.name)
    print("  languages:", v.languages)
    print("-----")

engine.setProperty(
    'voice',
    'com.apple.voice.compact.en-US.Samantha'
)

engine.setProperty('rate', 175)
engine.say("This is Samantha speaking.")
engine.runAndWait()