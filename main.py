from fastapi import FastAPI

app=FastAPI()

#デコレータ
#ルーティング
#("/")はパスオペレーション

#各HTTPメソッドをオペレーションと呼ぶ。
#asyncは非同期処理

@app.get("/hello")
async def index():
    return {"message":"hello"}

#クエリー
@app.get("/")
async def hello(name:str="json"):
    return {"message":f"{name},Hello"}

#パスパラメーターを取ってくる例
@app.get("/countries/{country_name}")
async def country(country_name:str):
    return {"country_name":country_name}

