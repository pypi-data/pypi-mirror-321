from re import I

import sympy

import IPython

#global DatosList,Documento,Orden,Color

#DatosList = []

#Documento = []

#Orden = 0

#global Color

#Color = "black"

#https://widdowquinn.github.io/coding/update-pypi-package/

#_print_Symbol

from AutoMindCloud.latemix import *

def Inicializar(n,color):

  global DatosList,Orden,Color#Documento
  
  DatosList = []

  #Documento = []

  Orden = n

  Color = color

  return DatosList
  
def search(symbolo):

  #global DatosList,Orden,Color#Documento

  for c_element in DatosList:
    if c_element[0] == symbolo:
      if isinstance(c_element[1],float):#Si tenemos un numero
          return "("+str(c_element[1])+")"
      elif isinstance(c_element[1],int):#Si tenemos un float
          return "("+str(c_element[1])+")"
      elif c_element[1] != None:#Si tenemos una expresión
          return "("+sympy.latex(c_element[1])+")"
      else:
        return sympy.latex(symbolo)#Si es None
  return sympy.latex(symbolo)

def Redondear(expr):#Redondeamos la expresión.
  if isinstance(expr, sympy.Expr) or isinstance(expr, sympy.Float):
    Aproximacion = expr.xreplace(sympy.core.rules.Transform(lambda x: x.round(Orden), lambda x: isinstance(x, sympy.Float)))
  elif isinstance(expr,float) or isinstance(expr,int):
    Aproximacion = round(expr,Orden)
  else:
    Aproximacion = expr
  return Aproximacion

def S(c_componente):#Guardar
  global DatosList,Orden,Color#Documento
  dentro = False
  for element in DatosList:

    #Si es un elemento None, entonces guardamos de forma especial:
    if element[1] == None:
      element[1] = element[0]

    if element[0] == c_componente[0]:
      element[1] = c_componente[1]
      dentro = True#Si el elemento ha sido guardado antes, entonces no lo volvemos a ingresar. Sino que sobre escribimos lo que dicho
      #componente significaba con el valor actual que se desea guardar.

      
  if dentro == False:
    
    DatosList.append(c_componente)#Si el elemento no estaba adentro, simplemente lo agregamos.

  #Renderizado Gris
  if c_componente[1] == None or dentro == False:
    D(c_componente)#Hacemos un print renderizado en color gris para indicar que el elemento ha sido definido/guardado
  else:
    D(c_componente)#Hacemos un print renderizado en color gris para indicar que el elemento ha sido definido/guardado

def D(elemento):#Por default se imprime en rojo, para indicar que es un derivado.
  #global DatosList,Orden,Color#Documento

  print("")
  Tipo = None
  if isinstance(elemento,sympy.core.relational.Equality):#Si el elemento ingresado es una ecuación, entonces la identificamos
    Tipo = "Ecuacion"
  elif isinstance(elemento,list):#Si el elemento ingresado es un componente, entonces lo identificamos.
    Tipo = "Componente"
    c_componente = elemento
  
  if Tipo == "Ecuacion":#Si hemos identificado el elemento ingresado como una ecuación, entonces la imprimimos en rojo

    a = sympy.latex(elemento.args[0])

    b = "="

    c = sympy.latex(elemento.args[1])

    texto = a + b + c
    #texto = texto.replace("text", Estilo)

    IPython.display.display(IPython.display.Latex("$\\textcolor{"+Color+"}{"+texto+"}$"))
    #Documento.append(texto)

  if Tipo == "Componente":#Si hemos identificado el elemento ingresado como un componente, entonces lo imprimimos en rojo


    #if not isinstance(c_componente[0],str):#isinstance(c_componente[0],sy.core.symbol.Symbol) or isinstance(c_componente[0],sy.core.symbol.Symbol) :
    a = sympy.latex(c_componente[0])

    b = " = "

    if c_componente[1] == c_componente[0]:#== None:<---------------------------------------------------------------------------------------------------------------------------
      c = "?"
    else:
      c = sympy.latex(Redondear(c_componente[1]))
    
    texto = a + b + c
      #texto = texto.replace("text", Estilo)
    IPython.display.display(IPython.display.Latex("$\\textcolor{"+Color+"}{"+texto+"}$"))
    #Documento.append(texto)


def R(string):
  #global DatosList,Orden,Color#Documento
  IPython.display.display(IPython.display.Latex("$\\textcolor{"+Color+"}{"+string+"}$"))

def E(expr):
  
  print("")

  global DatosList,Orden,Color#Documento
  
  IPython.display.display(IPython.display.Latex("$\\textcolor{"+Color+"}{"+"400"+"}$"))

  if isinstance(expr,sympy.core.relational.Equality):#Si tenemos una igualdad
    izquierda = expr.args[0]
    derecha = expr.args[1]
    texto = latemix(izquierda) + " = " + latemix(derecha)

    return IPython.display.display(IPython.display.Latex("$\\textcolor{"+Color+"}{"+texto+"}$"))
  elif isinstance(expr,list):#Si tenemos un componente
    texto = sympy.latex(expr[0]) + " = " + latemix(expr[1])
    return IPython.display.display(IPython.display.Latex("$\\textcolor{"+Color+"}{"+texto+"}$"))
  elif isinstance(expr,sympy.core.mul.Mul):
    texto = latemix(expr)
    return IPython.display.display(IPython.display.Latex("$\\textcolor{"+Color+"}{"+texto+"}$"))


