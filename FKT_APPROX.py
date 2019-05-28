# -*- coding: utf-8 -*-
"""
Created on Fri May 24 12:46:25 2019

@author: daryl
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 11:33:37 2019

@author: ddeford
"""


from FKT import FKT
import networkx as nx #Requires at least networkx 2.3+
import matplotlib.pyplot as plt
import random
import math
import numpy as np
import time




def K_approx(K, its):
    
    vals=[]
    
    for i in range(its):
        
        temp =1

        
        G=K.copy()
        
        
        nlist = list(G.nodes())
        
        while len(nlist) > 0:
            
            H = (G.subgraph(nlist)).copy()
            
            elist = list(G.edges())
            
            possible = []
            notused = []
        
            #print(possible)
            for edge in elist:
        
            
                H.remove_nodes_from([edge[0],edge[1]])
    
                C=list((H.subgraph(c) for c in nx.connected_components(H)))
                
                compprod = 1
                for comp in C:
                    if len(list(comp.nodes())) %2 == 1:
                        compprod = 0
                            #break
                    else:
                        compprod = compprod * round(FKT((nx.adjacency_matrix(comp)).todense()))#FKT((nx.adjacency_matrix(comp)).todense())
                
                val = compprod
                #print(val)
        
                if val == 0:
                    notused.append(edge)
                else:
                    possible.append(edge)
                    
                    
                H = (G.subgraph(nlist)).copy()

                    
                    
            touse = random.choice(possible)
            
            #print(touse,touse[0])
                
                
            nlist.remove(touse[0])
            nlist.remove(touse[1])
            G.remove_nodes_from([touse[0],touse[1]])
                
                
                
            #print(len(possible))
            temp = temp * len(possible)
            #print(temp)
            
        vals.append(temp)
        
    return vals
        
        
def K_approx2(K, its):
    
    vals=[]
    wins = []
    
    for i in range(its):
        
        temp =1

        
        G=K.copy()
        
        nlist = list(G.nodes())
        
        while len(nlist) > 0:
                        
            elist = list(G.edges())
            
            
            if elist ==[]:
                success = 0
                break
            
            temp = temp * len(elist)
            
            
            touse = random.choice(elist)
            
            #print(touse,touse[0])
                
            nlist.remove(touse[0])
            nlist.remove(touse[1])
            G.remove_nodes_from([touse[0],touse[1]])
            
        if len(nlist) == 0:
            success = 1
            
        wins.append(success)
        vals.append(temp)
        
    return wins, vals
        
#wa, va = K_approx2(test_G,10000)
#np.mean(wa)*np.mean(va)/math.factorial(8)
            
        
            
        
           
            

              
     
            
test_G = nx.grid_graph([4,4])

print(round(FKT(nx.adjacency_matrix(test_G).todense())))

#test_G = nx.convert_node_labels_to_integers(test_G)   

a = K_approx(test_G,1000)

print(np.mean(a)/math.factorial(8))

dkskhdas
Adj = np.loadtxt("./data/graphs/Alaska.csv")


print(round(FKT(Adj)))
a = K_approx(nx.Graph(Adj),10)

print(np.mean(a)/math.factorial(20))



                
            

    
    
