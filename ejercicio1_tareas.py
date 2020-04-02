'''
Createdo on 2020 --- MUIINF

@author: Vicent Castell && Luis Ehate
'''
import pyhop

def traer_andando(state,conductor,ciudad):
    cond = state.ubi_conductor[conductor]
    if cond not in state.ciudad:
        return [('viajar_a_pie', conductor, ciudad)]
    else:
        for p in state.parada:
         if (ciudad in state.senda[p]) and (p in state.senda[cond]): 
            return [('viajar_a_pie', conductor, ciudad)]
    return False

def traer_conduciendo(state,conductor,ciudad):
    cond = state.ubi_conductor[conductor]
    if cond not in state.ciudad:
        return False
    else:
        for i in range(len(state.carretera)):
            if ((ciudad == state.carretera[i][0]) and (cond==state.carretera[i][1])): 
                return [('viajar_en_camion', conductor, ciudad)]
    return False

def no_traer_conductor(state,conductor,ciudad):
    cond = state.ubi_conductor[conductor]
    if cond == ciudad:
        return []
    return False

def no_conseguir_camion(state,camion,destino):
    cam=state.ubi_camion[camion]
    if cam==destino:
        return[]
    return False

def traer_camion(state,camion,destino):
    for conductor in state.conductor:
        return[ ('conseguir_conductor',conductor,destino),
                ('conductor_subir_camion', conductor, camion),
                ('viajar_en_camion',conductor, destino),
                ('conductor_bajar_camion', conductor, camion)
                ]

def func_main(state, objetos_destinos):
    for dupla in range(len(objetos_destinos)):
        print('numero de objetos '+ str(range(len(objetos_destinos))))
        objeto = objetos_destinos[dupla][0]
        destino = objetos_destinos[dupla][1]
        if objeto in state.conductor:
            return[('mover_conductor_destino', objeto, destino)]
        elif objeto in state.paquete:
            return[('mover_paquete_ciudad',objeto, destino)]
        elif objeto in state.camion:
            return[('mover_camion_ciudad',objeto, destino)]
        else:
            return []    
    return False 

def func_mover_camion_ciudad(state, conductor, camion, destino):
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
                ('viajar_en_camion',conductor, destino),
                ('conductor_bajar_camion', conductor, camion)]
    return []    



    

def func_paquete_destino(state, conductor, camion, paquete, destino):
    if destino not in state.ciudad:
        print('La ciudad '+destino+' no existe')
        return False
    elif paquete not in state.paquete:
        print('El paquete '+paquete+' no existe')
        return False

    paq = state.ubi_paquete[paquete]
    if paq != destino:
        if paq not in state.camion :
            return[ ('conseguir_camion',camion,destino),
                    ('conseguir_conductor',conductor,destino),
                    ('cargar_paquete', camion, paquete, conductor),
                    ('conductor_subir_camion', conductor, camion),
                    ('viajar_en_camion',conductor, destino),
                    ('conductor_bajar_camion', conductor, camion),
                    ('descargar_paquete', camion, paquete, conductor)
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
#pyhop.declare_methods('traer_conductor',traer_andando, traer_conduciendo)
#pyhop.declare_methods('conseguir_conductor', no_traer_conductor, traer_cond)
pyhop.declare_methods('conseguir_camion',no_conseguir_camion,traer_camion)
pyhop.declare_methods('conseguir_conductor', no_traer_conductor, traer_conduciendo,traer_andando)
pyhop.declare_methods('mover_camion_ciudad', func_mover_camion_ciudad)
pyhop.declare_methods('mover_conductor_destino', func_mover_conductor_destino)
pyhop.declare_methods('mover_paquete_ciudad', func_paquete_destino)
pyhop.declare_methods('mover_todo_destino', func_main)

#Metodos Auxiliares

    
pyhop.print_methods()




