import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Application configuration."""
    
    # API
    FLASK_HOST = os.getenv("FLASK_HOST", "0.0.0.0")
    FLASK_PORT = int(os.getenv("FLASK_PORT", 5000))
    DEBUG = os.getenv("DEBUG", "True") == "True"
    
    # Data
    DEFAULT_DAYS = int(os.getenv("DEFAULT_DAYS", 365))
    DEFAULT_HORIZON = int(os.getenv("DEFAULT_HORIZON", 5))
    AVAILABLE_STOCKS = os.getenv("AVAILABLE_STOCKS", "AAPL,MSFT,GOOGL,TSLA,SPY,AMZN,NVDA,META").split(",")
    
    # ML
    SEQ_LENGTH = int(os.getenv("SEQ_LENGTH", 60))
    LSTM_INPUT_SIZE = int(os.getenv("LSTM_INPUT_SIZE", 1))
    LSTM_HIDDEN_SIZE = int(os.getenv("LSTM_HIDDEN_SIZE", 64))
    LSTM_NUM_LAYERS = int(os.getenv("LSTM_NUM_LAYERS", 2))
    EPOCHS = int(os.getenv("EPOCHS", 100))
    BATCH_SIZE = int(os.getenv("BATCH_SIZE", 32))
    LEARNING_RATE = float(os.getenv("LEARNING_RATE", 0.001))
    DROPOUT = float(os.getenv("DROPOUT", 0.2))
    
    # Paths
    MODEL_PATH = os.getenv("MODEL_PATH", "models/lstm_volatility.pth")
    DATA_PATH = os.getenv("DATA_PATH", "data/")
    
    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
