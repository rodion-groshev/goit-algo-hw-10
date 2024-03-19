import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize Profit", pulp.LpMaximize)

# Визначення змінних
A = pulp.LpVariable('A', lowBound=0, cat='Integer')  # Кількість лимонаду
B = pulp.LpVariable('B', lowBound=0, cat='Integer')  # Кількість фруктового соку

# Функція цілі (Максимізація прибутку)
model += A + B, "Profit"

# Додавання обмежень
model += 2 * A + 1 * B <= 100  # Обмеження води
model += 1 * A <= 50  # Обмеження цукру
model += 1 * A <= 30  # Обмеження соку
model += 2 * B <= 40  # Обмеження пюре

# Розв'язання моделі
model.solve()

# Вивід результатів
print("Виробляти продуктів А:", A.varValue)
print("Виробляти продуктів Б:", B.varValue)
