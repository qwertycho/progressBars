import sys
import time

class ProgressBar:
    progres = 0
    selected_bracket = 0
    brackets = [
        ["[", "]"],
        ["{", "}"],
        ["I","I"],
        ["|", "|"]
    ]

    def __init__(self, width = 10, finalCount = 100, emptyChar = " ", progressChar = "#", showPercentage = True):
        self.width = width
        self.finalCount = finalCount
        self.emptyChar = emptyChar
        self.progressChar = progressChar
        self.showPercentage = showPercentage

    def set_brackets(self, bracket_number: int):
        if bracket_number < len(self.brackets) and bracket_number > 0:
            self.selected_bracket = bracket_number
        else:
            print("WARNING: bracket type of of range. Expected: 0-%i, got: %i" % (len(self.brackets), bracket_number))

    def add_brackets(self, start, end):
        self.brackets.append([start, end])
        return len(self.brackets) - 1

    def tick(self, progres = 1):
        self.progres += progres

        if not progres == 0:
            percentage = int(self.progres / self.finalCount * 100) 
        else:
            percentage = 0
        
        shape = self.progressChar * int(self.width * percentage / 100)
        shape += self.emptyChar * (self.width - len(shape))
        
        if self.showPercentage:
            sys.stdout.write("\r" + self.brackets[self.selected_bracket][0] + "%-{w}s".format(w=self.width) % (shape) + self.brackets[self.selected_bracket][1] + " %d%%" % (int(percentage)))   
        else:
           # sys.stdout.write("\r%s%-{w}s%s".format(w=self.width) % (self.brackets[self.selected_bracket][0] ,shape, self.brackets[self.selected_bracket][1]))
            sys.stdout.write("\r" + self.brackets[self.selected_bracket][0] + "%-{w}s".format(w=self.width) % (shape) + self.brackets[self.selected_bracket][1])   
