def fazer_lista():
    try:
        lista = [1, 2, 3, 4, 5]
        print(f'A media é: {sum(lista)/len(lista)}')
    except ZeroDivisionError:
        print("A lista está vazia, não é possível calcular a média.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        

fazer_lista()