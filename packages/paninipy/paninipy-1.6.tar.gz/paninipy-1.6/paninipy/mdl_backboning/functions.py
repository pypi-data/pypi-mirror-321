import numpy as np
from scipy.special import loggamma

def logchoose(n,k):
    """computes log of binomial coefficient"""
    if n == k: return 0
    return loggamma(n+1) - loggamma(k+1) - loggamma((n-k)+1)

def logmultiset(n,k):
    """computes log of multiset coefficient"""
    return logchoose(n+k-1,k)


def MDL_backboning(elist,directed=True,out_edges=True,allow_empty=True):
    
    """
    input: elist consisting of directed tuples [(i,j,w_ij)] for edges i --> j with weight w_ij
           'directed' arg tells us whether input edge list is directed or undirected
           'out_edges' arg tells us whether to track out-edges or in-edges attached to each node in the local pruning method (does not matter for undirected elist)
           'allow_empty': by symmetry, the DL is identical for complete/empty graphs in the global objective, and complete/empty neighborhoods in local objective. defaults to leaving these empty when situation is encountered, but setting allow_empty = False will keep the complete graph/neighborhoods
    output: edge lists and inverse compression ratios for global and local MDL backbones
    """

    def fglobal(W,E,Wb,Eb):
        """
        global description length objective
        """  
        initial_cost = np.log(W-E+1) + np.log(W+1) + np.log(E+1)
        return initial_cost + logchoose(E,Eb) + logchoose(Wb-1,Eb-1) + logchoose(W-Wb-1,E-Eb-1)

    def flocal(si,ki,sbi,kbi):
        """
        local description length objective at node-level
        """
        initial_cost = np.log(si-ki+1) + np.log(si+1) + np.log(ki+1)
        return initial_cost + logchoose(ki,kbi) + logchoose(sbi-1,kbi-1) + logchoose(si-sbi-1,ki-kbi-1)

    #add two directed edges for each undirected edge if input is undirected. don't duplicate self-edges.
    if not(directed):
        self_edge_indices = set([i for i,e in enumerate(elist) if e[0] == e[1]])
        elist = list(elist) + [(e[1],e[0],e[2]) for i,e in enumerate(elist) if not(i in self_edge_indices)]

    #reverse edge order if we want the local pruning method to focus on in-degrees and in-strengths
    #does not make any difference for undirected networks
    if not(out_edges):
        elist = [(e[1],e[0],e[2]) for e in elist]

    #computational complexity bottleneck: sort edge list by decreasing weight in O(ElogE) time
    elist = sorted(elist,key = lambda e:e[-1],reverse=True) 

    #initialize variables for input network
    W = sum([e[-1] for e in elist])
    E = len(elist)
    adj_edges,adj_weights = {},{}
    for e in elist:
        i,j,w_ij = e
        if not(i in adj_edges): adj_edges[i] = []
        if not(i in adj_weights): adj_weights[i] = []
        adj_edges[i].append(j)
        adj_weights[i].append(w_ij)
    nodes = set([e[0] for e in elist]+[e[1] for e in elist])
    N = len(nodes)

    #greedily add edges to global backbone and track total description length
    Lglobal0 = fglobal(W,E,0,0)
    Lglobal = Lglobal0
    min_DL_global = Lglobal
    backbone_Eb = 0
    Wb,Eb = 0,0
    for e in elist:
        
        i,j,w_ij = e
        Eb += 1
        Wb += w_ij
        Lglobal += fglobal(W,E,Wb,Eb) - fglobal(W,E,Wb-w_ij,Eb-1) 
       
        if Lglobal < min_DL_global:
            min_DL_global = Lglobal
            backbone_Eb = Eb

    if (backbone_Eb == 0) and not(allow_empty): backbone_Eb = E #by symmetry, DL is equivalent, so can choose to keep all edges
    
    #greedily add edges to local backbone and track description length at each node
    Llocal0 = 0.
    min_DL_local = Llocal0
    backbone_degrees = {}
    for i in adj_edges:
        
        si,ki,sbi,kbi = sum(adj_weights[i]),len(adj_edges[i]),0,0
        Llocali = flocal(si,ki,0,0)
        Llocal0 += Llocali
        best_Llocali,best_kbi,best_sbi = Llocali,kbi,sbi
        for w_ij in adj_weights[i]:
            
            kbi += 1
            sbi += w_ij
            Llocali += flocal(si,ki,sbi,kbi) - flocal(si,ki,sbi-w_ij,kbi-1)
            
            if Llocali < best_Llocali:
                best_Llocali = Llocali
                best_kbi = kbi
                best_sbi = sbi

        if (best_kbi == 0) and not(allow_empty): #by symmetry, DL is equivalent, so can choose to keep all edges
            best_kbi = ki
            
        min_DL_local += best_Llocali
        backbone_degrees[i] = best_kbi
                
    #construct MDL-optimal backbone edgelists based on identified description lengths
    backbone_global = elist[:backbone_Eb]

    backbone_local = []
    for i in adj_edges:
        MDL_kbi = backbone_degrees[i]
        for index,j in enumerate(adj_edges[i][:MDL_kbi]):
            backbone_local.append((i,j,adj_weights[i][index]))

    if out_edges == False: #if out_edges == False, reverse edge order for local method back to format of input
        backbone_local = [(e[1],e[0],e[2]) for e in backbone_local]
    
    if not(directed): #convert backbone to undirected edge tuples if input was undirected
        backbone_global = np.unique([tuple([sorted([e[0],e[1]])+[e[2]]]) for e in backbone_global])
        backbone_local = np.unique([tuple([sorted([e[0],e[1]])+[e[2]]]) for e in backbone_local])

    #compute inverse compression ratios
    baseline_DL = max(Lglobal0,Llocal0)
    compression_global,compression_local = min_DL_global/baseline_DL,min_DL_local/baseline_DL
    
    return backbone_global,backbone_local,compression_global,compression_local