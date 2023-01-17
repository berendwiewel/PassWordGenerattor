# Python Code Generator
import random, os, sys
class Code:
    '''
    This class provides a randomized password generator.
    '''
    
    def __init__(self, number_lower_case : int = int(input('Please give the number of lower case strings you want in your password: '))
                 , number_upper_case: int = int(input('Please give the number of upper case strings you want in your password: '))
                 , number_signs:int=int(input('Please give the number of symbols you want in your password: '))):
        
        self.number_lower_case = number_lower_case
        self.number_upper_case = number_upper_case
        self.number_signs = number_signs
        self.word = ''
        
    def restart(self):
        '''
        The restart method restarts the program again.
        This is used when the amount of letters for the password is lower then 10
        '''
        os.execl(sys.executable, sys.executable, *sys.argv)
        
    def counting(self):
        '''
        The counting method returns the sum of the input values
        '''
        return self.number_lower_case + self.number_signs + self.number_upper_case
    
    def shuffle(self, word : str):
        '''
        The shuffle method returns the shuffled version of the generated password. 
        Param word: the input variable is the word you want to shuffle
        '''
        word = list(word)
        random.shuffle(word)
        new_password = ''.join(word)
        return new_password
    
    def checking_symbols(self):
        '''
        This method replaces symbols that are deemed unwanted
        '''
        nonosigns =':;,"`\''
        for x in self.word:
                if x in nonosigns:
                    self.word = self.word.replace(x,chr(random.randrange(48,58))) 
                    
    def adding_character_to_password(self):
        '''
        This method adds a character to the password depending on the amount given at the question phase. 
        '''
        if self.number_lower_case > 0:
            self.word += chr(random.randrange(97,123))
            self.number_lower_case -= 1
        elif self.number_upper_case >0:
            self.word += chr(random.randrange(65,90))
            self.number_upper_case -= 1
        else:
            self.word += chr(random.randrange(33,65))
            self.number_signs -=1
        
    def generator(self):
        '''
        This method generates the password by running all previously created methods. 
        '''
        if self.counting() <= 9:
            print('Please fill in the minimum required amount of 10')
            self.restart()
        else:
            while 0 < self.counting():
                self.adding_character_to_password()
            self.checking_symbols()
            print(f'Your new password is : {self.shuffle(self.word)}')
        
codee = Code()
codee.generator()