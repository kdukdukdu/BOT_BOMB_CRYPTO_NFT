def loadconfig():
    import yaml
    print('Oi')
    stream = open("config.yaml", 'r')# LÊ AS CONNFIGURAÇÕES O ARQUIVO
    config = yaml.safe_load(stream)
    c_time_loop = config['time_intervals']

def loadinread():
    import cv2 as cv2

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
    
    #go_moeda = cv2.imread('targets/moeda.png')#Botão da Moeda

    ok_bt = cv2.imread('targets/new50/erro/ok.png')#botão ok