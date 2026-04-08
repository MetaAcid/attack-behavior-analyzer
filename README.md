# Attack Behavior Analyzer

Python-проект для выявления аномального поведения в сетевой активности с использованием методов машинного обучения.

---

## Описание

Проект моделирует задачу поведенческого анализа в cybersecurity:
- анализ сетевой активности
- выявление подозрительных IP
- поиск аномалий в паттернах поведения
- формирование структурированного отчёта

В основе используется `Isolation Forest` для anomaly detection.

---

## Функциональность

Система:
- загружает данные из CSV
- подготавливает признаки для анализа
- обучает модель `IsolationForest`
- выявляет аномальные записи
- присваивает уровень риска
- объясняет, почему поведение отмечено как подозрительное
- сохраняет результат в JSON

---

## Запуск

### Установка зависимостей
pip install -r requirements.txt

### Стандартный запуск
python src/main.py

### Запуск с указанием файла данных
python src/main.py --data data/sample_logs.csv --output output/anomalies.json

---

## Используемые признаки

Модель анализирует:

- requests — количество запросов
- failed_logins — количество неудачных попыток входа
- unique_paths — количество уникальных путей
- time_between_requests — интервал между запросами

---

## Используемая модель

Isolation Forest применяется для поиска аномалий без необходимости размеченного датасета.

Это позволяет моделировать задачи:

- threat detection
- behavioral analysis
- suspicious activity identification

---

## Выходные данные

### Результат сохраняется в:
output/anomalies.json

### Пример структуры:
```text
{
  "dataset": "data/sample_logs.csv",
  "summary": {
    "total_anomalies": 1,
    "high": 1,
    "medium": 0,
    "low": 0
  },
  "anomalies": [
    {
      "ip": "192.168.1.14",
      "requests": 300,
      "failed_logins": 50,
      "unique_paths": 80,
      "time_between_requests": 0.05,
      "risk_level": "HIGH",
      "description": "Suspicious behavior detected: high request volume, multiple failed login attempts, unusually broad path access, very short interval between requests"
    }
  ]
}
```
---

## Ограничения
- используется синтетический датасет
- модель не обучается на реальных production-логах
- проект не заменяет полноценные SIEM/UEBA решения

---

## Возможные улучшения

- визуализация результатов
- потоковая обработка событий
- расширенный feature engineering
- explainable ML
- интеграция с логами из SOC pipeline


---

## Архитектура

```text
attack-behavior-analyzer/
├── src/
│   ├── main.py
│   ├── data_loader.py
│   ├── feature_engineering.py
│   ├── model.py
│   ├── detector.py
│   └── reporter.py
├── data/
│   └── sample_logs.csv
├── output/
│   └── anomalies.json
├── requirements.txt
└── README.md