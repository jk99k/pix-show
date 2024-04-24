from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import shutil
import os
from typing import List

app = FastAPI()

# アップロードされた写真を保存するディレクトリのパス
upload_dir = "./uploads"

# アップロードされた写真を保存する関数
def save_uploaded_file(upload_dir: str, upload_file: UploadFile):
    try:
        # ファイルを保存する
        with open(os.path.join(upload_dir, upload_file.filename), "wb") as buffer:
            shutil.copyfileobj(upload_file.file, buffer)
    finally:
        # ファイルを閉じる
        upload_file.file.close()

# 複数のファイルを受け取るエンドポイント
@app.post("/upload/")
async def upload_files(files: List[UploadFile] = File(...)):
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    
    # アップロードする写真の数が5枚を超える場合はエラーを返す
    max_files = 5
    if len(files) > max_files:
        raise HTTPException(status_code=400, detail="Max files limit exceeded. Max 5 files allowed.")

    for file in files:
        save_uploaded_file(upload_dir, file)
    return JSONResponse(status_code=201, content={"message": "Files uploaded successfully"})
    