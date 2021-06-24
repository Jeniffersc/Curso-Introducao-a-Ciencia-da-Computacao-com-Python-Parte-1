def main():
    escolha_CouP = int(input("Bem vindo ao jogo NIM! Escolha: \n1 - para jogar uma partida isolada \n2 - para jogar um campeonato 2 \n"))
    if escolha_CouP==1:
        input("Voce escolheu uma partida!")
    else:
        if escolha_CouP==2:
            input("Voce escolheu um campeonato!")
        else:
            while escolha_CouP!=1 or escolha_camp!=2:
                escolha_CouP = int(input("Escolha novamente: "))
                if escolha_CouP==1:
                    input("Voce escolheu uma partida!")
                else:
                    if escolha_CouP==2:
                        input("Voce escolheu um campeonato!")

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogadas? ")) #Limite de peças retiradas por rodada
    #Usuario
    if n % (m+1) == 0:
        print("Você começa!")
        usuario_escolhe_jogada(n, m)
        if usuario_escolhe_jogada(n, m) == 1:
            print ("Você tirou uma peça.")
        else:
            print ("Você tirou ", usuario_escolhe_jogada(n, m) ," peças.")          
        tot = n
        tot = tot - usuario_escolhe_jogada(n, m)
        if tot == 1:
            print ("Agora resta apenas uma peça no tabuleiro.")
        else:
            print ("Agora restam ", tot, "peças no tabuleiro.")
             
    #Computador        
    else:
        print("Computador começa!")
        computador_escolhe_jogada(n, m)
        if computador_escolhe_jogada(n, m) == 1:
            print ("O computador tirou uma peça.")
        else:
            print ("O computador tirou ", computador_escolhe_jogada(n, m) ," peças.")
        tot = n
        tot = tot - computador_escolhe_jogada(n, m)
        if tot == 1:
            print ("Agora resta apenas uma peça no tabuleiro.")
        else:
             print ("Agora restam ", tot, "peças no tabuleiro.")


    #Próximas Chamadas
    if n % (m+1) == 0:
        while tot<n and tot>0:        
            computador_escolhe_jogada(n, m)
            if computador_escolhe_jogada(n, m) == 1:
                print ("O computador tirou uma peça.")
            else:
                print ("O computador tirou ", computador_escolhe_jogada(n, m) ," peças.")
            tot = tot - computador_escolhe_jogada(n, m)
            if tot == 1:
                print ("Agora resta apenas uma peça no tabuleiro.")
            else:
                 print ("Agora restam ", tot, "peças no tabuleiro.")
        
            if tot<n and tot>0:
                usuario_escolhe_jogada(n, m)
                if usuario_escolhe_jogada(n, m) == 1:
                    print ("Você tirou uma peça.")
                else:
                    print ("Você tirou ", usuario_escolhe_jogada(n, m) ," peças.") 
                tot = tot - usuario_escolhe_jogada(n, m)
                if tot == 1:
                    print ("Agora resta apenas uma peça no tabuleiro.")
                else:
                     print ("Agora restam ", tot, "peças no tabuleiro.")
            else:
                tot = tot
    else:
        while tot<n and tot>0:  
            usuario_escolhe_jogada(n, m)
            if usuario_escolhe_jogada(n, m) == 1:
                print ("Você tirou uma peça.")
            else:
                print ("Você tirou ", usuario_escolhe_jogada(n, m) ," peças.")          
            tot = n
            tot = tot - usuario_escolhe_jogada(n, m)
            if tot == 1:
                print ("Agora resta apenas uma peça no tabuleiro.")
            else:
                 print ("Agora restam ", tot, "peças no tabuleiro.")

            if tot<n and tot>0:
                computador_escolhe_jogada(n, m)
                if computador_escolhe_jogada(n, m) == 1:
                    print ("O computador tirou uma peça.")
                else:
                    print ("O computador tirou ", computador_escolhe_jogada(n, m) ," peças.")
                tot = tot - computador_escolhe_jogada(n, m)
                if tot == 1:
                    print ("Agora resta apenas uma peça no tabuleiro.")
                else:
                     print ("Agora restam ", tot, "peças no tabuleiro.")
            else:
                tot = tot

def computador_escolhe_jogada(n, m):
    tot = n
    if tot <= m:
        c_retirar = tot
    else:
        c_retirar = n - (m+1)
    return (c_retirar) 

def usuario_escolhe_jogada (n, m):
    u_retirar = int(input("Quantas peças você vai tirar? "))
    if u_retirar <= m and u_retirar <= n:
        tot = n
        tot = tot - u_retirar
    else:
        u_retirar = int(input("Oops! Jogada inválida! Tente de novo. \nQuantas peças você vai tirar? "))
        if u_retirar <= m and u_retirar <= tot:
            tot = tot - u_retirar
        else:
            u_retirar = int(input("Oops! Jogada inválida! Tente de novo. \nQuantas peças você vai tirar? "))
    return (u_retirar)

