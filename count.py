

"""Counts number of instances"""

import os
import json

PATH0 = './'
# _, folders0, _ = os.walk(PATH0).__next__()
folders0 = ['Conventional', 'NoObstacles', 'NR1', 'NR2', 'SingleRack', 'TwelveRacks']

N = 0
for namef0 in folders0:
    path = PATH0 + namef0
    _, folders, _ = os.walk(path + '/instances/').__next__()

    # for namef1 in folders:
    #     path2 = path + '/instances/' + namef1 + '/' + namef1 + '.json'
    #     with open(path2, 'r') as f:
    #         inst = json.load(f)

    N += len(folders)

print("There are " + str(N) + " instances.")