from graphics import *
from function_Snake_Game import *
width = 700
height = 500
win = GraphWin('GRAPH', width, height, autoflush=False)
win.setBackground('white')

temp = [205.547999859, 5.27900075912, 105.158000469, 405.22399807,
        205.572999239, 405.471998692, 205.779999971, 305.569999933,
        205.60000062, 405.668000937, 205.395000935, 205.732999802,
        205.397001743, 404.999000549, 205.406001091, 405.308999538,
        205.457999468, 104.989000082, 315.69500041, 505.931000948,
        605.488999605, 205.281000137, 305.307999849, 115.565000057,
        315.754998446, 205.255000353, 405.341000557, 105.484002113,
        305.631999493, 5.65999937057, 105.81200099, 205.392998934,
        405.364997864, 105.590000629, 6.023001194, 215.396999598,
        305.486000299, 115.235999584, 415.629002333, 315.422999382,
        5.50700139999, 505.541002274, 205.620998383, 105.4670012,
        205.511000395, 305.595000505, 5.64000034332, 205.720000744,
        105.29300046, 5.60800051689, 105.530000448]

nb_max = max(temp)
width_ratio = (width*9)/(len(temp)*10)
height_ratio = (nb_max*9)/(height*10)


for i in range(len(temp)-1):
    # temp2.append([i*5,500-temp[i]/2])
    a = Rectangle(Point(i*width_ratio, temp[i]*height_ratio),
                  Point(i*width_ratio+5, temp[i]*height_ratio+5))
    a.setFill('black')
    a.draw(win)

# drawing_pixel(temp2, 'black', 1, win)

win.getMouse()
