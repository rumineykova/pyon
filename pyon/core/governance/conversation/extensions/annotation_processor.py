class AssertionParser(object):
    START_TOCKEN = '@{'
    END_TOCKEN = '}'
    DELIMITER = ':'

    def parse(self, assertion):
        assertion = str(assertion)
        assertion = assertion.replace(self.START_TOCKEN, '')
        assertion = assertion.replace(self.END_TOCKEN, '')
        k, v = assertion.split(self.DELIMITER)
        #mydict = dict((k.strip(), v.strip()) for k,v in
        #      (item.split(':') for item in assertion.split(',')))
        #for key, val in mydict.iteritems():
        #    print 'Items: %s, %s' %(key, val)
        return  {k.strip(): v.strip()}

class Assertion(object):
    def __init__(self, assertion_statement):
        self.statement = assertion_statement
    @classmethod
    def create(cls, assertion_statement):
        print 'In creating assertions', assertion_statement
        parser = AssertionParser()
        parsed_statement = parser.parse(assertion_statement)
        return parsed_statement
        
    def check(self, context):
        return True
        #print "Pass annotation@@@@@@@@@@@________________________________@@@@@@@@@@@@@@@@@@@@@@@@"
        #return eval(self.statement, context)
 

test = '@{s=="Hello"}'
context = {'x': 3, 'y':5, 's':"Hello"}
def main():
    print 'Ihu'
    assertion = Assertion.create(test)
    print assertion.statement
    p = assertion.check(context) 
    if p: print ' It Is True'
    else: print 'It Is False'
     
if __name__=="__main__":
    main()
     
