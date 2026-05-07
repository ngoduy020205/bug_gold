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
    
    # Nhận ID gói từ Web truyền lên (nếu không có thì mặc định là 7)
    productId = request.args.get('productId', '7')
    money = "1"
    
    # Session ID cứng của bạn
    cookie = "PHPSESSID=bskoh80nq21rlulqpakotjdaq6"
    
    url = f"http://nhangiatruyenky.com:126/api.php/pf/sygame/pay_web/?srv_id={srv_id}&role_id={role_id}&money={money}&name={name}&productId={productId}"
    
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
