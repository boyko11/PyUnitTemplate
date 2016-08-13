class Calculator:
    id = 1

    def __init__(self):
        print 'Calculator __init__ : {0}'.format(self.id)

    def power(self, base, degree):
        print 'Calculator id: {0}, power method invoked with base: {1} and degree: {2}'\
            .format(self.id, base,degree)
        return base ** degree
