# -*- coding: utf-8 -*-
"""
Grupo: 035
Bernardo Esteves 87633
Francisco Barata 87656

"""

import numpy as np

import itertools

class Node():

    def __init__(self, prob, parents=[]):
        self.parents = parents
        self.prob = prob

    
    def computeProb(self, evid):
        # vamos buscar os valores da evidencia, conforme os pais
        prob_index=np.take(evid,self.parents)  # O(Nr_pais)
        # item tem de ser tuple para escolher o elemento
        prob = self.prob.item(tuple(prob_index))  # O(1) ->numpy
        return [1-prob,prob]
    
class BN():

    def __init__(self, gra, prob):
        self.gra = gra
        self.prob = prob

    def computePostProb(self, evid):
        '''
        O(2**(desconhecidos)* O(nr_nos*O(nr_pais por no)))
        '''
        index_calcular = evid.index(-1)

        nr_unk = evid.count([])
        matrix = np.zeros((2**nr_unk,len(evid)))
        matrix[:,index_calcular] = 1
        matrix_combinacoes = np.array([x for x in itertools.product(*[[0,1] for _ in range(nr_unk)])])
        i_comb = 0

        for index,ev in enumerate(evid):
            if ev == 1:
                matrix[:,index] = 1
            elif ev == []:
                matrix[:,index] = matrix_combinacoes[:,i_comb]
                i_comb += 1
        # Matrix

        p = np.sum([self.computeJointProb(linha.astype(int)) for linha in matrix])

        matrix[:, index_calcular] = 0
        not_p = np.sum([self.computeJointProb(linha.astype(int)) for linha in matrix])

        alpha = 1/(p+not_p)

        return alpha * p
        
        
    def computeJointProb(self, evid):
        '''
        O(nr_nos*O(nr_pais por no))
        '''
        final_p = 1
        for index,p in enumerate(self.prob):
            prob_node= p.computeProb(evid) # calcular prob do no O(1)
            final_p *= prob_node[evid[index]] # ir buscar se e true/false conforme ev
        return final_p
