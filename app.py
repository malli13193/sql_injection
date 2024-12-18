from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/search')
def search():
    name = request.args.get('name', '')
    return jsonify({"message": f"Search results for {name}"})

if __name__ == "__main__":
    app.run(debug=True)
