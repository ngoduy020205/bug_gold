from flask import Flask, request
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/buy')
def buy():
    srv_id = request.args.get('srv_id')
    role_id = request.args.get('role_id')
    name = request.args.get('name')
    productId = request.args.get('productId', '7')
    
    # Lấy thông số nhận diện Game từ Web (3: Hokage, 4: Mythic)
    game_id = request.args.get('game', '3') 
    money = "1"
    
    # Dùng chung Session ID
    cookie = "PHPSESSID=bskoh80nq21rlulqpakotjdaq6"
    
    # Phân luồng Server
    if game_id == '4': # Mythic Shinobi
        base_url = "http://103.116.38.87:91/api.php/pf/sygame/pay_web/"
    elif game_id == '3': # Hokage Saga
        base_url = "http://160.30.113.78:1118/api.php/pf/sygame/pay_web/"
    elif game_id == '2': # Shinobi Classic (Cũ - Giữ lại phòng hờ)
        base_url = "http://160.30.112.91:96/api.php/pf/sygame/pay_web/"
    else: # Nhẫn Giả (Cũ - Giữ lại phòng hờ)
        base_url = "http://nhangiatruyenky.com:126/api.php/pf/sygame/pay_web/"
        
    url = f"{base_url}?srv_id={srv_id}&role_id={role_id}&money={money}&name={name}&productId={productId}"
    
    headers = {
        "Cookie": cookie,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    try:
        res = requests.get(url, headers=headers, timeout=10)
        return res.text
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
