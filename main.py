from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello from FastAPI!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# 機械学習モデルのロードや推論はここに記述していきます
# from tensorflow.keras.models import load_model
# model = load_model("your_model.h5")

# @app.post("/predict")
# async def predict_data(data: YourInputModel):
#     # prediction_result = model.predict(data)
#     return {"prediction": "some_result"}