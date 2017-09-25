class A(object):
    def _internal_use(self):
        print("personal mod")
    def __meth(self):
        pass
print(dir(A()))

class B(A):
    def __meth(self):
        pass

b = B()


print(dir(B()))