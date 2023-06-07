import matplotlib.pyplot as plt

path = 'graph_plotter'

x = [1,2,3,4]
y = [10,11,12,4]

tick_label = ['one', 'two', 'three','four']

plt.bar(x, y, tick_label = tick_label, width = 0.8,color = ['yellow', 'black'])

plt.xlabel('X axis')
plt.ylabel('Y axis')

plt.title('Demo Graph Bar chart')
plt.legend()

plt.savefig(path + '/the_bar_graph.png')