import os
import shutil

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# アップロードされた写真を保存するディレクトリのパス
upload_dir = "./uploads"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 静的ファイルへのパスにアクセスすることで画像を閲覧することができるように
app.mount("/uploads", StaticFiles(directory=upload_dir), name="uploads")

# アップロードされた写真を保存する関数
def save_uploaded_file(upload_dir: str, upload_file: UploadFile) -> None:
    try:
        # ファイルを保存する
        if upload_file.filename is not None:
            with open(os.path.join(upload_dir, upload_file.filename), "wb") as buffer:
                shutil.copyfileobj(fsrc=upload_file.file, fdst=buffer)
    finally:
        # ファイルを閉じる
        upload_file.file.close()

# 複数のファイルを受け取るエンドポイント
@app.post(path="/")       
async def upload_files(files: list[UploadFile] = File(default=...)) -> JSONResponse:
    if not os.path.exists(path=upload_dir):
        os.makedirs(name=upload_dir)
    
    # アップロードする写真の数が5枚を超える場合はエラーを返す
    max_files = 5
    if len(files) > max_files:
        raise HTTPException(status_code=400, detail="Max files limit exceeded. Max 5 files allowed.")

    for file in files:
        save_uploaded_file(upload_dir=upload_dir, upload_file=file)
    return JSONResponse(status_code=201, content={"message": "Files uploaded successfully"})
    
    
# ファイルへのパスを配信するエンドポイント
@app.get(path="/")
def get_file_path() -> JSONResponse:
    if not os.path.exists(path=upload_dir):
        raise HTTPException(status_code=404, detail="No files uploaded yet.")
    
    # アップロードされた写真のパスを取得する
    files: list[str] = os.listdir(path=upload_dir)
    return JSONResponse(status_code=200, content={"files": files})