data=[
    {"nombre":"Camilo Diaz"     , "edad": 20, "documento": 142, "clave": 123},
    {"nombre":"Maria Jimenez"   , "edad": 15, "documento": 24, "clave": 345},
    {"nombre":"Lesly Correa"    , "edad": 19, "documento": 34, "clave": 578},
    {"nombre":"Nicolas Cortes"  , "edad": 25, "documento": 44, "clave": 891},
    {"nombre":"Norberto Cortes" , "edad": 19, "documento": 54, "clave": 234},
    {"nombre":"Stephen smith"   , "edad": 21, "documento": 64, "clave": 567},
    {"nombre":"Carlos Ramirez"  , "edad": 35, "documento": 74, "clave": 741},
    {"nombre":"Juan Palacio"    , "edad": 45, "documento": 84, "clave": 912},
    {"nombre":"Alma Perez"      , "edad": 60, "documento": 94, "clave": 963},
    {"nombre":"Sara Fernandez"  , "edad": 18, "documento": 40, "clave": 678},
    {"nombre":"Sofia Montes"    , "edad": 24, "documento": 15, "clave": 852}
]

import json

nombreArchivo="dataUsuarios.json"
ruta="cajero/"+ nombreArchivo

with open(ruta, "w") as file:
    json.dump(data,file)

