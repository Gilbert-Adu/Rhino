"""
This is a test for rhino.py
"""
import rhino
import introcs

def testA():
    moses=rhino.Rhino("Moses",2000,3,"M")
    introcs.assert_equals(moses.getName(),'Moses')
    introcs.assert_equals(moses.getYear(),2000)
    introcs.assert_equals(moses.getMonth(),3)
    introcs.assert_equals(moses.isMale(),True)
    introcs.assert_equals(moses.getMother(),'')
    introcs.assert_equals(moses.getFather(),'')
    introcs.assert_equals(moses.getNumChildren(),None)


def testB():
    viola=rhino.Rhino("Viola",2001,2,"F")
    viola.setTag(1)
    introcs.assert_equals(viola.getTag(),1)
    viola.addMother("Elsie")
    introcs.assert_equals(viola.getMother(),'Elsie')
    viola.addFather("Gilbert")
    introcs.assert_equals(viola.getFather(),'Gilbert')



def testC():

    elsie= rhino.Rhino("Elsie",1999,9,"F")
    elsie.addNumChildren(1)
    gilbert= rhino.Rhino("Gilbert",1999,3,"M")
    gilbert.addNumChildren(1)

    jon=rhino.Rhino("Jon",1999,11,"M")
    jon.addNumChildren(1)

    viola=rhino.Rhino("Viola",2001,2,"F")
    viola.setTag(1)
    viola.addMother(elsie)
    viola.addFather(gilbert)

    moses=rhino.Rhino("Moses",2000,3,"M")
    moses.setTag(4)
    moses.addMother(viola)
    moses.addFather(jon)
    moses.addNumChildren(3)

    "Remove hash tags to see effect of each commented line"
    #viola.toString()
    #moses.getMother().toString()

def testD():

    viola=rhino.Rhino("Viola",2001,2,"F")
    moses=rhino.Rhino("Moses",2000,3,"M")

    elsie= rhino.Rhino("Elsie",1999,9,"F")
    gilbert= rhino.Rhino("Gilbert",1999,3,"M")

    jon=rhino.Rhino("Jon",1999,11,"M")
    bronco= rhino.Rhino("Bronco",1999,11,"M")



    "Remove hash tags to see effect of each commented line"
    #rhino.Compare(viola,moses)
    #rhino.Compare(elsie,gilbert)
    #rhino.Compare(bronco,jon)




print("Module rhinotester passed all tests")
testA()
testB()
testC()
testD()
