from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/square/<int:n>")
def get_square(n):
    return jsonify({
        "number": n,
        "square_of_number": n ** 2
    })

if __name__ == "__main__":
    app.run(debug=True)