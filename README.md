# mlops-flight-delay
демо проект курса MLOps (7с)

## Структура проекта
bash

```
mlops-flight-delay/
│
├── data/                # Данные (версируются через DVC)
├── src/
│   ├── preprocess.py    # Очистка и подготовка данных
│   ├── train.py         # Обучение модели
│   ├── predict.py       # Скрипт для предсказаний
│   ├── api.py           # REST API (FastAPI)
│   └── utils.py
│
├── models/              # Сохраненные модели (MLflow)
├── airflow/             # DAG для пайплайнов
├── docker/              # Dockerfile
├── tests/               # pytest тесты
├── .github/workflows/   # CI/CD
└── README.md
```
