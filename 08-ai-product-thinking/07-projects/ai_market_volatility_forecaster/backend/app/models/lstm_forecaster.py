import numpy as np
import torch
import torch.nn as nn
from sklearn.preprocessing import MinMaxScaler

class LSTMVolatilityForecaster(nn.Module):
    def __init__(self, input_size=1, hidden_size=64, num_layers=2):
        super().__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Sequential(nn.Linear(hidden_size, 32), nn.ReLU(), nn.Linear(32, 1))
    
    def forward(self, x):
        lstm_out, _ = self.lstm(x)
        return self.fc(lstm_out[:, -1, :])

def prepare_sequences(data, seq_length=60):
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(data.reshape(-1, 1))
    X, y = [], []
    for i in range(len(scaled) - seq_length):
        X.append(scaled[i:i+seq_length])
        y.append(scaled[i+seq_length])
    return np.array(X), np.array(y), scaler
