import time
import sys

while True:
    criarsenha = input('Crie sua senha: ')
    confirmarsenha = input('Confirme sua senha: ')

    if criarsenha != confirmarsenha:
        print('As senhas não coincidem.')
        continue
    
    senha = input('Digite sua senha: ')
    
    if senha == confirmarsenha:
        # Função para simular um carregamento com uma barra de progresso
        def barra_progresso(total, tempo_espera=0.1):
            for i in range(total+1):
                porcentagem = (i / total) * 100
                barra = ('#' * i).ljust(total)
                sys.stdout.write(f'\r[{barra}] {porcentagem:.2f}%')
                sys.stdout.flush()
                time.sleep(tempo_espera)
            print("\nCarregamento completo!")
            print('Feliz Ano Novo, meu chapa!')
        
        # Chamando a função
        barra_progresso(30, 0.1)  # total de 30 unidades, espera 0.1s entre cada atualização
        break  # Sai do loop após o carregamento
    else:
        print('Senha incorreta, tente novamente.')
