<p align="justify">
Nossa mente e consciência são o resultado da correlação de variáveis armazenadas analogicamente no nosso cérebro através da estrutura morfológica dos neurônios. Cada neurônio utiliza uma combinação única entre o número de terminais de entrada e saída que representam cada um dos segmentos de memória da mente.
Tudo o que somos, vimemos, sentimos e pensamos está salvo nos padrões que essas correlações neurocelulares estabelecem entre elas. Mas como surgem essas correlações? Foi em 1970 que o matemático e pesquisador neurocientífico John Horton Conway provou matematicamente que os padrões encontrados na mente de seres vivos, na natureza e em todo o universo não necessitam de um arquiteto para surgirem. Através de interações completamente randômicas é possível o surgimento de regras simples que com o passar do tempo vão se tornando cada vez mais complexas a medida que o número de interações aumenta fazendo com que novas correlações possam emergir de maneira cada vez mais lógica e menos aleatória.
Conway batizou esse algoritmo matemático de Game of Life (Jogo da Vida), que desde então passou a ser aplicado em diversos ramos de estudo desde a Física até a Biologia, Genética, Economia, Geologia e Medicina. O algoritmo atualmente é estudado principalmente através de simulações computacionais e é capaz de prever fenômenos físico-biológicos de características estocásticas com um grau de precisão relativamente aceitável se levarmos em consideração que esses fenômenos não poderiam ser previstos antes deste método.
A simulação consiste em um conjunto de retângulos dispostos em uma área delimitada que se movem de forma desordenada e à medida que tocam uns nos outros são geradas interferências que se propagam para os quadrantes ao redor. Depois de alguns minutos começam a surgir os primeiros padrões e em poucas horas passam a surgir correlações que vão se tornando cada vez mais lógicas.
<pre>
	<code>
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
	</code>
</pre>
<img src="https://github.com/aiquantumneuro/neurociencia_computacional/blob/main/game_of_life.png">
</p>
<p align="justify">
Na primeira linha do código estamos importando da biblioteca Neuraline do módulo de Neurociência Computacional e de dentro do módulo estamos acessando o arquivo do Game of Life.
Na segunda linha estamos usando uma variável de nome game_of_life para instanciar a classe GameOfLife que foi importada do arquivo.
Na terceira linha estamos usando a variável result para armazenar o resultado da execução do método run.
O método run possui a parâmetro frame_proportion que controla as dimensões para os eixos X e Y da área delimitadora por onde os quadrantes irão se movimentar, o parâmetro interval_in_milliseconds referente a taxa de atualização entre um frame e outro em milissegundos, o parâmetro singulair_interaction que se for habilitado como True irá manter as interações em um único grupo de quadrantes e o parâmetro dual_interaction que mantêm a interação em dois grupos de quadrantes se definido como True.
Na última linha exibimos o resultado da execução que será True se as configurações estiverem corretas ou False se estiverem erradas.
</p>
<p align="justify">
O monitoramento dos sinais cerebrais através de um eletroencefalograma poderá ser facilmente interpretado com os recursos da classe de eletroencefalografia. A proporção entre os tipos de ondas captadas poderá ser utilizada para traçar diagnósticos ou para acionar comandos em periféricos através da mente.
<pre>
	<code>
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
	</code>
</pre>
<img src="https://github.com/aiquantumneuro/neurociencia_computacional/blob/main/electroencephalography.png">
</p>
<p align="justify">
<pre>
	<code>
# acessando o neuraline para importar o módulo de neurociência computacional
from Neuraline.ComputationalNeuroscience.electroencephalography import Electroencephalography
electroencephalography = Electroencephalography(
	delta=[0, 3], # intervalo de frequência em Hertz para ondas do tipo Delta
	theta=[4, 7], # intervalo de frequência em Hertz para ondas do tipo Theta
	alpha=[8, 12], # intervalo de frequência em Hertz para ondas do tipo Alpha
	beta=[13, 30], # intervalo de frequência em Hertz para ondas do tipo Beta
	gamma=[30, 100] # intervalo de frequência em Hertz para ondas do tipo Gamma
) # instanciação da classe com uma variável objeto
# também é possível visualizar as proporções de ondas através de um arquivo de áudio WAV gerado por uma eletroencefalografia
# o arquivo de exemplo corresponde a uma captação real da atividade neural de uma pessoa acordada em repouso
result = electroencephalography.plotBandWAV(
	url_path='sound_of_neural_activity.wav', # arquivo de áudio captado por uma atividade cerebral real
	sampling_rate_in_hertz=512, # taxa de amostragem em Hertz
	bar_values=False # exibição dos valores de frequência nas barras do gráfico
)
print(result) # exibição do resultado da execução, se estiver tudo correto retornará verdadeiro
	</code>
</pre>
<img src="https://github.com/aiquantumneuro/neurociencia_computacional/blob/main/electroencephalography_wav.png">
<p align="justify">
Observe que existe uma maior incidência de sinais correspondentes à frequência Alpha que é gerada quando uma pessoa está acordada e descansando. As ondas Beta são geradas quando uma pessoa está acordada executando alguma atividade, ondas do tipo Theta correspondem a sonolência e as do tipo Delta ao sono profundo.
</p>
</p>
<p align="justify">
<div align="justify">
Para promover ações em dispositivos de hardware através da mente, basta ler os sinais do eletroencefalograma e atribuí-los ao treinamento de um algoritmo de Inteligência Artificial. O monitoramento é feito com o indivíduo executando uma tarefa particular enquanto o eletroencefalograma capta o comportamento da atividade cerebral. Cada tarefa executada é interrompida para o salvamento dos sinais de cada ação. Posteriormente o conjunto de sinais é passado como entrada para o treinamento do algoritmo com uma saída que represente cada ação executada. Com o treinamento encerrado basta monitorar a nova atividade cerebral com o indivíduo imaginando executar uma das tarefas e passar essa nova lista de sinais para a predição que retornará a ação correspondente.
</div>
<br>
<pre>
	<code>
'''
Podemos treinar um algoritmo de aprendizado de máquina com os padrões de sinais para cada ação desejada 
e posteriormente executar uma ação específica em algum dispositivo de hardware quando o indivíduo repetir 
um padrão de pensamento semelhante. Dessa forma é possível controlar um hardware qualquer apenas com o pensamento.
'''
'''
importação do algoritmo k_nearest_neighbors contido na sessão de Aprendizado Supervisionado 
do submódulo para Aprendizado de Máquina no módulo de Inteligência Artificial
'''
from Neuraline.ArtificialIntelligence.MachineLearning.SupervisedLearning.k_nearest_neighbors import KNearestNeighbors
k_nearest_neighbors = KNearestNeighbors() # criação do objeto com a instanciação da classe

'''
cada uma das listas foi alimentada com valores capturados de um eletroencefalograma enquanto 
o indivíduo executava tarefas específicas. As listas podem ser capturadas de forma direta através
de uma conexão com o hardware de eletroencefalografia ou por meio da leitura de um arquivo WAV
salvo pelo eletroencefalograma.
'''
''' listas numéricas com padrões de sinais fictícios (somente para exemplo) '''
signals1 = [2, 1, 4, 5, 3, 7, 9, 8, 5, 1] # sinais de pensamento enquanto teclava a letra A
signals2 = [5, 7, 1, 8, 2, 9, 3, 1, 4, 7] # sinais de pensamento enquanto teclava a letra B
signals3 = [5, 3, 9, 1, 7, 2, 4, 3, 9, 2] # sinais de pensamento enquanto teclava a letra C
''' lista com os valores de entrada para o treinamento '''
inputs = [signals1, signals2, signals3]
''' lista com os valores de saída para o treinamento '''
outputs = ['A', 'B', 'C']
''' treinamento do algoritmo K-Nearest Neighbors '''
k_nearest_neighbors.fit(inputs=inputs, outputs=outputs, k=0)
new_inputs = [5, 7, 1, 8, 2, 9, 3, 2, 4, 7] # novas entradas para o pensamento sem a ação
result = k_nearest_neighbors.predict(inputs=[new_inputs])[0] # predição do resultado
''' avaliação da tecla a ser acionada com o pensamento '''
if result == 'A':   print('rotina para a digitação da tecla A')
elif result == 'B': print('rotina para a digitação da tecla B')
elif result == 'C': print('rotina para a digitação da tecla C')
	</code>
</pre>
<div align="justify">
O mesmo pode ser feito com qualquer outro algoritmo de Inteligência Artificial devidamente configurado para o conjunto de dados como por exemplo o algoritmo de Máquina de Vetores de Suporte.
</div>
<br>
<pre>
	<code>
'''
importação do algoritmo support_vector_machine contido na sessão de Aprendizado Supervisionado 
do submódulo para Aprendizado de Máquina no módulo de Inteligência Artificial
'''
from Neuraline.ArtificialIntelligence.MachineLearning.SupervisedLearning.support_vector_machine import SupportVectorMachine
support_vector_machine = SupportVectorMachine() # criação do objeto com a instanciação da classe
'''
cada uma das listas foi alimentada com valores capturados de um eletroencefalograma enquanto
o indivíduo executava tarefas específicas. As listas podem ser capturadas de forma direta através
de uma conexão com o hardware de eletroencefalografia ou por meio da leitura de um arquivo WAV
salvo pelo eletroencefalograma.
'''
''' listas numéricas com padrões de sinais fictícios (somente para exemplo) '''
signals1 = [2, 1, 4, 5, 3, 7, 9, 8, 5, 1] # sinais de pensamento enquanto teclava a letra A
signals2 = [5, 7, 1, 8, 2, 9, 3, 1, 4, 7] # sinais de pensamento enquanto teclava a letra B
signals3 = [5, 3, 9, 1, 7, 2, 4, 3, 9, 2] # sinais de pensamento enquanto teclava a letra C
''' lista com os valores de entrada para o treinamento '''
inputs = [signals1, signals2, signals3]
''' lista com os valores de saída para o treinamento '''
outputs = ['A', 'B', 'C']
''' treinamento do algoritmo Support Vector Machine '''
support_vector_machine.fit(inputs=inputs, outputs=outputs, gamma=3)
new_inputs = [5, 7, 1, 8, 2, 9, 3, 2, 4, 7] # novas entradas para o pensamento sem a ação
result = support_vector_machine.predict(inputs=[new_inputs])[0] # predição do resultado
''' avaliação da tecla a ser acionada com o pensamento '''
if result == 'A':   print('rotina para a digitação da tecla A')
elif result == 'B': print('rotina para a digitação da tecla B')
elif result == 'C': print('rotina para a digitação da tecla C')	
	</code>
</pre>
<div align="justify">
Da mesma forma que os padrões puderam ser reconhecidos e aplicados com os algoritmos de Aprendizado de Máquina K-Nearest Neighbors e Support Vector Machine também é possível utilizar a mesma técnica com algoritmos baseados em Árvores de Decisão como por exemplo o Decision Tree.
</div>
<br>
<pre>
	<code>
'''
importação do algoritmo decision_tree contido na sessão de Aprendizado Supervisionado 
do submódulo para Aprendizado de Máquina no módulo de Inteligência Artificial
'''
from Neuraline.ArtificialIntelligence.MachineLearning.SupervisedLearning.decision_tree import DecisionTree
decision_tree = DecisionTree() # criação do objeto com a instanciação da classe
'''
cada uma das listas foi alimentada com valores capturados de um eletroencefalograma enquanto
o indivíduo executava tarefas específicas. As listas podem ser capturadas de forma direta através
de uma conexão com o hardware de eletroencefalografia ou por meio da leitura de um arquivo WAV
salvo pelo eletroencefalograma.
'''
''' listas numéricas com padrões de sinais fictícios (somente para exemplo) '''
signals1 = [2, 1, 4, 5, 3, 7, 9, 8, 5, 1] # sinais de pensamento enquanto teclava a letra A
signals2 = [5, 7, 1, 8, 2, 9, 3, 1, 4, 7] # sinais de pensamento enquanto teclava a letra B
signals3 = [5, 3, 9, 1, 7, 2, 4, 3, 9, 2] # sinais de pensamento enquanto teclava a letra C
''' lista com os valores de entrada para o treinamento '''
inputs = [signals1, signals2, signals3]
''' lista com os valores de saída para o treinamento '''
outputs = ['A', 'B', 'C']
''' treinamento do algoritmo Decision Tree '''
decision_tree.fit(inputs=inputs, outputs=outputs, extra_trees=False)
new_inputs = [5, 7, 1, 8, 2, 9, 3, 2, 4, 7] # novas entradas para o pensamento sem a ação
result = decision_tree.predict(inputs=[new_inputs])[0] # predição do resultado
''' avaliação da tecla a ser acionada com o pensamento '''
if result == 'A':   print('rotina para a digitação da tecla A')
elif result == 'B': print('rotina para a digitação da tecla B')
elif result == 'C': print('rotina para a digitação da tecla C')
	</code>
</pre>
<div align="justify">
Todos os algoritmos de Inteligência Artificial que sejam de Aprendizado Supervisionado poderão ser aplicados para reconhecer padrões desse tipo. Você deverá realizar testes com os algoritmos de sua preferência testando configurações diferentes nos parâmetros até encontrar o algoritmo que seja mais adequado para a sua situação.
</div>
</p>
