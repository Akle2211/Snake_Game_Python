# this is Henrijs's code, refactored by Luca
#


###IMPORT###
from operator import itemgetter
from Neural_Network_Function_Snake_Game import *
from Files_function import *
import random


###FUNCTION###


###GLOBAL VARIABLE###
k = 100
newbreedarray = []  # with misc fitnesses
bigarray = []  # 3 layers THICC roughly

for i in range(k):
    print("i: ", i)
    ###INIT FILES###
    aweights1 = open(str(i)+"weights1", "r+")
    aweights11 = open(str(i)+"weights11", "r+")
    aweights111 = open(str(i)+"weights111", "r+")
    aweights1111 = open(str(i)+"weights1111", "r+")
    aweights11111 = open(str(i)+"weights11111", "r+")
    aweights111111 = open(str(i)+"weights111111", "r+")
    aweights1111111 = open(str(i)+"weights1111111", "r+")
    file_weights_1 = [aweights1, aweights11, aweights111,
                      aweights1111, aweights11111, aweights111111,
                      aweights1111111]

    abiashidden1 = open(str(i)+"biashidden1", "r+")

    aweights2 = open(str(i)+"weights2", "r+")
    aweights22 = open(str(i)+"weights22", "r+")
    aweights222 = open(str(i)+"weights222", "r+")
    aweights2222 = open(str(i)+"weights2222", "r+")
    aweights22222 = open(str(i)+"weights22222", "r+")
    aweights222222 = open(str(i)+"weights222222", "r+")
    aweights2222222 = open(str(i)+"weights2222222", "r+")
    file_weights_2 = [aweights2, aweights22, aweights222,
                      aweights2222, aweights22222, aweights222222,
                      aweights2222222]

    abiasoutput = open(str(i)+"biasoutput", "r+")
    afitness = open(str(i)+"fitness", "r+")

    ###READING FILES###
    print("len of file_weights_1: ", len(file_weights_1))
    weights_1 = assign_weight_layer(file_weights_1)
    biashidden1 = abiashidden1.read().split(',')
    weights_2 = assign_weight_layer(file_weights_2)
    biasoutput = abiasoutput.read().split(',')
    fitness = afitness.read()

    ###GENERATION(what is that?)###
    generationarray = []
    generationarray.append(fitness)

    for i in range(7):
        biashidden1[i] = int(biashidden1[i])
        biasoutput[i] = int(biasoutput[i])

    for weight in weights_1:
        generationarray.append(weight)

    generationarray.append(biashidden1)

    for weight in weights_2:
        generationarray.append(weight)

    generationarray.append(biasoutput)
    bigarray.append(generationarray)

print("OUT OF THE FOR LOOP")
# print bigarray[0]
sortedbigarray = sorted(bigarray, key=itemgetter(0), reverse=True)
# print sortedbigarray[0]
for i in range(25):  # swap
    newbreedarray.append(swap(sortedbigarray[i*2], sortedbigarray[i*2+1], 1))
    newbreedarray.append(swap(sortedbigarray[i*2], sortedbigarray[i*2+1], 2))
# GENERATE NEW KIDS
# print newbreedarray[0]
for a in range(50):
    # weights1 = []
    # weights11 = []
    # weights111 = []
    # weights1111 = []
    # weights11111 = []
    # weights111111 = []
    # weights1111111 = []
    weights_1 = 7*[[]]
    biashidden1 = []
    weights2 = []
    weights22 = []
    weights222 = []
    weights2222 = []
    weights22222 = []
    weights222222 = []
    weights2222222 = []
    biasoutput = []
    fitness = 0
    for i in range(7):  # make random weights
        weights_1[i] = rand_list(7, -4, 4)
        print(weights_1)
        # weights1.append(random.randint(-4, 4))
        # weights11.append(random.randint(-4, 4))
        # weights111.append(random.randint(-4, 4))
        # weights1111.append(random.randint(-4, 4))
        # weights11111.append(random.randint(-4, 4))
        # weights111111.append(random.randint(-4, 4))
        # weights1111111.append(random.randint(-4, 4))
        biashidden1.append(random.randint(-4, 4))
        # weights2.append(random.randint(-4, 4))
        # weights2.append(random.randint(-4, 4))
        # weights22.append(random.randint(-4, 4))
        # weights222.append(random.randint(-4, 4))
        # weights2222.append(random.randint(-4, 4))
        # weights22222.append(random.randint(-4, 4))
        # weights222222.append(random.randint(-4, 4))
        # weights2222222.append(random.randint(-4, 4))
        weights_2[i] = rand_list(7, 4, 4)
        biasoutput.append(random.randint(-4, 4))
    generationarray = []  # append those newly made weights to newbreedarray through generation array
    generationarray.append(fitness)

    for weight in weights_1:
        generationarray.append(weight)
    # generationarray.append(weights1)
    # generationarray.append(weights11)
    # generationarray.append(weights111)
    # generationarray.append(weights1111)
    # generationarray.append(weights11111)
    # generationarray.append(weights111111)
    # generationarray.append(weights1111111)
    generationarray.append(biashidden1)
    for weight in weights_2:
        generationarray.append(weight)
    # generationarray.append(weights2)
    # generationarray.append(weights22)
    # generationarray.append(weights222)
    # generationarray.append(weights2222)
    # generationarray.append(weights22222)
    # generationarray.append(weights222222)
    # generationarray.append(weights2222222)
    generationarray.append(biasoutput)
    newbreedarray.append(generationarray)
# WORKS TILL HERE
print("IT GOT TO TRUNCATING STAGE!")

for i in range(100):
    aweights1 = open(str(i)+"weights1", "r+")  # OPEN ALL THE FILES IN Read and Write mode
    aweights11 = open(str(i)+"weights11", "r+")
    aweights111 = open(str(i)+"weights111", "r+")
    aweights1111 = open(str(i)+"weights1111", "r+")
    aweights11111 = open(str(i)+"weights11111", "r+")
    aweights111111 = open(str(i)+"weights111111", "r+")
    aweights1111111 = open(str(i)+"weights1111111", "r+")
    abiashidden1 = open(str(i)+"biashidden1", "r+")
    aweights2 = open(str(i)+"weights2", "r+")
    aweights22 = open(str(i)+"weights22", "r+")
    aweights222 = open(str(i)+"weights222", "r+")
    aweights2222 = open(str(i)+"weights2222", "r+")
    aweights22222 = open(str(i)+"weights22222", "r+")
    aweights222222 = open(str(i)+"weights222222", "r+")
    aweights2222222 = open(str(i)+"weights2222222", "r+")
    abiasoutput = open(str(i)+"biasoutput", "r+")
    afitness = open(str(i)+"fitness", "r+")
    # get rid of their content before writing to them
    aweights1.truncate()
    aweights11.truncate()
    aweights111.truncate()
    aweights1111.truncate()
    aweights11111.truncate()
    aweights111111.truncate()
    aweights1111111.truncate()
    abiashidden1.truncate()
    aweights2.truncate()
    aweights22.truncate()
    aweights222.truncate()
    aweights2222.truncate()
    aweights22222.truncate()
    aweights222222.truncate()
    aweights2222222.truncate()
    abiasoutput.truncate()
    afitness.truncate()
    # write to the files the newbreed array
    for b in range(7):
        if b == 6:
            # afitness.write(str(newbreedarray[i][0][b]))
            aweights1.write(str(newbreedarray[i][1][b]))
            aweights11.write(str(newbreedarray[i][2][b]))
            aweights111.write(str(newbreedarray[i][3][b]))
            aweights1111.write(str(newbreedarray[i][4][b]))
            aweights11111.write(str(newbreedarray[i][5][b]))
            aweights111111.write(str(newbreedarray[i][6][b]))
            aweights1111111.write(str(newbreedarray[i][7][b]))
            abiashidden1.write(str(newbreedarray[i][8][b]))
            aweights2.write(str(newbreedarray[i][9][b]))
            aweights22.write(str(newbreedarray[i][10][b]))
            aweights222.write(str(newbreedarray[i][11][b]))
            aweights2222.write(str(newbreedarray[i][12][b]))
            aweights22222.write(str(newbreedarray[i][13][b]))
            aweights222222.write(str(newbreedarray[i][14][b]))
            aweights2222222.write(str(newbreedarray[i][15][b]))
            abiasoutput.write(str(newbreedarray[i][16][b]))
        else:
            abiasoutput.write(str(newbreedarray[i][16][b]))
            abiasoutput.write(",")
            aweights1.write(str(newbreedarray[i][1][b]))
            aweights1.write(",")
            aweights11.write(str(newbreedarray[i][2][b]))
            aweights11.write(",")
            aweights111.write(str(newbreedarray[i][3][b]))
            aweights111.write(",")
            aweights1111.write(str(newbreedarray[i][4][b]))
            aweights1111.write(",")
            aweights11111.write(str(newbreedarray[i][5][b]))
            aweights11111.write(",")
            aweights111111.write(str(newbreedarray[i][6][b]))
            aweights111111.write(",")
            aweights1111111.write(str(newbreedarray[i][7][b]))
            aweights1111111.write(",")
            abiashidden1.write(str(newbreedarray[i][8][b]))
            abiashidden1.write(",")
            aweights2.write(str(newbreedarray[i][9][b]))
            aweights2.write(",")
            aweights22.write(str(newbreedarray[i][10][b]))
            aweights22.write(",")
            aweights222.write(str(newbreedarray[i][11][b]))
            aweights222.write(",")
            aweights2222.write(str(newbreedarray[i][12][b]))
            aweights2222.write(",")
            aweights22222.write(str(newbreedarray[i][13][b]))
            aweights22222.write(",")
            aweights222222.write(str(newbreedarray[i][14][b]))
            aweights222222.write(",")
            aweights2222222.write(str(newbreedarray[i][15][b]))
            aweights2222222.write(",")
        # print newbreedarray[i][0]
        # afitness.write(str(newbreedarray[i][0]))
print("DONE!!!")
