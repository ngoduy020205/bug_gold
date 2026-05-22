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
    
    # Lấy thông số nhận diện Game từ Web gửi lên
    game_id = request.args.get('game', '1') 
    money = "1"
    
    # Dùng chung Session ID
    cookie = "PHPSESSID=bskoh80nq21rlulqpakotjdaq6"
    
    # Phân luồng Server
    if game_id == '2':
        # API của Shinobi Classic
        base_url = "http://160.30.112.91:96/api.php/pf/sygame/pay_web/"
    else:
        # API của Nhẫn Giả Truyền Kỳ
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
