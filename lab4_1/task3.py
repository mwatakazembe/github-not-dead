import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(10, 10))

body = patches.Ellipse(xy = (0.5,0.5), width=0.4, height=0.6, facecolor='#1b6e18', edgecolor='black')
leg1 = patches.Ellipse(xy = (0.405,0.65), width=0.1, height=0.3, angle=45, facecolor='#b3f542', edgecolor='black')
leg2 = patches.Ellipse(xy = (0.605,0.65), width=0.1, height=0.3, angle=135, facecolor='#b3f542', edgecolor='black')
leg3 = patches.Ellipse(xy = (0.605,0.35), width=0.1, height=0.3, angle=45, facecolor='#b3f542', edgecolor='black')
leg4 = patches.Ellipse(xy = (0.405,0.35), width=0.1, height=0.3, angle=135, facecolor='#b3f542', edgecolor='black')
head = patches.Ellipse(xy = (0.5,0.57), width=0.17, height=0.6, facecolor='#b3f542', edgecolor='black')
eye1 = patches.Circle((0.4565, 0.83), radius=0.009, facecolor='black')
eye2 = patches.Circle((0.5424, 0.83), radius=0.009, facecolor='black')
tail = patches.Polygon([(0.5, 0.16), (0.49, 0.2), (0.51, 0.2)], closed=True, facecolor='#b3f542', edgecolor='black')

ax.add_patch(leg1)
ax.add_patch(leg2)
ax.add_patch(leg3)
ax.add_patch(leg4)
ax.add_patch(head)
ax.add_patch(body)
ax.add_patch(tail)
ax.add_patch(eye1)
ax.add_patch(eye2)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
plt.axis('off')
plt.show()