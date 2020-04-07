import pandas as pd
import cv2
import configparser
import numpy as np

map = pd.read_csv('map.csv')
h = pd.read_csv('heuristics.csv')
h_estimate = np.array([0]*(h.shape[0]))
destination = 0
Dict = {}       #Contains information about the indexing of nodes
for i in h.index:
    if(h['h'][i]==0):
        destination = i
    h_estimate[i] = h['h'][i]
    Dict[h['node'][i]] = i
list = [(v, k) for k, v in Dict.items()] #Contains information about the indexing of nodes
print("Destination is node no." +  str(destination) + ": " + str(list[destination][1]))
print(h_estimate)


#dist: it's a 2D array of distance information between each nodes 
dist = np.array([[-1]*(h.shape[0])]*(h.shape[0]))
dist = dist - np.diag(np.diag(dist))
for i in range(len(map)):
    print(map.loc[i,"distance"])
    dist[Dict[map.loc[i,"start"]]][Dict[map.loc[i,"end"]]] = map.loc[i,"distance"]
    dist[Dict[map.loc[i,"end"]]][Dict[map.loc[i,"start"]]] = map.loc[i,"distance"]
print(dist)

open_list = []
closed_list = []
start_node = 0  #Starting node
current_node = start_node #current_node
previous_node = np.array([0]*(h.shape[0])) #Array maintaining history of previous node for each node
f = np.array([0]*(h.shape[0]))  
g = np.array([0]*(h.shape[0]))  #distance of each node from start node 
i = 0
for col in dist[start_node]:
    g[i] = col
    i+=1
print(g)
open_list.append(current_node)

def compute_params(current_node,open_list_node):
    if(dist[open_list_node][current_node]>=0):
        if(g[open_list_node] > g[current_node] + dist[open_list_node][current_node]):
            g[open_list_node] = g[current_node] + dist[open_list_node][current_node]

def update_node(current_node):
    global open_list
    for i in open_list:
        if i != current_node:
            
    



