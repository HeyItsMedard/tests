import matplotlib.pyplot as plt


fig, ax = plt.subplots(2,2)
ax1, ax2, ax3, ax4 = ax.flatten()
ax1.barh([0, 1], [2, 2])
ax2.bar([0, 1], [2, 2])
ax3.plot([0, 1], [2, 2])
ax4.scatter([0, 1], [2, 2])

fig.savefig('demo.png')
# plt.show()
