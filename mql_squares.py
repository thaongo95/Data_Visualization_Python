import matplotlib.pyplot as plt


x_values = range(100)
y_values = [x**2 for x in x_values]

# ~ plt.plot(x_value, squares, linewidth=7)
plt.figure(dpi=128, figsize=(10,6))
plt.scatter(x_values,y_values, edgecolor='none', c=y_values, cmap=plt.cm.Reds, s=2)
plt.title("value", fontsize=24)
plt.axis([0, 100, 0, 10000])
plt.xlabel("Xvalue", fontsize=14)
plt.ylabel("Yvalue", fontsize=14)
plt.gca().get_xaxis().set_visible(False)

plt.axis('off')
#plt.gca().get_yaxis().set_visible(False)
# ~ plt.savefig("scatter_plot.png", bbox_inches = 'tight')
plt.show()
