'''
Createdo on 2020 --- MUIINF

@author: Vicent Castell && Luis Ehate
'''
import pyhop

def traer_andando(state,conductor,ciudad):
    cond = state.ubi_conductor[conductor]
    if cond not in state.ciudad:
        return [('viajar_a_pie',state, conductor, ciudad)]
    else:
        for p in state.parada:
         if (ciudad in state.senda[p]) and (p in state.senda[cond]) 
        return [('viajar_a_pie',state, conductor, ciudad)]
    return False

def no_traer_conductor(state,conductor,ciudad):
    cond = state.ubi_conductor[conductor]
    if cond == ciudad:
        return []
    return False

def func_main(state, objetos_destinos):
#no se lo que hay que poner


def func_mover_camion_ciudad(state, camion, conductor, destino):
    if destino not in state.ciudad:
        print('La ciudad '+destino+' no existe')
        return False
    if camion not in state.camion:
        print('El camion '+camion+ ' no existe')
        return False
    cam = state.ubi_camion[camion]
    cond = state.ubi_conductor[conductor]
    if cond == cam:
        return[('conductor_subir_camion', conductor, camion),
               ('viajar_en_camion',conductor, destino)
                ]
    else:
        return[ ('conseguir_conductor',conductor,destino),
                ('conductor_subir_camion', conductor, camion),
                ('viajar_en_camion',conductor, destino)]
    return False


def func_paquete_destino(state, camion, conductor, paquete, destino):
    if destino not in state.ciudad:
        print('La ciudad '+destino+' no existe')
        return False
    elif paquete not in state.paquete:
        print('El paquete '+paquete+' no existe')
        return False

    paq = state.ubi_paquete[paquete]
    if paq != destino:
        if paq not it state.camion :
            return[('conseguir_conductor',conductor,destino),
                    ('cargar_paquete', camion, paquete, conductor)
                    ('conductor_subir_camion', conductor, camion)
                    ('viajar_en_camion',conductor, destino)
                    ]
        elif paq in state.camion :
            return[('viajar_en_camion',conductor, destino)]
    else:
        return[]


def func_mover_conductor_destino(state, conductor, destino):
    if destino not in state.ciudad:
        print('La ciudad '+destino+' no existe')
        return False
    elif conductor not in state.conductor:
        print('El conductor '+conductor+' no existe')
        return False

    cond = state.ubi_conductor[conductor]
    if cond != destino:
        return[('conseguir_conductor',conductor,destino)]
    else:
        return[]    
        



# Declaración de métodos
pyhoy.declare_methods('traer_conductor',traer_andando, traer_conduciendo)
pyhop.declare_methods('conseguir_conductor', no_traer_conductor, traer_conductor)
pyhop.declare_methods('mover_camion_ciudad', func_mover_camion_ciudad)
pyhop.declare_methods('mover_conductor_destino', func_mover_conductor_destino)
pyhop.declare_methods('mover_paquete_ciudad', func_paquete_destino)
pyhop.declare_methods('mover_todo_destino', func_main)

#Metodos Auxiliares

    
pyhop.print_methods()




