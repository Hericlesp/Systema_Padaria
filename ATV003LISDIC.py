codigo=['01','02','03','04','05']
#codigo=[]
#codDesc={}
#descricao=[]
#total = 0
descPrec={
    'uva':8.00,
    'pera':9.00,
    'maca':7.00,
}
#preco=[]
#preco={}
itenVend={

}

loop=0
venda="2"


def ml():
    print('==='*15)


def intro():
    ml()
    print("\n")
    print("                 TECNOSYS                       ")
    print("     ...gestão de estoque e vendas...            ")
    print('\n')
    ml()

# def intro2():
#     ml()
#     print("           1            2          3     ")
#     print("       PRODUTOS     CADASTRO    VENDAS   ")
#     ml()
#     print('  TECLE A OPERAÇÃO:  ')
#     operacao=int(input('     '))

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
                #print(codDesc,)
                #print(descPrec,)
                #print('R$', preco)
                #print('\n'*6)
                login()
                #break


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
            #comanda()
            ml()
            print('         1                2        exit')
            print('  FINALIZAR VENDA   ADD PRODUTO    MENU') 
            venda=str(input('    ')).upper
            ml()
            if venda=='1':
                comanda()

            elif venda=='EXIT':
                login()

            else:
                total = 0
                print(' NOVO LANCHE: ')
                for pedido in descPrec:
                    print('   DIGITE O PRODUTO:           VOLTAR: exit')  
                    produto=str(input(' ')).upper()
                    for produto in descPrec:
                        itenVend[produto]=descPrec[produto]
                        total += descPrec[pedido]
                        ml()
                        print('   PEDIDO ADD AO CARRINHO ')
                        ml()
                        
                    print(' VER COMANDA:  1        VOLTAR: exit')
                    carrinho=str(input('    '))
                    ml()
                    if produto=='exit':
                        comanda()

                    elif carrinho=='exit':
                    #cadastro()
                        login()
                    else:
                        comanda()
                    #itenVend[pedido]=descPrec['']
            


def login():
    import os
    os.system('cls')
    print("\n"*4)
    ml()
    ml()
    print("\n")
    print("                 TECNOSYS                       ")
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
        #print(codDesc)
        #print(descPrec)
        for item in descPrec:
            print(item, '  R$ ',descPrec[item])
        # #print(preco, end='  ')
        print('\n')
        ml()
        # print('                 2    ')
        # print('     CADASTRAR NOVO PRODUTO?  (sim / nao)') 
        print('     VOLTA: exit      CADASTRAR: 02')
        cad2=str(input('    '))
        ml()
        if cad2=='exit':
            #cadastro()
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
            venda=str(input('    ')).upper
            ml()
            if venda==1:
                comanda()
            elif venda=='EXIT':
                login()
            else:
                total = 0
                print(' NOVO LANCHE: ')
                for pedido in descPrec:
                    print('   DIGITE O PRODUTO:           VOLTAR: exit')  
                    produto=str(input(' ')).upper()
                    
                    for produto in descPrec:
                        itenVend[produto]=descPrec[produto]
                        total += descPrec[pedido]
                        ml()
                        print('   PEDIDO ADD AO CARRINHO ')
                        ml()
                    print(' VER COMANDA:  1        VOLTAR: exit')
                    carrinho=str(input('    '))
                    ml()
                    if produto=='exit':
                        comanda()

                    elif carrinho=='exit':
                    #cadastro()
                        login()
                    else:
                        comanda()
                    #itenVend[pedido]=descPrec['']

            
            
      
def comanda():
    total = 0
    import os
    os.system('cls')
    print("     --- COMANDA ---   ")
    intro()
    print('   PEDIDO BALCÃO: ')
    ml()
    #total = total
    for vendidos in itenVend:
        print(vendidos, '  R$ ',itenVend[vendidos])
        total += itenVend[vendidos]
    ml()
    print('   TOTAL PEDIDO:           R$  ',total)
    ml()
    print('  ')
    print('          1               2        EXIT')
    print(' FINALIZAR PEDIDO   ADD PRODUTO    MENU')
    final=str(input('  '))
    if final == 1:
        #limpar a comanda e voltar ao menu de vendas
        print(' PEDIDO FINALIZADO ')
        print('tecle enter para sair')
        enter=str(input('   '))
        login()
        #add comando de limpar lista de itens venvidos

    elif final == 2:
        vender()
    
    else:
        login()

login()
