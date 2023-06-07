import matplotlib.pyplot as plt

path = 'graph_plotter'

x1 = [2,4,5]
y1 = [2,3,6]

plt.plot(x1,y1, color='green', linestyle='dashed', linewidth=5, marker='o ', markerfacecolor='red', markersize=15, label = 'Line 1')

x2 = [5,2,3]
y2 = [4,1,4]

plt.plot(x2,y2, label = 'Line 2')

plt.xlabel('X axis')
plt.ylabel('Y axis')

plt.title('Demo Graph')
plt.legend()

plt.savefig(path + '/the_graph.png')