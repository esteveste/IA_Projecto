# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:51:49 2018

@author: mlopes
"""
import numpy as np


class Node():
    def __init__(self, prob, parents = []):
        self.parents=parents
        self.prob = prob

    
    def computeProb(self, evid):
        # vamos buscar o valor da pro
        prob = self.prob.item(tuple(np.take(evid,self.parents))) # item tem de ser tuple para escolher o elemento
        return [1-prob,prob]
    
class BN():
    def __init__(self, gra, prob):
        self.gra = gra
        self.prob = prob

    def computePostProb(self, evid):

        return 0
        
        
    def computeJointProb(self, evid):
        return np.prod([p.computeProb(evid)[evid[index]] for index,p in enumerate(self.prob)])
