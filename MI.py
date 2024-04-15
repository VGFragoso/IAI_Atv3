class BaseConhecimento:
    def __init__(self):
        self.fatos = {}
        self.regras = {}

    def adicionar_fato(self, item, caracteristicas):
        self.fatos[item] = caracteristicas

    def adicionar_regra(self, condicoes, resultado):
        self.regras[tuple(sorted(condicoes.items()))] = resultado

    def inferir(self, caracteristicas):
        melhor_condicao = None
        numero_de_itens_na_melhor_condicao = 0

        for condicoes in self.regras:
            checagem_de_itens = [item in caracteristicas.items() for item in condicoes]
            if all(checagem_de_itens):
              qtde_itens_condicao_atual = len(checagem_de_itens)
              if qtde_itens_condicao_atual > numero_de_itens_na_melhor_condicao: ##Alteração realizada por Luigi
                numero_de_itens_na_melhor_condicao = qtde_itens_condicao_atual
                melhor_condicao = condicoes

        if melhor_condicao is not None:
          return self.regras[melhor_condicao]

        return None

base = BaseConhecimento()

base.adicionar_regra({"rodas": 2}, "ciclo")
base.adicionar_regra({"rodas": 3, "motor": "nao"}, "ciclo") #Alteração realizada por Luigi
base.adicionar_regra({"rodas": 4, "motor": "sim"}, "automovel")

base.adicionar_regra({"veiculoTipo": "ciclo", "rodas": 2, "motor": "nao"}, "bicicleta")
base.adicionar_regra({"veiculoTipo": "ciclo", "rodas": 3, "motor": "nao"}, "triciclo")
base.adicionar_regra({"veiculoTipo": "ciclo", "rodas": 2, "motor": "sim"}, "motocicleta")

base.adicionar_regra({"veiculoTipo": "automovel", "tamanho": "pequeno", "portas": 2}, "CarroSport")
base.adicionar_regra({"veiculoTipo": "automovel", "tamanho": "medio", "portas": 4}, "Sedan")
base.adicionar_regra({"veiculoTipo": "automovel", "tamanho": "medio", "portas": 3}, "Minivan")
base.adicionar_regra({"veiculoTipo": "automovel", "tamanho": "grande", "portas": 4}, "UtilitarioSport")

while True: ##Adição do laço While com o inpt do usuário referente as duas intâncias da inferência 
    entrada_rodas = int(input("Quantidade de rodas do veículo (2, 3 ou 4): "))
    entrada_motor = input("Possui motor (sim ou nao): ")

    caracteristicas_veiculo = {"rodas": entrada_rodas, "motor": entrada_motor}

    tipo_veiculo = base.inferir(caracteristicas_veiculo)

    if tipo_veiculo:
        if tipo_veiculo == "ciclo":
            caracteristicas_ciclo = {"veiculoTipo": "ciclo", "rodas": entrada_rodas, "motor": entrada_motor}
            tipo_ciclo = base.inferir(caracteristicas_ciclo)

            if tipo_ciclo:
                print(f"O veículo é um {tipo_ciclo}")
                break ##Primeiro Break para caso seja um ciclo.
            else:
                print("Não foi possível determinar o tipo específico do ciclo")

        elif tipo_veiculo == "automovel":
            tamanho = input("Tamanho do automóvel (pequeno, medio ou grande): ")
            portas = int(input("Quantidade de portas do automóvel (2, 3 ou 4): "))
            caracteristicas_automovel = {"veiculoTipo": "automovel", "tamanho": tamanho, "portas": portas}
            tipo_automovel = base.inferir(caracteristicas_automovel)

            if tipo_automovel:
                print(f"O veículo é um {tipo_automovel}")
                break ##Segundo Break com o tipo de automovel.
            else:
                print("Não foi possível determinar o tipo específico do automóvel")

    else:
        print("Não foi possível determinar o tipo do veículo")
