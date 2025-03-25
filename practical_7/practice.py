import redis
import json
from flask import Flask, jsonify

r = redis.Redis( host="localhost", port=6379, db=0, decode_responses=True)

products_data = {
    "1": {
        "product_name": "fruity",
        "is_healthy": False
    },
    "2": {
        "product_name": "Granola bars",
        "is_healthy": True
    },
    "3": {
        "product_name": "Nuts and seeds",
        "is_healthy": True
    },
}

app = Flask(__name__)

for product_id, product_info in products_data.items():
    r.set(product_id, json.dumps(product_info))

@app.route("/get/<productId>")
def get_product_by_id(productId):
    value = r.get(product_id)
    if(value):
        return jsonify({
            "key": productId,
            "value": json.loads(value)
        })
    else:
        return jsonify({
            "key": productId,
            "value": "Value is not set for respective key"
        })

if __name__ == "__main__":
    app.run(debug=True)

