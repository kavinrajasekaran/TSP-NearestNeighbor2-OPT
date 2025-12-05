import numpy as np
import time
import math
import os

N = 1000
timelimit = 59 
studentid = "919711804"
filepatha = "TSP_1000_euclidianDistance.txt"
filepathb = "TSP_1000_randomDistance.txt"
def gettotalcost(path, distmatrix):
    cost = 0
    for i in range(len(path)):
        cost += distmatrix[path[i], path[(i + 1) % N]]
    return cost

def solvenn(distmatrix, startnode):
    count = 0
    path = [startnode]
    visited = np.zeros(N, dtype=bool)
    visited[startnode] = True
    current = startnode
    
    #nearest unvisited neighbor
    for i in range(N - 1):
        bestnode = -1
        mindist = float('inf')
        
        for j in range(N):
            if not visited[j]:
                count += 1
                if distmatrix[current, j] < mindist:
                    mindist = distmatrix[current, j]
                    bestnode = j
        visited[bestnode] = True
        path.append(bestnode)
        current = bestnode
    
    return path, count

def solve2opt(path, distmatrix, starttime):
    count = 0
    currpath = list(path)
    improved = True
    
    # keep improving till no swaps or timeup 
    while improved:
        improved = False
        
        if time.time() - starttime > timelimit:
            break
            
        for i in range(N):
            for j in range(i + 2, N):
                if j == N - 1 and i == 0:
                    continue
                # a and b are the endpoints of the first edge
                A = currpath[i]
                B = currpath[(i + 1) % N]
                # c and d  are the endpoints of the second edge
                C = currpath[j]
                dnode = currpath[(j + 1) % N]

                # (new edges cost) - (old edges cost) and if negative, new path is shorter
                change = (distmatrix[A, C] + distmatrix[B, dnode]) - (distmatrix[A, B] + distmatrix[C, dnode])
                count += 1
                if change < 0:
                    currpath[i+1:j+1] = currpath[i+1:j+1][::-1]
                    improved = True
        
            # sometimes i kept going deeper and deeper and it passed the time limit so i added this to check every 5000 cycles

            #  this is what causes it to go slighlty over 59 seconds but it's fine, helps us be in check 
            if count % 5000 == 0:
                if time.time() - starttime > timelimit:
                    return currpath, count
    return currpath, count

def getdistmatrix(filepath):
    distmatrix = np.zeros((N, N))
    
    with open(filepath, 'r') as f:
        # Skip the first two header lines
        f.readline()
        f.readline()
        
        # Assume it's an edge list (Node1 Node2 Distance) for ANY file
        for line in f:
            parts = line.split()
            if len(parts) >= 3:
                u = int(parts[0]) - 1
                v = int(parts[1]) - 1
                d = float(parts[2])
                distmatrix[u, v] = d
                distmatrix[v, u] = d
                
    return distmatrix


def solvegraph(filepath):
    cyclesevaluated = 0
    
    print("Loading data from:", filepath)
    distmatrix = getdistmatrix(filepath)
    
    starttime = time.time()
    bestpath = []
    bestcost = float('inf')
    runs = 0
    
    startnodes = np.random.choice(N, 10, replace=False)
    
    print("Starting")
    
    while time.time() - starttime < timelimit:
        runs += 1
        
        # initial path 
        if runs <= 10:
            p, count1 = solvenn(distmatrix, startnodes[runs-1])
        else:
            if len(bestpath) > 0:
                p = np.random.permutation(np.array(bestpath)).tolist()
                count1 = 0
            else:
                p, count1 = solvenn(distmatrix, 0)
        
        cyclesevaluated += count1
        
        # 2opt
        p, count2 = solve2opt(p, distmatrix, starttime)
        cyclesevaluated += count2
        
        c = gettotalcost(p, distmatrix)
        if c < bestcost:
            bestcost = c
            bestpath = p
            print("Run", runs, ": Cost", round(bestcost, 2))
            
    print("Total Runs:", runs)
    print("Time Used:", round(time.time() - starttime, 2), "seconds")
    print("Final Cost:", round(bestcost, 2))
    print("Cycles:", cyclesevaluated)
    print("-" * 50)
    
    return bestpath


patha = solvegraph(filepatha)
pathb = solvegraph(filepathb)
fname = "solution_" + studentid + ".txt"
stra = ",".join([str(x + 1) for x in patha])
strb = ",".join([str(x + 1) for x in pathb])
with open(fname, 'w') as f:
    f.write(stra + "\n")
    f.write(strb)
    
print("Saved to", fname)