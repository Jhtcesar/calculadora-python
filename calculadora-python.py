#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print('Bem-vindo(a) à calculadora!')


# In[ ]:


operacao = input("\nEscolha uma operação abaixo:\n\nSoma (+)\nSubtração (-)\nMultiplicação (*)\nDivisão (/)\n\n")


# In[ ]:


while True: 
        try:
            firstnum = float(input("\nInsira o primeiro número: "))
            break
            
        except ValueError:
                    print("\nCaracter inválido!")


# In[ ]:


while True: 
        try:
            secondnum = float(input("Insira o segundo número: "))
            break
            
        except ValueError:
                    print("\nCaracter inválido!")


# In[ ]:


def som(firstnum, secondnum):
        print("\nO resultado é:", float(firstnum + secondnum))
    
def sub(firstnum, secondnum):
        print("\nO resultado é:", float(firstnum - secondnum))
        

def mult(firstnum, secondnum):
        print("\nO resultado é:", float(firstnum * secondnum))
        
    
def div(firstnum, secondnum):
        while True: 
                try:
        
                    firstnum / secondnum == 0
                    print("\nO resultado é:", float(firstnum / secondnum))
                    break
    
                except ZeroDivisionError:
                    print("\nErro de divisão por zero!")
                    break


# In[ ]:


if operacao == "+":
    som(firstnum, secondnum)
    
elif operacao == "-":
    sub(firstnum, secondnum)

elif operacao == "*":
    mult(firstnum, secondnum)

elif operacao == "/":
    div(firstnum, secondnum)
              
else:
    print("\nOperação inválida!")


# In[ ]:


input('\nPressione (Enter) para sair.')

