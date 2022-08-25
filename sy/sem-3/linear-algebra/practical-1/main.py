import matplotlib.pyplot as plt
a = 1 + 2j
b = 3 + 4j

print("Addition of two complex numbers : ", a + b )
print(f"The conjugate of a = {a} is {a.conjugate()}")


complex_numbers = [1 + 2j, 3 + 4j, 4 + 7j, 8 + 9j]
X = [x.real for x in complex_numbers]
Y = [x.imag for x in complex_numbers]
plt.scatter(X, Y, color = "blue")
plt.show()



