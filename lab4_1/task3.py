import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(8, 6))

body = patches.Polygon([(0.3, 0.5), (0.7, 0.7), (0.7, 0.3)], closed=True, facecolor='blue', edgecolor='black')
tail = patches.Polygon([(0.7, 0.5), (0.9, 0.6), (0.9, 0.4)], closed=True, facecolor='orange', edgecolor='black')
eye = patches.Circle((0.45, 0.6), radius=0.03, facecolor='white', edgecolor='black')
pupil = patches.Circle((0.45, 0.6), radius=0.01, facecolor='black')

ax.add_patch(body)
ax.add_patch(tail)
ax.add_patch(eye)
ax.add_patch(pupil)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
plt.axis('off')
plt.show()