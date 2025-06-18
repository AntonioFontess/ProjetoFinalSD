import random
import time

def monte_carlo_pi(num_pontos: int) -> float:
    """
    Estima o valor de pi usando o método de Monte Carlo.

    Args:
        num_pontos (int): número de pontos aleatórios a serem gerados

    Returns:
        float: estimativa de pi
    """
    dentro_do_circulo = 0

    for _ in range(num_pontos):
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1:
            dentro_do_circulo += 1

    return 4 * dentro_do_circulo / num_pontos

def main():
    total_pontos = 10_000_000  # Você pode testar com 100_000, 1_000_000, etc.
    
    print(f"Executando com {total_pontos} pontos...")
    inicio = time.time()

    pi_estimado = monte_carlo_pi(total_pontos)

    fim = time.time()
    duracao = fim - inicio

    print(f"Estimativa de pi: {pi_estimado}")
    print(f"Tempo de execução: {duracao:.4f} segundos")

if __name__ == "__main__":
    main()
