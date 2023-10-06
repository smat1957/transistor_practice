import matplotlib.pyplot as plt

# default : figsize=(6.4, 4.8) 
fig = plt.figure( figsize=(8.0, 6.0) )
ax = fig.add_subplot()

ymax = 10
decade = 5
for n in range(decade):
    for x in range(1*pow(10, n), 10*pow(10, n)+10*n, pow(10,n)):
        ax.plot( [x,x], [0,10], color="0.5", linewidth="1" )
for y in range(0, ymax + 1):
    ax.plot( [1, pow(10, decade)], [y, y], color="0.5", linewidth="1" )
ax.set_xscale('log')

plt.axis("off")
plt.show()
# default : dpi=100
plt.savefig('logscale.png', dpi=600)
