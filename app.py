from flask import Flask, request
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/buy')
def buy():
    srv_id = request.args.get('srv_id', '')
    role_id = request.args.get('role_id')
    name = request.args.get('name')
    productId = request.args.get('productId', '21')
    
    # Lấy thông số nhận diện Game từ Web (3: Hokage, 4: Học Viện, 5: Uchia)
    game_id = request.args.get('game', '5') 
    money = "1"
    
    # Dùng chung Session ID cố định
    cookie = "PHPSESSID=bskoh80nq21rlulqpakotjdaq6"
    
    # Phân luồng Server máy chủ
    if game_id == '5': # Uchia Truyền Kỳ (Có Port động)
        try:
            # Tách số ra từ chuỗi "symlf_X" (VD: "symlf_2" -> "2")
            server_num = int(srv_id.replace("symlf_", ""))
            port = 90 + server_num
        except:
            # Trừ hao nếu nhập linh tinh thì lấy Port 91 làm gốc
            port = 91
            
        base_url = f"http://103.149.252.111:{port}/api.php/pf/sygame/pay_web/" 
        
    elif game_id == '4': # Học Viện Shinobi (Port cố định 100 theo bạn gửi trước đó)
        base_url = "http://180.93.98.5:100/api.php/pf/sygame/pay_web/"
        
    elif game_id == '3': # Hokage Saga
        base_url = "http://160.30.113.78:1118/api.php/pf/sygame/pay_web/"
        
    else: 
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
