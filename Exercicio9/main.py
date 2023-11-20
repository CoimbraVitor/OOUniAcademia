from Funcionario import Funcionario
from Dependente import Dependente
from Cargo import Cargo



def main():
    programador = Cargo(nome="Programador", salario_base=5000)
    funcionario1 = Funcionario("Vitor", programador, "23/05/2001")
    dependente1 = Dependente("Alice", "16/02/2015")
    dependente2 = Dependente("Felipe", "03/09/2010")

    programador.calcular_salario_bruto(250)
    funcionario1.adicionar_dependente(dependente1)
    funcionario1.adicionar_dependente(dependente2)
    print(f"Salário líquido: {funcionario1.calcular_salario_liquido()}")
    funcionario1.listar_dependentes()






if __name__ == "__main__":
    main()