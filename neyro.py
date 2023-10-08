import sqlite3

con = sqlite3.connect('db_glagoli.db')
word = input('Введите слова для поиска через пробел: ').split()
cur = con.cursor()
sr_spec = [0, 0, 0, 0]
for i in range(len(word)):
  glag = word[i]
  query = f"SELECT * FROM glagolchiki WHERE  Glagol ='{glag}'"
  cur.execute(query)

  rows = cur.fetchall()
  for row in rows:
      print('Найденное слово: ', row)

  key = rows[0][0]
  query = f"SELECT * FROM Pokozateli WHERE  Id = {key}"
  cur.execute(query)
  specs = cur.fetchall()
  for spec in specs:
      print('Найденное слово: ', spec)


  for i in range(len(sr_spec)):
      sr_spec[i] += specs[0][i+1]

  print(sr_spec)

for i in range(4):
    sr_spec[i] = round(sr_spec[i] / len(word))
print(sr_spec)
con.close()


























# Входные данные - вакансии
#job = input() # Входные данные - вакансии
 # Вакансия 
# Входные данные - рабочие
  # Рабочий 
#workers = [int(input()) for i in range(4)] 
# Создаем модель нейронной сети vacancies = [input() for i in range(4)]
'''
mass = np.zeros((4, 4))
for i in range(4):
   for j in range(4):
        mass[i, j] = int.from_bytes(input().encode('utf-8'), 'little')
        
        #mass[i, j] = mass[i, j].astype(dtype=object)
        #print(mass[i, j].decode('utf8'))
print(mass)
'''
'''
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(5, input_shape=(5,)),
])

# Компилируем модель
model.compile(optimizer='adam', loss='mse')
  
# Обучаем модель
model.fit(workers, vacancies, epochs=10)

# Получаем тензор с предсказаниями
predictions = model.predict(workers)

# Выводим предсказания
for i, prediction in enumerate(predictions):
    print("Рабочий {}: {}".format(i+1, prediction))

import numpy as np

def sigmoid(x): return 1 / (1 + np.exp(-x))

class Network:
def init(self):
self.weights = None
self.biases = None

def train(self, inputs, targets, learning_rate=0.1):
n_samples = len(inputs)
for i in range(n_samples):
self.update_weights_and_biases(inputs[i], targets[i], learning_rate)

def update_weights_and_biases(self, input_vector, target_value, learning_rate):
input_layer_node_values = input_vector
output_layer_node_value = sigmoid(np.dot(input_layer_node_values, self.weights) + self.biases)
error = target_value - output_layer_node_value
delta_output_layer = error * output_layer_node_value * (1 - output_layer_node_value)
self.weights += np.
Продолжи
dot(delta_output_layer, input_layer_node_values.T)
self.biases += delta_output_layer

def predict(self, job_description):
return np.argmax(sigmoid(np.dot(job_description, self.weights) + self.biases))
Данные для обучения (список кортежей, где первый элемент - описание работы, а второй - требуемые характеристики)
training_data = [
(“Курьер”, [4, 7, 3, 2]),
(“Грузчик”, [5, 8, 4, 1]),
(“Продавец-консультант”, [6, 9, 5, 0])
]

Создаем нейросеть
network = Network()

Обучаем нейросеть на данных training_data
for _ in range(1000): # 1000 итераций обучения
random.shuffle(training_data) # Перемешиваем данные для каждой итерации обучения
for job_description, target_values in training_data:
network.train(job_description.
'''