# This is a Snake game by Henrijs and Luca, using the
# standard graphics.py library !
#
# This is the files function script, to ease read of code.
#
# 28 april 2018

###IMPORTS###
import os


###FILING SYSTEM FUNCTIONS###

# writing_files takes an empty text file and a list of values,
# then write each of these value in the text file.
def writing_files(file, values):
    for value in values:  # Output weights
        file.write(str(value))
        # file.write(value)
        if values.index(value) < len(values) - 1:
            file.write(",")
    file.close()


# assign_weight_layer takes in a list of text files,
# and for each text file, it assign the values in a list (temp2),
# then each list(temp2) is assigned to a big, general list(temp3)
def assign_weight_layer(file_weights):
    temp = []
    temp2 = []
    temp3 = []
    for weight_file in file_weights:
        temp.append(weight_file.read().split(','))
    # returns these values as int !
    for values in temp:
        for value in values:
            temp2.append(int(value))
        temp3.append(temp2)
    return temp3


# Henrijs's function, to write text files in a seperate folder
# rather than in the main script folder.
# (really neat code btw ;) )
def write_file_to_folder(folder_name, filename, what_to_write):
    if not os.path.exists(folder_name):  # check if dir exists
        os.makedirs(folder_name)  # make it if it doesnt
    f = open(folder_name + "//" + filename, "w")
    f.write(what_to_write)
    f.close()


def write_file_to_subfolder(folder_name, subfolder_name, filename, what_to_write):
    if not os.path.exists(folder_name):  # check if dir exists
        os.makedirs(folder_name)  # make it if it doesnt
    if not os.path.exists(folder_name + "//" + subfolder_name):
        os.makedirs(folder_name + "//" + subfolder_name)  # make it if it doesnt
    f = open(folder_name + "//" + subfolder_name + "//" + filename, "w")
    f.write(what_to_write)
    f.close()


def convert_arr_to_writeable_str(array):
    outputstring = ""
    for i in range(len(array)):
        outputstring = outputstring + str(array[i]) + ","
    outputstring = outputstring[:-1]  # REMOVES LAST COMMA
    return outputstring
