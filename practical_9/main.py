from flask import Flask , jsonify

#Initializing flask in the variable app
app = Flask(__name__)

#Create route for taking number form params to return the square of it
@app.route("/square/<n>")

#Square function
def square(n):
    try:
        n = int(n)
        return_data = {
            "number": n,
            "square_of_number": n**2
        }
        return jsonify(return_data)
    except:
        return_data = {
            "input": n,
            "error": "Not a number"
        }
        return jsonify(return_data)

if __name__ == "__main__":
    app.run(debug=True)