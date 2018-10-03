# PLOTTING CHEAT SHEET
by Simon Schmid. Work in progress, without any guarantees

# SETUP
**`%matplotlib inline`**                                *- use command to display plots in notebooks*

**`import matplotlib.pyplot as plt`**                   *- to use everything with plt.*

**`import matplotlib.ticker as ticker`**

**`import matplotlib.dates as dates`**

**`matplotlib.rcParams['pdf.fonttype'] = 42`**          *- to export in type2 fonts not type3*

# PANDAS BUILT-IN FUNCTION
**`df.plot()`**                                         *- default: a line chart* ([reference](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&ved=2ahUKEwiwmsquzOrdAhVFiywKHXp1C6sQFjAAegQICRAB&url=https%3A%2F%2Fpandas.pydata.org%2Fpandas-docs%2Fstable%2Fgenerated%2Fpandas.DataFrame.plot.html&usg=AOvVaw1IwZzuSZC6J1kHBeNKYUhP))
-    `linewidth=n`                                      *- width of line in linechart*

`kind="bar"`                                            *- vertical bar chart*
-    `stacked=True/False`                               *- for stacked bar charts*
-    `x="field1", y="field2"`                           *- specify series to use for x and y explicitly*

`kind="barh"`                                           *- horizontal bar chart*
-    `stacked=True/False`                               *- for stacked bar charts*
-    `x="field1", y="field2"`                           *- specify series to use for x and y explicitly*

`kind="scatter"`                                        *- scatterplot*
-    `s=number`                                         *- size of the dots in a scatterplot (can be a list)*
-    `x="field1", y="field2"`                           *- specify series to use for x and y explicitly*
-    `alpha=number`                                     *- alphavalue (transparency)*
-    `s=number`                                         *- size of scatter-dots, can be a list*
-    `ylim=(val1, val2)`                                *- set min and max of y-axis*

## Format Options                                        
-    `figsize=(valx, valy)`                             *- define size of the graph*
-    `title="title"`                                    *- the title*
-    `legend="True/False"`                              *- display a legend*
-    `label="labellist"`
-    `color="color/colorlist"`                          *- set color of line/bar, can be a list*

## WHERE TO PLOT                                        
-    `ax=otherplot`                                     *- Plot on some existing chart ("otherplot")*

## Histograms
**`df["field1"].hist()`**                           *- returns a graphical histogram*
-    `bins=n`                                       *- change number of bins to n*
-    `bins=[n1, n2, n3, ...]`                       *- set specific ranges*

# MATPLOTLIB PLOTTING
fig, ax = plt.subplots()                #create separate handles for the figure and axis

df.plot(ax=ax)                          #add a plot to the figure and axis specified
ax.plot()                               #other way to add a plot to the figure and axis
ax.scatter()
ax.pie()
ax.bar()
ax.barh()
ax.hlines()
...                                     #overwiew: https://matplotlib.org/2.0.2/api/axes_api.html

# MULTIPLE SUBPLOTS
fig = plt.figure()                      #create the figure seperately
ax = fig.add_subplot(vpos, hpos, n)     #add an axis to the figure, at the nth position in a (v*h) grid


#FORMATTING THE PLOT - MAIN SETUP
fig.set_size_inches(x, y)               #Set the sizes

.set_title("Title")                     #Set the title
    fontsize=number
.spines['right'].set_visible(True/False) #display borders around canvas
        'left'
        'top'
        'bottom'
.set_xlim([min, max])                   #set range on the x-Axis
.set_ylim([min, max])                   #Set range on the y-Axis

#FORMATTING THE AXES - LABELS
.axis('off')                            #remove the axes completely
.set_xlabel("Label")                    #Set label of horizontal axis
    fontsize=number
.set_ylabel("Label")                    #Set label of vertical axis
    fontsize=number
.xaxis.set_ticks_position('top')        #position of ticks
                          'bottom'
                          'none'


#FORMATTING THE AXES - TICKS
.xaxis.set_ticks(listofticks)

.xaxis.set_major_locator()              #efine ticks frequency in a time plot
    dates.YearLocator()
    dates.MonthLocator()

.xaxis.set_major_formatter()            #define the date format of the ticks in a time plot
    dates.DateFormatter('format')
    ticker.FormatStrFormatter('%0.1f')

fig.autofmt_xdate()                     #auto-rotate labels

.axes.set_xticklabels()                 #define and format the tick labels (non-time graph)
    fontsize=n
    rotation=n

#FORMATTING THE LEGEND
ax.legend(True)                         #Complete list of options:
    fontsize=number                     #https://matplotlib.org/2.0.2/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend
    loc=n                               #0=best, 1=up,right, 2=up,left, ...

#FORMATTING THE GRID
.grid(True)                             #Turn on all grid
.grid(axis='y')                         #Turn on grid on y-axis only

#FORMATTING THE BACKGROUND
ax.set_facecolor("color")               #

#SPECIAL FEATURES
ax.fill_between(x_values, y_mins, y_maxes) #Fill the area between y_mins and y_maxes

#EXPORT
import matplotlib
matplotlib.rcParams['pdf.fonttype'] = 42 #important for the fonts

plt.tight_layout()                       #make sure the layout has no overlap in export

plt.savefig("file.pdf")                  #export to pdf
    transparent=True

plt.savefig("file.svg")                  #export to pdf
    transparent=True/False               #Transparency
    bbox_inches=n/'tight'                #define the box
    pad_inches=n                         #padding around the figure
