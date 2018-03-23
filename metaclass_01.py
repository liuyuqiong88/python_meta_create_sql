class A(object):
    # @staticmethod
    def test(self):
        print("class A")

# a = A()

# @staticmethod
# def test():
#     print("hahah")

B = type("B",(object,),{ "test": A.test })
help(B)
print(B.__dict__)
b = B()
b.test()

class C(type):
    def __new__(cls, *args, **kwargs):
        return type.__new__(cls,classname,)
