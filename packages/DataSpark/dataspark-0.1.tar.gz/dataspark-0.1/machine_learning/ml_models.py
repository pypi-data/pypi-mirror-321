from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def simple_regression(df, target_column, feature_columns):
    """
    Perform simple linear regression on the given data.
    
    :param df: DataFrame
    :param target_column: Name of the column to predict
    :param feature_columns: List of feature column names
    :return: Trained model, predictions, and MSE
    """
    X = df[feature_columns]
    y = df[target_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    
    return model, predictions, mse