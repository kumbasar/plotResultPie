

import matplotlib.pyplot as plt

# The slices will be ordered and plotted counter-clockwise.
labels = [r'Pass', r'Fail', r'Skip']
sizes = [200, 10, 1]
colors = ['yellowgreen', 'red' , 'blue']
fig = plt.figure()
patches, texts = plt.pie(sizes, colors=colors, startangle=90)
plt.suptitle('Scenarios')

plt.legend(patches, labels, loc="right")
fig.set_figheight(2)
fig.set_figwidth(4)

# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')
plt.tight_layout()
plt.show()