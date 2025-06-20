# thread_servidor.py

import threading
import socket

# Esta classe herda de Thread e contém a lógica para atender um cliente
class ThreadServidor(threading.Thread):

    def __init__(self, conexao, endereco, pontosParaSimular, resultadosParciais, lock):
        # Construtor da classe
        threading.Thread.__init__(self)
        self._conexao = conexao
        self._endereco = endereco
        self._pontosParaSimular = pontosParaSimular
        self._resultadosParciais = resultadosParciais
        self._lock = lock
        print(f"Cliente {self._endereco} conectado. Thread de atendimento criada.")

    def run(self):
        # O método que executa em paralelo
        with self._conexao:
            try:
                # Envia a tarefa para o cliente
                self._conexao.sendall(str(self._pontosParaSimular).encode('utf-8'))
                
                # Recebe o resultado do cliente
                resultadoBytes = self._conexao.recv(1024)
                pontosNoCirculo = int(resultadoBytes.decode('utf-8'))
                
                # Usa um "lock" para adicionar o resultado à lista de forma segura
                with self._lock:
                    self._resultadosParciais.append(pontosNoCirculo)

            except Exception as e:
                print(f"Erro com o cliente {self._endereco}: {e}")
        
        print(f"Comunicação com {self._endereco} finalizada.")