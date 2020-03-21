'''
Createdo on 2020 --- MUIINF

@author: Vicent Castell && Luis Ehate
'''
import pyhop

def func_main(state, objetos_destinos):
    for dupla in objetos_destinos:
        objeto = dupla[0]
        destino = dupla[1]
        if objeto in state.camion: # es un camion
            lugar_objeto = state.ubi_camion[objeto]
            if not(destino == lugar_objeto):
                vacio = 'no'
                return [
                        ('mover_camion_ciudad', objeto, vacio , destino),
                        ('mover_todo_destino', objetos_destinos )
                        ]        
        elif objeto in state.conductor: # es un conductor
            lugar_objeto = state.ubi_conductor[objeto]
            if not(destino == lugar_objeto):
                return [
                        ('mover_conductor_destino', objeto, destino),
                        ('mover_todo_destino', objetos_destinos )
                        ]  
        elif objeto in state.paquete:  # es un paquete
            lugar_objeto = state.ubi_paquete[objeto]
            if not(destino == lugar_objeto):
                return [
                        ('mover_paquete_ciudad', objeto, destino),
                        ('mover_todo_destino', objetos_destinos )
                        ] 
        else:
            print( 'Objeto seleccionado no es un camion/conductor/paquete')
            return False        
        
    return []

def func_mover_camion_ciudad(state, camion, conductor, destino):
    if destino not in state.ciudad:
        print('La ciudad '+destino+' no existe')
        return False
    if camion not in state.camion:
        print('El camion '+camion+ ' no existe')
        return False
    # si el conductor es 'no' es que no hay ningun conductor asignado 
    if ((conductor not in state.conductor) and (conductor != 'no')):
        print('El conductor '+conductor+' noexiste')
        return False

    lugar=state.ubi_camion[camion]
    if conductor =='no':
        conductor = asignarConductor(state, lugar)

    if conductor == 'no_conductores':
        print('No hay conductores disponibles en este momento')
        return False

    #bajar al camion al conductor
    if lugar == destino:
        if state.ubi_conductor[conductor] == camion:
            return [('conductor_bajar_camion', conductor, camion)]
        else:
            return[]
    if (state.ubi_conductor[conductor] != lugar) and (state.ubi_conductor[conductor] != camion): # traer conductor si no esta en la ciudad o en el camion
        return [   ('mover_conductor_destino',  conductor, lugar),
                   ('mover_camion_ciudad', camion , conductor, destino)
                ]
    if state.ubi_conductor[conductor] != camion: # estoy subido?
        return [   ('subir_conductor_camion', conductor, camion), 
                   ('mover_camion_ciudad', camion , conductor, destino)
            ]      
    if lugar != destino: # estoy subido y voy viajando
            return [ 
                     ('mover_camion_ciudad', camion , conductor, destino) 
                    ]
    else: 
            print('No hay carretera para que el camion '+camion+' llegue a '+ destino)
            return False 
            

    # aqui nunca llegará
    return False

def func_paquete_destino(state, paquete, destino):
    if destino not in state.ciudad:
        print('La ciudad '+destino+' no existe')
        return False
    elif paquete not in state.paquete:
        print('El paquete '+paquete+' no existe')
        return False

    lugarPaquete = state.ubi_paquete[paquete]
    conductor_accede_camion = 'no'
    i=0
    conductor = 'no_conductores'
    camion = 'no_camion'
    while (conductor_accede_camion == 'no') and (i<len(state.conductor)):
        conductor = seleccionarConductor(state, lugarPaquete)
        camion = seleccionarCamion(state, state.ubi_conductor[conductor])
        if (camion != 'no_camion_accesible') and (camion != 'no_camion'):
            conductor_accede_camion = 'ok'
        i+1

    if conductor == 'no_condustores':
        print("No hay coductores disponibles")
        return False
    camion = seleccionarCamion(state, lugarPaquete)
    if (camion =='no_camion') ot (camion == 'no_camion_accesible'):
        print("No hay ni conductores ni camiones disponibles")
        return False
    lugarCamion = state.ubi_camion[camion]
    if not  (lugarPaquete == destino):
        ruturn[
            ('mover_conductor_destino', conductor, lugarCamion),
            ('mover_camion_ciudad', camion, conductor, lugarPaquete),
            ('cargar_paquete', camion, paquete, conductor),
            ('mover_camion_ciudad', camion, conductor, destino),
            ('descargar_paquete', camion, paquete, conductor)
        ]         

    return []

def func_mover_conductor_destino(state, conductor, destino):
    if(destino not in state.ciudad) and (destino not in state.parada):
        print('La ciudad '+ciudad+ ' no existe')
        return False
     if conductor not in state.conductor:
         print('El conductor '+conductor+ ' no existe' )
         return False
    lugar = state.ubi_conductor[conductor]
    if lugar != destino:
        camion= seleccionarCamion(state,lugar)
        if (camion == 'no_camion'):
            print("No hay camiones disponibles")
            return False
        elif(camion == 'no_camion_accesible'):
            print("No hay camiones disponibles para el conductor asignados")
            return False
        else:
            lugarCamion = ubi_camion[camion]
            if ciudad_destino == 'no_conectado'
                print("No hay conexion por carretera")
                return False
            elif ciudad_destino = destino
                return [
                    ('mover_conductor_destino', conductor, lugarCamion),
                    ('mover_camion_ciudad', camion, conductor, destino)
                ]  
            else:
                return[
                    ('mover_conductor_destino', conductor, lugarCamion),
                    ('mover_camion_ciudad', camion, caonductor, ciudad_destino),
                    ('mover conductor_destino', conductor, destino)
                ]    
    else:
        return []
        

# Declaración de métodos
pyhop.declare_methods('mover_todo_destino', func_main)
pyhop.declare_methods('mover_camion_ciudad', func_mover_camion_ciudad)
pyhop.declare_methods('mover_conductor_destino', func_mover_conductor_destino)
pyhop.declare_methods('mover_paquete_ciudad', func_paquete_destino)


#Metodos Auxiliares

def asignarConductor(state, lugar):
    if len(state.conductor) == 0
        return 'no_conductores'
    for conductor in state.conductor:
        if state.ubi_conductor[conductor] == lugar:
            state.cola_conductores.remove(conductor)
            state.cola_conductores.insert(len(state.cola_conductores), conductor)
            return conductor
    conductor = state.cola_conductores.pop(0)
    state.cola_conductores.insert(len(state.cola_conductores), conductor)
    return conductor

def seleccionarConductor(state, lugar):
    if len(state.conductor) ==0:
        return 'no_conductores'
    for cond in state.conductor:
        if state.ubi_conductor[cond] == lugar:
            state.cola_conductores.remove(cond)
            state.cola_conductores.inser(len(state.cola_conductores) , cond)
            return cond
    cond = state.cola_conductores.pop(0)
    state.cola_conductores.insert(len(state.cola_conductores) , cond)
    return cond

def seleccionarCamion (state, lugar):
    if len(state.camion) == 0:
        return 'no_camion'
    for cam in state.camion:
        if(state.ubi_camion[cam] == lugar):
            state.cola_camiones.remove(cam)
            state.cola_camiones.insert(len(state.cola_camiones) , cam)
            return cam
    return 'no_camion_accesioble'        

    
pyhop.print_methods()




