class BaseConhecimento:
    def __init__(self):
        self.fatos = {}
        self.regras = {}

    def adicionar_fato(self, item, caracteristicas):
        self.fatos[item] = caracteristicas

    def adicionar_regra(self, condicoes, resultado):
        self.regras[tuple(sorted(condicoes.items()))] = resultado

    def inferir(self, caracteristicas):
        for condicoes in self.regras:
            if all(item in caracteristicas.items() for item in condicoes):
                return self.regras[condicoes]
        return None

base = BaseConhecimento()

base.adicionar_regra({"rodas": 2}, "ciclo")
base.adicionar_regra({"rodas": 3}, "ciclo")
base.adicionar_regra({"rodas": 4, "motor": "sim"}, "automovel")

base.adicionar_regra({"veiculoTipo": "ciclo", "rodas": 2, "motor": "nao"}, "bicicleta")
base.adicionar_regra({"veiculoTipo": "ciclo", "rodas": 3, "motor": "nao"}, "triciclo")
base.adicionar_regra({"veiculoTipo": "ciclo", "rodas": 2, "motor": "sim"}, "motocicleta")

base.adicionar_regra({"veiculoTipo": "automovel", "tamanho": "pequeno", "portas": 2}, "CarroSport")
base.adicionar_regra({"veiculoTipo": "automovel", "tamanho": "medio", "portas": 4}, "Sedan")
base.adicionar_regra({"veiculoTipo": "automovel", "tamanho": "medio", "portas": 3}, "Minivan")
base.adicionar_regra({"veiculoTipo": "automovel", "tamanho": "grande", "portas": 4}, "UtilitarioSport")

while True:
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
                break  
            else:
                print("Não foi possível determinar o tipo específico do ciclo")
        elif tipo_veiculo == "automovel":
            print(tipo_veiculo)
           
            tamanho = input("Tamanho do automóvel (pequeno, medio ou grande): ")
            portas = int(input("Quantidade de portas do automóvel (2, 3 ou 4): "))
            caracteristicas_automovel = {"veiculoTipo": "automovel", "tamanho": tamanho, "portas": portas}
            tipo_automovel = base.inferir(caracteristicas_automovel)
            
            if tipo_automovel:
                print(f"O veículo é um {tipo_automovel}")
                break
            else:
                print("Não foi possível determinar o tipo específico do automóvel")
                
    else:
        print("Não foi possível determinar o tipo do veículo")
