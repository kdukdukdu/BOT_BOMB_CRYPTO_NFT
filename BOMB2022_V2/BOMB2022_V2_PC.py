from ast import Break
import time
import cv2 as cv2
import numpy
from matplotlib import pyplot as plt
import pyautogui
from datetime import datetime
import sys
############
import mss
import yaml
import random

if __name__ == '__main__': 
    stream = open("config.yaml", 'r')# LÊ AS CONNFIGURAÇÕES O ARQUIVO
    config = yaml.safe_load(stream)
    c_time_loop = config['time_intervals']
    
    go_conect = cv2.imread('targets/new50/login_assinar_meta/connect.png')#Botão para Iniciar o Jogo
    go_select_sign_meta1 = cv2.imread('targets/new50/login_assinar_meta/assina1.png')#Botao para Confirmar na Metamask
    go_select_sign_meta2 = cv2.imread('targets/new50/login_assinar_meta/assinar2.png')#Botao para Confirmar na Metamask

    go_map = cv2.imread('targets/new50/treasure-hunt-icon.png')#botão entrar no jogo
    go_back = cv2.imread('targets/new50/voltar.png')#botão voltar pagina
    x_button = cv2.imread('targets/new50/x.png')#botão fechar
    go_hero_work_ini = cv2.imread('targets/new50/heroes.png')#botão selecao hero

    tela_ini1 = cv2.imread('targets/new50/findbox/telaini1.png')#botão voltar pagina
    tela_ini2 = cv2.imread('targets/new50/findbox/telaini2.png')#botão voltar pagina
    tela_work1 = cv2.imread('targets/new50/findbox/telawork1.png')
    tela_work2 = cv2.imread('targets/new50/findbox/telawork2.png')


    hero_epic = cv2.imread('targets/new50/heroes/hero_epico.png')#botão voltar pagina
    hero_supr = cv2.imread('targets/new50/heroes/hero_supraro.png')#botão voltar pagina
    hero_raro = cv2.imread('targets/new50/heroes/raro.png')#botão voltar pagina
    hero_commum = cv2.imread('targets/new50/heroes/commun.png')#botão voltar pagina
    workgreen = cv2.imread('targets/new50/heroes/workgreen.png')#botão voltar pagina
    noworkred = cv2.imread('targets/new50/heroes/noworkred.png')#botão voltar pagina

    hero_rest = cv2.imread('targets/new50/heroes/rest_hero.png')#botão voltar pagina
    go_work = cv2.imread('targets/new50/heroes/work.png')#botao colocar pra trabalhar
    go_home = cv2.imread('targets/new50/heroes/home.png')#botao colocar pra trabalhar
    go_upgrade = cv2.imread('targets/new50/heroes/upgrade.png')#botao colocar pra trabalhar
    
    go_rest_nowork = cv2.imread('targets/new50/heroes/rest_hero.png')#botao colocar pra trabalhar
    go_all_work = cv2.imread('targets/new50/heroes/go_all_work.png')#botão selecao hero
    go_all_nowork = cv2.imread('targets/new50/heroes/go_all_nowork.png')#botão selecao hero
    
    go_new_map = cv2.imread('targets/new50/mapa/new-map.png')#botão ok
    go_select_hero1 = cv2.imread('targets/new50/mapa/select-hero1.png')#botão selecao hero
    go_select_hero11 = cv2.imread('targets/new50/mapa/select-hero2.png')#botão selecao hero   
    go_hero_work_map = cv2.imread('targets/new50/mapa/heroes.png')#botão selecao hero
    
    bau_d1 = cv2.imread('targets/new50/mapa/dourado_teste/1.png')#buscar bau d
    bau_d2 = cv2.imread('targets/new50/mapa/dourado_teste/2.png')#buscar bau d

    bau_m1 = cv2.imread('targets/new50/mapa/madeira_teste/1.png')#buscar bau d
    bau_m2 = cv2.imread('targets/new50/mapa/madeira_teste/2.png')#buscar bau d
    
    ok_bt = cv2.imread('targets/new50/erro/ok.png')#botão ok
###########################SCREEM TELA & BOX########################################
def printScreenTela():
    with mss.mss() as sct:
        # Não entendi o motivo deste comando
        monitor = {"top": 160, "left": 160, "width": 1000, "height": 135}

        sct_img = numpy.array(sct.grab(sct.monitors[0]))
        return sct_img[:,:,:3]

def printScreenBox(x,y,w,h):
    with mss.mss() as sct:
        # The screen part to capture
        monitor = {"top": y, "left": x, "width": w, "height": h}
        # Grab the data
        sct_img = numpy.array(sct.grab(monitor))
        return sct_img[:,:,:3]    

###################################################################
def Scroll(scroolnum = -100):#Padrão Baixo
    last = 1
    while last < 21:
        #carregando todos os usuarios
        pyautogui.scroll(scroolnum)
        if(last == 21):
            time.sleep(0.3)
            break

        last = last + 1
        time.sleep(0.1)
##########################################################################################

#################################VERSÃO 2022###########################################
def horarioexato():
    return datetime.today().strftime("%Hh%Mmin%Ss DO DIA %d/%m/%Y")

def findElementosScreen(screen,find_in_inscreen, threshold=0.85, debug_mode='rectangles'):
    result = cv2.matchTemplate(screen, find_in_inscreen, cv2.TM_CCOEFF_NORMED)
    #Pega os valores max_val -> % de acerto na Busca, Max_loc --> coordenada X,Y encontrada
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val >= threshold:
        #print('ACERTIVIDADE '+str(max_val)+'%')
        locations = numpy.where(result >= threshold)
        
        #ALTURA E LARGURA DA IMG EM BUSCA
        find_img_h = find_in_inscreen.shape[0]
        find_img_w = find_in_inscreen.shape[1]
        
        locations = list(zip(*locations[::-1]))
        
        rectangles = []
        for loc in locations:
            rect = [int(loc[0]), int(loc[1]), find_img_w, find_img_h]
            # Add every box to the list twice in order to retain single (non-overlapping) boxes
            rectangles.append(rect)
            rectangles.append(rect)

        rectangles, weights = cv2.groupRectangles(rectangles, groupThreshold=1, eps=0.5)
        
        points_ini = []
        points_end = []
        points_center = []
        if len(rectangles):
            #print('Found needle.')

            line_color = (0, 255, 0)
            line_type = cv2.LINE_4
            marker_color = (255, 0, 255)
            marker_type = cv2.MARKER_CROSS

            # Loop over all the rectangles
            for (x, y, w, h) in rectangles:
                points_ini.append((x, y))
                points_end.append((x + w, y + h))

                # Determine the center position
                center_x = x + int(w/2)
                center_y = y + int(h/2)
                # Save the points
                points_center.append((center_x, center_y))
                
                if debug_mode == 'rectangles':
                    # Determine the box position
                    top_left = (x, y)
                    bottom_right = (x + w, y + h)
                    # Draw the box
                    cv2.rectangle(screen, top_left, bottom_right, color=line_color, 
                                lineType=line_type, thickness=2)
                elif debug_mode == 'points':
                    # Draw the center point
                    cv2.drawMarker(screen, (center_x, center_y), 
                                color=marker_color, markerType=marker_type, 
                                markerSize=40, thickness=2)

        return points_ini, points_center,points_end
    else:
        return [],[],[]

def coordTelaXY(find_in_inscreen):
    screen = printScreenTela()#printa a tela
    cv2.imwrite('resultados/PrintTelaOk.jpg',screen)#guarda a imagem 
    screen = cv2.imread('resultados/PrintTelaOk.jpg')#carrega a imagem
    return findElementosScreen(screen,find_in_inscreen)

def findTelaXY(find_in_inscreen,onclicked= False,doubleclick = False,addX = 0,addY = 0,f5Pag = False,listUn = False,workheroes = False):#BUSCA EM TODA A TELA A POSIÇÃO DAS IMAGENS
    screen = printScreenTela()#printa a tela
    cv2.imwrite('resultados/PrintTelaOk.jpg',screen)#guarda a imagem 
    screen = cv2.imread('resultados/PrintTelaOk.jpg')#carrega a imagem

    pini,pcenter,pend = findElementosScreen(screen,find_in_inscreen)

    if(len(pcenter)>0):
        cont = 1
        for (pini,pcenter) in zip(pini,pcenter):
            (xc,yc) = pcenter
            
            if(onclicked):
                ############################### RETIRAR O VALOR -40 EM TELAS NORMAIS######################################
                pyautogui.moveTo(xc+addX,yc+addY,0.4)
                pyautogui.click(xc+addX,yc+addY,interval=1)
                #########################################################################################################
                #time.sleep(0.5)
            if(doubleclick):
                pyautogui.doubleClick()
                time.sleep(1.5)
            
            if(f5Pag):
                time.sleep(1.5)
                pyautogui.hotkey('ctrl', 'f5')

            if(listUn and cont == 1):#SÓ QUERO QUE LIST O PRIMEIRO ELEMENTO
                break
            if(workheroes):
                if(cont % 5 == 0):
                    Scroll(workheroes)

            cont = cont + 1
        return True
    else:
        return False
    #SELEÇÃO DAS COORDENADAS PRINCIPAIS DE TODAS AS TELAS. #COORD_INI/#COORD_CENTRO/#COORD_FIM       
def findBoxImgPoints(findImgRef, refaddX, refaddY,w,h,findListImgInRef,listaddX = 0,listaddY = 0,onclicked = False,
movPoint = False,movPointIniaddX = 0, movPointIniaddY = 0, movPointEndaddX = 0, movPointEndaddY = 0,qtdRepeatChk = 1,ListUni = False,goGreen = False, goRed = False,adcWork = False): #BUSCA TODOS AS BOX COM PONTOS CARACTERÍSTICOS
    #SELEÇÃO DAS COORDENADAS PRINCIPAIS DE TODAS AS TELAS.

    piniref,pcenter1,pendref = coordTelaXY(findImgRef)#PEGA APENAS AS COORDENADAS TOP=LEFT X/Y
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
                screen = printScreenBox(x,y,w,h)
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

                    p_list_ini,p_list_center,p_list_end = findElementosScreen(screen,listimg)

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
    #checkXBack()
    while findTelaXY(go_conect) or findTelaXY(ok_bt) or findTelaXY(go_select_sign_meta1) or findTelaXY(go_select_sign_meta2): 
        findTelaXY(go_select_sign_meta1,True,True,-50,-200)
        sleepTime(2,'VERIFICANDO POSSÍVEL CONFIRMAÇÃO DE ASSINATURA')
        findTelaXY(go_select_sign_meta2,True)
        ############################CHECK INICIAL################################
        if(findTelaXY(ok_bt)):
            sleepTime(2,'ENCONTRAMOS UM BOTÃO OK/CONEXAO ÀS {} '.format(horarioexato()))
            findTelaXY(ok_bt,True)
            sleepTime(12,'IREMOS ATUALIZAR CADA UMA DA(S) PAGINA(S) :)')   
        #########################################################################
        ############################VERIFICAR SE TEM BOTÃO DE CONEXÃO WALET################################
        if (findTelaXY(go_conect)):
            print('BOTÃO CONECT ENCONTRADO NA TELA! IREMOS DAR F5 ÀS {} '.format(horarioexato()))
            contconta = 1

            while(findTelaXY(go_conect)): #CLICA SO NO PRIMEIRO ENTRAR - SERÁ VERIFICADO UM POR UM
                findTelaXY(go_conect,True,True,0,-100,True,True) #ATUALIZA A 1° PAGINA
                sleepTime(15,'INICIANDO O LOGIN NA(S) CONTA  N° '+str(contconta)) #TEMPO CONSIDERÁVEL PARA ATUALIZAR PAGINA
                findTelaXY(go_conect,True,True,0,0,False,True) #CLICA APENAS NA 1° PAGINA

                sleepTime(12,'CLICANDO NO BOTÃO CONECTED N° '+str(contconta))#TEMPO CONSIDERÁVEL PARA ATUALIZAR PAGINA
                #ENQUANTO TIVER A CAIXA DE CONFIRMAÇÃO METAMASK ELE FICA AQUI DENTRO TENTANDO CLICAR.
                contx = 1

                findTelaXY(go_select_sign_meta2,True)
                sleepTime(3)
                while(findTelaXY(go_select_sign_meta1)):
                    print('Tentativa '+str(contx)+'°')
                    #sleepTime(15,'Tentativa '+str(contx)+'°')#
                    findTelaXY(go_select_sign_meta1,True,True,-50,-200,False,True)
                    sleepTime(3)
                    findTelaXY(go_select_sign_meta2,True)
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
        sleepTime(5,'INICIANDO COM TODOS OS HEROES  FULL')
        ################APENAS SELEÇÃO ALL - HEROES#############
        findTelaXY(go_hero_work_ini,True)
        #print('COLOCANDO OS HEROS PARA TRABALHAR')
        sleepTime(5,'COLOCANDO OS HEROS PARA TRABALHAR')
        findTelaXY(go_all_work,True)
        time.sleep(2)
        
        findTelaXY(x_button,True)
        print('ENTRAREMOS EM TODOS OS MAPAS')
        sleepTime(5,'ENTRAREMOS EM TODOS OS MAPAS')
        findTelaXY(go_map,True)
        
        print('VERIFICANDO SE NÃO TEMOS TELA INICIAL')
        sleepTime(5)
        
        if findTelaXY(go_hero_work_ini) or findTelaXY(x_button):
            continue
        else:
            break
#######################################################################################
def heroesSelectTpIni(com = False,rare = False,supr = False,epic = False,leg = False,supleg = False):    
    find = None
    checkXBack()
    print('INICIANDO O PROCESSO DE SELEÇÃO DOS HEROES- ÀS {} '.format(horarioexato()))
    findTelaXY(go_hero_work_ini,True)
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
    while findTelaXY(go_upgrade) == False and cont < 10:
        findTelaXY(x_button,True)
        findTelaXY(go_back,True)
        findTelaXY(go_hero_work_ini,True)
        cont = cont + 1

    findBoxImgPoints(go_upgrade,-390,-190,260,195,listFind,120,-1,True,True,20,-6,0,18,3)

    cont = 0
    while (findTelaXY(x_button) or findTelaXY(go_map)) and cont < 10:
        findTelaXY(x_button,True)
        time.sleep(1)
        findTelaXY(go_map,True)
        cont = cont + 1
    
    findTelaXY(x_button,True)
    time.sleep(1)
    findTelaXY(go_map,True)

def updateMapaHero():
    sleepTime(5,'ATUALIZANDO A POSIÇÃO DOS BOMBER HEROES')
    findTelaXY(go_back,True)
    sleepTime(2)
    findTelaXY(x_button,True)
    sleepTime(2)
    findTelaXY(go_map,True)

def newMap():
    sleepTime(5,'ABRINDO O PRÓXIMO MAPA')
    checkXBack()
    findTelaXY(go_new_map,True)

def reloadContas():
    sleepTime(5,'VAMOS REINICIAR TODAS AS CONTAS F5')
    checkXBack()
    #sys.stdout.write('\n VAMOS REINICIAR TODAS AS CONTAS  - ÀS {} '.format(horarioexato()))
    
    findTelaXY(go_hero_work_ini,True)
    sleepTime(2)
    findTelaXY(go_all_nowork,True)
    sleepTime(2)
    #newMap()
    #time.sleep(1.5)
    checkXBack()
    findTelaXY(go_hero_work_ini,True,False,0,-100,True) # CLICA ACIMA E ATUALIZA CADA UMA DAS PAGINAS
    CheckLogin()
 ################FUNÇÕES AUXILIARES#############   
def checkXBack():
    while(findTelaXY(go_back) or findTelaXY(x_button)):
        findTelaXY(x_button,True)
        sleepTime(2)
        findTelaXY(go_back,True)
        sleepTime(2)

def sleepTime(qtdseg = 1, info_msg = ''):
    #sys.stdout.write('Será necessário aguardar '+str(y)+'s')
    for x in range((qtdseg), 0,-1):
        print(f'{"Aguarde: "+str(x)} seg. ### {info_msg} \r', end="")
        time.sleep(1) 

def main():
    cont = 0
    #listFind = [hero_supr]
    #print('INICIANDO COM OS RAROS - ÀS {} '.format(horarioexato()))
    #heroesSelectTpIni(False,False,False,True)
    reloadContas()
    return
###########################AMBIENTE DE TESTE########################################
    
    #sleepTime(2,'VAMOS BUSCAR OS BAUS :)')
    #if(findTelaXY(bau_d1,True)):
      #  print('BAU 01 DOURADO ENCONTRADO!')
    
    #if(findTelaXY(bau_d2,True)):
     #   print('BAU 02 DOURADO ENCONTRADO!')
    
    #if(findTelaXY(bau_m1,True)):
     #   print('BAU 01 MADEIRA ENCONTRADO!')
    #findTelaXY(bau_d2,True)
    ##################################################################
    #listFind = [hero_raro,hero_commum]
                #150,-5
    #findTelaXY(x_button,True)
    #findTelaXY(go_back,True)
    #findTelaXY(go_hero_work_ini,True)
    #findBoxImgPoints(go_upgrade,-390,-190,260,195,listFind,120,-10,True,True,20,-5,0,18,3)
    #findTelaXY(x_button,True)
    #time.sleep(1)
    #findTelaXY(go_hero_work_ini,True)
    #findBoxImgPoints(go_upgrade,-390,-190,260,195,listFind,120,-10,True,True,20,-5,0,18,3)
    #time.sleep(1)
    #findTelaXY(x_button,True)
    #time.sleep(1)
    #findTelaXY(go_map,True)
    #findTelaXY(go_upgrade,True,False,-300)
    ######################################################################################
    #if(findTelaXY(bau_m2)):
    #    cont = cont + 1
    #    print('BAU 02 MADEIRA ENCONTRADO!')

    #print('\n TOTAL DE BAUS ENCONTRADOS:'+str(cont))
   # sleepTime(2,'Finalizado')
    #findTelaXY(go_select_sign_meta1,True,True,-50,-200)
      
 ###########################AMBIENTE DE TESTE########################################
    while True:
        cont = 1
        print('SE GOSTOU DO BOOT DO BOMB - FIQUE A VONTADE PARA PASSAR UM CAFE/BCOINHA :)')
        print('CARTEIRA WALET: 0xAc8b000865BdBcD6C4eD4Ac85475Afd57DD2244D')

        print('BOT BOMBCRYPTO 2022 - INICIAL NO SISTEMA. Aguarde 5s...')
        time.sleep(5)
        t_cont = {
            "check_bt_login" : 0,#ok CHEK ERRO - LOGIN ETC
            "time_refresh_position" : 0, #ok ATUALIZAR MAPA SAIR E VOLTAR
            "hero_comum_work" : 0,#ok
            "hero_raro_work" : 0,
            "hero_sraro_work" : 0,
            "hero_epico_work" : 0,
            "hero_full_work" : 0,
            "check_bt_map" : 0,#ok
            "time_reboot_bot": 0
        }

        cont = 1
        now_loop = time.time() #INICIO DO PRIMEIRO LOOP PRINCIPAL

        t_cont['hero_comum_work'] = t_cont['hero_raro_work'] = t_cont['hero_sraro_work'] = t_cont['hero_epico_work'] = now_loop #PRA NÃO ENTRAR A PRIMEIRA VEZ UMA VEZ
        ###################################INICIADO O LOOP PRINCIPAL###################################
        while True:
            now = time.time()#DEFINE UM TIME AO ENTRAR. EX.: 101516
            random_number = 0.1*random.uniform(5, 10)   

            ###### CONDIÇÃO - VERIFICA LOGIN & LOGAR - METAMASK - BOMBER - VERIFICAR PAG ERRO
            if (now - t_cont['check_bt_login']) > (c_time_loop['check_bt_login'] * 60):
                t_cont['check_bt_login'] = now
                #sys.stdout.write('\n VERIFICANDO A PRESENÇA DO BOTÃO CONECT OU LOGIN - ÀS {} '.format(horarioexato()))
                CheckLogin()   
                           
            ######COLOCANDO TODOS FULL A 1° VEZ###################
            if (now - t_cont['hero_full_work']) > (c_time_loop['hero_full_work'] * 60):
                t_cont['hero_full_work'] = now
                #sys.stdout.write('\n VERIFICANDO A PRESENÇA DO BOTÃO CONECT OU LOGIN - ÀS {} '.format(horarioexato()))
                print('INICIANDO COM TODOS OS HEROES - ÀS {} '.format(horarioexato()))
                herosFullWorkIni()
                #updateMapaHero()      
            ####################WORK TRABALHAR HEROS################################  
            if (now - t_cont['hero_sraro_work']) > (c_time_loop['hero_sraro_work'] * 60):
                t_cont['hero_sraro_work'] = now
                print('INICIANDO COM OS SUPER RAROS - ÀS {} '.format(horarioexato()))
                heroesSelectTpIni(False,False,True)
                #updateMapaHero()
                
            if (now - t_cont['hero_comum_work']) > (c_time_loop['hero_comum_work'] * 60):
                t_cont['hero_comum_work'] = now
                print('INICIANDO COM OS COMUNS - ÀS {} '.format(horarioexato()))
                heroesSelectTpIni(True)
                #updateMapaHero()


            if (now - t_cont['hero_raro_work']) > (c_time_loop['hero_raro_work'] * 60):
                t_cont['hero_raro_work'] = now
                print('INICIANDO COM OS RAROS - ÀS {} '.format(horarioexato()))
                heroesSelectTpIni(False,True)
                #updateMapaHero()
            
            if (now - t_cont['hero_epico_work']) > (c_time_loop['hero_epico_work'] * 60):
                t_cont['hero_epico_work'] = now
                print('INICIANDO COM OS EPICOS - ÀS {} '.format(horarioexato()))
                heroesSelectTpIni(False,False,False,True)
                #updateMapaHero()
            ###### CONDIÇÃO - SAIR DO MAPA - VOLTAR E ENTRAR NO MAPA
            if (now - t_cont['time_refresh_position']) > (random_number*c_time_loop['time_refresh_position'] * 60):
                t_cont['time_refresh_position'] = now
                updateMapaHero() 
            
            if (now - t_cont['time_reboot_bot']) > (random_number*c_time_loop['time_reboot_bot'] * 60):
                t_cont['time_reboot_bot'] = now
                reloadContas()
                
main()
