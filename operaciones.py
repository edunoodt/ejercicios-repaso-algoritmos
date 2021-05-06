def suma (a,b):
    return a+b

def resta(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    return a/b

oper = input('Ingrese operacion, utilizando espacios entre los terminos y los símbolos:  ')
termino=''
stack=[]

for elemento in oper:
    if elemento != ' ':
        termino = termino+elemento
        
    else:
       stack.append(termino)
       termino=''
stack.append(termino)
if stack[1]=='+':
    result = suma(float(stack[0]),float(stack[2]))
elif stack[1]=='-':
    result = resta(float(stack[0]),float(stack[2]))
elif stack[1]=='*':
    result = mult(float(stack[0]),float(stack[2]))
elif stack[1]=='/':
    result = div(float(stack[0]),float(stack[2]))

print (result)