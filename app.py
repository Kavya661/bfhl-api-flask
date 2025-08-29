from flask import Flask, request, jsonify,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/bfhl', methods=['POST'])
def bfhl():
    try:
        data = request.get_json()
        input_array = data.get("data", [])

        even_numbers = [x for x in input_array if isinstance(x, int) and x % 2 == 0]
        odd_numbers = [x for x in input_array if isinstance(x, int) and x % 2 != 0]
        alphabets = [x.upper() for x in input_array if isinstance(x, str) and x.isalpha()]
        special_characters = [x for x in input_array if isinstance(x, str) and not x.isalnum()]
        sum_of_numbers = sum([x for x in input_array if isinstance(x, int)])

        concatenated = "".join([c for c in input_array if isinstance(c, str) and c.isalpha()])
        reverse_alternate_caps = "".join(
            [ch.upper() if i % 2 == 0 else ch.lower() for i, ch in enumerate(concatenated[::-1])]
        )

        response = {
            "is_success": True,
            "user_id": "kavyakomar_123",
            "email": "kavyakomar@example.com",
            "roll_number": "22BCE9284",
            "even_numbers": even_numbers,
            "odd_numbers": odd_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum_of_numbers": sum_of_numbers,
            "reverse_alternate_caps": reverse_alternate_caps
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 400


@app.route('/bfhl', methods=['GET'])
def get_bfhl():
    sample_response = {
        "is_success": True,
        "user_id": "sample_user_123",
        "email": "sample@example.com",
        "roll_number": "22BCE9284",
        "even_numbers": [2, 4, 6],
        "odd_numbers": [1, 3, 5],
        "alphabets": ["A", "B", "C"],
        "special_characters": ["@", "#"],
        "sum_of_numbers": 21,
        "reverse_alternate_caps": "CbA"
    }
    return jsonify(sample_response)


if __name__ == '__main__':
    app.run(debug=True)
