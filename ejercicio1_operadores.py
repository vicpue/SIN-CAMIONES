'''
Createdo on 2020 --- MUIINF

@author: Vicent Castell && Luis Ehate
'''

import pyhop

def cargar_paquete(state, camion, paquete, conductor):
    if(state.ubi_camion[camion] == state.ubi_paquete[paquete] and state.ubi_paquete[paquete] == state.ubi_conductor[conductor]):
        print('El conductor '+conductor+ ' ha cargado el paquete '+paquete+' en el camion '+camion)
        state.ubi_paquete[paquete] = camion
        state.contenido_camiones[camion].insert(len(state.contenido_camiones),paquete)
        return state
    else:
        if state.ubi_camion[camion] != state.ubi_paquete[paquete]:
            print('El paquete '+paquete+' NO se ha podido cargar en el camion '+camion+' porque estan en ubicaciones diferentes')
            return False
        if state.ubi_paquete[paquete] != state.ubi_conductor[conductor]:    
            print('El condutor '+conductor+' NO se ha podido cargar el paquete '+paquete+' porque estan en ubicaciones diferentes')
            return False

def descargar_paquete(state, camion, paquete, conductor):
    if state.ubi_camion[camion] == state.ubi_conductor[conductor]:
        print('El conductor '+conductor+ ' ha descargado el paquete '+paquete+' del camion '+camion+ ' en la cuidad '+ state.ubi_camion[camion])
        state.ubi_paquete[paquete] = state.ubi_camion[camion]
        state.contenido_camiones[camion].remove(paquete)
        return state
    else:
        print('El conductor '+conductor+ ' NO ha descargado el paquete '+paquete+' del camion '+camion+ ' porque estan en ubicaciones diferentes')
        return False 

def conductor_subir_camion(state, conductor, camion):
    if state.ubi_camion[camion] == state.ubi_conductor[conductor]:
        print('El conductor '+conductor+' ha subido al camion '+camion)
        state.ubi_conductor[conductor] = camion
        return state
    else:
        print('El conductor '+conductor+' NO ha podido subir al camion '+camion+' porque estan en ubicaciones diferentes')
        return False

def conductor_bajar_camion(state, conductor, camion):
    state.ubi_conductor[conductor] = state.ubi_camion[camion]
    return state

def viajar_en_camion(state,conductor, camion, destino):
    lugar = state.ubi_camion[camion]
    for i in range(len(state.carretera)):
        if (((lugar == state.carretera[i][0]) and (destino == state.carretera[i][1])) or (destino == lugar)):
            state.ubi_camion[camion] = destino
            state.ubi_conductor[conductor] = destino
            return state
    else:
        return False

def viajar_a_pie(state, conductor, destino):
    lugar = state.ubi_conductor[conductor]
    if lugar not in state.parada:
        for p in state.parada:
            for x in state.senda:
                if ((destino == x[0]) and (p == x[1])):
                    for y in state.senda:
                        if((p == y[0]) and (lugar == y[1])):
                            state.ubi_conductor[conductor] = destino
                            return state
    else:
        for i in range(len(state.senda)):
            if((lugar == state.senda[i][0]) and (destino == state.senda[i][1])):
                state.ubi_conductor[conductor] = destino
                return state
    return False
    
pyhop.declare_operators(cargar_paquete, descargar_paquete, conductor_subir_camion, conductor_bajar_camion, viajar_en_camion, viajar_a_pie)
pyhop.print_operators()
