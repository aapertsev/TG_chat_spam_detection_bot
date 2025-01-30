import pandas as pd
import joblib
from catboost import CatBoostClassifier
from sklearn.model_selection import train_test_split

# Загрузка датасета
splits = {'train': 'data/train-00000-of-00001-daf190ce720b3dbb.parquet', 'test': 'data/test-00000-of-00001-fa9b3e8ade89a333.parquet'}
df_train = pd.read_parquet("hf://datasets/Deysi/spam-detection-dataset/" + splits["train"])
df_test = pd.read_parquet("hf://datasets/Deysi/spam-detection-dataset/" + splits["test"])

# Разделение на данные и метки
X_train, X_test = df_train["text"], df_test["text"]
y_train, y_test = df_train["label"].apply(lambda x: 1 if x == "spam" else 0), df_test["label"].apply(lambda x: 1 if x == "spam" else 0)



print(X_train.shape, y_train.shape)
# Создаем модель CatBoost с поддержкой текстовых фичей
model = CatBoostClassifier(
    iterations=500,  # Количество итераций
    depth=6,  # Глубина дерева
    learning_rate=0.1,  # Скорость обучения
    loss_function="Logloss",  # Функция потерь (бинарная классификация)
    eval_metric="Accuracy",  # Метрика качества
    verbose=50,  # Вывод промежуточных результатов
    text_features=[0]  # Первая колонка - текст
)

# Обучаем модель
model.fit(X_train, y_train, eval_set=(X_test, y_test))

# Сохранение модели
joblib.dump(model, "catboost_spam_model.pkl")

print("✅ CatBoost-модель успешно обучена и сохранена!")
