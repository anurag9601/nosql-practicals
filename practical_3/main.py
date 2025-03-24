import redis 
from flask import Flask, jsonify

#Initializing and connecting a redis
r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

app = Flask(__name__)

@app.route("/set/string/<key>/<value>")
def redis_set_value(key, value):
    try:
        r.set(key, value)
        response = {
            "success": True,
            "key": key,
            "value": value
        }
        return jsonify(response)
    except:
        return jsonify({
            "error": "something went wrong"
        })

@app.route("/get/string/<key>")
def redis_get_value(key):
    try:
        value = r.get(key)
        response = {
            "success": True,
            "key": key,
            "value": value
        }
        return jsonify(response)
    except:
        return jsonify({
            "error": "something went wrong"
        })
    
@app.route("/del/string/<key>")
def redis_del_value(key):
    try:
        value = r.delete(key)
        response = {
            "success": True,
            "key": key,
            "deleted_value": value
        }
        return jsonify(response)
    except:
        return jsonify({
            "error": "something went wrong"
        })
    
if __name__ == "__main__":
    app.run(debug=True)

