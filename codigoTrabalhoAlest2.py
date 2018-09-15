from datetime import datetime
saida = ""
index = 0
cont = 1
max = 0



#####################################METODOS########################################3

def faz_a_magica_left(pre, cent, cont, index):
    aux = cent.index(pre[index])
    tal = cent[cent.index(pre[index])]


    if cent[:aux - 1] != None:
            cent_left = cent[:aux - 1]
            pre = pre[1:]
            cont += 1
            index += 1
            print(cent)
            if pre[index] in cent:
                return faz_a_magica_left(pre, cent_left, cont, index)

    cont -= 1
    return cont



def faz_a_magica_right(pre, cent, cont, index):
    aux = cent.index(pre[index])
    tal = cent[cent.index(pre[index])]

    if pre[index]in cent:
        if cent[aux + 1:] != None:
            cent_rigth = cent[aux + 1:]
            pre = pre[1:]
            cont += 1
            index += 1
            print(cent)
            return faz_a_magica_right(pre, cent_rigth, cont, index)
    cont -= 1
    return cont

'''
def faz_a_magica(pre, cent, cont, index):
    aux = cent.index(pre[index])
    tal = cent[cent.index(pre[index])]

    if pre[index] in cent:
        if cent[:aux - 1] != None:
            cent_left = cent[:aux - 1]
            pre = pre[1:]
            cont += 1
            index += 1
            print(cent)
            return faz_a_magica(pre, cent_left, cont, index)
    print(cent)

    if pre[index]in cent:
        if cent[aux + 1:] != None:
            cent_rigth = cent[aux + 1:]
            pre = pre[1:]
            cont += 1
            index += 1
            print(cent)
            return faz_a_magica(pre, cent_rigth, cont, index)


    cont -= 1
    return cont
'''
'''
def faz_a_magica(pre, cent, cont, index):
    aux = cent.index(pre[index])
    tal = cent[cent.index(pre[index])]
    if pre[index] in cent:

        index +=1
        centL = cent[:aux-1]
        if centL != None or centL != " ":
            cont += 1
            faz_a_magica(pre,centL,cont,index)
        centR = cent[aux + 1:]
        if centR != None:
            cont += 1
            faz_a_magica(pre, centR, cont, index)
        cont -= 1
    return cont

'''
def faz_a_magica(pre,cent):
    global index, cont
    global max
    #print('index' +str(index))
    target = pre[index]
    #print('pre ' + str(pre))
    #print('estou na palavra: ' + target)
    #print('lista central '+cent)
    #print('nivel'+str(cont))
    #print('max' + str(max))
    
    if target in cent:
        here = target
        index+=1
        cent_esquera= cent[:cent.index(here)]
        #print('centralE: ' + str(cent_esquera))
        cent_direita = cent[cent.index(here)+1:]
        #print('centralD: ' + str(cent_direita))
        #print()
        if cont > max:
            max = cont
            #print(max)
        #if target in cent_esquera:
        if len(cent_esquera)>0:
            cont += 1
            faz_a_magica(pre,cent_esquera)
        
        #if target in cent_direita:
        if len(cent_direita)>0:
            cont += 1
            faz_a_magica(pre,cent_direita)

    
    cont -= 1
    return max

############################## MAIN ##########################################


with open(r"casos_t1/caso50.txt", "r") as tal:
    for i in tal: saida += i

arquivo_dividido = saida.split('\n')

pre = arquivo_dividido[0].split(' ')#.replace(" ","") tenho que resolver dos espacos

cent = arquivo_dividido[1].split(' ')#.replace(" ","")
#print(pre +'\n'+cent);exit()
#print('pre '+pre)
#for i in pre:
#    print(str(i)+' '+str(cont))
#    cont+=1
#exit()
inicio = datetime.now().microsecond
faz_a_magica(pre, cent)
print('Total de niveis: '+ str(max))
fim = datetime.now().time().microsecond
print('inicio: '+str(inicio)+ ' microsegundos')
print('fim: ' + str(fim)+ ' microsegundos')
print('total de tempo: '+ str((int(str(fim))-int(str(inicio)))/1000000.0)+' em segundos')

#faz_a_magica_left(pre, cent, cont, index)

#faz_a_magica_right(pre, cent, cont, index)
