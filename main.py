from flask import Flask, request, jsonify
from flask_cors import CORS
import news_models

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
CORS(app)

@app.route('/api/v1/news', methods=['GET'])
def get_news():
    result = news_models.get_news()
    
    data = {
            
            'status': 200,
            'data': result
        
        }
    
    resp = jsonify(data)
    resp.status_code = 200
    
    return resp

@app.route('/api/v1/news/<int:id>', methods=['GET'])
def get_news_by_id(id):
    try:
        result = news_models.get_news_by_id(id)
        data = {
                
                'status': 200,
                'data': result
            
            }
        
        resp = jsonify(data)
        resp.status_code = 200
        
        return resp
    except:
        data = {
                
                'status': 404,
                'message': "Data Not Found"
            
            }
        
        resp = jsonify(data)
        resp.status_code = 404
        
        return resp

@app.route('/api/v1/news', methods=['POST'])
def insert_news():
    
    news_details = request.json
    title = news_details['title']
    content = news_details['content']
    datetime = news_details['datetime']
    flag = news_details['flag']
    result = news_models.insert_news(title, content, datetime, flag)
    
    data = {
        
            'status': 201,
            'message': 'Success!'
        
        }
    
    resp = jsonify(data)
    resp.status_code = 201
    
    return resp

@app.route('/api/v1/news/<int:id>', methods=['PUT'])
def update_students(id):
    
    news_details = request.json
    id = news_details['id']
    title = news_details['title']
    content = news_details['content']
    datetime = news_details['datetime']
    flag = news_details['flag']
    result = news_models.update_news(id, title, content, datetime, flag)
    
    data = {
        
            'status': 200,
            'message': 'Success!'
        
        }
    
    resp = jsonify(data)
    resp.status_code = 200
    
    return resp

@app.route('/api/v1/news/<int:id>', methods=['PATCH'])
def patch_students(id):
    
    news_details = request.json
    id = news_details['id']
    flag = news_details['flag']
    result = news_models.patch_news(id, flag)
    
    data = {
        
            'status': 200,
            'message': 'Success!'
        
        }
    
    resp = jsonify(data)
    resp.status_code = 200
    
    return resp

@app.route('/api/v1/news/<int:id>', methods=['DELETE'])
def delete_news(id):
    result = news_models.delete_news(id)
    
    data = {
            
            'status': 200,
            'message': "Success!"
        
        }
    
    resp = jsonify(data)
    resp.status_code = 200
    
    return resp

@app.errorhandler(404)
def not_found(error=None):
    message = {
        
            'status': 404,
            'message': 'Not Found: ' + request.url
        }
    
    resp = jsonify(message)
    resp.status_code = 404
    
    return resp


if __name__ == "__main__":
    app.run(debug=True)