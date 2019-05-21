

import matplotlib.pyplot as plt

# The slices will be ordered and plotted counter-clockwise.
labels = [r'Pass', r'Fail', r'Skip']
sizes = [200, 10, 1]
colors = ['yellowgreen', 'red' , 'blue']
explode=(0, 0.05, 0,)
fig = plt.figure()
patches, texts = plt.pie(sizes, explode=explode ,autopct=None, shadow=True, colors=colors, startangle=90)
plt.suptitle('Test Scenarios')

plt.legend(patches, labels, loc="center right")
fig.set_figheight(2)
fig.set_figwidth(4)

# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')
plt.tight_layout()
plt.show()