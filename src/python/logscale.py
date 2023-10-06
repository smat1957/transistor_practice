import matplotlib.pyplot as plt

# default : figsize=(6.4, 4.8) 
fig = plt.figure( figsize=(8.0, 6.0) )
ax = fig.add_subplot()

ymax = 10
decade = 5
for n in range(decade):
    for x in range(1*pow(10, n), 10*pow(10, n)+10*n, pow(10,n)):
        if x==pow(10,n) or x==10*pow(10, decade-1):
            ax.plot( [x,x], [0,10], color="0.5", linewidth="0.8", linestyle="solid" )
        else:
            ax.plot( [x,x], [0,10], color="0.2", linewidth="0.5", linestyle=(0, (1, 3)) )
for y in range(0, ymax + 1):
    if y==0 or y==ymax:
        ax.plot( [1, pow(10, decade)], [y, y], color="0.2", linewidth="0.5", linestyle="solid" )
    else:
        ax.plot( [1, pow(10, decade)], [y, y], color="0.2", linewidth="0.5", linestyle="dotted" )
ax.set_xscale('log')

plt.axis("off")
plt.show()
# default : dpi=100
plt.savefig('logscale.png', dpi=600)
