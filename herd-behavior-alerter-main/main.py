from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import asyncio
import random, pandas as pd

app = FastAPI()

# Allow frontend React to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Products
products = ["Shoes","T-shirt","Laptop","Headphones","Backpack","Watch","Mobile","Book"]
window_size = 30
z_threshold = 2.0
event_log = []

def detect_trending(df):
    counts = df['product'].value_counts()
    if counts.empty: return []
    mean, std = counts.mean(), counts.std() if counts.std()>0 else 1
    trending = []
    for p,c in counts.items():
        z = (c-mean)/std
        if z > z_threshold:
            trending.append({"product":p,"count":int(c),"zscore":round(float(z),2)})
    return trending

async def generate_event():
    return {
        "product": random.choice(products),
        "event": random.choice(["view_product","add_to_cart"]),
        "timestamp": str(pd.Timestamp.now())
    }

@app.websocket("/ws/trending")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    global event_log
    while True:
        event = await generate_event()
        event_log.append(event)
        df = pd.DataFrame(event_log[-window_size:])
        trending = detect_trending(df)
        if trending:
            await ws.send_json({"alerts": trending})
        await asyncio.sleep(1)
