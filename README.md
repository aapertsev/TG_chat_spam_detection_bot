# 🚀 Telegram Chat Spam Detection Bot

Этот проект представляет собой **Telegram-бота**, который анализирует сообщения в чате и определяет, являются ли они **спамом**. Для классификации используется модель **CatBoost**, обученная на датасете спам-сообщений. Бот автоматически удаляет спам и предупреждает участников.

---

## 📌 Функциональность
✅ Проверяет все сообщения в чате на наличие спама  
✅ Использует **ML-модель (CatBoost)** для классификации сообщений  
✅ Удаляет спам или отправляет предупреждение  

---

## 🚀 Развертывание проекта

### **1️⃣ Установка зависимостей**
Убедитесь, что у вас установлен **Python 3.8+** и **Git**.

Клонируйте репозиторий:
```bash
git clone https://github.com/aapertsev/TG_chat_spam_detection_bot.git
cd TG_chat_spam_detection_bot
```
Создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # Для macOS/Linux
venv\Scripts\activate  # Для Windows
```
Установите библиотеки:
```bash
pip install -r requirements.txt
```
### **2️⃣ Настройка переменных окружения**
Создайте .env файл и укажите Telegram-токен и API-URL:
```bash
echo "TELEGRAM_BOT_TOKEN=your_secret_token" > .env
echo "SPAM_API_URL=http://localhost:5000/predict" >> .env
```
ИЛИ создайте файл .env вручную:
```.env
TELEGRAM_BOT_TOKEN=your_secret_token
SPAM_API_URL=http://localhost:5000/predict
```
## **3️⃣ Запуск API**
```bash
python spam_api.py
```
По умолчанию API работает на http://localhost:5001.

Проверить работу API можно с помощью Postman или cURL
## **4️⃣ Запуск бота**
```bash
python spam_bot.py
```

## **📌 TODO (планируемые улучшения)**
✅ Подключить обучение модели на новых данных в реальном времени  
✅ Добавить поддержку голосовых сообщений (Whisper API)  
✅ Разработать веб-интерфейс для просмотра статистики спама  
✅ Оптимизировать API для быстрого анализа сообщений  

👨‍💻 Автор  
📌 Разработчик: Перцев Александр  
🔥 Если проект оказался полезным, поставьте ⭐ на GitHub! 🚀  
