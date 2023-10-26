from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error

def preprocess(df):
    df.columns = ["sample_id", "ph", "temperature", "turbidity", "do", "conductivity"]
    df = df.drop(columns="sample_id")

    return df

def tt_splitter(df):
    y = df.do
    x = x = df.iloc[:,[0,1,2,4]]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)
    dictio = {
        "x_train": x_train,
        "x_test": x_test,
        "y_train": y_train,
        "y_test": y_test
    }

    return dictio

def rf_model(x_train, x_test, y_train, y_test):
    model = RandomForestRegressor(n_estimators=1000, random_state=42)
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    metrics = {
        "r2": r2_score(y_test, y_pred),
        "mae": mean_absolute_error(y_test, y_pred),
        "rmse": mean_squared_error(y_test, y_pred, squared = False)
    }

    return [model, metrics]