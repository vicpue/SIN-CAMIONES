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
            return [('bajar_conductor_camion', conductor, camion)]
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
        z = siguienteCiudad_camion( state, lugar , destino, camion) 
        print ("z: " + z)
        if z != 'no_conectado':
            return [ ('viajar_op_camion', camion, z), 
                     ('mover_camion_a_ciudad', camion , conductor, destino) 
                    ]
        else: # no hay conexion por carretera 
            print('No hay carretera para que el camion '+camion+' llegue a '+ destino)
            return False 
            

    # aqui nunca llegará
    return False


def func_paquete_destino()

def func_mover_conductor_destino()

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



    
pyhop.print_methods()




