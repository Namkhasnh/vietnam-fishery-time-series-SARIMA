# ========================
# IMPORT LIBRARIES
# ========================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_absolute_percentage_error, mean_squared_error


# ========================
# LOAD DATA
# ========================
df = pd.read_excel("data.xlsx")
df = df.rename(columns={
    "Thời gian": "date",
    "Tổng Sản Lượng Thủy Sản": "value"
})

df["date"] = pd.to_datetime(df["date"])
df = df.set_index("date").asfreq("MS")


# ========================
# 1) TREND = MOVING AVERAGE 12 MONTHS
# ========================
df["trend_MA12"] = df["value"].rolling(window=12, center=True).mean()

plt.figure(figsize=(15,5))
plt.plot(df["value"], label="Original")
plt.plot(df["trend_MA12"], label="Trend (MA12)", linewidth=3)
plt.title("Trend bằng Trung Bình Trượt 12 Tháng")
plt.grid(True)
plt.legend()
plt.show()


# ========================
# 2) DETREND → CHU KỲ (SEASONALITY)
# ========================
df["detrended"] = df["value"] - df["trend_MA12"]

plt.figure(figsize=(15,5))
plt.plot(df["detrended"], color="orange")
plt.title("Chu kỳ sau khi khử trend")
plt.grid(True)
plt.show()


# ========================
# 3) ZOOM 3 NĂM BẤT KỲ
# ========================
def zoom_3years(df, start_year):
    start = f"{start_year}-01-01"
    end = f"{start_year+2}-12-01"
    zoom_df = df.loc[start:end]

    plt.figure(figsize=(16,5))
    plt.plot(zoom_df.index, zoom_df["value"], marker="o")
    plt.title(f"Zoom dữ liệu {start_year}–{start_year+2}")
    plt.grid(True)
    plt.show()

# ví dụ zoom 2015–2017
zoom_3years(df, 2015)


# ========================
# 4) TRAIN–TEST SPLIT
# ========================
train = df.iloc[:-12]
test = df.iloc[-12:]


# ========================
# 5) TRAIN SARIMA
# ========================
model = SARIMAX(
    train["value"],
    order=(1,1,1),
    seasonal_order=(1,1,1,12),
    enforce_stationarity=False,
    enforce_invertibility=False
).fit()

sarima_pred = model.get_forecast(steps=12).predicted_mean


# ========================
# 6) EVALUATION
# ========================
rmse = np.sqrt(mean_squared_error(test["value"], sarima_pred))
mape = mean_absolute_percentage_error(test["value"], sarima_pred)

print("SARIMA RMSE:", rmse)
print("SARIMA MAPE:", mape)


# ========================
# 7) PLOT TEST vs FORECAST (ZOOM)
# ========================
plt.figure(figsize=(16,6))
plt.plot(test.index, test["value"], label="Test (Actual)", linewidth=4)
plt.plot(sarima_pred.index, sarima_pred, label="Forecast (SARIMA)", linewidth=4)
plt.title("Test vs Forecast (SARIMA)", fontsize=20)
plt.grid(True)
plt.legend(fontsize=14)
plt.show()

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# ========================
# ACF – PACF PLOT
# ========================
plt.figure(figsize=(16,5))
plot_acf(df["value"].dropna(), lags=40, ax=plt.gca())
plt.title("ACF – AutoCorrelation Function")
plt.grid(True)
plt.show()

plt.figure(figsize=(16,5))
plot_pacf(df["value"].dropna(), lags=40, ax=plt.gca(), method='ywm')
plt.title("PACF – Partial AutoCorrelation Function")
plt.grid(True)
plt.show()