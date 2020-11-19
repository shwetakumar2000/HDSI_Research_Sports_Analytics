import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Rectangle, ConnectionPatch

def draw_court(ax):
    #Court 
    Court = Rectangle([0,0], width = 36, height = 78, fill = False)
    #Allies, Net
    LeftAlley = Rectangle([0,0], width = 4.5, height = 78, fill = False)
    RightAlley = Rectangle([31.5,0], width = 4.5, height = 78, fill = False)
    NetLine = ConnectionPatch([-2,39], [38,39], "data", "data")
    
    #Service Boxes
    LeftServeBox = Rectangle([4.5,18], width = 13.5, height = 42, fill = False)
    RightServeBox = Rectangle([18,18], width = 13.5, height = 42, fill = False)
    
    element = [Court, LeftAlley, RightAlley, LeftServeBox, RightServeBox, NetLine]
    for i in element:
        ax.add_patch(i)

fig=plt.figure() #set up the figures
fig.set_size_inches(3.5, 7)
ax=fig.add_subplot(1,1,1)
draw_court(ax) #overlay elements on court
plt.ylim(-2, 80)
plt.xlim(-4, 40)
#plt.axis('off')
plt.savefig('court.png')
plt.show()