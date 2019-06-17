"""
Name: Gilbert Adu
Date: 8th June 2019
"""


"""
An instance of this class is monitoring the data of a single rhino


Parameter n: This is the name of the rhino
Precondition: name is a string

Parameter y: This represents the year in which the particular rhino was born
Precondition: year is an int

Parameter month: This is the month in which the rhino was born
Precondition: month is an int

Parameter g: This is the sex of the rhino
Precondition: gender is either M or F

Parameter m: This is the mother of this rhino
Precondition: mother is a rhino object

Parameter f: This is the father of this rhino
Precondition: father is a rhino object

Parameter c: This is the number of offspring this rhino has
Precondition: children is an int

Parameter t: This is the tag of a particular rhino in the park
Precondition: tag is an int
"""

class Rhino():




    def __init__(self,n,y,month,g,m="",f="",c=None,t=None):

        self.name=n
        self.year=y
        self.month=month
        self.gender=g

        self.mother=m
        self.father=f
        self.children=c
        self.tag= t

    def getName(self):
        return self.name

    def getYear(self):
        return self.year

    def getMonth(self):
        return self.month

    def isMale(self):
        if (self.gender=="M"):
            return True
        else:
            return False

    def getTag(self):
        return self.tag

    def getMother(self):
        return self.mother

    def getFather(self):
        return self.father

    def getNumChildren(self):
        return self.children

    def setTag(self,value):
        self.tag=value

    def addMother(self,mom):
        self.mother=mom

    def addFather(self,dad):
        self.father=dad

    def addNumChildren(self,num):
        self.children= num


    def toString(self):

        print('Name: '+self.name,'D.O.B: '+str(self.month)+'/'+str(self.year),'Sex: '+self.gender,'Tag No.: '+str(self.tag),'NumberOfChildren: '+str(self.children),sep="\n")
        print('Mother: '+self.mother.name, 'Father: '+self.father.name,sep="\n")



def Compare(first,second):

    if first.getYear() > second.getYear():
        print(first.name+' is older than '+second.name)

    elif first.getYear()== second.getYear():
        if first.getMonth() > second.getMonth():
            print(second.name+' is older than '+first.name)
        elif (first.getMonth()== second.getMonth()):

            print(first.name+' and '+second.name+' are the same age')

        else:
            print(first.name+ ' is older than '+ second.name)


    else:
        print(second.name + ' is older than '+first.name)
