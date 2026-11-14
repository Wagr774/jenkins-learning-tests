import requests

def test_get_posts_success():
    # Запрос к тестовому API
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    
    # Проверяем, что статус код 200
    assert response.status_code == 200
    
    # Проверяем, что данные пришли в нужном формате
    data = response.json()
    assert "title" in data
    assert data["id"] == 1

def test_get_posts_not_found():
    # Запрос к несуществующей записи (проверка ошибки)
    response = requests.get("https://jsonplaceholder.typicode.com/posts/9999")
    
    # В данном API 9999 вернет 404 или пустой объект, 
    # но для примера проверим, что данные не те, которые мы ждем
    assert response.status_code == 404
