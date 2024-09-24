class Veiculo:
    def __init__(self, id, tempo_chegada):
        self.id = id
        self.tempo_chegada = tempo_chegada
        self.tempo_espera = 0

    def atualizar_tempo_espera(self, tempo_atual):
        self.tempo_espera = tempo_atual - self.tempo_chegada
