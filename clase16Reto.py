# Control de Flujo en Python

# Estructuras condicionales - RETO

# RETO piedra, papel o tijera

import random

computers_wins = 0
user_wins = 0

options = ('piedra', 'papel', 'tijera')

rounds = 1

while True:

  #print('*' * 10)
  print('ROUND =>', rounds)
  #print('*' * 10)

  print('COMPUTADORA: ', computers_wins)
  print('    USUARIO: ', user_wins)

  user_option = input('piedra, papel o tijera => ')
  user_option = user_option.lower()

  rounds += 1
  
  if not user_option in options:
    print('Esa opción no es válida')
    continue 
    #exit() #buen tip de los comentarios
  
  computer_option = random.choice(options) #tambien podemos usar una lista en lugar de una tupla
  
  print('    User option =>', user_option)
  print('Computer option =>', computer_option)
  
  if user_option == computer_option:
    print('*' * 16)
    print('*   EMPATE   *')
    print('*' * 16)
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('piedra gana a tijera')
      print('*' * 16)
      print('* USUARIO GANO *')
      print('*' * 16)
      user_wins += 1
    else:
      print('papel le gana a piedra')
      print('*' * 19)
      print('* COMPUTADORA GANO *')
      print('*' * 19)
      computers_wins += 1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('papel le gana a piedra')
      print('*' * 16)
      print('* USUARIO GANO *')
      print('*' * 16)
      user_wins += 1
    else:
      print('tijera gana a papel')
      print('*' * 19)
      print('* COMPUTADORA GANO *')
      print('*' * 19)
      computers_wins += 1
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('tijera gana a papel')
      print('*' * 16)
      print('* USUARIO GANO *')
      print('*' * 16)
      user_wins += 1
    else:
      print('piedra gana a tijera')
      print('*' * 19)
      print('* COMPUTADORA GANO *')
      print('*' * 19)
      computers_wins += 1
  
  if computers_wins == 3:
    print('------------LA COMPUTADORA GANO--------------')
    break
  if user_wins == 3:
    print('-----------------TU GANASTE------------------')
    break