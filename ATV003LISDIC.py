#codigo=['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20']
#codigo=[]
#codDesc={}
#descricao=[]
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
    print("\n"*4)
    ml()
    ml()
    print("\n")
    print("                 TECNOSYS                       ")
    print("     ...gestão de estoque e vendas...            ")
    print('\n')
    ml()
    ml()

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
            print('NOVO PRODUTO?  (sim / nao)' )
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
                print(descPrec,)
                #print('R$', preco)
                print('\n'*6)
                break




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
    #print(codDesc)
    print(descPrec)
    #print(preco, end='  ')
    print('\n')
    ml()
    print('                 2    ')
    print('     CADASTRAR NOVO PRODUTO?  (sim / nao)') 
    cad2=str(input('    '))
    ml()
    if cad2=='sim':
         cadastro()
        
                
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
    print(descPrec)
    ml()
    total=0
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
                itenVend[pedido]=descPrec[descricao]

            
            
            
def comanda():
    print("     --- COMANDA ---   ")
    intro()
    print('   PEDIDO BALCÃO: ')
    ml()
    itens()

    ml()
    print('   TOTAL PEDIDO: ')
