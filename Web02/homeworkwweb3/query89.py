import mlab
from models.river import River

mlab7.connect()

#Ex8

river_in_Africa = River.objects(continent = "Africa")

print(river_in_Africa)

#Ex9

river_less_than_1000 = River.objects(continent ="S. America",length__lt = 1000)

print(river_less_than_1000)