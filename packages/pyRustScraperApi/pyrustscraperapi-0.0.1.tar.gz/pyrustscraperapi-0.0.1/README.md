# RustScraper API

## О проекте

RustScraper API - это мощный инструмент для парсинга данных о товарах с популярных маркетплейсов. API написано на языке Rust, что обеспечивает высокую производительность и надежность работы.

Проект разрабатывается и поддерживается одним человеком. По вопросам использования или приобретения доступа обращайтесь в Telegram: [@Nikita5612](https://t.me/Nikita5612).

Доступ к сервису предоставляется на платной основе. Подробности - в личных сообщениях.

## Основные возможности

- Поддержка крупнейших маркетплейсов:
  - Wildberries
  - Ozon
  - Яндекс.Маркет
  - МегаМаркет
- Гибкая система обхода блокировок через прокси-серверы
- Поддержка пользовательских cookies для сохранения настроек сессии
- WebSocket-подключение для отслеживания статуса парсинга в реальном времени
- Простой и понятный REST API интерфейс
- Детальная валидация входящих данных
- Система очередей для распределения нагрузки

## Начало работы

### 1. Установка

Установите библиотеку через pip:

```bash
pip install rustscraper-api
```

### 2. Получение тестового токена

Для начала работы получите тестовый токен через метод `/test-token`. Токен предоставляется для уникальных IP-адресов и действует ограниченное время.

Пример:

```python
from rustscraper_api import Client

client = Client()
test_token = client.get_test_token()
print(test_token)
```

### 3. Создание заказа

Заказ на парсинг состоит из трёх компонентов:
- **Список товаров** (products)
- **Пул прокси-серверов** (proxyPool)
- **Пользовательские cookies** (cookies)

#### Поддерживаемые форматы ссылок на товары

- Короткий формат: `маркет/id`
  - `wb/145700662` (Wildberries)
  - `oz/1736756863` (Ozon)
  - `ym/1732949807-100352880819` (Яндекс.Маркет)
  - `mm/100065768905` (МегаМаркет)
- Полный URL товара с маркетплейса.

Пример:

```python
from rustscraper_api.models import Order

order = Order(
    products=["wb/145700662", "oz/1736756863"],
    proxy_pool=["username:password@proxyhost:port"],
    cookies=[{"name": "session", "value": "example_cookie_value"}]
)
```

### 4. Отправка заказа

```python
order_hash = client.send_order(order)
print(f"Заказ отправлен: {order_hash}")
```

### 5. Отслеживание выполнения заказа

Отслеживайте выполнение задачи через REST API или WebSocket:

#### REST API

```python
task = client.get_task(order_hash)
print(task)
```

#### WebSocket

```python
for update in client.stream_task(order_hash):
    print(update)
```

## Обработка ошибок

Каждая ошибка содержит:
- **Тип ошибки** (error)
- **Код ошибки** (code)
- **Сообщение** (message)

Пример обработки ошибок:

```python
try:
    order_hash = client.send_order(order)
except ApiError as e:
    print(f"Ошибка: {e.error}, Код: {e.code}, Сообщение: {e.message}")
```

## Примеры использования

### Получение информации о токене

```python
token_info = client.get_token_info()
print(token_info)
```

### Получение состояния API

```python
api_state = client.get_api_state()
print(api_state)
```

### Асинхронный клиент

Для использования асинхронного клиента:

```python
from rustscraper_api import AsyncClient

async with AsyncClient(token="your_token") as client:
    order_hash = await client.send_order(order)
    async for update in client.stream_task(order_hash):
        print(update)
```

## Ограничения

- Лимит на количество товаров в заказе
- Лимит на количество одновременных обработок
- Время жизни токена (TTL)
- Лимит на количество WebSocket подключений

## Контакты

Для получения доступа или вопросов об API обращайтесь в Telegram: [@Nikita5612](https://t.me/Nikita5612).

## Лицензия

Этот проект распространяется под [MIT License](LICENSE).
