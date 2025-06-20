# cliente_pi.py

import socket
import random
import time

# --- Configurações do Cliente ---
# Se o servidor estiver em outra máquina, coloque o IP dela aqui
HOST = '127.0.0.1'  # 'localhost' para testes na mesma máquina
PORT = 50000      

def calcularPontosNoCirculo(pontosASimular):
    pontosNoCirculo = 0
    for _ in range(pontosASimular):
        x = random.random()
        y = random.random()
        if (x*x + y*y) <= 1:
            pontosNoCirculo += 1
    return pontosNoCirculo

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            print("Tentando conectar ao servidor...")
            s.connect((HOST, PORT))
            print("Conectado! Aguardando tarefa...")
            
            dadosRecebidos = s.recv(1024)
            pontosASimular = int(dadosRecebidos.decode('utf-8'))
            print(f"Tarefa recebida: simular {pontosASimular} pontos.")
            
            inicio_proc = time.time()
            resultadoParcial = calcularPontosNoCirculo(pontosASimular)
            fim_proc = time.time()
            print(f"Processamento local concluído em {fim_proc - inicio_proc:.4f} segundos.")
            
            s.sendall(str(resultadoParcial).encode('utf-8'))
            print(f"Resultado ({resultadoParcial}) enviado. Encerrando.")

        except ConnectionRefusedError:
            print("Erro de conexão: O servidor não está ativo ou recusou a conexão.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()