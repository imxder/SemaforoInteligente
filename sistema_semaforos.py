from veiculos import Veiculo
from semaforos import Semaforo
import time
import random

class SistemaSemaforo:
    def __init__(self):
        # Inicializa os semáforos em suas respectivas direções
        self.semaforos = {
            "Norte": Semaforo("Norte"),
            "Sul": Semaforo("Sul"),
            "Leste": Semaforo("Leste"),
            "Oeste": Semaforo("Oeste")
        }
        self.tempo_atual = 0

    def adicionar_veiculos(self):
        """
        Adiciona veículos aleatoriamente em cada direção, simulando o trânsito.
        """
        for direcao, semaforo in self.semaforos.items():
            num_veiculos = random.randint(0, 5)  # Simula veículos chegando aleatoriamente
            for i in range(num_veiculos):
                veiculo = Veiculo(f"V_{direcao}_{i}", self.tempo_atual)
                semaforo.adicionar_veiculo(veiculo)

    def atualizar(self):
        """
        Atualiza o estado dos semáforos a cada ciclo.
        A prioridade é abrir o semáforo com mais veículos. Se não houver, abre o que está fechado por mais tempo.
        """
        self.tempo_atual += 1

        # Fecha todos os semáforos inicialmente
        for semaforo in self.semaforos.values():
            semaforo.atualizar_estado("vermelho")

        # Verifica se há algum semáforo com mais de 3 veículos
        semaforo_maior_fila = max(self.semaforos.values(), key=lambda s: len(s.veiculos))

        # Prioridade 1: Semáforo com mais veículos
        if len(semaforo_maior_fila.veiculos) > 3:
            semaforo_maior_fila.atualizar_estado("verde")
        else:
            # Prioridade 2: Semáforo que está fechado há mais de 30 segundos
            semaforo_tempo_fechado = max(self.semaforos.values(), key=lambda s: s.tempo_fechado)
            if semaforo_tempo_fechado.deve_abrir():
                semaforo_tempo_fechado.atualizar_estado("verde")

        self.exibir_estados()

        # Libera veículos no semáforo que ficou verde
        liberados = semaforo_maior_fila.liberar_veiculos()
        print(f"Semáforo {semaforo_maior_fila.direcao} - Veículos liberados: {liberados}")

    def exibir_estados(self):
        """
        Exibe o estado de cada semáforo e quantos veículos estão esperando.
        """
        for direcao, semaforo in self.semaforos.items():
            print(f"Semáforo {direcao} - Veículos esperando: {len(semaforo.veiculos)}")

    def executar(self, ciclos=10):
        """
        Executa o sistema de semáforos por um número de ciclos determinado.
        """
        for _ in range(ciclos):
            self.adicionar_veiculos()
            self.atualizar()
            time.sleep(1)  # Espera de 1 segundo entre cada ciclo para simular o tempo real

if __name__ == "__main__":
    sistema = SistemaSemaforo()
    sistema.executar(20)  