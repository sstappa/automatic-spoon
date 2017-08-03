import os.path

# Get the directory name for data files

directory = os.path.dirname(os.path.abspath(__file__))  
print directory

name1='Arizona'
name2='California'

#initialize the aggregators
years1=[]
number_of_fat_people1=[]
years2=[]
number_of_fat_people2=[]

filename = os.path.join(directory+str("\\")+str("obesity_v2.csv"))
print filename


# Scan one year's file at a time
for year in range(0,1):
    # Open the file
    filename = os.path.join(directory+str("\\")+str("obesity_v2.csv"))
    print filename
    datafile = open(filename,'r')
    # Go through all the names that year
    for line in datafile:
        year, state, number = line.split(',')
        # Aggregate based on name1
        if state == name1: #and year == '2011':
            print "arizona"
            years1.append(year)
            print years1
            number_of_fat_people1 += [number]   
            print number_of_fat_people1
        #Aggregate based on name2
        if state == name2:
            years2.append(year)
            number_of_fat_people2 += [number]        
    #Close that year's file
    datafile.close()

import matplotlib.pyplot as plt
'''
pie_graph = matplotlib.pyplot.pie(number_of_fat_people1, explode=None, labels=(years1[0]+","+number_of_fat_people1[0],years1[1]+","+number_of_fat_people1[1],years1[2]+","+number_of_fat_people1[2],years1[3]+","+number_of_fat_people1[3],years1[4]+","+number_of_fat_people1[4]), colors=('b', 'g','r','m', 'k'),
    autopct=None, pctdistance=0.6, shadow=False,
    labeldistance=1.1, startangle=None, radius=None)     
pie_graph2 = matplotlib.pyplot.pie(number_of_fat_people2, explode=None, labels=(years2[0]+","+number_of_fat_people2[0],years2[1]+","+number_of_fat_people2[1],years2[2]+","+number_of_fat_people2[2],years2[3]+","+number_of_fat_people2[3],years2[4]+","+number_of_fat_people2[4]), colors=('b', 'g','r','m', 'k'),
    autopct=None, pctdistance=0.6, shadow=False,
    labeldistance=1.1, startangle=None, radius=None)      
print "i got here"'''

quantities1 = number_of_fat_people1 
quantities2 = number_of_fat_people2 
labels = years1 
colors = ['pink', 'red','green','blue','brown', 'yellow']
autopct = '%.0f%%'
fig, ax = plt.subplots(1,2)
ax[0].pie(quantities1,labels=labels,colors=colors,autopct='%.0f%%')
ax[1].pie(quantities2,labels=labels,colors=colors,autopct='%.0f%%')
ax[0].set_aspect(1)
ax[1].set_aspect(1)
ax[0].set_title('# of fat people in '+name1)
ax[1].set_title('# of fat people in '+name2)
fig.show()

#pie_graph = matplotlib.pyplot.subplots()
#ax.set_title('Simple plot')
#pie_graph, pie_graph2 = matplotlib.pyplot.subplots(1,2)
#matplotlib.pyplot.show(pie_graph)
#matplotlib.pyplot.show(pie_graph2)
#matplotlib.pyplot.imshow()            
#this code will do a line graph only    
# Plot on one set of axes.
'''import matplotlib.pyplot as plt
fig, ax = plt.subplots(1,1)
ax.plot(years1,number_of_fat_people1,'#0000FF')
ax.plot(years2,number_of_fat_people2,'#FF00FF')

ax.set_title('Total fat people in ' +
             name1 + ' (blue) or ' + name2 + ' (pink)')
fig.show()'''