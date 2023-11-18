from random import randint

def load_lines():
  inputFile = open("lines.txt")
  lineList = []
  for line in inputFile:
    voice = line.split("\n")
    lineList.append(voice[0])
  return lineList

voicelines = []
voicelines = load_lines()
randIndex = randint(0, len(voicelines) - 1);
print(voicelines[randIndex])
