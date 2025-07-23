import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7]
y=[25,30,32,36,40,45,47]
plt.plot(x,y,marker='o',linestyle='-',color='r')
plt.title("temperature of the week")
plt.xlabel("days of the week")
plt.ylabel("degrees in celsius")
plt.show()