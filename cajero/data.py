data=[
    {"nombre":"Camilo Diaz"     , "edad": 20, "documento": 142, "clave":123, "salario":100},
    {"nombre":"Maria Jimenez"   , "edad": 15, "documento": 24, "clave": 345, "salario":50},
    {"nombre":"Lesly Correa"    , "edad": 19, "documento": 34, "clave": 578, "salario":650},
    {"nombre":"Nicolas Cortes"  , "edad": 25, "documento": 44, "clave": 891, "salario":340},
    {"nombre":"Norberto Cortes" , "edad": 19, "documento": 54, "clave": 234, "salario":3540},
    {"nombre":"Stephen smith"   , "edad": 21, "documento": 64, "clave": 567, "salario":3540},
    {"nombre":"Carlos Ramirez"  , "edad": 35, "documento": 74, "clave": 741, "salario":450},
    {"nombre":"Juan Palacio"    , "edad": 45, "documento": 84, "clave": 912, "salario":1320},
    {"nombre":"Alma Perez"      , "edad": 60, "documento": 94, "clave": 963, "salario":35410},
    {"nombre":"Sara Fernandez"  , "edad": 18, "documento": 40, "clave": 678, "salario":145410},
    {"nombre":"Sofia Montes"    , "edad": 24, "documento": 15, "clave": 852, "salario":5450}
]

import json

nombreArchivo="datosUsuarios.json"
ruta="cajero/"+ nombreArchivo

with open(ruta, "w") as file:
    json.dump(data,file)

