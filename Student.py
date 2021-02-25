# The Student class (you'll edit and expand on this)
class Student():
    
    '''
    This class is designed to include information about individual students.
    Currently this class has the following attributes:
    
    name : this is the student's name
    gpa : this is the student's curret gpa
    '''
    
    def __init__(self, name='', gpa=0.0, years = 0, courses = []):
        self.name = name
        self.gpa = gpa
        self.years = years
        self.courses = courses
        
    def get_name(self):
        '''
        This function prints the name of the student
        '''
        print("My name is", self.name)
        
    def get_gpa(self):
        '''
        This function prints the gpa of the student
        '''
        print("My gpa is", self.gpa)
        
    def get_year(self):
        
        
        '''
        This function prints the year of the student
        '''
        print("My year is", self.year)   
        
    def enroll(self, courses):
        
        '''
        This class is designed takes as input a list of courses and adds 
        them as an attribute to the student
        '''
        self.courses = courses


        
    def display_courses(self):
        print('I am enrolled in', self.courses)
              
              
        
        
       
           
    def years_till_graduation(self):
        print('I will graduate in', self.years, 'years')
     
 
    
      
              
              
class Spartan(Student):
    
    def set_motto(self,motto):
        self.motto = motto
        
     
    def school_spirit(self):
        print('My name is', self.get_name, ' I am a spartan. My motto is:', self.motto)
      

        
