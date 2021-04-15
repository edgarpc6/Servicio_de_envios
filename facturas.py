from paquete import paquetesl
from clientes import clientel
from datetime import datetime

factural =[
    {"id":0,"total":11850.0,"fecha":datetime.now(),"cliente":clientel[0],"items":[paquetesl[0],paquetesl[2]]},
    {"id":1,"total":17840.0,"fecha":datetime.now(),"cliente":clientel[6],"items":[paquetesl[1],paquetesl[5]]},
    {"id":2,"total":17100.0,"fecha":datetime.now(),"cliente":clientel[4],"items":[paquetesl[4]]},
    {"id":3,"total":16000.0,"fecha":datetime.now(),"cliente":clientel[2],"items":[paquetesl[6]]},
    {"id":4,"total":26450.0,"fecha":datetime.now(),"cliente":clientel[1],"items":[paquetesl[4],paquetesl[1]]},
    {"id":5,"total":7550.0,"fecha":datetime.now(),"cliente":clientel[3],"items":[paquetesl[3]]},
    {"id":6,"total":5940.0,"fecha":datetime.now(),"cliente":clientel[5],"items":[paquetesl[5]]}
]