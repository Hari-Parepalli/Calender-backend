from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def calculate_day(n, m, y):
    leap = (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)
    normal = {
        "january": 0, "february": 3, "march": 3,
        "april": 6, "may": 1, "june": 4,
        "july": 6, "august": 2, "september": 5,
        "october": 0, "november": 3, "december": 5
    }
    leap_year = {
        "january": 6, "february": 2, "march": 3,
        "april": 6, "may": 1, "june": 4,
        "july": 6, "august": 2, "september": 5,
        "october": 0, "november": 3, "december": 5
    }
    mcode = leap_year[m] if leap else normal[m]
    ycode = (6 - 2 * ((y // 100) % 4)) % 7
    x = y % 100
    z = x // 4
    ans = (n + mcode + x + z + ycode) % 7
    days = [
        "Sunday", "Monday", "Tuesday",
        "Wednesday", "Thursday", "Friday", "Saturday"
    ]
    return days[ans]

@app.route('/api/dayofweek', methods=['POST'])
def day_of_week():
    data = request.json
    n = int(data['date'])
    m = data['month'].lower()
    y = int(data['year'])
    try:
        result = calculate_day(n, m, y)
        return jsonify({'day': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
