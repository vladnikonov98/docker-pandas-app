import pandas as pd

# Загружаем данные из data.csv
data = pd.read_csv('data.csv')

# Вычисляем среднюю зарплату
average_salary = data['salary'].mean()
print(f"Средняя зарплата сотрудников: {average_salary:.2f}")

# Отбираем сотрудников старше 30 лет
employees_over_30 = data[data['age'] > 30]
print("\nСотрудники старше 30 лет:")
print(employees_over_30)