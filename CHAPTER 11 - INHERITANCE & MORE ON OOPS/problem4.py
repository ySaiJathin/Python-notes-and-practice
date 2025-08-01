#  Write a class ‘Complex’ to represent complex numbers, along with overloaded 
# operators ‘+’ and ‘*’ which adds and multiplies them.

# class complex:
#     def __init__(self,number):
#         self.number=number


#     def __add__(self,num):
#         return self.number+num.number

#     def __mul__(self,num):
#         return self.number*num.number
    

# c=complex
# n1=c.number
# n2=c.number

# print(n1+n2)
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return Complex(real_part, imag_part)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

# Example usage
c1 = Complex(3, 2)
c2 = Complex(1, 7)

sum_result = c1 + c2
product_result = c1 * c2

print("Sum:", sum_result)
print("Product:", product_result)