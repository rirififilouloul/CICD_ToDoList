from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    {
        "title": "Faire les courses",
        "content": "Pain, beurre, lait",
        "date" : "2021-10-10"
    },
    {
        "title": "Aller chez le coiffeur",
        "content": "Coupe de cheveux",
        "date" : "2021-10-10"
    },
    {
        "title": "Acheter un nouveau téléphone",
        "content": "Samsung S21",
        "date" : "2021-10-10"
    }
]


@app.route('/data')
def get_incomes():
    return jsonify(todos)

app.run(port=5000)

