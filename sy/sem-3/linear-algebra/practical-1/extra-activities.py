import matplotlib.pyplot as plt
print("(1+3j) + (10+20j) = ", (1+3j) + (10+20j) )



x = 1 + 3j
print("(x - 1)**2 = ", (x - 1)**2)
print("1+2j*3 = ", (1+2j)*3 )
print("4*3j**2 = ", 4*3j**2)
x = 1+3j
print(f"For x = {x} the real part is {x.real} and the imaginary part is {x.imag} and conjugate is {x.conjugate()}")

S = [3+3j, 4+3j, 2+1j, 2.5+1j, 3+1j, 3.25+1j]
X = [x.real for x in S]
Y = [x.imag for x in S]
plt.scatter(X, Y, color = "green")
plt.show()

