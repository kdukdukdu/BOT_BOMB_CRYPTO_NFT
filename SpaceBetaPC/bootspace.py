import time
import cv2 as cv2
import numpy
import pyautogui
from datetime import datetime
############
import mss
import yaml

if __name__ == '__main__': 
    stream = open("config.yaml", 'r')# LÊ AS CONNFIGURAÇÕES O ARQUIVO
    config = yaml.safe_load(stream)
    
    c_time_loop = config['time_intervals']
    temp_time_nav = c_time_loop['nav_full_work']

    c_time_zoom = config['zoom_nav_bomber']
    select_nav_tp = config['select_nav_tp']
    config_boss = config['config_boss']
    #go_7_nav
    #if(config_boss[''])
    #if(findTelaXY(go_7_nav,False,False,0,0,False,False,0.96)

    c_time_work_fight = config['time_work_fight']#UPDATE FUTURO
    #global contnav = 0
    if(c_time_zoom['zoom_33']):
        print('OBS: ZOOM NAVEGADOR DE TODAS AS CONTAS DEVE ESTAR EM --> 33%')
        past_name = '33'
    elif(c_time_zoom['zoom_50']):
        print('OBS: ZOOM NAVEGADOR DE TODAS AS CONTAS DEVE ESTAR EM --> 50%')
        past_name = '50'
    elif (c_time_zoom['zoom_100']):
        print('OBS: ZOOM NAVEGADOR DE TODAS AS CONTAS DEVE ESTAR EM --> 50%')
        past_name = '100'
    #ENTRADA CONECTE - ASSINATURA - LOGIN
    go_conect= cv2.imread('targets/new'+past_name+'/ini_jogo/conect_1.png')#OK
    go_asinar = cv2.imread('targets/new'+past_name+'/ini_jogo/assinar_1.png')#OK
    go_asinar_full = cv2.imread('targets/new'+past_name+'/ini_jogo/assinar_11.png')#OK

    go_play = cv2.imread('targets/new' + past_name + '/ini_jogo/play_1.png')  # OK

    nav_supr_1 = cv2.imread('targets/new'+past_name+'/raridade_nav/supr_1.png')#OK
    nav_raro_1 = cv2.imread('targets/new'+past_name+'/raridade_nav/raro_1.png')#OK
    nav_comum_1 = cv2.imread('targets/new'+past_name+'/raridade_nav/comum_1.png')#OK

    go_ini_boss = cv2.imread('targets/new'+past_name+'/ini_nav/fight_boss_1.png')#OK
    go_select_nav = cv2.imread('targets/new' + past_name + '/ini_nav/fight_1.png')  # OK

    chk_map_0_nav_boss = cv2.imread('targets/new' + past_name + '/ini_nav/map_0_nav_boss.png')  # OK

    boss_surrender_bt = cv2.imread('targets/new'+past_name+'/ini_nav/boss/surrender/surrender.png')
    boss_surrender_confirm = cv2.imread('targets/new'+past_name+'/ini_nav/boss/surrender/confirm_surrender.png')

    boss_1_surrend = cv2.imread('targets/new'+past_name+'/ini_nav/boss/boss1.png')
    boss_2_surrend = cv2.imread('targets/new'+past_name+'/ini_nav/boss/boss2.png')
    boss_3_surrend = cv2.imread('targets/new'+past_name+'/ini_nav/boss/boss3.png')
    boss_4_surrend = cv2.imread('targets/new'+past_name+'/ini_nav/boss/boss4.png')
    boss_5_surrend = cv2.imread('targets/new'+past_name+'/ini_nav/boss/boss5.png')
    boss_6_surrend = cv2.imread('targets/new'+past_name+'/ini_nav/boss/boss6.png')
    boss_7_surrend = cv2.imread('targets/new'+past_name+'/ini_nav/boss/boss7.png')
    boss_8_surrend = cv2.imread('targets/new'+past_name+'/ini_nav/boss/boss8.png')
    boss_9_surrend = cv2.imread('targets/new'+past_name+'/ini_nav/boss/boss9.png')
    boss_10_surrend = cv2.imread('targets/new'+past_name+'/ini_nav/boss/boss10.png')
    boss_11_surrend = cv2.imread('targets/new'+past_name+'/ini_nav/boss/boss11.png')
    boss_12_surrend = cv2.imread('targets/new'+past_name+'/ini_nav/boss/boss12.png')
    boss_13_surrend = cv2.imread('targets/new'+past_name+'/ini_nav/boss/boss13.png')

    #GO - QTD NAV:
    go_7_nav = cv2.imread('targets/new' + past_name + '/ini_nav/qtd_select_nav/go_7_select_nav.png')  # OK
    go_8_nav = cv2.imread('targets/new' + past_name + '/ini_nav/qtd_select_nav/go_8_select_nav.png')  # OK
    go_9_nav = cv2.imread('targets/new' + past_name + '/ini_nav/qtd_select_nav/go_9_select_nav.png')  # OK
    go_10_nav = cv2.imread('targets/new' + past_name + '/ini_nav/qtd_select_nav/go_10_select_nav.png')  # OK
    go_11_nav = cv2.imread('targets/new' + past_name + '/ini_nav/qtd_select_nav/go_11_select_nav.png')  # OK
    go_12_nav = cv2.imread('targets/new' + past_name + '/ini_nav/qtd_select_nav/go_12_select_nav.png')  # OK
    go_13_nav = cv2.imread('targets/new' + past_name + '/ini_nav/qtd_select_nav/go_13_select_nav.png')  # OK
    go_14_nav = cv2.imread('targets/new' + past_name + '/ini_nav/qtd_select_nav/go_14_select_nav.png')  # OK
    go_15_nav = cv2.imread('targets/new' + past_name + '/ini_nav/qtd_select_nav/go_15_select_nav.png')  # OK
    
    go_back_nav = cv2.imread('targets/new' + past_name + '/ini_nav/back_nav_bt_1.png')  # OK
    go_base_nav = cv2.imread('targets/new' + past_name + '/ini_nav/base.nav.png')  # OK
    go_remove_nav = cv2.imread('targets/new' + past_name + '/ini_nav/remove_nav_1.png')  # OK

    go_selecfull50_nav = cv2.imread('targets/new' + past_name + '/ini_nav/full50_1.png')  # OK
    go_selecfull60_nav = cv2.imread('targets/new' + past_name + '/ini_nav/full60_1.png')  # OK
    go_selecfull70_nav = cv2.imread('targets/new' + past_name + '/ini_nav/full70_1.png')  # OK
    go_selecfull80_nav = cv2.imread('targets/new' + past_name + '/ini_nav/full80_1.png')  # OK
    go_selecfull90_nav = cv2.imread('targets/new' + past_name + '/ini_nav/full90_1.png')  # OK
    go_selecfull100_nav = cv2.imread('targets/new' + past_name + '/ini_nav/full100_1.png')  # OK

    erro_ok_bt = cv2.imread('targets/new'+past_name+'/erro/ok_erro_1.png')#OK
    erro_close_bt = cv2.imread('targets/new'+past_name+'/erro/close_erro_1.png')#OK
    erro_confirm_lose_bt = cv2.imread('targets/new'+past_name+'/erro/erro_confirm_lose_1.png')#OK
    erro_confirm_boss = cv2.imread('targets/new' + past_name + '/erro/chk_confirm_1.png')  # OK

########################### SCREEM TELA & BOX ########################################
def printScreenTela():
    with mss.mss() as sct:
        monitor = {"top": 160, "left": 160, "width": 1000, "height": 135}
        sct_img = numpy.array(sct.grab(sct.monitors[0]))
        return sct_img[:,:,:3]

def printScreenBox(x,y,w,h):
    with mss.mss() as sct:
        monitor = {"top": y, "left": x, "width": w, "height": h}
        sct_img = numpy.array(sct.grab(monitor))
        return sct_img[:,:,:3]

def findElementosScreen(screen,find_in_inscreen, threshold=0.80, debug_mode='rectangles'):
    result = cv2.matchTemplate(screen, find_in_inscreen, cv2.TM_CCOEFF_NORMED)
    #Pega os valores max_val -> % de acerto na Busca, Max_loc --> coordenada X,Y encontrada
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    #print('ACERTIVIDADE ' + str(max_val) + '%')
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

def findTelaXyQtd(find_in_inscreen,threshold = 0.90):
    screen = printScreenTela()  # printa a tela
    cv2.imwrite('resultados/PrintTelaOk.jpg', screen)  # guarda a imagem
    screen = cv2.imread('resultados/PrintTelaOk.jpg')  # carrega a imagem

    pini, pcenter, pend = findElementosScreen(screen, find_in_inscreen, threshold)

    return len(pcenter)

def findTelaXY(find_in_inscreen,onclicked= False,doubleclick = False,addX = 0,addY = 0,f5Pag = False,listUn = False, threshold = 0.90):#BUSCA EM TODA A TELA A POSIÇÃO DAS IMAGENS
    screen = printScreenTela()#printa a tela
    cv2.imwrite('resultados/PrintTelaOk.jpg',screen)#guarda a imagem 
    screen = cv2.imread('resultados/PrintTelaOk.jpg')#carrega a imagem

    pini,pcenter,pend = findElementosScreen(screen, find_in_inscreen, threshold)
    #print('Qtd de ocorrencias: '+str(len(pcenter)))
    if(len(pcenter)>0):
        cont = 1
        for (pini,pcenter) in zip(pini,pcenter):
            (xc,yc) = pcenter
            if(onclicked):
                pyautogui.moveTo(xc+addX,yc+addY,0.2)
                pyautogui.click(xc+addX,yc+addY)
                pyautogui.moveTo(xc+addX+50,yc+addY+50,0.2)

            if(doubleclick):
                pyautogui.moveTo(xc + addX, yc + addY, 0.2)
                pyautogui.doubleClick()
                pyautogui.moveTo(xc + addX+50, yc + addY+50, 0.2)
                time.sleep(0.5)
            
            if(f5Pag):
                time.sleep(1)
                pyautogui.hotkey('ctrl','shift', 'r')
                time.sleep(2)
                pyautogui.hotkey('ctrl','f5')
                time.sleep(2)
                pyautogui.hotkey('f5')

            if(listUn and cont == 1): break

            cont = cont + 1
        return True
    else:
        return False


#################################VERSÃO 2022###########################################
#SELEÇÃO DAS COORDENADAS PRINCIPAIS DE TODAS AS TELAS. #COORD_INI/#COORD_CENTRO/#COORD_FIM
def findBoxImgPoints(findImgRef, refaddX, refaddY,w,h,findListImgInRef,listaddX = 0,listaddY = 0,onclicked = False,
movPoint = False,movPointIniaddX = 0, movPointIniaddY = 0, movPointEndaddX = 0, movPointEndaddY = 0,qtdRepeatChk = 1,ListUni = False, select_full = False): #BUSCA TODOS AS BOX COM PONTOS CARACTERÍSTICOS
    #SELEÇÃO DAS COORDENADAS PRINCIPAIS DE TODAS AS TELAS.
    qtdRepeatChk = config_boss['qtd_rolagem_selectnav']

    piniref,pcenter1,pendref = coordTelaXY(findImgRef)#PEGA APENAS AS COORDENADAS TOP=LEFT X/Y
    #LOOP PRINCIPAL -  A QUAL GERENCIA TODAS AS TELAS - BOX
    if(len(piniref)>0):
        cont1 = 1 #contador da imagem
        for (piniref,pendref) in zip(piniref,pendref):
            contRepeatMovLoop = 1
            #contnaves2 = 0
            while contRepeatMovLoop <= qtdRepeatChk:

                #CHECK FULL - LIMIT BUSCAR
                #print(str(qtdRepeatChk)+' == '+str(contRepeatMovLoop))
                #if (findTelaXY(go_15_nav,False,False,0,0,False,False,0.97) or contRepeatMovLoop == qtdRepeatChk):
                    #print('Possível, temos 15 Naves pra trabalhar - FIGHT BOSS!')
                    #findTelaXY(go_ini_boss, True)
                #    time.sleep(1)
                    #findTelaXY(go_ini_boss, False, True)
                #    time.sleep(1)
                #    pyautogui.click()
            
                 #   CheckErroConfirm()
                 #   break
                
                #################################
                (xi,yi) = pendref
                
                x = int(xi)+int(refaddX)

                #y = int(yi-50)+int(refaddY)
                y = int(yi)+int(refaddY)
                #pyautogui.moveTo(x, y, 0.2)
                #pyautogui.moveTo(x+movPointEndaddX, y+movPointEndaddY, 0.2)
                #return
                time.sleep(0.5)
                #TRABALHO DENTRO DA BOX - ACHO QUE É DESNECESSÁRIO
                screen = printScreenBox(x+movPointEndaddX, y+movPointEndaddY,w,h)
                cv2.imwrite('resultados/PrintBox'+str(cont1)+'.jpg',screen)#guarda a imagem 
                screen = cv2.imread('resultados/PrintBox'+str(cont1)+'.jpg')#carrega a imagem      
                cont1 = cont1 + 1  

                for listimg in findListImgInRef: 
                    #EVITAR O BUUG DE NÃO SELEÇÃO DO PRIMEIRO HERO LISTADO
                    time.sleep(0.5)
                    p_list_ini,p_list_center,p_list_end = findElementosScreen(screen,listimg, 0.90)
                    print(len(p_list_center))

                    #return
                    #EVITAR O BUUG DE NÃO SELEÇÃO DO PRIMEIRO HERO LISTADO
                    #pyautogui.moveTo(x=x+50,y=y+100,duration=0.2)
                    #pyautogui.click()
                    #print('Achou '+str(len(p_list_center)))
                    #contnaves2 = contnaves2 + len(p_list_center)
                    if(len(p_list_center) > 0):
                        cont2 = 1
                        for (p_ini,p_center) in zip(p_list_ini,p_list_center):
                                                        
                            (map_x,map_y) = p_center
                            #print('-> X=',map_x,', -> Y=',map_y)
                            if(onclicked):
                                ###################FAZ A BUSCA 01 DA NAVES
                                cont = 0
                                while(cont < 15 and findTelaXY(listimg)):
                                    findTelaXY(listimg,True,False,0,0,False,True,0.90)
                                    global contnav
                                    contnav = contnav + 1
                                    print ('QTD DE NAVE ATUAL --> '+str(contnav))
                                    time.sleep(0.5)
                                    cont = cont + 1
                                    if(contnav == config_boss['max_nav'] or contnav >= 15):
                                        break
                                #########SE ACHOU AS 15, ENTRA PRA TRABALHAR#######
                                #pyautogui.moveTo(x+map_x+listaddX+movPointEndaddX,y+map_y+listaddY+movPointEndaddY,0.2)
                                #pyautogui.click()
                                #pyautogui.doubleClick()
                                #time.sleep(0.5)
                            else: 
                                pyautogui.moveTo(x+map_x+listaddX+movPointEndaddX,y+map_y+listaddY+movPointEndaddY,0.2)

                            if(ListUni and cont2 == 1):#SÓ QUERO QUE LIST O PRIMEIRO ELEMENTO
                                break

                            cont2 = cont2 + 1
                #SE ENCONTROU ALGO - PERCORRE :) = OU SEJA, TAMANHO DA LISTA É MAIOR QUE 0
                if(movPoint):
                    
                    pyautogui.moveTo(x=x+movPointIniaddX,y=y+movPointIniaddY,duration=0.5)
                    #pyautogui.click()
                    pyautogui.mouseDown()
                    time.sleep(0.2)
                    pyautogui.moveTo(x=x + movPointEndaddX,y = y + movPointEndaddY, duration=0.5)
                    #pyautogui.moveTo(x=xmovend+movPointEndaddX,y=ymovend+movPointEndaddY,duration=0.5)
                    time.sleep(0.5)
                    pyautogui.mouseUp()
                    pyautogui.click()
                    time.sleep(0.5)
                    ##SÓ PARA DAR UM CLICK NO MEIO DA LISTA DE HEROES
                contRepeatMovLoop = contRepeatMovLoop + 1
            time.sleep(1)
            contnav
            if(contnav >= config_boss['min_nav'] or contnav >=15):
                return True
        return True
    else:
        return False

def CheckErroConfirm():
    #print('VERIFICANDO BOTÃO CONFIRM (ALGUM ERRO)')
    if(findTelaXY(erro_confirm_lose_bt) or findTelaXY(erro_confirm_boss)):
        findTelaXY(erro_confirm_lose_bt, True)
        time.sleep(0.5)
        findTelaXY(erro_confirm_boss, True)
        time.sleep(0.5)
        findTelaXY(erro_confirm_lose_bt, False, True)
        time.sleep(0.5)
        findTelaXY(erro_confirm_boss, False,  True)
        time.sleep(0.5)

    if(findTelaXY(erro_confirm_lose_bt)):
        print('BOTÃO CONFIRM OU CLOSE. ALGO DEU ERRADO - IREMO REINICIAR O JOGO')
        findTelaXY(erro_confirm_lose_bt,True,False,0,0,True)
        return False
################# LOGIN 100% #########################################################################
def CheckLogin():
    CheckErroConfirm()
    #checkXBackIniPag()
    while True:
        if (findTelaXY(erro_ok_bt) or findTelaXY(erro_close_bt)):
            print('ENCONTRAMOS UM BOTÃO OK/CLOSE ÀS {} '.format(horarioexato()))
            print('AGUARDE ALGUNS SEGUNDOS')
            findTelaXY(erro_ok_bt, True)
            time.sleep(0.5)
            findTelaXY(erro_close_bt, True)
            time.sleep(0.5)
            continue

        if(findTelaXY(go_conect) == False and findTelaXY(go_asinar) == False and findTelaXY(go_play) == False):
            #print('Não encontramos nada!')
            findTelaXY(erro_confirm_lose_bt, True)
            time.sleep(0.5)
            findTelaXY(erro_close_bt, True)
            time.sleep(0.5)
            findTelaXY(erro_ok_bt, True)
            time.sleep(0.5)
            time.sleep(2)
            break

        if (findTelaXY(go_conect)):
            print('ENCONTRADO BOTÃO CONECT...')
            time.sleep(1)
            print('CLICANDO NO BOTÃO CONECT, AGUARDE UM MOMENTO')
            findTelaXY(go_conect, False,True)

            print('AGUARDANDO BOTÃO ASSINAR...')
            cont = 0
            while cont < 5 and findTelaXY(go_asinar) == False:
                time.sleep(2)
                cont = cont + 1
                if(cont == 30):
                    break

        if(findTelaXY(go_asinar)):
            print('CLICANDO NO BOTÃO ASSINAR, AGUARDE UM MOMENTO')

            findTelaXY(go_asinar, False, True)
            time.sleep(1)
            findTelaXY(go_asinar_full, True, True, 110, 340)

            print('AGUARDANDO BOTÃO PLAY...')

            cont = 0
            while cont < 5 and findTelaXY(go_play) == False:
                time.sleep(2)
                cont = cont + 1
                if(cont == 30):
                    break

        if (findTelaXY(go_play)):
            print('CLICANDO NO BOTÃO PLAY, AGUARDE UM MOMENTO')
            findTelaXY(go_play, False, True)

            print('AGUARDANDO TELA INICIAL...')

            cont = 0
            while cont < 5 and findTelaXY(go_ini_boss) == False:
                time.sleep(2)
                findTelaXY(boss_surrender_confirm,True,True,0,0,False,False,0.80)
                cont = cont + 1
                if(cont == 30):
                    break

            time.sleep(3)
            herosFullWorkIni()
        return False
##########################################################################################
def herosFullWorkIni():
    CheckErroConfirm()

    if(findTelaXY(go_conect) or findTelaXY(go_asinar) or findTelaXY(go_play)):
        print('ALGUM PROBLEMA - AO VERIFICAR AS NAVES - VAMOS VERIFICAR LOGIN')
        CheckLogin()
        return False

    if (findTelaXY(go_ini_boss) == False):
        checkSurrend()
        CheckErroConfirm()
        findTelaXY(go_back_nav,True)
        time.sleep(10)
        findTelaXY(go_back_nav, False,True)

        print('AGUARDANDO TELA PRINCIPAL ...')
        cont = 0
        CheckErroConfirm()
        while cont < 20 and findTelaXY(go_ini_boss) == False:
            time.sleep(1)
            findTelaXY(boss_surrender_confirm,True,True,0,0,False,False,0.80)
            cont = cont + 1
            if(cont == 60):
                break
            

        if (findTelaXY(go_ini_boss) == False):
            CheckErroConfirm()
            time.sleep(1)
            findTelaXY(go_back_nav,True)
            time.sleep(10)
            findTelaXY(go_back_nav, False,True)


    #ENTRA SE TIVER NA TELA INICIAL
    if (findTelaXY(go_ini_boss)):
        updateStamina()
        global contnav
        contnav = 0
        if(findTelaXY(go_7_nav,False,False,0,0,False,False,0.96)):
            contnav = 7
        if(findTelaXY(go_8_nav,False,False,0,0,False,False,0.96)):
            contnav = 8
        if(findTelaXY(go_9_nav,False,False,0,0,False,False,0.96)):
            contnav = 9
        if(findTelaXY(go_10_nav,False,False,0,0,False,False,0.96)):
            contnav = 10
        elif(findTelaXY(go_11_nav,False,False,0,0,False,False,0.96)):
            contnav = 11
        elif(findTelaXY(go_12_nav,False,False,0,0,False,False,0.96)):
            contnav = 12
        elif(findTelaXY(go_13_nav,False,False,0,0,False,False,0.96)):
            contnav = 13
        elif(findTelaXY(go_14_nav,False,False,0,0,False,False,0.96)):
            contnav = 14
        elif(findTelaXY(go_15_nav,False,False,0,0,False,False,0.96)):
            contnav = 15
        print ('INICIO EM QTD DE NAVES --> '+str(contnav))
        if(contnav == 0):
            cont = 0
            while(cont < 7 and findTelaXY(go_remove_nav,True,False,0,0,False,True,0.90)):
                findTelaXY(go_remove_nav,True,False,0,0,False,True,0.90)
                time.sleep(0.5)
                cont = cont + 1
        else:
            if(contnav == 15):
                print('TOTAL DE NAVES SELECIONADAS --> '+ str(contnav)+'  ÀS {} '.format(horarioexato()))
                findTelaXY(go_ini_boss, True)
                time.sleep(0.5)
                findTelaXY(go_ini_boss, False, True)
                time.sleep(0.5)
                pyautogui.click()
                c_time_loop['nav_full_work'] = temp_time_nav
                return True
        #return False
        print('ESTAMOS NA TELA PRINCIPAL - VAMOS VERIFICAR AS NAVES - MIN 50% DE POWER')
        find = go_select_nav  # ListFind, 100, 23,
        #find = go_selecfull60_nav  # ListFind, 90, 23,
        #find = go_selecfull70_nav #ListFind, 80, 23,
        #find = go_selecfull80_nav #ListFind, 70, 23,
        #find = go_selecfull90_nav #ListFind, 60, 23,
        #find = go_selecfull100_nav #ListFind, 50, 23,
        listFind = [find]

        ###################FAZ A BUSCA 01 DA NAVES
        contchk = 1
        while contchk <= 2:
            cont = 0
            while(cont < 15 and findTelaXY(find)):
                findTelaXY(find,True,False,0,0,False,True,0.90)
                contnav = contnav + 1
                print ('QTD DE NAVE ATUAL --> '+str(contnav))
                time.sleep(0.5)
                cont = cont + 1
                if(contnav == config_boss['max_nav'] or contnav >= 15):
                    break
            #########SE ACHOU AS 15, ENTRA PRA TRABALHAR#######
            time.sleep(1)
            if(contnav >= config_boss['min_nav']):
                print('TOTAL DE NAVES SELECIONADAS --> '+ str(contnav)+'  ÀS {} '.format(horarioexato()))
                findTelaXY(go_ini_boss, True)
                time.sleep(0.5)
                findTelaXY(go_ini_boss, False, True)
                time.sleep(0.5)
                pyautogui.click()
                c_time_loop['nav_full_work'] = temp_time_nav
                return True
            else:
                updateStamina()
                #########SAI DO LOOP#######
                #SE NÃO ACHOU AS 15, TENTA BUSCAR NO SCROLL
                findBoxImgPoints(go_ini_boss, -385, -55, 240, 213, listFind, 0, 0, True, True, 0, 0, 0, -210)  # 50%
                CheckErroConfirm()
                #AQUI, AS NAVES ESTÃO TRABALHANDO EM 5S
                if(contnav >= config_boss['min_nav']):
                    print('TOTAL DE NAVES SELECIONADAS --> '+ str(contnav)+'  ÀS {} '.format(horarioexato()))
                    findTelaXY(go_ini_boss, True)
                    time.sleep(0.5)
                    findTelaXY(go_ini_boss, False, True)
                    time.sleep(0.5)
                    pyautogui.click()
                    c_time_loop['nav_full_work'] = temp_time_nav
                    return True
                else:
                    contchk = contchk + 1
                    print('IREMOS VERIFICAR MAIS UMA VEZ AS NAVES - MIN 50% - AGUARDANDO TELA PRINCIPAL')

        #SE CHEGOU AQUI, TEM MENOS QUE MENOS QUE A QTD MÍNIMA DE NAVES
        contnav = 0
        print('TEMOS MENOS QUE O MÍNIMO DE '+str(config_boss['min_nav'])+' NAVES')
        print('VAMOS DESATIVAR TODAS AS NAVES. AGUARDE -'+str(2*c_time_loop['nav_full_work'])+' MINUTOS ÀS {} '.format(horarioexato()))
        c_time_loop['nav_full_work'] = 2*temp_time_nav
        findTelaXY(go_back_nav,True)
        time.sleep(0.5)
        findTelaXY(go_back_nav, False,True)
        CheckErroConfirm()

        cont = 1
        while cont < 5 and findTelaXY(go_ini_boss) == False:
            time.sleep(2)
            cont = cont + 1
        cont = 0
        while(cont < 7 and findTelaXY(go_remove_nav,True,False,0,0,False,True,0.90)):
            findTelaXY(go_remove_nav,True,False,0,0,False,True,0.90)
            time.sleep(0.5)
            cont = cont + 1
        # c_time_loop['time_refresh_position']

        return False
    else:
        return False
    #findBoxScrollImg(go_ini_boss, -650, -405, 397, 339, go_selecfull80_nav, 130, 42, True, True, 0, -150, -45, -45, 9)
def updateStamina():
    print('ATUALIZANDO A STAMINA DAS NAVES - LOGO VAMOS INICIAR :)')
    if (findTelaXY(go_ini_boss)):
        findTelaXY(go_base_nav,True)
        time.sleep(1)
        findTelaXY(go_back_nav,True)
        time.sleep(1)
        findTelaXY(go_base_nav, False,True)
        time.sleep(1)
        findTelaXY(go_back_nav, False,True)

def checkSurrend():
    print('VAMOS FAZER DO SURRENDER...')   
    time.sleep(2)
    findTelaXY(boss_surrender_bt,True,True,0,0,False,False,0.80)
    time.sleep(2)
    findTelaXY(boss_surrender_confirm,True,True,0,0,False,False,0.80)
    time.sleep(5)
    return
    if(findTelaXY(boss_1_surrend,False,False,0,0,False,False,0.80)):
        print('CONFIRMAÇÃO DO SURRENDER 01...')    
    if(findTelaXY(boss_2_surrend,False,False,0,0,False,False,0.80)):
        print('CONFIRMAÇÃO DO SURRENDER 02...')    
    if(findTelaXY(boss_3_surrend,False,False,0,0,False,False,0.80)):
        print('CONFIRMAÇÃO DO SURRENDER 03...')    
    if(findTelaXY(boss_4_surrend,False,False,0,0,False,False,0.80)):
        print('CONFIRMAÇÃO DO SURRENDER 04...')    
    if(findTelaXY(boss_5_surrend,False,False,0,0,False,False,0.80)):
        print('CONFIRMAÇÃO DO SURRENDER 05...')    
    if(findTelaXY(boss_6_surrend,False,False,0,0,False,False,0.80)):
        print('CONFIRMAÇÃO DO SURRENDER 06...')    
    if(findTelaXY(boss_7_surrend,False,False,0,0,False,False,0.80)):
        print('CONFIRMAÇÃO DO SURRENDER 07...')    
    if(findTelaXY(boss_8_surrend,False,False,0,0,False,False,0.80)):
        print('CONFIRMAÇÃO DO SURRENDER 08...')    
    if(findTelaXY(boss_9_surrend,False,False,0,0,False,False,0.80)):
        print('CONFIRMAÇÃO DO SURRENDER 09...')    
    if(findTelaXY(boss_10_surrend,False,False,0,0,False,False,0.80)):
        print('VAMOS FAZER DO SURRENDER 10...')   
        time.sleep(2)
        findTelaXY(boss_surrender_bt,True,True,0,0,False,False,0.80)
        time.sleep(2)
        findTelaXY(boss_surrender_confirm,True,True,0,0,False,False,0.80)

    if(findTelaXY(boss_11_surrend,False,False,0,0,False,False,0.80)):
        print('VAMOS FAZER DO SURRENDER 11...')    
        
#######################################################################################
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
    cont = contnav = 0
 ###########################AMBIENTE DE TESTE########################################
    #INSTALAÇÕES - PIP
        #1° pip install opencv-python
        #2° pip install matplotlib
        #3° pip install PyAutoGUI
        #4° pip install mss
        #5° pip install yaml2 
        #6° pip install PyYAML
    #print('Kdu')
    #CheckLogin()
    #herosFullWorkIni()
    #if(findTelaXY(boss_1)):
    #    time.sleep(3)
    #    findTelaXY(boss_surrender_bt,False,True)
    #    time.sleep(3)
    #    findTelaXY(boss_surrender_bt,False,True)
    
    #return 
 ###########################AMBIENTE DE TESTE########################################
    while True:
        print('SE GOSTOU DO BOOT DO SPACECRYPTO - FIQUE A VONTADE PARA PASSAR UM CAFÉ - BUSD/BNB :)')
        print('CARTEIRA WALET: 0xAc8b000865BdBcD6C4eD4Ac85475Afd57DD2244D \n')
        print('BOT SPACECRYPTO 2022 - INICIAL NO SISTEMA. Aguarde 3s...')
        time.sleep(3)
        t_cont = {
            "check_bt_login" : 0,#ok CHEK ERRO - LOGIN ETC
            "time_refresh_position" : 0, #ok ATUALIZAR MAPA SAIR E VOLTAR
            "nav_comum_work" : 0,"nav_raro_work" : 0,"nav_sraro_work" : 0,
            "nav_epico_work" : 0,"nav_mitica_work" : 0,"nav_full_work" : 0,"time_surrend_bot": 0
        }

        t_work_map = {
            "now_work_hero": 0, #VARÍAVEL QUE PEGARA SEMPRE O VALOR DA HORA EXATA AO COLOCAR HEROES
            "time_work_hero": 0 #VARIÁVEL QUE VAI PEGAR O TIME DETERMINADO PARA FICAR TRABALHANDO NO MAPA
        }

        now_loop = time.time() #INICIO DO PRIMEIRO LOOP PRINCIPAL

        t_cont['nav_comum_work'] = now_loop
        t_cont['nav_raro_work'] = t_cont['nav_sraro_work'] = now_loop
        t_cont['nav_epico_work'] = now_loop #PRA NÃO ENTRAR A PRIMEIRA VEZ UMA VEZ

        ###################################INICIADO O LOOP PRINCIPAL###################################
        while True:
            now = time.time()#DEFINE UM TIME AO ENTRAR. EX.: 101516
            #random_number = 0.1*random.uniform(5, 10)   

            ###### CONDIÇÃO - VERIFICA LOGIN & LOGAR - METAMASK - BOMBER - VERIFICAR PAG ERRO
            if (now - t_cont['check_bt_login']) > (c_time_loop['check_bt_login'] * 60):
                CheckLogin()
                t_cont['check_bt_login'] = now

            if (now - t_cont['time_surrend_bot']) > (c_time_loop['time_surrend_bot'] * 60):
                #CheckLogin()
                #updateStamina()
                t_cont['time_surrend_bot'] = now      

            #################### WORK FULL################################
            if(select_nav_tp['full_']):
                ######COLOCANDO TODOS FULL A 1° VEZ###################
                if (now - t_cont['nav_full_work']) > (c_time_loop['nav_full_work'] * 60):
                    c_time_loop['nav_full_work'] = temp_time_nav
                    print('INICIANDO FULL COM TODOS AS 15 NAVES - ÀS {} '.format(horarioexato()))
                    herosFullWorkIni()

                    t_cont['nav_full_work'] = now
                    t_cont['time_refresh_position'] = now
            #################### WORK RARIDADE ################################
            elif(select_nav_tp['raridade_']):        
                if (now - t_cont['nav_comum_work']) > (c_time_loop['nav_comum_work'] * 60):
                    print('INICIANDO COM OS COMUNS - ÀS {} '.format(horarioexato()))
                    #t_cont['nav_comum_work'] = now
                
            #################### CONDIÇÕES REFRESH ################################
            if (now - t_cont['time_refresh_position']) > (c_time_loop['time_refresh_position'] * 60):
                #herosFullWorkIni()
                CheckErroConfirm()
                #checkSurrend()
                #if(findTelaXY(chk_map_0_nav_boss,False,False,0,0,False,False,0.80)):
                    #c_time_loop['nav_full_work'] = 5
                    #print('TEMOS  0 NAVES, VAMOS VOLTAR A TELA PRINCIPAL -  ÀS {} '.format(horarioexato()))
                    #findTelaXY(go_back_nav,True)
                #    time.sleep(1)
                    #findTelaXY(go_back_nav, False,True)
                    #CheckErroConfirm()
                    #herosFullWorkIni()


                t_cont['time_refresh_position'] = now
main()