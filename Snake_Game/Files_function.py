# This is a Snake game by Henrijs and Luca, using the
# standard graphics.py library !
#
# This is the files function script, to ease read of code.
#
# 28 april 2018


###FILING SYSTEM FUNCTIONS###
def writing_files(file, values):
    for value in values:  # Output weights
        file.write(str(value))
        # file.write(value)
        if values.index(value) < len(values) - 1:
            file.write(",")
    file.close()


def assign_weight_layer(file_weights):
    temp = []
    temp2 = []
    temp3 = []
    for weight_file in file_weights:
        temp.append(weight_file.read().split(','))
    # returns these values as int !
    print("temp: ", temp)
    for values in temp:
        for value in values:
            temp2.append(int(value))

        temp3.append(temp2)
    print("temp3: ", temp3)
    return temp3
