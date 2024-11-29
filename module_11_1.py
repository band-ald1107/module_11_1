import requests

response = requests.get('https://api.github.com/users/octocat')

if response.status_code == 200:
    data = response.json()
    print(f"Имя пользователя: {data['name']}")
    print(f"Логин: {data['login']}")
    print(f"Портфолио: {data['html_url']}")
else:
    print(f"Ошибка запроса: {response.status_code}")

import pandas as pd

data = pd.read_csv('data.csv')


print("Первые 5 строк данных:")
print(data.head())


average_age = data['Age'].mean()
average_salary = data['Salary'].mean()
city_counts = data['City'].value_counts()


print("\nСредний возраст:", average_age)
print("Средняя зарплата:", average_salary)
print("\nКоличество людей из каждого города:")
print(city_counts)

import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('data.csv')
names = data['Name']
salaries = data['Salary']
plt.figure(figsize=(10, 5))
plt.bar(names, salaries, color='skyblue')
plt.title('Зарплаты сотрудников')
plt.xlabel('Сотрудники')
plt.ylabel('Зарплата')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()