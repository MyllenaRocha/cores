# \033[m
nome = "Myllena"
print("Olá, {}{}{}".format("\033[37m", nome, "\033[m"))

cores = {'verde': "\033[32m",
         'vermelho': "\033[31m",
         'amarelo': "\033[33m",
         'azul': "\033[34m",
         'magenta': "\033[35m",
         'ciano': "\033[36m",
         'cinza': "\033[37m",
         'limpo': "\033[m"}

print("Opção de cores: \033[1;33m(verde),(vermelho),(amarelo),(azul),(magenta),(ciano),(cinza)\033[m")
escolha = str(input('Escolha uma cor: '))
while (escolha != 'verde' and escolha != 'azul' and escolha != 'vermelho' and escolha != 'ciano' and escolha != 'magenta' and escolha != 'cinza' and escolha != 'amarelo'):
    print("{}OPÇÃO INVÁLIDA!{}".format(cores['vermelho'], cores['limpo']))
    print("Opção de cores: \033[1;31m(verde),(vermelho),(amarelo),(azul),(magenta),(ciano),(cinza)\033[m")
    escolha = str(input('Escolha uma cor: '))
if escolha == 'verde':
    print('{}Legal{}'.format(cores['verde'], cores['limpo']))
elif escolha == 'amarelo':
    print("{}Legal{}".format(cores['amarelo'], cores['limpo']))
elif escolha == 'vermelho':
    print("{}Legal{}".format(cores['vermelho'], cores['limpo']))
elif escolha == 'azul':
    print('{}legal{}'.format(cores['azul'], cores['limpo']))
elif escolha == 'magenta':
    print("{}Legal{}".format(cores['magenta'], cores['limpo']))
elif escolha == 'ciano':
    print("{}Legal{}".format(cores['ciano'], cores['limpo']))
elif escolha == 'cinza':
    print('{}Legal{}'.format(cores['cinza'], cores['limpo']))




