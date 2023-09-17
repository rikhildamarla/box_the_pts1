import numpy as np

#place holder for txt file reading
myArray = []

#read txt file
fo = open("in.txt", "r")
for line in fo:
    #adding all of the numbers in the txt file into the array
    for nbr in line.split():
        myArray.append(int(nbr))

#sets a placeholder for the array of the coordinates
coord_list = []

#the loop that makes the list of lists(coordinates)
for i in range(myArray[0]):
    x = []
    x.append(myArray[1])
    x.append(myArray[2])
    myArray.remove(myArray[1])
    myArray.remove(myArray[1])
    coord_list.append(x)

coord_list = np.array(coord_list)
#print(coord_list)


group = []

for i in coord_list:
    for j in coord_list:
        group.append([tuple(i), tuple(j), (np.linalg.norm(i - j))])

for i in group:
    if i[1][0] - i[0][0] == 0 :
        group.remove(i)


for i in group:
    x1 = i[0][0]
    x2 = i[1][0]
    y1 = i[0][1]
    y2 = i[1][1]
    slopes = (y2 - y1) / (x2 - x1)
    i.append(slopes)

for i in group:
    if i[3] == -0 or 0:
        group.remove(i)


#create a list only for distances
distances_list = []

#holds filtered group
filtered_group = []

for subgroup in group:
    distance = subgroup[2]

    #if the distance is not in list, add it and then append it to filtered group
    if distance not in distances_list:
        distances_list.append(distance)
        filtered_group.append(subgroup)

#print filtered list
group = filtered_group
placeholder1 = []

#now we determine if all the points are on one of each side of the lines
for j in group:
    val_one_side = []
    x1 = j[0][0]
    x2 = j[1][0]
    y1 = j[0][1]
    y2 = j[1][1]

    slope = (y2 - y1) / (x2 - x1)
    on_one_side = y1 + slope * (x2 - x1)

    #placeholders
    above_line = True
    below_line = True

    for xi, yi in coord_list:
        on_one_side = y1 + slope * (xi - x1)
        if yi > on_one_side:
            below_line = False
        elif yi < on_one_side:
            above_line = False

    #bool result
    result = above_line or below_line
    if result == True:
        placeholder1.append(j)

group = placeholder1

for i in group:
    #to find the angle of rotation, we have to find the arc-tan of the slope, convert it into degrees, and then use absolute value so -90 < theta < 90
    angle_of_rotation = round(abs(np.degrees(np.arctan(i[3]))), 3)
    i.append(angle_of_rotation)

print('------------------------------------------------------')

for i in group:
    x1 = i[0][0]
    x2 = i[1][0]
    y1 = i[0][1]
    y2 = i[1][1]
    slopes = (y2 - y1) / (x2 - x1)
    midpoint_of_len = [((x1 + x2) / 2), ((y1 + y2) / 2)]
    i.append(midpoint_of_len)




dist_between_midpoint_2_points = []
parallel_pt_dist = []
subsubgroup = []
for i in group:
    for j in coord_list:
        i.append(i[5])
        dist_between_midpoint_2_points.append(list(i))
        parallel_pt_dist.append((np.linalg.norm(i[5] - j)) - 1)
        dist_between_midpoint_2_points.append(parallel_pt_dist)




for i in group:
    print(i)
