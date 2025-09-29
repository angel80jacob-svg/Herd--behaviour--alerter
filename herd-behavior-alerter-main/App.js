import React, { useEffect, useState } from "react";

function App() {
  const [alerts, setAlerts] = useState([]);

  useEffect(() => {
    const ws = new WebSocket("ws://localhost:8000/ws/trending");
    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.alerts) {
        setAlerts(data.alerts);
      }
    };
    return () => ws.close();
  }, []);

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>🔥 Real-time Herd Behavior Alerter</h1>
      {alerts.length === 0 ? (
        <p>No trending products yet...</p>
      ) : (
        <ul>
          {alerts.map((a, i) => (
            <li key={i}>
              <strong>{a.product}</strong> → {a.count} events (z={a.zscore})
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default App;
