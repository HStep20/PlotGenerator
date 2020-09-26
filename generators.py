import random

Genre = []
Plot = []
WBCultural = []
WBPhysical = []
Theme = []
datasets = [Genre, Plot, Theme]
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


def designateWorldbuilding():
    WBString = ""
    count = random.randint(1, 4)
    for i in range(count):
        culturalOrPhysical = random.randint(0, 1)
        if culturalOrPhysical == 0:
            WBString += WBCultural[random.randint(0, len(WBCultural) - 1)]
        else:
            WBString += WBPhysical[random.randint(0, len(WBPhysical) - 1)]
        if (i == (count - 2)) and (count != 1):
            WBString += ", and "
        elif not (i == count - 1):
            WBString += ", "
    return WBString

def returnOutput():
    if output[0][0] in ('A', 'E', 'I', 'O', 'U'):
        article = "an "
    else:
        article = "a "

    return (
            "Brainstorm " + article + output[0] + " book "
            "using the " + output[1] + " plot "
            "where " + designateWorldbuilding() + " play a role in the story, "
            "and it touches on the theme of " + output[2]
    )
