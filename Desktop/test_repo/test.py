import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 60, 1000) # start, finish, n points
d_r = 1 * t
d_s = 4 * (t-30)
fig, ax = plt.subplots()
plt.title('Power production')
plt.xlabel('time (in days)')
plt.ylabel('power (in kj)')
ax.set_xlim([0, 60])
ax.set_ylim([0, 100])
ax.plot(t, d_r, c='green')
ax.plot(t, d_s, c='brown')
plt.axvline(x=40, color='purple', linestyle='--')
_ = plt.axhline(y=40, color='purple', linestyle='--')
plt.show()