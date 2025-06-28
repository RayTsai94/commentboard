README FILE 112403014 蔡睿中
# Django Comment Board 後端啟動說明

## 環境需求
- Python 3.8 以上

## 安裝步驟

1. **安裝相依套件**

請安裝 Django：
```
pip install django
```

2. **資料庫遷移**

初始化資料庫（建立留言表格）：
```
python manage.py makemigrations
python manage.py migrate
```

3. **啟動伺服器**

執行：
```
python manage.py runserver
```

4. **開啟前端頁面**

在瀏覽器輸入：
```
http://127.0.0.1:8000/
```
即可看到留言板頁面，並可正常與 Django 後端互動。
 

## 其他說明

- 若要進入 Django 管理後台，可先建立管理員帳號：
```
python manage.py createsuperuser
```
然後到 `http://127.0.0.1:8000/admin/` 登入。
- 所有留言資料都會存進 SQLite 資料庫
 
- API 路徑：
- 取得留言：`127.0.0.1 /api/comments/`
- 新增留言：`127.0.0.1 /api/comments/post/`

API可以在postman進行測試

**Method**：選擇 `POST`
**URL**：輸入  
   ```
   127.0.0.1:8000/api/comments/post/
   ```
**Headers**：新增  
   ```
   Content-Type: application/json
   ```
**Body**：選擇 `raw`，格式選 `JSON`，填入範例資料：

```json
{
    "name": "測試使用者",
    "comment": "這是一則測試留言"
}
```

按下「Send」即可測試set API
 
**Method**：選擇 `GET`
**URL**：輸入  
   ```
   http://127.0.0.1:8000/api/comments/
   ```
按下「Send」即可測試get API


 
