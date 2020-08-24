import random
Genre = []
Plot = []
WBCultural = []
WBPhysical = []
Theme = []
datasets = [Genre, Plot, WBCultural, WBPhysical, Theme]
output = []

def setup():
    for line in open('GenFiles/Genre.txt', 'r'):
        Genre.append(line.rstrip())
    for line in open('GenFiles/Plot.txt', 'r'):
        Plot.append(line.rstrip())
    for line in open('GenFiles/WBCultural.txt', 'r'):
        WBCultural.append(line.rstrip())
    for line in open('GenFiles/WBPhysical.txt', 'r'):
        WBPhysical.append(line.rstrip())
    for line in open('GenFiles/Theme.txt', 'r'):
        Theme.append(line.rstrip())
    generate()
def generate():
    output.clear()
    for item in datasets:
        output.append(item[random.randint(0, len(item) - 1)])
    return returnOutput()
def returnOutput():
    return(
        "Brainstorm a " + output[0] + " book "
        "using the " + output[1] + " plot " 
        "where " + output[2] + " and " + output[3] + " play a role in the story, "
        "and it touches on the theme of " + output[4]
          )
