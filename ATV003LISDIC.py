codigo=['01','02','03','04','05']
descPrec={
    'MAÇA':7.00,
    'UVA':8.00,
    'PERA':9.00,
}

itenVend={

}

descQuant={

}

loop=0
venda="2"


def ml():
    print('==='*15)


def intro():
    ml()
    print("\n")
    print("                 TECNÓSYS                       ")
    print("     ...gestão de estoque e vendas...            ")
    print('\n')
    ml()



def cadastro():
        import os
        os.system('cls')
        print("\n"*4)
        ml()
        while True:

            ml()
            print('  PRODUTO:          VOLTAR: exit' )
            descricao=str(input('    ')).upper()
            if descricao =="EXIT":
                login()
            print('  PREÇOS: ' )
            preco=(float(input('    ')))
            descPrec[descricao]=preco
            ml()
            print('NOVO PRODUTO:  (sim / nao)     MENU: exit' )
            cad=str(input('  ')).lower()
            if cad != 'sim':
                import os
                os.system('cls')

                print("\n"*4)
                ml()
                print("          ..PRODUTO     ")
                print("          CADASTRADO..  ")
                ml()
                ml()
                print("\n"*4)
                login()


def vender():
        import os
        os.system('cls')
        print("\n"*4)
        ml()
        ml()
        for item in descPrec:
            print(item, '  R$ ',descPrec[item])
        ml()
        
        while True:
            ml()
            print('            1                2       exit ')
            print('     FINALIZAR VENDA   ADD PRODUTO   MENU') 
            venda=str(input('    ')).lower()
            ml()
            if venda==1:
                comanda()
            elif venda=='exit':
                login()
            else:
                total = 0
            
                print(' NOVO LANCHE: ')
                ml()
                print('                            VOLTAR: exit')
                print('DIGITE O PRODUTO:           ')  
                produto=str(input(' ')).upper()
                if produto=="EXIT":
                    login()
                print('QUANTIDADE DESEJADA: ')
                quantidade=float(input('  '))
                if quantidade=="EXIT":
                    login()
                                

                if produto in descPrec:         
                    itenVend[produto]=descPrec[produto]
                    descQuant[produto]=quantidade
                    total += (descPrec[produto]*quantidade)
                    ml()
                    print('   PEDIDO ADD AO CARRINHO ')
                    ml()
                else:
                    ml()
                    print('PRODUTO NAO ENCONTRADO')
                    ml()

                print('                               VOLTAR: exit')    
                print(' VER COMANDA:  1       ADD PRODUTO: 2')
                carrinho=str(input('    ')).lower()
                ml()
                if carrinho=='exit':
                  login()

                #chama cmandao.
                elif carrinho=='1':
                    comanda()
                else:
                    vender()


def login():
    import os
    os.system('cls')
    print("\n"*4)
    ml()
    ml()
    print("\n")
    print("                 TECNÓSYS                       ")
    print("     ...gestão de estoque e vendas...            ")
    print('\n')
    ml()
    ml()
    print("       1         2         3          4 ")
    print("   PRODUTOS   CADASTRO   VENDAS   COMANDAS ")
    ml()
    print('  TECLE A OPERAÇÃO:  ')
    operacao=int(input('     '))
    if operacao == 1:
        import os
        os.system('cls')
        intro()
        for item in descPrec:
            print(item, '  R$ ',descPrec[item])
        print('\n')
        ml() 
        print('     VOLTA: exit      CADASTRAR: 02')
        cad2=str(input('    ')).lower()
        ml()
        if cad2=='exit':
            login()
        else:
            cadastro()
        
                
    elif operacao== 2:
        import os
        os.system('cls')
        print("\n"*4)
        ml()
        ml()
        cadastro()

    elif operacao== 4:
        import os
        os.system('cls')
        print("\n"*4)
        ml()
        ml()
        comanda()


    else:
        import os
        os.system('cls')
        print("\n"*4)
        ml()
        ml()
        for item in descPrec:
            print(item, '  R$ ',descPrec[item])
        ml()
        
        while True:
            #comanda()
            ml()
            print('            1                2       exit ')
            print('     FINALIZAR VENDA   ADD PRODUTO   MENU') 
            venda=str(input('    ')).lower()
            ml()
            if venda==1:
                comanda()
            elif venda=='exit':
                login()
            else:
                total = 0
            
                print(' NOVO LANCHE: ')
                ml()
                print('                            VOLTAR: exit')
                print('DIGITE O PRODUTO:           ')  
                produto=str(input(' ')).upper()
                if produto=="EXIT":
                    login()
                print('QUANTIDADE DESEJADA: ')
                quantidade=float(input('  '))
                if quantidade=="EXIT":
                    login()
                                

                if produto in descPrec:         
                    itenVend[produto]=descPrec[produto]
                    descQuant[produto]=quantidade
                    total += (descPrec[produto]*quantidade)
                    ml()
                    print('   PEDIDO ADD AO CARRINHO ')
                    ml()
                else:
                    ml()
                    print('PRODUTO NAO ENCONTRADO')
                    ml()

                print('                               VOLTAR: exit')    
                print(' VER COMANDA:  1       ADD PRODUTO: 2')
                carrinho=str(input('    ')).lower()
                ml()
                if carrinho=='exit':
                    login()

                #chama comanda.
                elif carrinho=='1':
                    comanda()

                else:
                    vender()




#finalizar venda.
def comanda():
    total = 0
    import os
    os.system('cls')
    print("     --- COMANDA ---   ")
    intro()
    print('   PEDIDO BALCÃO: ')
    ml()
    print('PRODUTO  QUANT.   PREÇO uni     TOTAL ')
    print('\n')

    for produto in itenVend:
        print(produto, '   ',descQuant[produto],'      | R$ ', itenVend[produto],'     R$',(itenVend[produto] * descQuant[produto]))
        total += (itenVend[produto]*descQuant[produto])
        

    ml()
    print('   TOTAL PEDIDO:           R$  ',total)
    ml()


    print('  ')
    print('                                        📜MENU: EXIT')
    print('        1               2             3     ')
    print('🖨️FIN.PEDIDO   ➕ADD.PRODUTO   ❌CANCELAR ')
    final=str(input('  '))
    if final == 1:
        comanda_final
    elif final==2:
        vender()
    elif final == '3':
        itenVend.clear()
        login()
    else:
        login()
       
        


def comanda_final():
    intro()
    print(' PEDIDO FINALIZADO ')
    print('DESEJA IDENTIFICAR? ')
    nome=str(input('     ')).upper()

    total = 0

    import os
    os.system('cls')
    #add forma de pagamento
    print("     --- COMANDA ---   ")
    intro()
    print('   PEDIDO BALCÃO: ')
    ml()
    print('IDENTIFICAÇÃO:  ',nome)
    ml()
    print('PRODUTO  QUANT.   PREÇO uni     TOTAL ')
    print('\n')

    for produto in itenVend:
        print(produto, '   ',descQuant[produto],'      | R$ ', itenVend[produto],'     R$',(itenVend[produto] * descQuant[produto]))
        total += (itenVend[produto]*descQuant[produto])
        

    ml()
    print('   TOTAL PEDIDO:           R$  ',total)
    ml()

    print('  ')
    print('        1       ')
    print(' 🖨️ FIN.PEDIDO ')
    imprimir=str(input('  '))
    if imprimir == 1:
        print(' PEDIDO FINALIZADO ')
        itenVend.clear()
        print('tecle enter para sair')
        enter=(input('   '))
        if enter !=0:
            login()


login()
#add login de entrada
#add forma de pagamento



