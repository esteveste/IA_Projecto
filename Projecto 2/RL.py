# -*- coding: utf-8 -*-
"""
Grupo: 035
Bernardo Esteves 87633
Francisco Barata 87656

"""
import numpy as np

import random

from tempfile import TemporaryFile

outfile = TemporaryFile()
	
class finiteMDP:

    def __init__(self, nS, nA, gamma, P=[], R=[], absorv=[]):
        self.nS = nS
        self.nA = nA
        self.gamma = gamma
        self.Q = np.zeros((self.nS,self.nA))
        self.P = P
        self.R = R
        self.absorv = absorv
        #importancia do que foi aprendido no passado (learning rate)
        self.alpha = 0.7
        
            
    def runPolicy(self, n, x0, poltype = 'greedy', polpar=[]):
        #nao alterar
        traj = np.zeros((n,4))
        x = x0
        J = 0
        for ii in range(0,n):
            a = self.policy(x,poltype,polpar)
            r = self.R[x,a]
            y = np.nonzero(np.random.multinomial( 1, self.P[x,a,:]))[0][0]
            traj[ii,:] = np.array([x, a, y, r])
            J = J + r * self.gamma**ii
            if self.absorv[x]:
                y = x0
            x = y
        
        return J,traj


    def VI(self):
        #nao alterar
        nQ = np.zeros((self.nS,self.nA))
        while True:
            self.V = np.max(self.Q,axis=1) 
            for a in range(0,self.nA):
                nQ[:,a] = self.R[:,a] + self.gamma * np.dot(self.P[:,a,:],self.V)
            err = np.linalg.norm(self.Q-nQ)
            self.Q = np.copy(nQ)
            if err<1e-7:
                break
            
        #update policy
        self.V = np.max(self.Q,axis=1) 
        #correct for 2 equal actions
        self.Pol = np.argmax(self.Q, axis=1)
                    
        return self.Q,  self.Q2pol(self.Q)

            
    def traces2Q(self, trace):
        self.Q = np.zeros((self.nS, self.nA))

        for step in trace:
            s,a,s_prime,r = step
            s,a,s_prime = int(s),int(a),int(s_prime)

            self.Q[s,a] = self.Q[s,a] + self.alpha * (r + self.gamma * np.max(self.Q[s_prime]) - self.Q[s,a])


        return self.Q
    
    def policy(self, x, poltype = 'exploration', par = []):
        #par e uma matriz Q

        if poltype == 'exploitation':
            #retorna o indice da acao que tem maior retorno
            a = np.argmax(par[x])

            
        elif poltype == 'exploration':
            # escolhe um numero random entre 0 e o numero de accoes
            a = random.randint(0, self.nA-1)

        return a
    
    def Q2pol(self, Q, eta=5):
        #nao fazer nada
        return np.exp(eta*Q)/np.dot(np.exp(eta*Q),np.array([[1,1],[1,1]]))
