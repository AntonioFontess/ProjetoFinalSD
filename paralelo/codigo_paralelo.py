import threading
import random
import time

TOTAL_PONTOS = 10_000_000
NUM_THREADS = 4

pontos_dentro_do_circulo = 0
lock = threading.Lock()

def calcula_parcial(qtd_pontos):
    global pontos_dentro_do_circulo
    pontos_local = 0

    for _ in range(qtd_pontos):
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1:
            pontos_local += 1

    # Atualiza o contador global com lock
    with lock:
        pontos_dentro_do_circulo += pontos_local

def main():
    global pontos_dentro_do_circulo
    threads = []
    inicio = time.time()

    # Divide os pontos igualmente e distribui o resto
    pontos_por_thread = [TOTAL_PONTOS // NUM_THREADS] * NUM_THREADS
    resto = TOTAL_PONTOS % NUM_THREADS
    for i in range(resto):
        pontos_por_thread[i] += 1

    # Cria e inicia as threads
    for pontos in pontos_por_thread:
        thread = threading.Thread(target=calcula_parcial, args=(pontos,))
        threads.append(thread)
        thread.start()

    # Aguarda todas as threads terminarem
    for thread in threads:
        thread.join()

    fim = time.time()

    pi_aproximado = 4 * (pontos_dentro_do_circulo / TOTAL_PONTOS)

    print(f"Pi aproximado: {pi_aproximado}")
    print(f"Tempo de execução paralelo: {fim - inicio:.4f} segundos")

if __name__ == "__main__":
    main()
