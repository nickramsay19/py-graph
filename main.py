import pygame, math
from graph import Graph, Function

# setup pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Graph Visualiser - Created by NR")

# setup graph
graph = Graph(screen, fromX=-100, toX=100, fromY=-100, toY=100)
graph.AddFunction(Function(lambda x : x, color=(255,0,0), width=5))
graph.AddFunction(Function(lambda x : (x + 70) ** 2, color=(0,0,255), width=5))
graph.AddFunction(Function(lambda x : math.e ** x, color=(0,150,0), width=5))

while True:

    # Check if user is quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill((255,255,255))
    
    graph.Draw()

    pygame.display.update()