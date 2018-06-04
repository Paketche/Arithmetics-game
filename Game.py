'''
Created on Dec 9, 2017

@author: Georgi Valchanov
'''
from Question import QuestionGenerator
import sys 
from builtins import str


class Game(object):
    '''
    classdocs
    '''
    menu = None
    menuOptions = list(range(0, 6))
    
    maxLevel = 7
    minLevel = 1
    # mistakes or correct answers to change level
    tochangeLVL = 3
    
    mistakes = 0
    correct = 0
    
    questionGenerator = None

    def __init__(self):
        '''
        Constructor.
        Creates a new game
        '''
        self.menu = "Select one of the following options:\n\n (1) Addition (2) Subtraction (3) Multiplication (4) Division (5) Random sums (6) Quit\n"
        self.questionGenerator = QuestionGenerator(1, 3)
        
    def startGame(self):
        '''
        Starts the game by asking the user what kind of math expressions do they want
        '''  
        self.mistakes = 0
        self.correct = 0
        
        selected = self.promtUser(self.menu, self.menuOptions)-1 
                      
                
        if selected in self.menuOptions[:-1]:  # if it is quit
            self.questionGenerator.changeOperator(self.questionGenerator.possibleOperators()[selected])
        else:
            sys.exit("Good bye")
    
    def askQuestions(self):
        '''
        Continues to ask the user questions until they get a question wrong and decide to quit
        '''
        while True:
            # get a question and its corrAns
            qna = self.questionGenerator.generateQnA()
            question = qna[0]
            corrAns = qna[1]

            # get user corrAns
            userAnswer = self.promtUser(question, list(range(0, 101)))
                    
            # actions for when the corrAns's correct or incorrect        
            if userAnswer == corrAns:
                print("Correct Answer")
                self.mistakes = 0
                self.correct += 1     
            else:
                print("Wrong. The correct answer is " + str(corrAns))
                self.correct = 0
                self.mistakes += 1
                # ask if the user wants to continue
                resp = self.promtUser("Press Y to try another sum or N to stop.\n", ["Y", "N"])
                if(resp == "N"): break
            
            # increase level if needed
            if(self.questionGenerator.getLevel() < self.maxLevel and self.correct == self.tochangeLVL):
                self.correct = 0
                print("Level up\n")
                self.questionGenerator.increaseLevel()
            # decrease level if needed        
            elif(self.questionGenerator.getLevel() > self.minLevel and self.mistakes == self.tochangeLVL):     
                self.mistakes = 0
                print("Level down")
                self.questionGenerator.decreaseLevel()
         
    def promtUser(self, question, rang):
        '''
        Takes a question as a string and a list of valid answers and prompts the user to answer the question
        until the answer is valid
        '''
        while True:
            try:
                answer = input(question)
                
                # cast the input appropriately
                # (user is mostly expected to answer with strings and numbers in this program,
                # it could be said that this is a bit hard coded)   
                if(type(rang[0]) is str):
                    answer = str(answer).upper()
                else:
                    answer = int(answer)
                
                if answer in rang:
                    return answer
               
                print ("Your answers is not in the range of options\n")
            except ValueError:
                print("your answer is not valid\n")    
    
