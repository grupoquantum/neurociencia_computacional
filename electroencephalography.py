# acessando o neuraline para importar o módulo de neurociência computacional
from Neuraline.ComputationalNeuroscience.electroencephalography import Electroencephalography
electroencephalography = Electroencephalography(
	delta=[0, 3], # intervalo de frequência em Hertz para ondas do tipo Delta
	theta=[4, 7], # intervalo de frequência em Hertz para ondas do tipo Theta
	alpha=[8, 12], # intervalo de frequência em Hertz para ondas do tipo Alpha
	beta=[13, 30], # intervalo de frequência em Hertz para ondas do tipo Beta
	gamma=[30, 100] # intervalo de frequência em Hertz para ondas do tipo Gamma
) # instanciação da classe com uma variável objeto
# se o parâmetro signals não for definido serão calculados valores aleatórios de exemplo
signals = [x for x in range(101)] # simulando os sinais de uma eletroencefalografia
result = electroencephalography.plotBandSignals(
	signals=signals, # sinais de frequência captados por um eletroencefalograma
	sampling_rate_in_hertz=512, # taxa de amostragem em Hertz
	bar_values=False # exibição dos valores de frequência nas barras do gráfico
)
print(result) # exibição do resultado da execução, se estiver tudo correto retornará verdadeiro
	