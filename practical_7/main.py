import redis
from flask import Flask , jsonify
import json

app = Flask(__name__)

r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

products = {
    1: {
        "product_name": "fruity",
        "is_healthy": False
    },
    2: {
        "product_name": "Granola bars",
        "is_healthy": True
    },
    3: {
        "product_name": "Nuts and seeds",
        "is_healthy": True
    },
}

for product_id, product_obj in products.items():
    r.set(str(product_id), json.dumps(product_obj))

@app.route("/get/<key>")
def get_value_by_key(key):
    value = r.get(key)

    try:
        result = {
            "key": key,
            "value": json.loads(value)
        }
    except:
        result = {
            "key": key,
            "value": "value is not present in the DB for respective key"
        }
    
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)