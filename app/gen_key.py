import secrets

# Генериране на 32-байтов API ключ
api_key = secrets.token_hex(16)  # Генерира 32-символен ключ
print("API Key:", api_key)
with open('api_key.txt', 'w') as file:
    file.write(api_key)
