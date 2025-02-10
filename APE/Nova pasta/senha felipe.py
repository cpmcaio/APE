while(True):
    criarsenha= (input('crie sua senha: '))
    confirmesuasenha=(input('confirme sua senha: '))
    if confirmesuasenha==criarsenha:
        senha= (input('digite sua senha: '))
    elif criarsenha!=confirmesuasenha:
        print('as senhas não coincidem!!')
        continue
    if confirmesuasenha==senha:
            print ('acesso liberado')
            print('bem vindo, cbum.')
            print('receba')
            print('em dezembro de 81...')
            print('siuuuuuuuuu')
            break
    else:
        print('senha inválida: ')
        continue
