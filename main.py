# simple fastapi app

import uvicorn
import asyncio
from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def ping(request: Request):
        print("Hello")
        await asyncio.sleep(2) # added await and changed time to asyncio
        print("Goodbye")
        return { "PING": "PONG!" }



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, workers=5)
