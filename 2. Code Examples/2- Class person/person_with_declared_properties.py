class Person:
    '''
    The Person class is an abstract representation of a person.
    It has 3 instance variables:
    _name - String - name of person
    _job - String - job person does
    _pay - Integer - salaray of person

    This class uses declared properties to simplify syntax for
    accessing instance variables.
    '''
    def __init__(self, name, job, pay):
        '''
        Constructor for class
        '''
        self._name = name
        self._job = job
        self._pay = pay

    def getName(self):
        '''
        Getter for _name attribute
        '''
        return self._name

    def setName(self, name):
        '''
        Setter for _name attribute
        '''
        self._name = name

    def setJob(self, job):
        '''
        Setter for _job attribute
        '''
        self._job = job

    def getJob(self):
        '''
        Getter for _job attribute
        '''
        return self._job

    def getPay(self):
        '''
        Getter for _pay attribute
        '''
        return self._pay

    def setPay(self, pay):
        '''
        Setter for _pay attribute
        '''
        self._pay = pay

    def givePayRaise(self, percentage):
        '''
        Method to give payraise to instance of class.
        Adds percentage of salary to _pay attribute
        percentage - Integer - between 1 and 99
        '''
        if percentage < 0 or percentage > 100:
            print("%i is an illegal value" % (percentage))
        else:
            self._pay += self._pay // 100 * percentage

    def __str__(self):
        '''
        Method to give string represenation of this instance
        '''
        return ("%s %s %d" % (self._name, self._job, self._pay))

    #Declare properties for our attributes
    name = property(getName, setName)
    job = property(getJob, setJob)
    pay = property(getPay, setPay)

#Very simple test block for our class. Instantiates an instance
#gives a pay raise, exercises properties and prints results.
cathal = Person('Cathal', 'dev', 70000)
cathal.givePayRaise(10)
print(cathal.pay)
cathal.pay = 100000
print(cathal.pay)

cathal.name = "Cathal H"
print(cathal.name)
cathal.job = "Developer"
print(cathal.job)
print(cathal)