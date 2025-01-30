from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Загружаем обученную CatBoost-модель
model = joblib.load("catboost_spam_model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json  # Получаем JSON-запрос
        if not data or "text" not in data:
            return jsonify({"error": "Не найден ключ 'text' в JSON"}), 400

        text = data["text"]
        
        # Проверяем входные данные
        if not isinstance(text, str) or len(text) == 0:
            return jsonify({"error": "Текст должен быть строкой и не пустым"}), 400

        # Делаем предсказание (убираем [0], если модель возвращает скаляр)
        prediction = model.predict([text])  # CatBoost иногда возвращает скаляр, а не массив
        probability = model.predict_proba([text])[0] # Получаем вероятность спама

        result = {
            "spam": bool(prediction),  # Преобразуем результат в bool
            "confidence": round(float(probability), 3)  # Преобразуем вероятность в число
        }

        return jsonify(result)

    except Exception as e:
        print(f"Ошибка обработки запроса: {e}")
        return jsonify({"error": "Внутренняя ошибка сервера"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
