'''
Created on Dec 9, 2017

@author: Georgi Valchanov
'''
from random import randint


class QuestionGenerator(object):
    level = 0
    operator = None
    operations = None
    startingNum = 1

    def __init__(self, intialLevel=1, initialNum=1):
        '''
        Constructor.
        Creates a Question generator with random questions.
        (the mode can be changed)
        first argument: the starting level of the game
        second argument: how big should the numbers at least be
        '''
        self.level = intialLevel
        self.startingNum = initialNum
            
        self.operator = 'r'
        self.operations = {'+': self.add, '-': self.subtract, '*': self.multiply, '/': self.divide, 'r': self.randomgen}
       
        
    def increaseLevel(self):
        '''
        Decreases the level of difficulty of the questions by one
        '''
        self.level += 1
        
    def decreaseLevel(self):
        '''
        Increases the level of difficulty of the questions by one
        '''
        self.level -= 1
        
    def getLevel(self):
        '''
        Returns the level of difficulty of the asked questions
        '''
        return self.level
    
    def changeOperator(self, operator):
        '''
        Changes the type of math expressions the instance generates. 
        Raises Value Error exception when the parameter is not a valid action
        '''
        if operator not in self.possibleOperators():
            raise ValueError("invalid action was selected")
        
        self.operator = operator
        
    def possibleOperators(self):
        '''
        Returns a list of possible math operations 
        '''
        return list(self.operations.keys())
        
    def generateQnA(self):
        '''
        Returns a tuple which holds a question as a string and the answer to it as integer 
        '''
        # get the tuple with the operator, the operands, and the result
        temp = self.operations[self.operator]()   
        a = temp[0]
        b = temp[1]
        currAct = temp[2]
        correctAns = temp[3]

        question = "How much is " + str(a) + str(currAct) + str(b) + " equal to?\n" 
        
        return (question, correctAns)
    
    # all of the for functions below pack the operator as part of the tuple in case they are being called from the random function   
    def add(self):
        '''
        Randomly generates numbers and returns a tuple of (operand a, operand b, operator('+', in this case), sum of first and second) 
        '''
        a = randint(0, self.level + self.startingNum)
        b = randint(0, self.level + self.startingNum)
        return (a, b, self.operator, a + b)

    def subtract(self):
        '''
        Randomly generates numbers and returns a tuple of (first num, second num, operator('-', in this case), difference between first and second).
        The second number is never bigger than the first 
        '''
        a = randint(0, self.level + self.startingNum)
        b = randint(0, a)
        return (a, b, self.operator, a - b)

    def multiply(self):
        '''
        Randomly generates numbers and returns a tuple of (first num, second num, operator('*', in this case), multiple of first and second).
        '''
        a = randint(0, self.level + self.startingNum)
        b = randint(0, self.level + self.startingNum)
        return (a, b, self.operator, a * b)

    def divide(self):
        '''
        Randomly generates numbers and returns a tuple of (first num, second num, operator('/', in this case), division of first and second).
        The second number is never zero and the division never has a remainder
        '''
        a = randint(1, self.level + self.startingNum)
        b = randint(1, a)
        
        # makes sure that the numbers will divide without a remainder 
        while (b > 1 and a % b != 0):  
            b -= 1
        
        return  (a, b, self.operator, int(a / b))
    
    def randomgen(self):
        '''
        Randomly chooses and returns the results of one of the arithmetic options in operations 
        '''
        # get only the arithmetic actions  
        aa = self.possibleOperators()[:-1]
        self.operator = self.choose(aa)
        
        # get the tuple
        result = self.operations[self.operator]()
        
        self.operator = 'r'  # set it back to random
        return result    

    def choose(self, args):
        '''
        Takes a list of elements and randomly returns one of the list's elements
        '''
        maxi = len(args) - 1
        randindex = randint(0, maxi)
        return args[randindex]
   
