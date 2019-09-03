import pygame, math

class Function:
    def __init__(self, l, color=(0,0,0), width=2):
        self.l = l
        self.color = color
        self.width = width

class Graph:
    def __init__(self, screen, fromX=-100, toX=100, fromY=-100, toY=100, functions=[]):
        self.screen = screen
        self.fromX = fromX
        self.toX = toX
        self.fromY = fromY
        self.toY = toY
        self.functions = functions

    def AddFunction(self, function):
        if self.functions.count(function) < 1:
            self.functions.append(function)

    def RemoveFunction(self, function):
        self.functions.remove(function)
        
    def GetFunctions(self):
        return self.functions

    def SetFunctions(self, functions):
        self.functions = functions

    def Draw(self):
        self.__drawGrid()
        for function in self.functions:
            self.__drawFunction(function)

    def __drawFunction(self, function):
        y = 0
        preY = 0
        for x in range(500):
            y = int(self.__mapToRange(function.l(self.__mapToRange(x, 0, 500, self.fromX, self.toX)), self.fromY, self.toY, 500, 0))
            if y < 500 and y > 0:
                pygame.draw.line(self.screen, function.color, (x - 1, preY), (x, y), function.width)
            preY = y

    def __mapToRange(self, inVal, inMin, inMax, outMin, outMax):
        return (inVal - inMin) * (outMax - outMin) / float(inMax - inMin) + outMin

    def __drawGrid(self, cellW=10, cellH=10):

        mappedX = float(0)
        mappedY = float(0)
        
        for x in range(500):
            mappedX = self.__mapToRange(x, 0, 500, self.fromX, self.toX)
            if mappedX == 0:
                pygame.draw.line(self.screen, (0,0,0), (x,0), (x,500), 2)
            elif mappedX % 1 == 0:
                pygame.draw.line(self.screen, (200,200,200), (x,0), (x,500), 1)
            
        for y in range(500):
            mappedY = self.__mapToRange(y, 0, 500, self.fromY, self.toY)
            if mappedY == 0:
                pygame.draw.line(self.screen, (0,0,0), (0,y), (500, y), 2)
            elif mappedY % 1 == 0:
                pygame.draw.line(self.screen, (200,200,200), (0,y), (500,y), 1)
        