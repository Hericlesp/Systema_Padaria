#codigo=['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20']
#codigo=[]
#codDesc={}
#descricao=[]
#total = 0
descPrec={

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
            print('  PRODUTO:' )
            descricao=str(input('    ')).upper()
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
    print("           1            2          3     ")
    print("       PRODUTOS     CADASTRO    VENDAS   ")
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
        print('     VOLTA: ( sim / nao)')
        cad2=str(input('    '))
        ml()
        if cad2=='sim':
            #cadastro()
            login()
        
                
    elif operacao== 2:
        import os
        os.system('cls')
        print("\n"*4)
        ml()
        ml()
        cadastro()

        

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
            comanda()
            ml()
            print('            1                      2    ')
            print('     FINALIZAR VENDA         ADD PRODUTO') 
            venda=str(input('    ')) 
            ml()
            if venda==1:
                comanda()

            elif venda==2:
                print('ADD NOVO LANCHE: ')
                for pedido in descPrec:
                    print('   DIGITE O PRODUTO: ')

                    total += descPrec[pedido]
                    print('   PEDIDO ADD AO CARRINHO')
                    itenVend[pedido]=descPrec['']

            
            
      
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

login()
