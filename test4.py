from eca import *
from eca.generators import start_offline_tweets
import numpy as np
import time
root_content_path = 'test5_static'
#Het leven is een wervelstorm en ik ben een vlieger :D
@event('init')
def setup(ctx, e):
    start_offline_tweets('data/p2000.txt', event_name='chirp', time_factor=10000)

def updateDict(cDict, c):
    c = tuple(c)
    if c in cDict:
        return cDict
    for coords in cDict:
        dif = (c[0] - coords[0])**2 + (c[1] - coords[1])**2
        cDict[coords].append(dif)
    cDict[c] = []
    return cDict

totalDict = {}
totalList = list()

def distance(c):
    global totalDict
    global totalList
    totalDict = updateDict(totalDict, c)
    totalList.append(tuple(c))
    if len(totalList) == 101:
        totalDict.pop(totalList.pop())
    print(totalDict)

@event('chirp')
def tweet(ctx, e):
    coor = e.data.get('geo').get('coordinates')
    text = e.data.get('text')
    #distance(coor)
    emit('one', {'text':text})
    emit('coords', {'action':'add','value':coor})
    time.sleep(0.1)
