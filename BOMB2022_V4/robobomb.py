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
    c_time_work_map = config['time_work_mapa']
    c_time_zoom = config['zoom_nav_bomber']
    select_bomber_tp = config['select_bomber_tp']
    
    if(c_time_zoom['zoom_33']):
        print('OBS: ZOOM NAVEGADOR DE TODAS AS CONTAS DEVE ESTAR EM --> 33%')
        past_name = '33'

    if(c_time_zoom['zoom_50']):
        print('OBS: ZOOM NAVEGADOR DE TODAS AS CONTAS DEVE ESTAR EM --> 50%')
        past_name = '50'
    
    go_conect = cv2.imread('targets/new'+past_name+'/login_assinar_meta/connect.png')#OK
    go_conect2 = cv2.imread('targets/new'+past_name+'/login_assinar_meta/connect2.png')#OK

    go_select_sign_meta1 = cv2.imread('targets/new'+past_name+'/login_assinar_meta/assina1.png')#OK
    go_select_sign_meta11 = cv2.imread('targets/new'+past_name+'/login_assinar_meta/assina11.png')#OK
    go_select_sign_meta2 = cv2.imread('targets/new'+past_name+'/login_assinar_meta/assinar2.png')#OK
    go_select_sign_meta3 = cv2.imread('targets/new'+past_name+'/login_assinar_meta/assinar3.png')#OK

    go_conect_meta = cv2.imread('targets/new'+past_name+'/login_assinar_meta/connect_meta.png')
    go_conect_meta_load = cv2.imread('targets/new'+past_name+'/login_assinar_meta/conect_meta_load.png')
    go_conect_meta_no_network = cv2.imread('targets/new'+past_name+'/login_assinar_meta/conect_meta_no_network.png')
    go_conect_meta_click_senha1 = cv2.imread('targets/new'+past_name+'/login_assinar_meta/conect_meta_click_senha1.png')
    go_conect_meta_click_senha2 = cv2.imread('targets/new'+past_name+'/login_assinar_meta/conect_meta_click_senha2.png')
    go_conect_meta_click_chk1 = cv2.imread('targets/new'+past_name+'/login_assinar_meta/conect_meta_click_chk1.png')
    go_conect_meta_click_chk2 = cv2.imread('targets/new'+past_name+'/login_assinar_meta/conect_meta_click_chk2.png')
    
    go_map = cv2.imread('targets/new'+past_name+'/treasure-hunt-icon.png')#OK
    go_back = cv2.imread('targets/new'+past_name+'/voltar.png')#OK
    x_button = cv2.imread('targets/new'+past_name+'/x.png')#OK
    go_hero_work_ini = cv2.imread('targets/new'+past_name+'/heroes.png')#OK

    hero_epic = cv2.imread('targets/new'+past_name+'/heroes/hero_epico.png')#OK
    hero_supr = cv2.imread('targets/new'+past_name+'/heroes/hero_supraro.png')#OK
    hero_raro = cv2.imread('targets/new'+past_name+'/heroes/raro.png')#OK
    hero_commum = cv2.imread('targets/new'+past_name+'/heroes/commun.png')#OK
    #workgreen = cv2.imread('targets/new'+past_name+'/heroes/workgreen.png')#OK
    #noworkred = cv2.imread('targets/new'+past_name+'/heroes/noworkred.png')#OK

    go_work = cv2.imread('targets/new'+past_name+'/heroes/work.png')#OK
    go_home = cv2.imread('targets/new'+past_name+'/heroes/home.png')#OK
    go_upgrade = cv2.imread('targets/new'+past_name+'/heroes/upgrade.png')#OK
    
    go_all_work = cv2.imread('targets/new'+past_name+'/heroes/go_all_work.png')#OK
    go_all_nowork = cv2.imread('targets/new'+past_name+'/heroes/go_all_nowork.png')
    
    go_new_map = cv2.imread('targets/new'+past_name+'/mapa/new-map.png')
    go_select_hero1 = cv2.imread('targets/new'+past_name+'/mapa/select-hero1.png')
    go_select_hero11 = cv2.imread('targets/new'+past_name+'/mapa/select-hero2.png')
    go_hero_work_map = cv2.imread('targets/new'+past_name+'/mapa/heroes.png')
    
    ok_bt = cv2.imread('targets/new'+past_name+'/erro/ok.png')#OK
    loaderro_bt = cv2.imread('targets/new'+past_name+'/erro/load.png')#OK
    erromemory1_bt = cv2.imread('targets/new'+past_name+'/erro/erromemory1.png')#OK
    erromemory2_bt = cv2.imread('targets/new'+past_name+'/erro/erromemory2.png')#OK
    
    erroupdate1_bt = cv2.imread('targets/new'+past_name+'/erro/erro_ok_update_1.png')#OK
    erroupdate2_bt = cv2.imread('targets/new'+past_name+'/erro/erro_ok_update_2.png')#OK
    erroupdate1_bt = cv2.imread('targets/new'+past_name+'/erro/erro_ok_update_1.png')#OK
    erroinit_bt = cv2.imread('targets/new'+past_name+'/erro/erro_init_log.png')#OK

    #bau_d1 = cv2.imread('targets/new'+past_name+'/mapa/dourado_teste/1.png')#buscar bau d
    #bau_d2 = cv2.imread('targets/new'+past_name+'/mapa/dourado_teste/2.png')#buscar bau d

    #bau_m1 = cv2.imread('targets/new'+past_name+'/mapa/madeira_teste/1.png')#buscar bau d
    #bau_m2 = cv2.imread('targets/new'+past_name+'/mapa/madeira_teste/2.png')#buscar bau d
    
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
#################################VERSÃO 2022###########################################
def findElementosScreen(screen,find_in_inscreen, threshold=0.85, debug_mode='rectangles'):
    result = cv2.matchTemplate(screen, find_in_inscreen, cv2.TM_CCOEFF_NORMED)
    #Pega os valores max_val -> % de acerto na Busca, Max_loc --> coordenada X,Y encontrada
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    #print('ACERTIVIDADE '+str(max_val)+'%')
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
                ############################### RETIRAR O VALOR -40 EM TELA PC KDU######################################
                #pyautogui.moveTo(xc+addX,yc+addY-40,0.4)
                #pyautogui.click(xc+addX,yc+addY-40,interval=1)
                ############################### RETIRAR TELAS NORMAIS######################################
                pyautogui.moveTo(xc+addX,yc+addY,0.2)
                pyautogui.click(xc+addX,yc+addY,interval=1)
                #########################################################################################################
                #time.sleep(0.5)
            if(doubleclick):
                pyautogui.doubleClick()
                time.sleep(1.5)
            
            if(f5Pag):
                time.sleep(1)
                pyautogui.hotkey('ctrl','shift', 'r')
                time.sleep(3.0)
                pyautogui.hotkey('ctrl','f5')
                time.sleep(3.0)
                pyautogui.hotkey('f5')

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
                ############################### RETIRAR O VALOR -50 TELA KDU######################################
                #y = int(yi-50)+int(refaddY)
                #####################################################################
                ############################### RETIRAR  TELAS NORMAIS######################################
                y = int(yi)+int(refaddY)
                ############################### RETIRAR O VALOR -50 EM TELAS NORMAIS######################################
                time.sleep(1)
                #TRABALHO DENTRO DA BOX - ACHO QUE É DESNECESSÁRIO
                screen = printScreenBox(x,y,w,h)
                cv2.imwrite('resultados/PrintBox'+str(cont1)+'.jpg',screen)#guarda a imagem 
                screen = cv2.imread('resultados/PrintBox'+str(cont1)+'.jpg')#carrega a imagem      
                cont1 = cont1 + 1  
                
                for listimg in findListImgInRef: 
                    #EVITAR O BUUG DE NÃO SELEÇÃO DO PRIMEIRO HERO LISTADO
                    time.sleep(2)

                    p_list_ini,p_list_center,p_list_end = findElementosScreen(screen,listimg)
                    
                    #EVITAR O BUUG DE NÃO SELEÇÃO DO PRIMEIRO HERO LISTADO
                    pyautogui.moveTo(x=x+50,y=y+100,duration=0.2)
                    pyautogui.click()

                    if(len(p_list_center) > 0):
                        cont2 = 1
                        for (p_ini,p_center) in zip(p_list_ini,p_list_center):
                                                        
                            (map_x,map_y) = p_center
                            #print('-> X=',map_x,', -> Y=',map_y)
                            
                            if(onclicked):
                                pyautogui.moveTo(x+map_x+listaddX,y+map_y+listaddY,0.2)
                                pyautogui.click()
                                #pyautogui.doubleClick()
                                time.sleep(0.5)
                            else: 
                                pyautogui.moveTo(x+map_x+listaddX,y+map_y+listaddY,0.7)

                            if(ListUni and cont2 == 1):#SÓ QUERO QUE LIST O PRIMEIRO ELEMENTO
                                break

                            cont2 = cont2 + 1
                
                #SE ENCONTROU ALGO - PERCORRE :) = OU SEJA, TAMANHO DA LISTA É MAIOR QUE 0
                if(movPoint):
                    xmovini = x
                    ############################### RETIRAR O VALOR -50 EM TELAS KDU######################################
                    #ymovini = int(yi-50)
                    #####################################################################
                    ############################### TELAS NORMAIS######################################
                    ymovini = int(yi)
                    #####################################################################
                    pyautogui.moveTo(x=xmovini+movPointIniaddX,y=ymovini+movPointIniaddY,duration=1)
                    #pyautogui.click()
                    pyautogui.mouseDown()
                    time.sleep(0.2)
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
def heroFullWork():
    if(findTelaXY(go_hero_work_ini)):
        sleepTime(2,'INICIANDO FULL - APÓS LOGIN TODOS OS HEROES - ÀS {} '.format(horarioexato()))
        ################APENAS SELEÇÃO ALL - HEROES#############
        findTelaXY(go_hero_work_ini,True,False,0,0,False,True)
        #print('COLOCANDO OS HEROS PARA TRABALHAR')
        time.sleep(2)
        findTelaXY(go_all_work,True)
        time.sleep(2)
        findTelaXY(x_button,True)
        print('VOLTANDO A TELA PRINCIPAL NO MAPA E ENTRANDO NO MAPA')
        findTelaXY(go_map,True,True,0,0,False,True)

def CheckLogin():
    while True:
        #VERIFICANDO POSSÍVEL ERRO 01
        if(findTelaXY(loaderro_bt)):
            print('O BOMBER DEVE ESTAR EM MANUTENÇÃO - TENTAREMOS LOGIN')
            findTelaXY(loaderro_bt,True,True,0,0,True,True) #ATUALIZA A 1° PAGINA
            sleepTime(10,'IREMOS VERIFICAR NOVAMENTE')
            continue

        #VERIFICANDO POSSÍVEL ERRO 02
        if(findTelaXY(erroupdate1_bt) or findTelaXY(erroupdate2_bt) or findTelaXY(erroinit_bt)):
            findTelaXY(erroupdate1_bt,True) #ATUALIZA APÓS UPDATE - MANUTENÇÃO 1
            findTelaXY(erroupdate2_bt,True) #ATUALIZA APÓS UPDATE - MANUTENÇÃO1
            time.sleep(1)
            findTelaXY(erroinit_bt,True,True,0,0,True) #ATUALIZA APÓS UPDATE - MANUTENÇÃO1
            sleepTime(10,'ATUALIZANDO APÓS UMA POSSÍVEL MANUTENÇÃO DO JOGO')
            continue
        #VERIFICANDO POSSÍVEL ERRO 03     
        if(findTelaXY(loaderro_bt) or findTelaXY(erromemory1_bt) or findTelaXY(erromemory2_bt)):
            print('O BOMBER DEVE ESTAR EM MANUTENÇÃO - TENTAREMOS LOGIN')
            findTelaXY(loaderro_bt,True,True,0,0,True) #ATUALIZA A 1° PAGINA
            findTelaXY(erromemory1_bt,True,True) #ATUALIZA A 1° PAGINA
            time.sleep(2)
            findTelaXY(erromemory2_bt,True,True,0,0,True) #ATUALIZA A 1° PAGINA
            findTelaXY(erroinit_bt,True,True,0,0,True) #ATUALIZA APÓS UPDATE - MANUTENÇÃO1
            sleepTime(10,'IREMOS VERIFICAR NOVAMENTE')
            continue

        #ENCONTRADO BOTÃO OK
        if (findTelaXY(ok_bt)):
            print('ENCONTRADO BOTÃO OK...')
            time.sleep(1)
            print('CLICANDO NO OK, AGUARDE UM MOMENTO')
            findTelaXY(ok_bt, True)
            pyautogui.moveRel(100,0)
            print('AGUARDANDO BOTÃO CONECTED...')
            cont = 0
            while cont < 5 and (findTelaXY(go_conect)==False and findTelaXY(go_conect2)==False and findTelaXY(go_conect_meta)==False):
                time.sleep(2)
                cont = cont + 1
                if(cont == 60):
                    break
            continue
        #ENCONTRADO CONECT
        if (findTelaXY(go_conect) or findTelaXY(go_conect2) or findTelaXY(go_conect_meta)):
            time.sleep(1)
            print('ENCONTRADO BOTÃO CONECT...')
            time.sleep(1)
            print('CLICANDO NO BOTÃO CONECT, AGUARDE UM MOMENTO, ENQUANTO ATUALIZAMOS TODOS OS MAPAS')
            updateMapaHero()
            findTelaXY(go_conect,True,False,0,0,False,True) #CLICA APENAS NA 1° PAGINA
            time.sleep(1)
            findTelaXY(go_conect_meta,True,False,0,0,False,True)

            time.sleep(1)
            pyautogui.hotkey('f11')#TELA CHEIA

            print('AGUARDANDO BOTÃO ASSINAR...')
            cont = 0
            while cont < 6 and (findTelaXY(go_select_sign_meta1)==False and findTelaXY(go_select_sign_meta11)==False 
            and findTelaXY(go_select_sign_meta2)==False and findTelaXY(go_select_sign_meta3)==False) :
                time.sleep(2)
                cont = cont + 1
                if(cont == 6 or findTelaXY(go_conect_meta_no_network)):
                    print('TEMPO EXCEDIDO, POSSÍVEL FOI DESLOGADO DA METAMASK. FAREMOS O LOGIN NA METAMASK')
                    print('PARA FUNCIONAR, TERÁ QUE COLOCAR A SENHA PADRÃO NO ARQUIVO CONFIG.YAML - EM TODAS AS CONTAS DA METAMASK! FIQUE TRANQUILO')
                    print('FIQUE TRANQUILO, NÃO IREMOS ROUBAR NENHUM VALOR DA SUA CARTEIRA METAMASK :)')
                    time.sleep(1)
                    if(findTelaXY(ok_bt)):
                        findTelaXY(ok_bt, True,False,0,0,False,True)
                        pyautogui.moveRel(100,0)
                        sleepTime(10,'IREMOS VERIFICAR NOVAMENTE')
                        
                    #findTelaXY(go_conect_meta_click_senha1,True,False,200,0,False,True)
                    #time.sleep(3)
                    #findTelaXY(go_conect_meta_click_senha2,True,False,200,0,False,True)
                    time.sleep(2)
                    pyautogui.hotkey('alt','shift','m')
                    time.sleep(6)

                    if(findTelaXY(go_conect_meta_click_chk2)):
                        #findTelaXY(go_conect_meta_click_chk2,True)
                        time.sleep(2)
                        pyautogui.typewrite(c_time_loop['login_senha_metamask'], interval=0.30) 
                        time.sleep(1)
                        pyautogui.hotkey('enter')
                        time.sleep(6)
                        if(findTelaXY(go_conect_meta_click_chk1)):
                            findTelaXY(go_conect_meta_click_chk1,True,False,200,0,False,True)
                            pyautogui.hotkey('f5')
                            time.sleep(1)
                            #pyautogui.hotkey('f11')#TELA CHEIA
                            sleepTime(5,'ATUALIZANDO A PAGINA PARA EVITAR POSSÍVEIS BUGS')  

                    elif(findTelaXY(go_conect_meta_click_chk1)):
                        findTelaXY(go_conect_meta_click_chk1,True,False,200,0,False,True)
                        pyautogui.hotkey('f5')
                        time.sleep(1)
                        #pyautogui.hotkey('f11')#TELA CHEIA
                        sleepTime(5,'ATUALIZANDO A PAGINA PARA EVITAR POSSÍVEIS BUGS')
    
                    break
            
            #CLICANDO NO BOTÃO ASSINAR1
            if(findTelaXY(go_select_sign_meta2) or findTelaXY(go_select_sign_meta3)):
                print('CLICANDO NO BOTÃO ASSINAR, AGUARDE UM MOMENTO ATÉ A TELA PRINCIPAL')

                findTelaXY(go_select_sign_meta2,True)
                time.sleep(1)
                pyautogui.moveRel(100,0)
                findTelaXY(go_select_sign_meta2,True)
                time.sleep(1)
                pyautogui.moveRel(100,0)
                time.sleep(1)
                findTelaXY(go_select_sign_meta3,True)
                time.sleep(1)
                pyautogui.moveRel(100,0)
                findTelaXY(go_select_sign_meta3,True)
                time.sleep(1)
                pyautogui.moveRel(100,0)
                print('AGUARDANDO A TELA PRINCIPAL DO BOMB PARA SELEÇÃO DOS HEROES...')
                cont = 0
                while cont < 10 and findTelaXY(go_hero_work_ini) == False:
                    time.sleep(2)
                    cont = cont + 1
                    if(cont == 60):
                        break
                time.sleep(1)
                heroFullWork()
                #pyautogui.hotkey('f11')#TELA CHEIA    
                #return False

            pyautogui.hotkey('f11')#TELA CHEIA    

        return False              
##########################################################################################
def herosFullWorkIni():
    #while True:
    checkXBackIniPag()
    ################APENAS SELEÇÃO ALL - HEROES#############
    findTelaXY(go_hero_work_ini,True)
    #print('COLOCANDO OS HEROS PARA TRABALHAR')
    time.sleep(1)
    findTelaXY(go_all_work,True)
    time.sleep(2)
    findTelaXY(go_all_work,True)
    time.sleep(3)
    findTelaXY(x_button,True)
    time.sleep(1)
    findTelaXY(go_map,True)
    time.sleep(1)
#######################################################################################
def heroesSelectTpIni(com = False,rare = False,supr = False,epic = False,leg = False,supleg = False):    
    find = None

    checkXBackIniPag()
    findTelaXY(go_hero_work_ini,True)
    sleepTime(3,'COLOCANDO OS HEROS PARA TRABALHAR')

    if(com):
        find = hero_commum

    if(rare):
        find = hero_raro    

    if(supr):
        find = hero_supr

    if(epic):
        find = hero_epic

    listFind = [find]
    
    cont = 0
    while findTelaXY(go_upgrade) == False and cont < 10:
        findTelaXY(x_button,True)
        findTelaXY(go_back,True)
        findTelaXY(go_hero_work_ini,True)
        cont = cont + 1

    if(c_time_zoom['zoom_33']):
        findBoxImgPoints(go_upgrade,-255,-120,175,135,listFind,78,-4,True,True,20,-6,0,3,4)#33%

    if(c_time_zoom['zoom_50']):
        findBoxImgPoints(go_upgrade,-390,-190,260,195,listFind,120,-1,True,True,20,-6,0,18,4)#50%

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
    sleepTime(2,' ATUALIZANDO A POSIÇÃO DOS BOMBER HEROES ÀS {} '.format(horarioexato()))
    checkXBackIniPag()
    findTelaXY(go_map,True)

def newMap():
    sleepTime(2,' ENTRANDO EM UM NOVO MAPA')
    #sleepTime(2,'ABRINDO O PRÓXIMO MAPA')
    checkXBackIniPag()
    findTelaXY(go_new_map,True)

def reloadContas():
    desativarHeroes()
    findTelaXY(go_hero_work_ini,True,False,0,-100,True) # CLICA ACIMA E ATUALIZA CADA UMA DAS PAGINAS   
    CheckLogin()

def desativarHeroes():
    checkXBackIniPag()
    findTelaXY(go_hero_work_ini,True)
    time.sleep(2)
    findTelaXY(go_all_nowork,True)
    time.sleep(2)
    findTelaXY(go_hero_work_ini,True)
    time.sleep(3)
    findTelaXY(go_all_nowork,True)
    time.sleep(2)
    checkXBackIniPag()

 ################FUNÇÕES AUXILIARES#############   
def checkXBackIniPag():
    while(findTelaXY(go_back) or findTelaXY(x_button)):
        findTelaXY(go_back,True)
        findTelaXY(x_button,True)
        time.sleep(1)
        findTelaXY(x_button,True)
        findTelaXY(go_back,True)
        time.sleep(1)

def sleepTime(qtdseg = 1, info_msg = '', newline = False):
    #sys.stdout.write('Será necessário aguardar '+str(y)+'s')
    for x in range((qtdseg), 0,-1):
        print(f'{"Aguarde: "+str(x)} seg. ===>  {info_msg} \r', end="")
        time.sleep(1) 
    if(newline):
        print('\n')

def horarioexato():
    return datetime.today().strftime("%Hh%Mmin%Ss DO DIA %d/%m/%Y")
################FUNÇÕES AUXILIARES#############   
def main():
    cont = 0
 ###########################AMBIENTE DE TESTE########################################   
    #while True:
    #findTelaXY(go_conect_meta_click_chk1,True,False,200)
    #CheckLogin()
    #return

    

    #return 
 ###########################AMBIENTE DE TESTE########################################
    while True:
        
        print('SE GOSTOU DO BOOT DO BOMB - FIQUE A VONTADE PARA PASSAR UM CAFE/BCOINHA :)')
        print('CARTEIRA WALET: 0xAc8b000865BdBcD6C4eD4Ac85475Afd57DD2244D \n')

        print('BOT BOMBCRYPTO 2022 - INICIAL NO SISTEMA. Aguarde 3s...')
        time.sleep(3)
        t_cont = {
            "check_bt_login" : 0,#ok CHEK ERRO - LOGIN ETC
            "time_refresh_position" : 0, #ok ATUALIZAR MAPA SAIR E VOLTAR
            "hero_comum_work" : 0,"hero_raro_work" : 0,"hero_sraro_work" : 0,
            "hero_epico_work" : 0,"hero_full_work" : 0,"time_reboot_bot": 0
        }

        t_work_map = {
            "now_work_hero": 0, #VARÍAVEL QUE PEGARA SEMPRE O VALOR DA HORA EXATA AO COLOCAR HEROES
            "time_work_hero": 0 #VARIÁVEL QUE VAI PEGAR O TIME DETERMINADO PARA FICAR TRABALHANDO NO MAPA
        }

        now_loop = time.time() #INICIO DO PRIMEIRO LOOP PRINCIPAL

        t_cont['time_reboot_bot'] = t_cont['hero_comum_work'] = now_loop
        t_cont['hero_raro_work'] = t_cont['hero_sraro_work'] = now_loop
        t_cont['hero_epico_work'] = now_loop #PRA NÃO ENTRAR A PRIMEIRA VEZ UMA VEZ

        ###################################INICIADO O LOOP PRINCIPAL###################################
        while True:
            now = time.time()#DEFINE UM TIME AO ENTRAR. EX.: 101516
            #random_number = 0.1*random.uniform(5, 10)   

            ###### CONDIÇÃO - VERIFICA LOGIN & LOGAR - METAMASK - BOMBER - VERIFICAR PAG ERRO
            if (now - t_cont['check_bt_login']) > (c_time_loop['check_bt_login'] * 60):
                CheckLogin()
                t_cont['check_bt_login'] = now  

            #################### WORK FULL################################
            if(select_bomber_tp['full_']):
                ######COLOCANDO TODOS FULL A 1° VEZ###################
                if (now - t_cont['hero_full_work']) > (c_time_loop['hero_full_work'] * 60):
                    updateMapaHero()
                    print('INICIANDO FULL COM TODOS OS HEROES - ÀS {} '.format(horarioexato()))
                    herosFullWorkIni()

                    t_cont['hero_full_work'] = now
                    
                    t_work_map['now_work_hero'] = now 
                    t_work_map['time_work_hero'] = c_time_work_map['hero_full_work']
            ##############################################################    
            
            #################### WORK RARIDADE ################################
            if(select_bomber_tp['raridade_']):
                if (now - t_cont['hero_comum_work']) > (c_time_loop['hero_comum_work'] * 60):
                    updateMapaHero()
                    print('INICIANDO COM OS COMUNS - ÀS {} '.format(horarioexato()))
                    heroesSelectTpIni(True)

                    t_cont['hero_comum_work'] = now
                    
                    t_work_map['now_work_hero'] = now 
                    t_work_map['time_work_hero'] = c_time_work_map['hero_comum_work']
                
                if (now - t_cont['hero_sraro_work']) > (c_time_loop['hero_sraro_work'] * 60):
                    updateMapaHero()
                    print('INICIANDO COM OS SUPER RAROS - ÀS {} '.format(horarioexato()))
                    heroesSelectTpIni(False,False,True)

                    t_cont['hero_sraro_work'] = now

                    t_work_map['now_work_hero'] = now 
                    t_work_map['time_work_hero'] = c_time_work_map['hero_sraro_work']

                if (now - t_cont['hero_raro_work']) > (c_time_loop['hero_raro_work'] * 60):
                    updateMapaHero()
                    print('INICIANDO COM OS RAROS - ÀS {} '.format(horarioexato()))
                    heroesSelectTpIni(False,True)

                    t_cont['hero_raro_work'] = now
                    
                    t_work_map['now_work_hero'] = now 
                    t_work_map['time_work_hero'] = c_time_work_map['hero_raro_work']
                
                if (now - t_cont['hero_epico_work']) > (c_time_loop['hero_epico_work'] * 60):
                    updateMapaHero()
                    print('INICIANDO COM OS ÉPICOS - ÀS {} '.format(horarioexato()))
                    heroesSelectTpIni(False,False,False,True)
                    
                    t_cont['hero_epico_work'] = now
                    
                    t_work_map['now_work_hero'] = now 
                    t_work_map['time_work_hero'] = c_time_work_map['hero_epico_work']

            ##############################################################    
            
            #################### CONDIÇÕES MAPA ################################
            if (now - t_cont['time_refresh_position']) > (c_time_loop['time_refresh_position'] * 60):
                updateMapaHero() 
                t_cont['time_refresh_position'] = now
            
            if (now - t_cont['time_reboot_bot']) > (c_time_loop['time_reboot_bot'] * 60):
                print('VAMOS REINICIAR TODAS AS CONTAS - ÀS {} '.format(horarioexato()))
                reloadContas()
                t_cont['time_reboot_bot'] = now
                
                t_work_map['now_work_hero'] = now 
                t_work_map['time_work_hero'] = c_time_work_map['hero_full_work']

            ######TIME WOR IN MAPA POR RARIDADE - CHECK 1 MIN###################
            if (now - t_work_map['now_work_hero']) > (t_work_map['time_work_hero'] * 60):
                print('DESATIVANDO TODOS OS HEROES - ÀS {} '.format(horarioexato()))
                desativarHeroes()
                
                t_work_map['now_work_hero'] = now
                t_work_map['time_work_hero'] = 1000000000  
            ##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#    
main()