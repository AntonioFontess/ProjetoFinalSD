import socket
import time
import threading
from thread_servidor import ThreadServidor 

HOST = '0.0.0.0'
PORT = 50000
totalPontos = 10_000_000
numClientes = 4

def main():
    resultadosParciais = []
    resultadosLock = threading.Lock()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # Socket principal do servidor
        s.bind((HOST, PORT))
        s.listen()

        print(f"Servidor escutando em {HOST}:{PORT}")
        print(f"Aguardando {numClientes} clientes se conectarem...")
        
        threadsAtivas = []
        pontosPorCliente = totalPontos // numClientes # Divide igualmente o total de pontos entre os clientes

        for _ in range(numClientes): # Recebendo as conexões
            conn, addr = s.accept()
            novaThread = ThreadServidor(conn, addr, pontosPorCliente, resultadosParciais, resultadosLock) # Cria nova conexão

            novaThread.start() # Inicia a thread
            threadsAtivas.append(novaThread) # Adiciona a thread na lista para controle
            
        print(f"\nTodos os {numClientes} clientes conectados. Disparando tarefas e aguardando conclusão...")
        
        inicio = time.time() # Marca o início do cálculo do tempo de processamento

        # Garante que todas as threads sejam executadas completamente para calcular com precisão o tempo de execução
        for thread in threadsAtivas: 
            thread.join()
        
        fim = time.time() # Marca o fim do cálculo do tempo de processamento
        
        totalPontosNoCirculo = sum(resultadosParciais) # Soma os resultados parciais de todas as threads/clientes

        piEstimado = 4 * totalPontosNoCirculo / totalPontos # Cálculo da estimativa do valor de pi
        tempoTotal = fim - inicio # Tempo gasto no processamento
        
        print("\n--- CÁLCULO FINALIZADO ---")
        print(f"Estimativa de Pi: {piEstimado}")
        print(f"Tempo de processamento distribuído: {tempoTotal:.4f} segundos")

if __name__ == "__main__":
    main()