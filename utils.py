from models import Pessoas

def insere_pessoas():
    pessoa = Pessoas(nome='Neiva', idade=25)
    print(pessoa)
    pessoa.save()

# Consulta dados na tabela pessoa
def consulta():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Neiva').first()
    print(pessoa.idade)

# Altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Neiva').first()
    pessoa.idade= 21
    pessoa.save()

# Exclui dados na tabela pessoa
def exclui_pessoa():
    pessoa = pessoa.query.filter_by(nome='Neiva').first()
    pessoa.delete()

if __name__ == '__main__':
    #insere_pessoas()
    #consulta()
    #altera_pessoa()
    exclui_pessoa()
    consulta_pessoas()