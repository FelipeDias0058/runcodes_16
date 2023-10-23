#Calcula o valor da prestação com base no valor da compra
def f_prestacao(v_compra):
    for p in range(1, 23):
        prestacao = v_compra / p
        print(f'{p}x de R$ {prestacao:.2f}')


def main():

    #Entrada de Dados
    v_compra = float(input())

    #Saída de Dados
    f_prestacao(v_compra)

if __name__ == '__main__':
    main()

    
