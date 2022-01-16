import findImgElement
import printscreenout
def findBoxImgPoints(findImgRef, refaddX, refaddY,w,h,findListImgInRef,listaddX = 0,listaddY = 0,onclicked = False,
movPoint = False,movPointIniaddX = 0, movPointIniaddY = 0, movPointEndaddX = 0, movPointEndaddY = 0,qtdRepeatChk = 1,ListUni = False,goGreen = False, goRed = False,adcWork = False): #BUSCA TODOS AS BOX COM PONTOS CARACTERÍSTICOS
    #SELEÇÃO DAS COORDENADAS PRINCIPAIS DE TODAS AS TELAS.

    piniref,pcenter1,pendref = findImgElement.coordTelaXY(findImgRef)#PEGA APENAS AS COORDENADAS TOP=LEFT X/Y
    #LOOP PRINCIPAL - BOMBCRYPTO A QUAL GERENCIA TODAS AS TELAS - BOX
    if(len(piniref)>0):
        cont1 = 1 #contador da imagem
        
        for (piniref,pendref) in zip(piniref,pendref):
            contRepeatMovLoop = 0
            while contRepeatMovLoop < qtdRepeatChk:
                (xi,yi) = pendref
                
                x = int(xi)+int(refaddX)
                ############################### RETIRAR O VALOR -50 EM TELAS NORMAIS######################################
                y = int(yi)+int(refaddY)
                ############################### RETIRAR O VALOR -50 EM TELAS NORMAIS######################################
                #pyautogui.moveTo(xi,int(yi-50),0.5)
                time.sleep(2)
                #yi = int(y)
                #pyautogui.moveTo(x,y,0.5)
                #TRABALHO DENTRO DA BOX - ACHO QUE É DESNECESSÁRIO
                screen = printscreenout.printScreenBox(x,y,w,h)
                cv2.imwrite('resultados/PrintBox'+str(cont1)+'.jpg',screen)#guarda a imagem 
                screen = cv2.imread('resultados/PrintBox'+str(cont1)+'.jpg')#carrega a imagem      
                cont1 = cont1 + 1  
                #
                #findListImgInRef
                for listimg in findListImgInRef: 
                    #print(' \n Quadro n° ', cont1,' --- ',p_work_center)
                    #EVITAR O BUUG DE NÃO SELEÇÃO DO PRIMEIRO HERO LISTADO
                    pyautogui.moveTo(x=x+50,y=y+100,duration=0.5)
                    pyautogui.click()
                    
                    p_list_ini,p_list_center,p_list_end = findImgElement.findElementosScreen(screen,listimg)

                    if(len(p_list_center) > 0):
                        cont2 = 1
                        for (p_ini,p_center) in zip(p_list_ini,p_list_center):
                                                        
                            (map_x,map_y) = p_center
                            #print('-> X=',map_x,', -> Y=',map_y)
                            
                            if(onclicked):
                                pyautogui.moveTo(x+map_x+listaddX,y+map_y+listaddY,0.5)
                                pyautogui.click()
                                #pyautogui.doubleClick()
                                time.sleep(1)
                            else: 
                                pyautogui.moveTo(x+map_x+listaddX,y+map_y+listaddY,0.5)

                            #time.sleep(1)

                            if(ListUni and cont2 == 1):#SÓ QUERO QUE LIST O PRIMEIRO ELEMENTO
                                break

                            cont2 = cont2 + 1
                
                #print('ij')
                #SE ENCONTROU ALGO - PERCORRE :) = OU SEJA, TAMANHO DA LISTA É MAIOR QUE 0
                if(movPoint):
                    xmovini = x
                    ############################### RETIRAR O VALOR -50 EM TELAS NORMAIS######################################
                    ymovini = int(yi)
                    ############################### RETIRAR O VALOR -50 EM TELAS NORMAIS######################################
                    pyautogui.moveTo(x=xmovini+movPointIniaddX,y=ymovini+movPointIniaddY,duration=1)
                    #pyautogui.click()
                    pyautogui.mouseDown()
                    time.sleep(0.5)
                    xmovend = x
                    ymovend = y
                    pyautogui.moveTo(x=xmovend+movPointEndaddX,y=ymovend+movPointEndaddY,duration=1.5)
                    pyautogui.mouseUp()
                    time.sleep(1)
                    ##SÓ PARA DAR UM CLICK NO MEIO DA LISTA DE HEROES

                contRepeatMovLoop = contRepeatMovLoop + 1

        return True
    else:
        return False

##########################################################################################
def CheckLogin():
    #VERIFICA ALGUM ERRO NA TELA - DE BOTÃO OK CONECTION - PT/BR
    #checkXBack()
    while findImgElement.findTelaXY(go_conect) or findImgElement.findTelaXY(ok_bt) or findImgElement.findTelaXY(go_select_sign_meta1) or findImgElement.findTelaXY(go_select_sign_meta2): 
        findImgElement.findTelaXY(go_select_sign_meta1,True,True,-50,-200)
        sleepTime(2,'VERIFICANDO POSSÍVEL CONFIRMAÇÃO DE ASSINATURA')
        findImgElement.findTelaXY(go_select_sign_meta2,True)
        ############################CHECK INICIAL################################
        if(findImgElement.findTelaXY(ok_bt)):
            sleepTime(2,'ENCONTRAMOS UM BOTÃO OK/CONEXAO ÀS {} '.format(horarioexato()))
            findImgElement.findTelaXY(ok_bt,True)
            sleepTime(12,'IREMOS ATUALIZAR CADA UMA DA(S) PAGINA(S) :)')   
        ############################################################
        ############################VERIFICAR SE TEM BOTÃO DE CONEXÃO WALET################################
        if (findImgElement.findTelaXY(go_conect)):
            print('BOTÃO CONECT ENCONTRADO NA TELA! IREMOS DAR F5 ÀS {} '.format(horarioexato()))
            contconta = 1

            while(findImgElement.findTelaXY(go_conect)): #CLICA SO NO PRIMEIRO ENTRAR - SERÁ VERIFICADO UM POR UM
                findImgElement.findTelaXY(go_conect,True,True,0,-100,True,True) #ATUALIZA A 1° PAGINA
                sleepTime(25,'INICIANDO O LOGIN NA(S) CONTA  N° '+str(contconta)) #TEMPO CONSIDERÁVEL PARA ATUALIZAR PAGINA
                findImgElement.findTelaXY(go_conect,True,True,0,0,False,True) #CLICA APENAS NA 1° PAGINA

                sleepTime(12,'CLICANDO NO BOTÃO CONECTED N° '+str(contconta))#TEMPO CONSIDERÁVEL PARA ATUALIZAR PAGINA
                #ENQUANTO TIVER A CAIXA DE CONFIRMAÇÃO METAMASK ELE FICA AQUI DENTRO TENTANDO CLICAR.
                contx = 1

                findImgElement.findTelaXY(go_select_sign_meta2,True)
                sleepTime(3)
                while(findImgElement.findTelaXY(go_select_sign_meta1)):
                    print('Tentativa '+str(contx)+'°')
                    #sleepTime(15,'Tentativa '+str(contx)+'°')#
                    findImgElement.findTelaXY(go_select_sign_meta1,True,True,-50,-200,False,True)
                    sleepTime(3)
                    findImgElement.findTelaXY(go_select_sign_meta2,True)
                    contx = contx + 1

                contconta = contconta + 1
        
                sleepTime(2,'SE TUDO TIVER CERTO, ESTAMOS ENTRANDO NA CONTA  N° '+str(contconta))
                sleepTime(2,'SÓ AGUARDAR 100% ATÉ A TELA INICIAL :)')
##########################################################################################
def herosFullWorkIni():
    while True:
        checkXBack()
        print('FULL')
        #print('INICIANDO O PROCESSO DE SELEÇÃO DOS HEROES- ÀS {} '.format(horarioexato()))
        sleepTime(5,'INICIANDO COM TOOS OS HEROES  FULL')
        ################APENAS SELEÇÃO ALL - HEROES#############
        findImgElement.findTelaXY(go_hero_work_ini,True)
        #print('COLOCANDO OS HEROS PARA TRABALHAR')
        sleepTime(5,'COLOCANDO OS HEROS PARA TRABALHAR')
        findImgElement.findTelaXY(go_all_work,True)
        time.sleep(1.5)
        
        findImgElement.findTelaXY(x_button,True)
        print('ENTRAREMOS EM TODOS OS MAPAS')
        sleepTime(5,'ENTRAREMOS EM TODOS OS MAPAS')
        findImgElement.findTelaXY(go_map,True)
        
        print('VERIFICANDO SE NÃO TEMOS TELA INICIAL')
        sleepTime(5)
        
        if findImgElement.findTelaXY(go_hero_work_ini) or findImgElement.findTelaXY(x_button):
            continue
        else:
            return False
#######################################################################################
def heroesSelectTpIni(com = False,rare = False,supr = False,epic = False,leg = False,supleg = False):    
    find = None
    checkXBack()
    print('INICIANDO O PROCESSO DE SELEÇÃO DOS HEROES- ÀS {} '.format(horarioexato()))
    findImgElement.findTelaXY(go_hero_work_ini,True)
    sleepTime(3,'COLOCANDO OS HEROS PARA TRABALHAR')

    if(com):
        print('Comum')
        find = hero_commum

    if(rare):
        print('Raro')
        find = hero_raro    

    if(supr):
        print('SuperRaro')
        find = hero_supr

    if(epic):
        print('Epico')
        find = hero_epic

    listFind = [find]
    #150,-5
    cont = 0
    while findImgElement.findTelaXY(go_upgrade) == False and cont < 10:
        findImgElement.findTelaXY(x_button,True)
        findImgElement.findTelaXY(go_back,True)
        findImgElement.findTelaXY(go_hero_work_ini,True)
        cont = cont + 1

    findBoxImgPoints(go_upgrade,-390,-190,260,195,listFind,120,-10,True,True,20,-5,0,18,3)
    cont = 0
    while (findImgElement.findTelaXY(x_button) or findImgElement.findTelaXY(go_map)) and cont > 10:
        findImgElement.findTelaXY(x_button,True)
        time.sleep(1)
        findImgElement.findTelaXY(go_map,True)
        cont = cont + 1
    
    findImgElement.findTelaXY(x_button,True)
    time.sleep(1)
    findImgElement.findTelaXY(go_map,True)

def updateMapaHero():
    sleepTime(5,'Atualizando Posição no Mapa')
    findImgElement.findTelaXY(go_back,True)
    sleepTime(2)
    findImgElement.findTelaXY(x_button,True)
    sleepTime(2)
    findImgElement.findTelaXY(go_map,True)

def newMap():
    sleepTime(5,'Abrindo o Próximo Mapa')
    checkXBack()
    findImgElement.findTelaXY(go_new_map,True)

def reloadContas():
    sleepTime(5,'VAMOS REINICIAR TODAS AS CONTAS F5')
    checkXBack()
    #sys.stdout.write('\n VAMOS REINICIAR TODAS AS CONTAS  - ÀS {} '.format(horarioexato()))
    
    findImgElement.findTelaXY(go_hero_work_ini,True)
    sleepTime(2)
    findImgElement.findTelaXY(go_all_nowork,True)
    sleepTime(2)
    #newMap()
    #time.sleep(1.5)
    checkXBack()
    findImgElement.findTelaXY(go_hero_work_ini,True,False,0,-100,True) # CLICA ACIMA E ATUALIZA
    CheckLogin()
 ################FUNÇÕES AUXILIARES#############   
def checkXBack():
    while(findImgElement.findTelaXY(go_back) or findImgElement.findTelaXY(x_button)):
        findImgElement.findTelaXY(x_button,True)
        sleepTime(2)
        findImgElement.findTelaXY(go_back,True)
        sleepTime(2)

def sleepTime(qtdseg = 1, info_msg = ''):
    #sys.stdout.write('Será necessário aguardar '+str(y)+'s')
    for x in range((qtdseg), 0,-1):
        print(f'{"Aguarde: "+str(x)} seg. ### {info_msg} \r', end="")
        time.sleep(1) 