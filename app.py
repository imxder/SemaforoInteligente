from flask import Flask, jsonify, render_template
import time
import threading
from sistema_semaforos import SistemaSemaforo

app = Flask(__name__)

sistema_semaforo = SistemaSemaforo()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/status')
def status():
    # Capturar as informações do estado dos semáforos e veículos
    status_data = {}
    for direcao, semaforo in sistema_semaforo.semaforos.items():
        status_data[direcao] = {
            'estado': semaforo.estado,
            'veiculos': len(semaforo.veiculos)
        }
    return jsonify(status_data)

def run_semaforo_system():
    # Executa o sistema de semáforos em um loop separado
    tempo_inicial = time.time()
    while True:
        sistema_semaforo.adicionar_veiculos()
        sistema_semaforo.atualizar()
    
        time.sleep(5)

        # Parar o sistema após 120 segundos
        if time.time() - tempo_inicial >= 120:
            print("Fim do ciclo de 120 segundos.")
            break

if __name__ == '__main__':
    # Rodar o sistema de semáforos em um thread separado
    thread = threading.Thread(target=run_semaforo_system)
    thread.start()
    app.run(debug=True)
