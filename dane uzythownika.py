import json
import string
import random
import time
from faker import Faker

start_time = time.time()
fake = Faker()
def generuj_losowy_ciag(dlugosc):
    znaki = string.ascii_letters + string.digits
    losowy_ciag = ''.join(random.choice(znaki) for _ in range(dlugosc))
    return losowy_ciag


dane_list = []

for i in range(100):
    data = {
        "First_name": fake.first_name(),
        "Last_name": fake.last_name(),
        "Username": fake.user_name(),
        "Email": fake.email(),
        "Password": fake.password()
    }
    dane_list.append(data)

# Ścieżka do pliku, w którym zapisane będą dane
file_path = 'Uzytkownicy.json'

# Zapisywanie danych do pliku
with open(file_path, 'w', encoding='utf-8') as json_file:
    json.dump(dane_list, json_file, ensure_ascii=False, indent=4)

print(f"Dane zostały zapisane do pliku {file_path}.")
end_time = time.time()
execution_time = end_time - start_time
print(execution_time)
