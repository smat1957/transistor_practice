import matplotlib.pyplot as plt

# default : figsize=(6.4, 4.8) 
fig = plt.figure( figsize=(8.0, 6.0) )
ax = fig.add_subplot()

ymax = 10
decade = 5
for n in range(decade):
    for x in range(1*pow(10, n), 10*pow(10, n)+10*n, pow(10,n)):
        if x==pow(10,n) or x==10*pow(10, decade-1):
            clr = "0.5"
            lnwdt = "0.8"
            lnstyl = "solid"
        else:
            clr = "0.2"
            lnwdt = "0.5"
            lnstyl = (0, (1, 3))
        ax.plot( [x,x], [0,10], color=clr, linewidth=lnwdt, linestyle=lnstyl )
for y in range(0, ymax + 1):
    if y==0 or y==ymax:
        clr = "0.2"
        lnwdt = "0.5"
        lnstyl = "solid"
    else:
        clr = "0.2"
        lnwdt = "0.5"
        lnstyl = "dotted"
    ax.plot( [1, pow(10, decade)], [y, y], color=clr, linewidth=lnwdt, linestyle=lnstyl )
ax.set_xscale('log')

plt.axis("off")
plt.show()
# default : dpi=100
plt.savefig('logscale.png', dpi=600)
