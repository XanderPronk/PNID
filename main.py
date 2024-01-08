class Test_class:  
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def get_sum(self):
        return self.a + self.b
    def get_difference(self):
        return self.a - self.b
    def get_product(self):
        return self.a * self.b
    def get_quotient(self):
        return self.a / self.b
    def test_fun(self):
        return True


if __name__ == "__main__":
    print("test")
    while True:
        a = str(input())
        print(a)


