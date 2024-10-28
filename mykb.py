import pandas as pd

# Створюємо базу знань у вигляді множини триплетів для методів регресії
KB = {
    ("Multiple Linear Regression", "перевага", "High accuracy in linear relationships"),
    ("Multiple Linear Regression", "перевага", "Suitable for small datasets"),
    ("Multiple Linear Regression", "перевага", "Robust to outliers"),
    ("Multiple Linear Regression", "недолік", "Sensitive to multicollinearity"),
    ("Multiple Linear Regression", "недолік", "Requires large sample size"),
    ("Weighted Linear Regression", "перевага", "Suitable for small datasets"),
    ("Weighted Linear Regression", "перевага", "Robust to outliers"),
    ("Weighted Linear Regression", "перевага", "Handles multicollinearity well"),
    ("Weighted Linear Regression", "недолік", "Requires large sample size"),
    ("Weighted Linear Regression", "недолік", "Assumes linearity"),
    ("LAD Linear Regression", "перевага", "Robust to outliers"),
    ("LAD Linear Regression", "перевага", "Handles multicollinearity well"),
    ("LAD Linear Regression", "перевага", "Interpretable coefficients"),
    ("LAD Linear Regression", "недолік", "Assumes linearity"),
    ("LAD Linear Regression", "недолік", "Complex interpretation"),
    
}

# Створюємо DataFrame і заповнюємо його з множини KB
df = pd.DataFrame(columns=["s", "p", "o"])
for i, (s, p, o) in enumerate(KB):
    df.loc[i] = {"s": s, "p": p, "o": o}

# Зберігаємо DataFrame у CSV-файл
csv_file_path = "/mnt/data/regression_methods_kb.csv"
df.to_csv(csv_file_path, index=False)

csv_file_path