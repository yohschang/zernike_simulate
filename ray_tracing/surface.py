from __future__ import division as __division__
import numpy as __np__
import matplotlib.pyplot as __plt__
from . import glass_funcs

# Ray Class

class Surface(object):
    '''
    Surface Class
    '''
    def __init__(self,wavelength_list,number,radius,thickness,glass,STO,__diameter__):
        self.wavelength_list = wavelength_list
        self.number = number
        self.radius = radius
        self.glass = glass
        self.indexlist = glass_funcs.glass2indexlist(wavelength_list,glass)
        self.thickness = thickness
        self.STO = STO
        self.__diameter__ = __diameter__
    def list(self):
        print('self_number',self.number)
        print(self.radius,self.thickness,self.indexlist)


def add(self,number,radius,thickness,glass,STO,output):
    """
    add a surface instance to a Lens Class
    input: a Lens Class
    """
    if output == True:
        s1 = str(number)
        s2 = outputjudge(radius)
        s3 = outputjudge(thickness)
        s4 = glass
        s5 = str(STO)
        print('-----------------------Add surface:-------------------------------')
        print('------------------------------------------------------------------')
        print("| {0:<5s} |  {1:<10s} |  {2:<11s} |  {3:<15s} |  {4:<5s} |".\
                    format('Num','Radius','Thickness','Glass','STO'))
        print('------------------------------------------------------------------')
        print("| {0:<5s} |  {1:<10s} |  {2:<11s} |  {3:<15s} |  {4:<5s} |".\
                    format(s1,s2,s3,s4,s5))
        print('------------------------------------------------------------------')
    else:
        print('Add surface: ',str(number))
    New_Surface = Surface(wavelength_list = self.wavelength_list,number=number,\
                            radius=radius,thickness=thickness,glass=glass,STO=STO,\
                            __diameter__=0)
    self.surface_list.append(New_Surface)

def outputjudge(number):
    if number >= 1000000 or number <= -1000000:
        s = 'Infinity'
    else:
        s = str(round(number,4))
    return s

# def update(number,key,value):
#   if key = 'STO':

#   else:
#       Lens_name.surfacelist[number].key = new_value

# def delete(number):
#   print 'delete surface x'



def list_index(self):
    print(self.indexlist)




