from flask import Flask, render_template, request, redirect, url_for
import psycopg2
from psycopg2 import sql, Error
import os

app = Flask(__name__)

def create_connection():
    try:
        connection = psycopg2.connect(
            user=os.getenv('DB_USERNAME'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
            database=os.getenv('DB_NAME')

        )
        return connection
    except Error as e:
        print("Error while connecting to PostgreSQL", e)
        return None

@app.route('/', methods=['GET'])
def index():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM goals")
        goals = cursor.fetchall()
        cursor.close()
        connection.close()
        return render_template('index.html', goals=goals)
    else:
        return "Error connecting to the PostgreSQL database", 500

@app.route('/add_goal', methods=['POST'])
def add_goal():
    goal_name = request.form.get('goal_name')
    if goal_name:
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO goals (goal_name) VALUES (%s)", (goal_name,))
            connection.commit()
            cursor.close()
            connection.close()
    return redirect(url_for('index'))

@app.route('/remove_goal', methods=['POST'])
def remove_goal():
    goal_id = request.form.get('goal_id')
    if goal_id:
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM goals WHERE id = %s", (goal_id,))
            connection.commit()
            cursor.close()
            connection.close()
    return redirect(url_for('index'))

@app.route('/health', methods=['GET'])
def health_check():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
