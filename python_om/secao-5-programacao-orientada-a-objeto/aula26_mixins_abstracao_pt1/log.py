# Abstração
# Herança - é um
# Log

# biblioteca para pegar o path do file
from pathlib import Path
LOG_FILE = Path(__file__).parent / 'log.txt' # pode colocar uma / para concatener seguido de uma str

class Log:

    # assinatura do método
    # esse método só existe para definir que existe esse metodo na classe Log
    # template method
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log')
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    
    def log_sucess(self, msg):
        return self._log(f'Sucess: {msg}')


    
# o desenvolvedor nao quer q vc use a classe super, ele quer q vc use 
# essa funcionalidade a geranca multipla

# para sobrepor um metodo, o metodo candidato a substituir precisa ter a 
# msm assinatura
'''
o que foi feito até agora? usei abstração para criar 3 metodos, o primeiro é restrito
q é log, segundo log_error e terceiro log_sucess. Nos metodos log_error e log_sucess, 
eu chamo o _log com uma msg, mas note que ao definir a classe LogPrintMixin, eu defino o
metodo _log, e ao chamar o log_error ou o log_sucess (por sua vez eles chamam o _log), 
elas vao usar o _log definido dentro da classe mais baixa e nao da classe super
'''
class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print('Salvando no log:', msg_formatada)
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')
        print(msg)
    
class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')

if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('qualquer coisa')
    lp.log_sucess('que legal')

    lf = LogFileMixin()
    lf.log_error('qualquer coisa')
    lf.log_sucess('que legal')

    print(LOG_FILE)
    print('##############')