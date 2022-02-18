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
    c_time_work_map = config['time_work_mapa']
    c_time_zoom = config['zoom_nav_bomber']
    select_bomber_tp = config['select_bomber_tp']
    
    if(c_time_zoom['zoom_33']):
        print('OBS: ZOOM NAVEGADOR DE TODAS AS CONTAS DEVE ESTAR EM --> 33%')
        past_name = '33'

    if(c_time_zoom['zoom_50']):
        print('OBS: ZOOM NAVEGADOR DE TODAS AS CONTAS DEVE ESTAR EM --> 50%')
        past_name = '50'

    if (c_time_zoom['zoom_100']):
        print('OBS: ZOOM NAVEGADOR DE TODAS AS CONTAS DEVE ESTAR EM --> 50%')
        past_name = '100'

    go_conect= cv2.imread('targets/new'+past_name+'/ini_jogo/conect_1.png')#OK
    go_asinar = cv2.imread('targets/new'+past_name+'/ini_jogo/assinar_1.png')#OK
    go_asinar_full = cv2.imread('targets/new'+past_name+'/ini_jogo/assinar_11.png')#OK

    go_play = cv2.imread('targets/new' + past_name + '/ini_jogo/play_1.png')  # OK

    nav_supr_1 = cv2.imread('targets/new'+past_name+'/raridade_nav/supr_1.png')#OK
    nav_raro_1 = cv2.imread('targets/new'+past_name+'/raridade_nav/raro_1.png')#OK
    nav_comum_1 = cv2.imread('targets/new'+past_name+'/raridade_nav/comum_1.png')#OK

    go_ini_boss = cv2.imread('targets/new'+past_name+'/ini_nav/fight_boss_1.png')#OK
    go_select_nav = cv2.imread('targets/new' + past_name + '/ini_nav/fight_1.png')  # OK
    go_7_nav = cv2.imread('targets/new' + past_name + '/ini_nav/go_7_select_nav.png')  # OK
    go_10_nav = cv2.imread('targets/new' + past_name + '/ini_nav/go_10_select_nav.png')  # OK
    go_15_nav = cv2.imread('targets/new' + past_name + '/ini_nav/go_15_select_nav.png')  # OK
    go_back_nav = cv2.imread('targets/new' + past_name + '/ini_nav/back_nav_bt_1.png')  # OK
    go_remove_nav = cv2.imread('targets/new' + past_name + '/ini_nav/remove_nav_1.png')  # OK
    go_selecfull60_nav = cv2.imread('targets/new' + past_name + '/ini_nav/full60_1.png')  # OK
    go_selecfull70_nav = cv2.imread('targets/new' + past_name + '/ini_nav/full70_1.png')  # OK
    go_selecfull80_nav = cv2.imread('targets/new' + past_name + '/ini_nav/full80_1.png')  # OK
    go_selecfull90_nav = cv2.imread('targets/new' + past_name + '/ini_nav/full90_1.png')  # OK
    go_selecfull100_nav = cv2.imread('targets/new' + past_name + '/ini_nav/full100_1.png')  # OK


    erro_ok_bt = cv2.imread('targets/new'+past_name+'/erro/ok_erro_1.png')#OK
    erro_close_bt = cv2.imread('targets/new'+past_name+'/erro/close_erro_1.png')#OK
    erro_confirm_lose_bt = cv2.imread('targets/new'+past_name+'/erro/erro_confirm_lose_1.png')#OK
    erro_confirm_boss = cv2.imread('targets/new' + past_name + '/erro/chk_confirm_1.png')  # OK

###########################SCREEM TELA & BOX########################################
def printScreenTela():
    with mss.mss() as sct:
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
#################################VERSÃO 2022###########################################
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
                pyautogui.click(xc+addX,yc+addY,interval=1)

            if(doubleclick):
                pyautogui.moveTo(xc + addX, yc + addY, 0.2)
                pyautogui.doubleClick()
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
#SELEÇÃO DAS COORDENADAS PRINCIPAIS DE TODAS AS TELAS. #COORD_INI/#COORD_CENTRO/#COORD_FIM
def findBoxImgPoints(findImgRef, refaddX, refaddY,w,h,findListImgInRef,listaddX = 0,listaddY = 0,onclicked = False,
movPoint = False,movPointIniaddX = 0, movPointIniaddY = 0, movPointEndaddX = 0, movPointEndaddY = 0,qtdRepeatChk = 1,ListUni = False, select_full = False): #BUSCA TODOS AS BOX COM PONTOS CARACTERÍSTICOS
    #SELEÇÃO DAS COORDENADAS PRINCIPAIS DE TODAS AS TELAS.
    piniref,pcenter1,pendref = coordTelaXY(findImgRef)#PEGA APENAS AS COORDENADAS TOP=LEFT X/Y
    #LOOP PRINCIPAL - BOMBCRYPTO A QUAL GERENCIA TODAS AS TELAS - BOX
    if(len(piniref)>0):
        cont1 = 1 #contador da imagem
        for (piniref,pendref) in zip(piniref,pendref):
            contRepeatMovLoop = 1
            contnaves = 0
            while contRepeatMovLoop <= qtdRepeatChk:
                if(contRepeatMovLoop == int(qtdRepeatChk/2) and findTelaXY(go_10_nav,False,False,0,0,False,False,0.96)):
                    #print('Selecionamos 10 Naves pra trabalhar - FIGHT BOSS! Apenas da Metade')
                    #findTelaXY(go_ini_boss, True)
                    #time.sleep(1)
                    #findTelaXY(go_ini_boss, False, True)
                    #time.sleep(1)
                    #pyautogui.click()
                    #time.sleep(2)
                    CheckErroConfirm()

                    #break;
                #CHECK FULL - LIMIT BUSCAR
                #print(str(qtdRepeatChk)+' == '+str(contRepeatMovLoop))
                if (findTelaXY(go_15_nav,False,False,0,0,False,False,0.96) or contRepeatMovLoop == qtdRepeatChk):
                    print('Possível, temos 15 Naves pra trabalhar - FIGHT BOSS!')
                    findTelaXY(go_ini_boss, True)
                    time.sleep(1)
                    findTelaXY(go_ini_boss, False, True)
                    time.sleep(1)
                    pyautogui.click()
                    time.sleep(2)
                    if(contnaves < 10):
                        print('Poucas Naves Encontradas :(. Total '+str(contnaves))

                    CheckErroConfirm()

                    break;
                #if (select_full):
                    #print('Selecionando Full Todos')
                    #findTelaXY(go_select_nav, True)
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
                    p_list_ini,p_list_center,p_list_end = findElementosScreen(screen,listimg, 0.97)
                    print(len(p_list_center))

                    #return
                    #EVITAR O BUUG DE NÃO SELEÇÃO DO PRIMEIRO HERO LISTADO
                    #pyautogui.moveTo(x=x+50,y=y+100,duration=0.2)
                    #pyautogui.click()
                    #print('Achou '+str(len(p_list_center)))
                    contnaves = contnaves + len(p_list_center)
                    if(len(p_list_center) > 0):
                        cont2 = 1
                        for (p_ini,p_center) in zip(p_list_ini,p_list_center):
                                                        
                            (map_x,map_y) = p_center
                            #print('-> X=',map_x,', -> Y=',map_y)
                            if(onclicked):
                                pyautogui.moveTo(x+map_x+listaddX+movPointEndaddX,y+map_y+listaddY+movPointEndaddY,0.2)
                                pyautogui.click()
                                #pyautogui.doubleClick()
                                time.sleep(0.5)
                            else: 
                                pyautogui.moveTo(x+map_x+listaddX+movPointEndaddX,y+map_y+listaddY+movPointEndaddY,0.2)

                            if(ListUni and cont2 == 1):#SÓ QUERO QUE LIST O PRIMEIRO ELEMENTO
                                break

                            cont2 = cont2 + 1
                #SE ENCONTROU ALGO - PERCORRE :) = OU SEJA, TAMANHO DA LISTA É MAIOR QUE 0
                if(movPoint):
                    #pyautogui.moveTo(x, y, 0.2)
                    #return
                    #xmovini = int(xi)
                    # ymovini = int(yi-100)
                    #ymovini = int(yi)
                    #####################################################################
                    #pyautogui.moveTo(x + movPointEndaddX, y + movPointEndaddY, 0.2)
                    #return
                    pyautogui.moveTo(x=x+movPointIniaddX,y=y+movPointIniaddY,duration=0.5)
                    #pyautogui.click()
                    pyautogui.mouseDown()
                    time.sleep(0.2)
                    pyautogui.moveTo(x=x + movPointEndaddX,y = y + movPointEndaddY, duration=0.5)
                    #pyautogui.moveTo(x=xmovend+movPointEndaddX,y=ymovend+movPointEndaddY,duration=0.5)
                    time.sleep(0.5)
                    pyautogui.mouseUp()
                    pyautogui.click()
                    time.sleep(0.2)
                    ##SÓ PARA DAR UM CLICK NO MEIO DA LISTA DE HEROES
                contRepeatMovLoop = contRepeatMovLoop + 1

        return True
    else:
        return False

def CheckErroConfirm():
    #print('VERIFICANDO BOTÃO CONFIRM (ALGUM ERRO)')

    if(findTelaXY(erro_confirm_lose_bt) or findTelaXY(erro_confirm_boss)):
        findTelaXY(erro_confirm_lose_bt, True)
        time.sleep(1)
        findTelaXY(erro_confirm_boss, True)
        time.sleep(1)
        findTelaXY(erro_confirm_lose_bt, False, True)
        time.sleep(1)
        findTelaXY(erro_confirm_boss, False,  True)
        time.sleep(1)

    if(findTelaXY(erro_confirm_lose_bt) or findTelaXY(erro_confirm_boss)):
        print('PROBLEMA NO BOTÃO CONFIRME - IREMO REINICIAR O JOGO')
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
            findTelaXY(erro_close_bt, True)
            time.sleep(10)
            continue

        if(findTelaXY(go_conect) == False and findTelaXY(go_asinar) == False and findTelaXY(go_play) == False):
            #print('Não encontramos nada!')
            findTelaXY(erro_confirm_lose_bt, True)
            findTelaXY(erro_close_bt, True)
            findTelaXY(erro_ok_bt, True)
            time.sleep(2)
            break

        print('AGUARDANDO BOTÃO CONECT...')

        if (findTelaXY(go_conect)):
            print('CLICANDO NO BOTÃO CONECT, AGUARDE UM MOMENTO')
            findTelaXY(go_conect, True)

            print('AGUARDANDO BOTÃO ASSINAR...')

            cont = 0
            while cont < 5 and findTelaXY(go_asinar) == False:
                time.sleep(2)
                cont = cont + 1

        if(findTelaXY(go_asinar)):
            print('CLICANDO NO BOTÃO ASSINAR, AGUARDE UM MOMENTO')

            findTelaXY(go_asinar, True)
            time.sleep(1)
            findTelaXY(go_asinar_full, True, True, 110, 340)

            print('AGUARDANDO BOTÃO PLAY...')

            cont = 0
            while cont < 5 and findTelaXY(go_play) == False:
                time.sleep(2)
                cont = cont + 1

        if (findTelaXY(go_play)):
            print('CLICANDO NO BOTÃO PLAY, AGUARDE UM MOMENTO')

            findTelaXY(go_play, True)

            print('AGUARDANDO TELA INICIAL...')

            cont = 0
            while cont < 5 and findTelaXY(go_ini_boss) == False:
                time.sleep(2)
                cont = cont + 1
        time.sleep(5)
        herosFullWorkIni()
        return False
##########################################################################################
def herosFullWorkIni():
    if(findTelaXY(go_conect) or findTelaXY(go_asinar) or findTelaXY(go_play)):
        return False

    if (findTelaXY(go_ini_boss) == False):
        time.sleep(2)
        findTelaXY(go_back_nav,True)
        findTelaXY(go_back_nav, True)

        print('AGUARDANDO TELA PRINCIPAL ASSINAR...')
        cont = 0
        while cont < 5 and findTelaXY(go_ini_boss) == False:
            time.sleep(2)
            cont = cont + 1

    if (findTelaXY(go_ini_boss)):
        print('ESTAMOS NA TELA PRINCIPAL - VAMOS VERIFICAR AS NAVES')
        find = go_selecfull70_nav #ListFind, 80, 23,
        #find = go_selecfull80_nav #ListFind, 70, 23,
        #find = go_selecfull90_nav #ListFind, 60, 23,
        #find = go_selecfull100_nav #ListFind, 50, 23,
        listFind = [find]

        findBoxImgPoints(go_ini_boss, -395, -50, 240, 213, listFind, 80, 23, True, True, 0, 0, 0, -210, 5, False,True)  # 50%
        time.sleep(5)
        findTelaXY(go_back_nav,True)
        time.sleep(1)
        findTelaXY(go_back_nav, False,True)
        CheckErroConfirm()
        time.sleep(2)
        #CHECK TELA PRINCIPAL
        cont = 0
        while cont < 5 and findTelaXY(go_ini_boss) == False:
            time.sleep(2)
            cont = cont + 1
        ################################################################
        findBoxImgPoints(go_ini_boss, -395, -50, 240, 213, listFind, 80, 23, True, True, 0, 0, 0, -210, 5, False,True)  # 50%
        ################################################################
        time.sleep(5)
        findTelaXY(go_back_nav, True)
        time.sleep(1)
        findTelaXY(go_back_nav, False, True)
        CheckErroConfirm()
        time.sleep(2)
        # CHECK TELA PRINCIPAL
        cont = 0
        while cont < 5 and findTelaXY(go_ini_boss) == False:
            time.sleep(2)
            cont = cont + 1
        ################################################################
        findBoxImgPoints(go_ini_boss, -395, -50, 240, 213, listFind, 80, 23, True, True, 0, 0, 0, -210, 5, False,
                         True)  # 50%
        ################################################################
    else:
        return False
    #findBoxScrollImg(go_ini_boss, -650, -405, 397, 339, go_selecfull80_nav, 130, 42, True, True, 0, -150, -45, -45, 9)
#######################################################################################
def heroesSelectTpIni(com = False,rare = False,supr = False):
    find = None

    print('COLOCANDO OS HEROS PARA TRABALHAR')

    if(com):
        find = nav_comum_1

    if(rare):
        find = nav_raro_1

    if(supr):
        find = nav_supr_1

    #if(epic):
    #    find = hero_epic

    listFind = [find]

    findBoxImgPoints(go_ini_boss, -650, -405, 397, 339, listFind, 320, 50, True, True, 0, -150, 0, -40, 2,False)  # 50%


def updateMapaHero():
    herosFullWorkIni()

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
    #INSTALAÇÕES - PIP
        #1° pip install opencv-python
        #2° pip install matplotlib
        #3° pip install PyAutoGUI
        #4° pip install mss
        #5° pip install yaml2 pip install PyYAML
    #print('Kdu')
    #findTelaXY(findListImgInRef, onclicked, False, listaddX, listaddY, False, False, 0.98)

    #findTelaXY(go_max_nav)
    #CheckLogin()
    #herosFullWorkIni()

    #heroesSelectTpIni(True)
    #findTelaXyQtd(go_selecfull80_nav, 0.98)
    #findBoxImgPoints(go_ini_boss, -650, -405, 397, 339, listFind, 0, 0, True, True, 0, -150, 0, -40, 7, False,True)  # 50%

    #findTelaXY(findListImgInRef, onclicked, False, listaddX, listaddY, False, False, 0.98)
    #findTelaXY(go_selecfull80_nav,False,False,130,42,False,False,0.98)
    #VERIFICA - COLOCA AO MENOS 12 NAVES
    #findBoxScrollImg(go_ini_boss, -650, -405, 397, 339, go_selecfull80_nav, 130, 42, True, True, 0, -150, -45, -45, 3)
    # CheckLogin()
    #return
 ###########################AMBIENTE DE TESTE########################################
    while True:
        print('SE GOSTOU DO BOOT DO BOMB - FIQUE A VONTADE PARA PASSAR UM CAFE/SPG/SPE :)')
        print('CARTEIRA WALET: 0xAc8b000865BdBcD6C4eD4Ac85475Afd57DD2244D \n')

        print('BOT SPACECRYPTO 2022 - INICIAL NO SISTEMA. Aguarde 3s...')
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
                    print('INICIANDO FULL COM TODOS AS 15 NAVES - ÀS {} '.format(horarioexato()))
                    herosFullWorkIni()

                    t_cont['hero_full_work'] = now
                    t_cont['time_refresh_position'] = now

                    #t_work_map['now_work_hero'] = now
                    t_work_map['time_work_hero'] = c_time_work_map['hero_full_work']
            ##############################################################    
            
            #################### WORK RARIDADE ################################
            if(select_bomber_tp['raridade_']):
                if (now - t_cont['hero_comum_work']) > (c_time_loop['hero_comum_work'] * 60):
                    updateMapaHero()
                    print('INICIANDO COM OS COMUNS - ÀS {} '.format(horarioexato()))
                    heroesSelectTpIni(True)

                    t_cont['hero_comum_work'] = now
                    
                    #t_work_map['now_work_hero'] = now
                    t_work_map['time_work_hero'] = c_time_work_map['hero_comum_work']

            ##############################################################    
            
            #################### CONDIÇÕES REFRESH ################################
            if (now - t_cont['time_refresh_position']) > (c_time_loop['time_refresh_position'] * 60):
                herosFullWorkIni()
                t_cont['time_refresh_position'] = now
main()