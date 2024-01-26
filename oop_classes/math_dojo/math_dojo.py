class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        for number in nums:
            self.result += number
        self.result += num
        return self
    def subtract(self, num, *nums):
        for number in nums:
            self.result -= number
        self.result -= num
        return self
    def multiply(self, num, *nums):
        if(self.result==0):
            self.result = 1
        for number in nums:
            self.result *= number
        self.result *= num
        return self
    def divide(self, num, *nums):
        if num == 0:
            return self
        for number in nums:
            if number == 0:
                continue
            self.result /= number
        self.result /= num
        return self    
md = MathDojo()
# to test:
x = md.divide(0).result
x = md.divide(2).result
x = md.add(2).add(2,5,3,2).result
x = md.subtract(2).subtract(2,5,3,2).result
x = md.multiply(2).multiply(2,5,3,2).result
x = md.multiply(0).multiply(2,5,3,2).result
x = md.divide(2).divide(2,0,3,0).result
x = md.divide(0).divide(0,0,3,0).result
x = md.add(2).add(2,5,1).subtract(3,2).result
x = md.subtract(10).result
x = md.divide(0).result
x = md.multiply(0).result
print(f"Results: {x}")	# should print 5
# run each of the methods a few more times and check the result!