class Semaforo:
    def __init__(self, direcao):
        self.direcao = direcao
        self.estado = "vermelho"
        self.veiculos = []
        self.tempo_fechado = 0
        self.tempo_aberto = 0

    def adicionar_veiculo(self, veiculo):
        self.veiculos.append(veiculo)

    def atualizar_estado(self, estado_novo):
        if estado_novo == "verde":
            self.estado = "verde"
            self.tempo_aberto += 1
            self.tempo_fechado = 0
        else:
            self.estado = "vermelho"
            self.tempo_fechado += 1
            self.tempo_aberto = 0

    def liberar_veiculos(self):
        if self.estado == "verde":
            liberados = len(self.veiculos)
            self.veiculos = []  # Todos os veículos passam
            return liberados
        return 0

    def deve_abrir(self):
        return len(self.veiculos) > 3 or self.tempo_fechado > 30
