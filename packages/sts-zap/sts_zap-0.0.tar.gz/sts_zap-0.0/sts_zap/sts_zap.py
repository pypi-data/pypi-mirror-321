def imports():
    """pip install mistralai==0.4.2"""

def zap(query: str):
    import os
    from mistralai.client import MistralClient
    api_key = os.environ.get("MISTRAL_API_KEY", "gimxwZGsv6ajWICNXoHEQ7CXZJzygWtx")
    model = "mistral-medium"  # Используйте правильное название модели от Mistral AI
    # Инициализация клиента Mistral AI
    client = MistralClient(api_key=api_key)
    # Отправка запроса к модели
    response = client.chat(
        model=model,
        messages=[
            {
                "role": "user",  # Роль пользователя
                "content": query,
                # Сообщение пользователя
            },
        ]
    )
    # Вывод ответа модели
    print(response.choices[0].message.content)
