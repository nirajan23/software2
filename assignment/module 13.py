#Ex.1

from flask import Flask, request
import json
import mysql.connector

app = Flask(__name__)


@app.route('/prime_number/<number>')
def prime_number(number):
    is_Prime = True
    number = int(number)
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                is_Prime = False
                break

    response = {
        "is_Prime": is_Prime,
        "Number": number
    }

    json_data = json.dumps(response, default=lambda o: o.__dict__, indent=4)

    return json_data


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)



#Ex.2


connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='airports',
    user='nirajan',
    password='pass_word',
    autocommit=True
)


app = Flask(__name__)


@app.route('/airport/<string:icao>')
def airport(icao):
    sql = "SELECT name, municipality FROM airports"
    sql += " WHERE ident='" + icao + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            name = row[0]
            location = row[1]

    response = {
        "Airport": name,
        "Location": location,
        "ICAO": icao
    }
    json_data = json.dumps(response, default=lambda o: o.__dict__, indent=4)

    return json_data


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
