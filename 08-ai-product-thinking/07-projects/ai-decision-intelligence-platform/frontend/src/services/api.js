import axios from "axios";

const API_BASE = "http://localhost:8000";

export const analyzeQuery = async (query) => {

  const response = await axios.post(
    `${API_BASE}/analyze`,
    { query }
  );

  return response.data;
};

export const createWebSocket = (onMessage) => {

  const ws = new WebSocket(
    "ws://localhost:8000/ws"
  );

  ws.onmessage = (event) => {

    const data = JSON.parse(event.data);

    onMessage(data);
  };

  return ws;
};
