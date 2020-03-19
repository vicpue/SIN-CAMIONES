'''
Createdo on 2020 --- MUIINF

@author: Vicent Castell && Luis Ehate
'''

import pyhop
import ejercicio1_operadores

#ESTADO INICIAL

state1=pyhop.State('state1')

state1.ciudad=['C0', 'C1', 'C2']
state1.parada=['S1', 'S2']
state1.camion=['T1', 'T2']
state1.conductor=['D1', 'D2']
state1.paquete=['P1', 'P2']
state1.senda={  'W1':['C0','S1'], 
                'W2':['S1', 'C1'],
                'W3':['C1','S2'],
                'W4':['S2','C2']
                }
state1.carretera={  'H01':['C0','C1'],
                    'H12':['C1','C2'],
                    'H02':['C0','C2']
                    }

#ESTADO DINAMICO

state1.ubi_camion ={'T1':'C1','T2':'C0'}
state1.ubi_conductor={'D1':'S1','D2':'C1'}
state1.ubi_paquete={'P1':'C0','P2':'C0'}

state1.cola_condutores=[]
state1.cola_camiones=[]
state1.contenido_camiones= {'T1':[], 'T2':[]}


pyhop.pyhop(state1, [ 
                     ('mover_todo_a_destino', [ ['D1', 'C1'], ['T1', 'C1'], ['P1', 'C1'], ['P2','C2']  ] )  
                     ], verbose=3)