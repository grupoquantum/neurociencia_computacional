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