print('Car brands available')
print('(1)Toyota',
      '(2)Nissan',
      '(3)Mazda',
      '(4)Jeep',
      '(5)Honda',
      '(6)Hyundai',
      '(7)BMW',
      '(8)Mercedes Benz',
      '(9)Daewoo',
      '(10)Tesla',
      '(11)Renault',
      '(12)Tata',
      '(13)Audi',
      '(14)Kia',
      '(15)Porsche',
      '(16)Volkswagen')

brand=int(input('Enter the number of your preferred car: '))
M= ['Camry','Corolla'] 
if brand ==1:
   print('The Toyota Cars Available are {} and {}'.format(M[0],M[1]))

data=[['Camry',30400],['Corolla',25000]]
model_1=str(input('Specify the model: '))

if model_1=='Camry':
   print('This car costs {}.'.format(data[0][1]))
elif model_1=='Corolla':
   print('This car costs {}.'.format(data[1][1]))
   

N= ['Patrol','Navarra'] 
if brand ==2:
  print('The Nissan Cars Available are {} and {}'.format(N[0],N[1]))

data_2=[['Patrol',40000],['Navarra',35000]]
model_2=str(input('Specify the model: '))

if model_2=='Patrol':
   print('This car costs {}.'.format(data[0][1]))
elif model_2=='Navarra':
   print('This car costs {}.'.format(data[1][1])) 
   

O= ['BT50','CX 5']
if brand ==3:
  print('The Mazda Cars Available are {} and {}'.format(O[0],O[1]))

data_3=[['BT50',10000],['CX 5',20000]]
model_3=str(input('Specify the model: '))

if model_3=='BT50':
   print('This car costs {}.'.format(data[0][1]))
elif model_3=='CX 5':
   print('This car costs {}.'.format(data[1][1]))

P=['Wrangler','Grand Cherokee']
if brand ==4:
   print('The Mazda Cars Available are {} and {}'.format(P[0],P[1]))

data=[['Wrangler',42000],['Grand Cherokee',23000]]
model_4=str(input('Specify the model: '))

if model_4=='Wrangler':
   print('This car costs {}.'.format(data[0][1]))
elif model_4=='Grand Cherokee':
   print('This car costs {}.'.format(data[1][1]))  


Q=['Civic','CRV']
if brand ==5:
  print('The Honda Cars Available are {} and {}'.format(Q[0],Q[1]))

data=[['Civic',60000],['CRV',55000]]
model_5=str(input('Specify the model: '))

if model_5=='Civic':
   print('This car costs {}.'.format(data[0][1]))
elif model_5=='CRV':
   print('This car costs {}.'.format(data[1][1]))   
   
R=['Elantra','Lantra']   
if brand ==6:
  print('The Hyundai Cars Available are {} and {}'.format(R[0],R[1]))

data=[['Elantra',15000],['Lantra',5000]]
model_6=str(input('Specify the model: '))

if model_6=='Elantra':
   print('This car costs {}.'.format(data[0][1]))
elif model_6=='Lantra':
   print('This car costs {}.'.format(data[1][1]))
   
S= ['X5','X1']
if brand ==7:
   print('The Mazda Cars Available are {} and {}'.format(S[0],S[1]))

data=[['X5',130000],['X1',90000]]
model_7=str(input('Specify the model: '))

if model_7=='X5':
   print('This car costs {}.'.format(data[0][1]))
elif model_7=='X1':
   print('This car costs {}.'.format(data[1][1]))

T=['A-Class','C-Class']
if brand ==8:
   print('The Mercedes Benz Cars Available are {} and {}'.format(T[0],T[1]))

data=[['A-Class',230000],['C-Class',200000]]
model_8=str(input('Specify the model: '))

if model_8=='A-Class':
   print('This car costs {}.'.format(data[0][1]))
elif model_8=='C-Class':
   print('This car costs {}.'.format(data[1][1]))

U=['Matiz','Labo']
if brand ==9:
   print('The Daewoo Cars Available are {} and {}'.format(U[0],U[1]))

data=[['Matiz',30000],['Labo',22000]]
model_9=str(input('Specify the model: '))

if model_9=='Matiz':
   print('This car costs {}.'.format(data[0][1]))
elif model_9=='Labo':
   print('This car costs {}.'.format(data[1][1]))

V=['Model Y','Model 3']
if brand ==10:
   print('The Tesla Cars Available are {} and {}'.format(V[0],V[1]))

data=[['Model Y',130000],['Model 3',122000]]
model_10=str(input('Specify the model: '))

if model_10=='Model Y':
   print('This car costs {}.'.format(data[0][1]))
elif model_10=='Model 3':
   print('This car costs {}.'.format(data[1][1]))

A=['Duster','Sandero']
if brand ==11:
   print('The Renault Cars Available are {} and {}'.format(A[0],A[1]))

data=[['Duster',60000],['Sandero',20000]]
model_11=str(input('Specify the model: '))

if model_11=='Duster':
   print('This car costs {}.'.format(data[0][1]))
elif model_11=='Sandero':
   print('This car costs {}.'.format(data[1][1]))

B=['Safari','Harrier']
if brand ==12:
   print('The Tata Cars Available are {} and {}'.format(B[0],B[1]))

data=[['Safari',10000],['Harrier',11000]]
model_12=str(input('Specify the model: '))

if model_12=='Safari':
   print('This car costs {}.'.format(data[0][1]))
elif model_12=='Harrier':
   print('This car costs {}.'.format(data[1][1]))


C=['A4','A6']
if brand ==13:
   print('The Audi Cars Available are {} and {}'.format(C[0],C[1]))

data=[['A4',60000],['A6',120000]]
model_13=str(input('Specify the model: '))

if model_13=='A4':
   print('This car costs {}.'.format(data[0][1]))
elif model_13=='A6':
   print('This car costs {}.'.format(data[1][1]))
   
D=['SantaFek','Sorento']   
if brand ==14:
   print('The Kia Cars Available are {} and {}'.format(D[0],D[1]))

data=[['SantaFek',70000],['Sorento',85000]]
model_14=str(input('Specify the model: '))

if model_14=='SantaFek':
   print('This car costs {}.'.format(data[0][1]))
elif model_14=='Sorento':
   print('This car costs {}.'.format(data[1][1]))
   
F= ['Beetle','Polo']
if brand ==15:
   print('The Volkswagen Cars Available are {} and {}'.format(F[0],F[1]))

data=[['Beetle',34000],['Polo',60000]]
model_15=str(input('Specify the model: '))

if model_15=='Beetle':
   print('This car costs {}.'.format(data[0][1]))
elif model_15=='Polo':
   print('This car costs {}.'.format(data[1][1])) 
   
#https://github.com/Akwasidk03/akwasi-scode.git   


   
