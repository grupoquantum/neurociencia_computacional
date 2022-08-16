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