import numpy as np
import matplotlib.pyplot as plt

#Method 1: compare with two lines of different gradients
fig, (ax1, ax2) = plt.subplots(1,2, sharex='all', sharey='all')
ax1.set(xlim=(0, 6), ylim=(0, 6))
fig.set_figwidth(15)

#line A
xlabels = np.linspace(1,10,10)
ylabels = np.linspace(1,8,10)
ax1.plot(xlabels,ylabels, color='blue')
ax1.text(3,3,'line A')

#line B (green)
Bxlabels = np.linspace(1,15,10)
Bylabels = np.linspace(1,8,10)
ax2.text(3,3,'line B')
ax2.plot(Bxlabels,Bylabels, color='green')

#line C (red)
Cxlabels = np.linspace(1,25,10)
Cylabels = np.linspace(0.5,8,10)
ax1.plot(Cxlabels, Cylabels, color='red')
ax1.text(3,0.8,'line C')
ax2.plot(Cxlabels, Cylabels, color='red')
ax2.text(3,0.8,'line C')

#calculate the dot products
dotAC=np.dot(Cxlabels,xlabels)
dotBC=np.dot(Cxlabels,Bxlabels)

print(f"dotAC={dotAC}\ndotBC={dotBC}")

#Method 2: compare with two triangles
#Lets draw two triangles keeping lengths AB and XY to be the same (ie like same number of points in an array)
fig, (ax1, ax2) = plt.subplots(1,2, sharex='all', sharey='all')
ax1.set(xlim=(0, 6), ylim=(0, 6))
fig.set_figwidth(15)

#Triangle ABC
ax1.text(1,2,'B')
ax1.text(5,2,'C')
ax1.text(5,5,'A')
ax1.plot((1,5,5,1),(2,2,5,2))

#Triange XYZ
length_AB=5
#let's say angle XYZ is 20 degrees
coord_Z=(np.cos(np.pi/8)*length_AB)+1
coord_X=(np.sin(np.pi/8)*length_AB)+2
ax2.text(1,2,'Y')
ax2.text(coord_Z,2,'Z')
ax2.text(coord_Z,coord_X,'X')
ax2.plot((1,coord_Z,coord_Z,1),(2,2,coord_X,2))

plt.show

#lines BC and lines YZ are both parellel to each other.
#line XY is more parallel to the above than line AB, due to the smaller angle.
#Therefore cosine(angle ABC)<cosine(angle XYZ). This is the same as BC*AB < YZ*XY.
#let's calculate the dot products

rangeAB=np.arange(2,5,0.75)
len_rangeAB=len(rangeAB)
rangeBC=np.linspace(2,2,len_rangeAB)

rangeXY = np.arange(2,coord_X,np.tan(np.pi/8))
len_rangeXY=len(rangeXY)
rangeYZ = np.linspace(2,2,len_rangeXY)

dot_ABC = np.dot(rangeAB,rangeBC)
dot_XYZ = np.dot(rangeXY,rangeYZ)

print(f"AB*BC={dot_ABC}\nXY*YZ={dot_XYZ}")
print('''
    The lines that are more parallel to each other have higher dot product.
    It makes sense because:
    1. Cosine of an angle always between 0 to 1. Cosine(0)=1
    2. Hence, the product of a cosine value and the hypothenuse is always less than or equal to the hypothenuse.
    3. So when two lines are more parallel, x moves closer to 1, because as mentioned Cosine(0)=1, Cosine(90degrees)=0
    3. So dot product is higher when points are more parallel to each other.
''')