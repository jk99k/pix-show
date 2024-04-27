from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import shutil
import os
from typing import List
from fastapi import Response
import sqlite3

# SQLiteデータベースのセットアップ
conn = sqlite3.connect('photos.db')
c = conn.cursor()

# テーブルの作成
c.execute('''CREATE TABLE IF NOT EXISTS photos
             (id INTEGER PRIMARY KEY AUTOINCREMENT, filename TEXT, upload_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')

# コミット
conn.commit()

app = FastAPI()

# アップロードされた写真を保存するディレクトリのパス
upload_dir = "./uploads"

# アップロードされた写真を保存する関数
def save_uploaded_file_and_record(upload_dir: str, upload_file: UploadFile):
    try:
        # ファイルを保存する
        with open(os.path.join(upload_dir, upload_file.filename), "wb") as buffer:
            shutil.copyfileobj(upload_file.file, buffer)
        # データベースに写真の情報を保存
        c.execute("INSERT INTO photos (filename) VALUES (?)", (upload_file.filename,))
        conn.commit()
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
        save_uploaded_file_and_record(upload_dir, file)
    return JSONResponse(status_code=201, content={"message": "Files uploaded successfully"})
 

# ディレクトリから写真ファイルを取得してクライアントに送信するエンドポイント
@app.get("/photos/")
async def get_photos():
    try:
        # ディレクトリが存在するか確認し、存在しない場合はエラーを返す
        if not os.path.exists(upload_dir):
            raise HTTPException(status_code=404, detail="Upload directory not found")

        # データベースから遅い写真の情報を取得
        c.execute("SELECT filename FROM photos ORDER BY upload_time LIMIT 100")
        photo_files = c.fetchall()

        # レスポンスに写真ファイルを書き込む
        responses = []
        for photo_file in photo_files:
            with open(os.path.join(upload_dir, photo_file[0]), "rb") as file:
                file_content = file.read()
                response = Response(content=file_content)
                response.headers["Content-Disposition"] = f"attachment; filename={photo_file[0]}"
                responses.append(response)

        return responses
      
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
    finally:
        conn.close()