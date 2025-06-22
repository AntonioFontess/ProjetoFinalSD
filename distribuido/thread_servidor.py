import threading
import socket

class ThreadServidor(threading.Thread):

    def __init__(self, conexao, endereco, pontosParaSimular, resultadosParciais, lock): # Construtor da classe
        threading.Thread.__init__(self)
        self._conexao = conexao
        self._endereco = endereco
        self._pontosParaSimular = pontosParaSimular
        self._resultadosParciais = resultadosParciais
        self._lock = lock
        print(f"Cliente {self._endereco} conectado. Thread de atendimento criada.")

    def run(self): # Método executado em paralelo em cada "thread.start()"
        with self._conexao:
            try:
                self._conexao.sendall(str(self._pontosParaSimular).encode('utf-8')) # Envia a tarefa para o cliente/thread
                
                resultadoBytes = self._conexao.recv(1024)  # Recebe o resultado do cliente
                pontosNoCirculo = int(resultadoBytes.decode('utf-8')) # Decodifica o resultado de bytes para int

                with self._lock: # Usa um "lock" para adicionar o resultado à lista de forma segura
                    self._resultadosParciais.append(pontosNoCirculo)

            except Exception as e:
                print(f"Erro com o cliente {self._endereco}: {e}")
        
        print(f"Comunicação com {self._endereco} finalizada.")