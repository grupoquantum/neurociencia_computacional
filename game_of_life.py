# acessando o neuraline para importar o módulo de neurociência computacional
from Neuraline.ComputationalNeuroscience.game_of_life import GameOfLife
game_of_life = GameOfLife() # instanciação da classe com uma variável objeto
result = game_of_life.run( # chamada do método de execução
	frame_proportion=50, # proporção do quadro, 50x50 quadrantes
	interval_in_milliseconds=100, # 100 milissegundos entre uma atualização e outra
	singulair_interaction=False, # interação com somente um único grupo de quadrantes desabilitada
	dual_interaction=False # interação entre somente dois grupos de quadrantes desabilitada
)
print(result) # exibição do resultado da execução, se estiver tudo correto retornará verdadeiro