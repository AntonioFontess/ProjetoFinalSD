import time

# Biblioteca time faz medição dos tempos

def medir_tempo_execucao(funcao, *args, **kwargs):

# Parâmetros:
# - funcao: função a ser executada.
# - *args: argumentos posicionais da função.
# - **kwargs: argumentos nomeados da função.

inicio = time.perf_counter()
resultado = funcao(*args, **kwargs)
fim = time.perf_counter()
duracao = fim - inicio

# Exemplo de chamada
# -------------------
# resultado = medir_tempo_execucao(calcular_pi_sequencial, 10_000_000)
# print(f"Pi estimado: {resultado['resultado']}")
# print(f"Tempo de execução: {resultado['tempo']:.4f} segundos")
# -------------------

return {
	'resultado': resultado,
	'tempo': duracao
}

