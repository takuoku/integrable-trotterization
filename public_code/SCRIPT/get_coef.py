import sys
sys.path.append(sys.path[0]+'/../GENERATED')
import parameters as para
import os
import shutil
import numpy as np
path = os.getcwd() 


# definitions
def generate_charge_coef(deg):
    with open(path +f'/MEAS_MATERIAL/q{deg}_plus_coefficients.dat','r') as f:
        content = f.readlines()

    with open(path +f'/GENERATED/coefficients.dat','w') as g:
      for line in content:
        sp = line.split('\t')
        beg = sp[0] +  '\t' + sp[1] + '\t'
        if sp[2][-1] == '\n':
          long_word = sp[2][:-1]
        else:
          long_word = sp[2]
        for i in range(para.site-2*deg-1):
          long_word = long_word + 'I'
        for i in range(para.site//2):
          new_line = beg
          for j in range(para.site):
            new_line = new_line + long_word[(j+2*i) % para.site]
          g.write(new_line+'\n')
    return path +f'/GENERATED/coefficients.dat'

def generate_char_dif_coef(deg):
  with open(path +f'/q{deg}_plus_coefficients.dat','r') as f:
    content = f.readlines()
  with open(path +f'/GENERATED/coefficients.dat','w') as g:
    data_dict = {}
    for line in content:
      sp = line.split('\t')
      if sp[2][-1] == '\n':
        long_op = sp[2][:-1]
      else:
        long_op = sp[2]
      for i in range(para.site-2*deg-1):
        long_op = long_op + 'I' 
      
      for i in range(para.site//2):
        new_op = ''
        for j in range(para.site):
          new_op = new_op + long_op[(j+2*i) % para.site]
        if not (new_op,int(sp[0])) in data_dict.keys():
            data_dict.update( { (new_op,int(sp[0])) : int(sp[1]) } )
        else: 
            data_dict.update( { (new_op,int(sp[0])) : data_dict[(new_op,int(sp[0]))] + int(sp[1]) } )  
      
      for i in range(para.site//2):
        new_op = ''
        for j in range(para.site):
          new_op = new_op + long_op[(j+1+2*i) % para.site]
        if not (new_op,int(sp[0])) in data_dict.keys():
            data_dict.update( { (new_op,int(sp[0])) : -((-1)**int(sp[0]))*int(sp[1]) } )
        else:
            data_dict.update( { (new_op,int(sp[0])) : data_dict[(new_op,int(sp[0]))] -((-1)**int(sp[0]))*int(sp[1]) } )
        
    for key in data_dict.keys():
        if data_dict[key] != 0:
            g.write(str(key[1]-1) + '\t' + str(data_dict[key]) + '\t' + key[0] + '\n')
  return path +f'/GENERATED/coefficients.dat'

def pauli_prod(op1,op2):
    if op1=='I' and op2=='I': return ['I',1]
    if op1=='X' and op2=='X': return ['I',1]
    if op1=='Y' and op2=='Y': return ['I',1]
    if op1=='Z' and op2=='Z': return ['I',1]
    if op1=='I' and op2=='X': return ['X',1]
    if op1=='I' and op2=='Y': return ['Y',1]
    if op1=='I' and op2=='Z': return ['Z',1]
    if op1=='X' and op2=='I': return ['X',1]
    if op1=='Y' and op2=='I': return ['Y',1]
    if op1=='Z' and op2=='I': return ['Z',1]
    if op1=='X' and op2=='Y': return ['Z',1j]
    if op1=='Y' and op2=='Z': return ['X',1j]
    if op1=='Z' and op2=='X': return ['Y',1j]
    if op1=='X' and op2=='Z': return ['Y',-1j]
    if op1=='Y' and op2=='X': return ['Z',-1j]
    if op1=='Z' and op2=='Y': return ['X',-1j]


def pauliopexp(pauliop,ini_st):
  exp = 1
  for position in range(len(pauliop)):
    if pauliop[position] == ini_st[position][1]:
        exp *= (-1)**ini_st[position][0]
    if pauliop[position] == "I": 
        continue
    if pauliop[position] != "I" and pauliop[position] != ini_st[position][1]:
        exp = 0
        break
  return exp 

# (re)generate observables
if para.observable_to_compute == 'charge':
    generate_charge_coef(para.degree_of_density)

if para.observable_to_compute == 'char_dif': 
    generate_char_dif_coef(para.degree_of_density)