import json

data=[
    {"nombre":"Camilo Diaz"     , "edad": 20, "codigo": "001", "clave": 123},
    {"nombre":"Maria Jimenez"   , "edad": 15, "codigo": "002", "clave": 345},
    {"nombre":"Lesly Correa"    , "edad": 19, "codigo": "003", "clave": 578},
    {"nombre":"Nicolas Cortes"  , "edad": 25, "codigo": "004", "clave": 891},
    {"nombre":"Norberto Cortes" , "edad": 19, "codigo": "005", "clave": 234},
    {"nombre":"Stephen smith"   , "edad": 21, "codigo": "006", "clave": 567},
    {"nombre":"Carlos Ramirez"  , "edad": 35, "codigo": "007", "clave": 741},
    {"nombre":"Juan Palacio"    , "edad": 45, "codigo": "008", "clave": 912},
    {"nombre":"Alma Perez"      , "edad": 60, "codigo": "009", "clave": 963},
    {"nombre":"Sara Fernandez"  , "edad": 18, "codigo": "010", "clave": 678},
    {"nombre":"Sofia Montes"    , "edad": 24, "codigo": "011", "clave": 852}
]





nombreArchivo="usuario.json"
ruta="proyecto/" + nombreArchivo
opcion="w"

with open(ruta, opcion) as file:
    json.dump(data, file)