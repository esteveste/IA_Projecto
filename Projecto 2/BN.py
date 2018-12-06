# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:51:49 2018

@author: mlopes
"""
import numpy as np
import itertools

class Node():
    def __init__(self, prob, parents = []):
        self.parents=parents
        self.prob = prob

    
    def computeProb(self, evid):
        # vamos buscar os valores da evidencia, conforme os pais
        prob_index=np.take(evid,self.parents)
        # item tem de ser tuple para escolher o elemento
        prob = self.prob.item(tuple(prob_index))
        return [1-prob,prob]
    
class BN():
    def __init__(self, gra, prob):
        self.gra = gra
        self.prob = prob

    def computePostProb(self, evid):

        index_calcular = evid.index(-1)

        nr_unk= evid.count([])
        matrix = np.zeros((2**nr_unk,len(evid)))
        matrix[:,index_calcular] = 1
        matrix_combinacoes = np.array([x for x in itertools.product(*[[0,1] for _ in range(nr_unk)])])
        i_comb =0
        for index,ev in enumerate(evid):
            if ev == 1:
                matrix[:,index] = ev
            elif ev == []:
                matrix[:,index] = matrix_combinacoes[:,i_comb]
                i_comb+=1
        # Matrix

        p = np.sum([self.computeJointProb(linha.astype(int)) for linha in matrix])

        matrix[:, index_calcular] = 0
        not_p =np.sum([self.computeJointProb(linha.astype(int)) for linha in matrix])

        alpha = 1/(p+not_p)

        return alpha * p
        
        
    def computeJointProb(self, evid):
        '''
        :return: retorna o produto das compute Probs
        '''
        return np.prod([p.computeProb(evid)[evid[index]] for index,p in enumerate(self.prob)])
