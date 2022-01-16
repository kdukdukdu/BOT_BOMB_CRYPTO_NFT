import cv2 as cv2
import printscreenout
import numpy
import pyautogui
import time

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
#######################################################################################################
def coordTelaXY(find_in_inscreen):
    screen = printscreenout.printScreenTela()#printa a tela
    cv2.imwrite('resultados/PrintTelaOk.jpg',screen)#guarda a imagem 
    screen = cv2.imread('resultados/PrintTelaOk.jpg')#carrega a imagem
    return findElementosScreen(screen,find_in_inscreen)
#######################################################################################################
def findTelaXY(find_in_inscreen,onclicked= False,doubleclick = False,addX = 0,addY = 0,f5Pag = False,listUn = False,workheroes = False):#BUSCA EM TODA A TELA A POSIÇÃO DAS IMAGENS
    screen = printscreenout.printScreenTela()#printa a tela
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
                    printscreenout.Scroll(workheroes)

            cont = cont + 1
        return True
    else:
        return False
#######################################################################################################