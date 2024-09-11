def swap_the_string(param, param1):
    new_param = []
    new_param1 = []
    new_param2 = []
    output = ""
    output2 = ""
    for index, count in zip(range (len(param)), range (len(param1))):
         new_param.append(param[index])
         new_param1.append(param1[count])
         new_param2.append(param[index])
    for counter,indices in zip(range( 0,2), range(0, 2)):
        new_param[counter] = new_param1[indices]
        new_param1[counter] = new_param2[indices]
    for i, j in zip (new_param, new_param1):
        output+=i
        output2+=j
    return output +" " +output2