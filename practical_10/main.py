from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/armstrong/<int:n>")
def get_armstrong(n):
    copy_n = n
    sum = 0
    digits = len(str(copy_n))

    while(n > 0):
        last_d = n % 10
        n = n//10
        sum += last_d**digits

    if(sum == copy_n):
        result = {
            "number": copy_n,
            "is_armstrong": True
        }
    else:
        result = {
            "number": copy_n,
            "is_armstrong": False
        }
    
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)


