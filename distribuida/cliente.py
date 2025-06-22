import socket
import random
import time

# aqui fica o ip host do servidor (como estamos fazendo teste localmente, usando o localhost)
HOST = '127.0.0.1' 
PORT = 50000      

# aqui faz um calculo de quantos pontos no circulo ele recebe
def calcularPontosNoCirculo(pontosASimular):
    pontosNoCirculo = 0
    for _ in range(pontosASimular):
        x = random.random() # posicao aleatoria de 0 a 1 no eixo x
        y = random.random() # posicao aleatoria de 0 a 1 no eixo y
        if (x*x + y*y) <= 1: # se a distância ao quadrado do ponto até o centro for menor ou igual ao raio de 1 do circulo ele assume que esta dentro do circulo
            pontosNoCirculo += 1
    return pontosNoCirculo

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            print("Servidor conectado")
            
            dadosRecebidos = s.recv(1024) # aqui, vai receber uma resposta do servidor de ate 1024 bytes
            pontosASimular = int(dadosRecebidos.decode('utf-8')) # recebe oa quantidade de pontos que cada cliente vai simular
            print(f"Tarefa para o cliente de simular {pontosASimular} pontos.")
            
            inicio_proc = time.time() # inicia o contador de tempo
            resultadoParcial = calcularPontosNoCirculo(pontosASimular) # recebe a quantidade de pontos dentro do circulo
            fim_proc = time.time() # finaliza o contador de tempo
            print(f"Processamento local concluído em {fim_proc - inicio_proc:.4f} segundos.")
            
            s.sendall(str(resultadoParcial).encode('utf-8')) # envia a resposta do resultado de volta para o servidor em bytes

        except ConnectionRefusedError:
            print("Erro de conexão: O servidor não está ativo ou recusou a conexão.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

# aqui ele inicia a main
if __name__ == "__main__": 
    main()