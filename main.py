import turtle

class circuito():
    corredores = []
    __posStartY = (-30, -10, 10, 30)
    __colorTurtle = ('red','blue','orange','green')
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__startLine = -width/2 + 20
        self.__finishLine = width/2 - 20
        
        self.__screen =turtle.Screen()
        self.__screen.setup(width, height)
        self.__screen.bgcolor('lightgray')
        
        self.__createRunners()
    
        
    def __createRunners(self): 
        for i in range(4):
            new_turtle = turtle.Turtle()
            new_turtle.shape('turtle')
            new_turtle.penup()
            new_turtle.color(self.__colorTurtle[i])
            new_turtle.setpos(self.__startLine,self.__posStartY[i])
            
            
            
            self.corredores.append(new_turtle)
            
    

if __name__ == '__main__':
    circuito = circuito(640,480)
    