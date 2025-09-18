import pandas as pd
from pathlib import Path

RAW_DATA = Path("data/raw/flights_sample.csv")
PROCESSED_DATA = Path("data/processed/processed.csv")

def preprocess():
    df = pd.read_csv(RAW_DATA)
    
    # Простая очистка
    df = df.dropna(subset=["DepTime", "ArrDelay"])
    
    # Примеры новых признаков
    df["DepHour"] = df["DepTime"] // 100
    df["IsWeekend"] = df["DayOfWeek"].isin([6, 7]).astype(int)
    
    Path("data/processed").mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_DATA, index=False)
    print(f"✅ Saved processed data to {PROCESSED_DATA}")

if __name__ == "__main__":
    preprocess()
