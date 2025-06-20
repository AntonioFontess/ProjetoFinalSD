# servidor_principal.py

import socket
import time
import threading
from thread_servidor import ThreadServidor 

# --- Configurações Principais ---
# Você pode alterar estes valores para os seus testes
HOST = '0.0.0.0'  # Deixe assim para o servidor aceitar conexões de qualquer IP
PORT = 50000
totalPontos = 100_000_000
numClientes = 4   # Quantos clientes o servidor vai esperar antes de começar

def main():
    # Estas variáveis são compartilhadas por todas as threads
    resultadosParciais = []
    resultadosLock = threading.Lock()

    # Cria o socket principal do servidor
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        
        print(f"--- Servidor Distribuído de Cálculo de Pi ---")
        print(f"Servidor escutando em {HOST}:{PORT}")
        print(f"Aguardando {numClientes} clientes se conectarem...")
        
        threadsAtivas = []
        pontosPorCliente = totalPontos // numClientes

        # Loop para aceitar as conexões
        for _ in range(numClientes):
            # Aceita uma nova conexão
            conn, addr = s.accept()
            
            # Cria um objeto da nossa classe Thread, passando a conexão e a tarefa
            novaThread = ThreadServidor(conn, addr, pontosPorCliente, resultadosParciais, resultadosLock)
            
            # Inicia a thread (o método run() será executado)
            novaThread.start()
            
            # Adiciona a thread à lista para controle
            threadsAtivas.append(novaThread)
            
        print(f"\nTodos os {numClientes} clientes conectados. Disparando tarefas e aguardando conclusão...")
        
        # Marca o tempo de início do processamento efetivo
        inicio = time.time()
        
        # Espera todas as threads da lista terminarem seus trabalhos
        for thread in threadsAtivas:
            thread.join()
        
        # Marca o tempo de fim
        fim = time.time()
        
        # Soma os resultados parciais de todas as threads
        totalPontosNoCirculo = sum(resultadosParciais)
        # Calcula a estimativa final de Pi
        piEstimado = 4 * totalPontosNoCirculo / totalPontos
        tempoTotal = fim - inicio
        
        print("\n--- CÁLCULO FINALIZADO ---")
        print(f"Estimativa de Pi: {piEstimado}")
        print(f"Tempo de processamento distribuído: {tempoTotal:.4f} segundos")

if __name__ == "__main__":
    main()