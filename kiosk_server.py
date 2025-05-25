
from flask import Flask, request, jsonify, send_file
import threading
import webbrowser
import os

app = Flask(__name__)

menu = [
    {"id": 1, "name": "아메리카노", "price": 3000},
    {"id": 2, "name": "카페라떼", "price": 3500},
    {"id": 3, "name": "카푸치노", "price": 4000}
]

orders = []

HTML_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "index.html"))

@app.route("/")
def serve_ui():
    return send_file(HTML_FILE)

@app.route("/menu", methods=["GET"])
def get_menu():
    return jsonify({"menu": menu})

@app.route("/order", methods=["POST"])
def order():
    data = request.get_json()
    items = data.get("items", [])
    total = sum(item["price"] for item in items)
    order_id = len(orders) + 1
    new_order = {
        "order_id": order_id,
        "items": items,
        "total": total,
        "status": "ordered"
    }
    orders.append(new_order)
    return jsonify({"message": "주문 완료", "order": new_order})

if __name__ == "__main__":
    threading.Timer(1.0, lambda: webbrowser.open("http://127.0.0.1:5000")).start()
    app.run(debug=True)
