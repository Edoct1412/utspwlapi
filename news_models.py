from db import get_db

def get_news():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT news_id, title, content, datetime FROM tbl_news_0441 WHERE flag = 1"
    cursor.execute(query)
    columns = [column[0] for column in cursor.description] 
    result = []
    
    for row in cursor.fetchall():
        result.append(dict(zip(columns, row)))
        
    return result
    
def get_news_by_id(id):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT news_id, title, content, datetime FROM tbl_news_0441 WHERE news_id = ? AND flag = 1"
    cursor.execute(query, [id])
    columns = [column[0] for column in cursor.description]
    result = []
    result.append(dict(zip(columns, cursor.fetchone())))
        
    return result

def insert_news(title, content, datetime, flag):
    db = get_db()
    cursor = db.cursor()
    query = "INSERT INTO tbl_news_0441(title, content, datetime, flag) VALUES (?,?,?,?)"
    cursor.execute(query, [title, content, datetime, flag])
    db.commit()
    return True

def update_news(id, title, content, datetime, flag):
    db = get_db()
    cursor = db.cursor()
    query = "UPDATE tbl_news_0441 SET title = ?, content = ?, datetime = ?, flag = ? WHERE news_id = ?"
    cursor.execute(query, [title, content, datetime, flag, id])
    db.commit()
    return True

def patch_news(id, flag):
    db = get_db()
    cursor = db.cursor()
    query = "UPDATE tbl_news_0441 SET flag = ? WHERE news_id = ?"
    cursor.execute(query, [flag, id])
    db.commit()
    return True

def delete_news(id):
    db = get_db()
    cursor = db.cursor()
    query = "DELETE FROM tbl_news_0441 WHERE news_id = ?"
    cursor.execute(query, [id])
    db.commit()
    return True
