from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="ishan@2212",
        database="airline_reservation"
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/passenger')
def passenger():
    return render_template('passenger.html')

@app.route('/add_passenger', methods=['POST'])
def add_passenger():
    try:
        db = get_db_connection()
        cursor = db.cursor()
        passenger_id = request.form['passenger_id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        age = request.form['age']
        gender = request.form['gender']
        
        query = "INSERT INTO passenger (passenger_id, name, email, phone, age, gender) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (passenger_id, name, email, phone, age, gender))
        db.commit()
        cursor.close()
        db.close()
        return redirect('/')  # redirects to index page
    except Exception as e:
        print(f"An error occurred: {e}")  # Log the error to the console
        return "An error occurred while adding the passenger. Please try again."

@app.route('/crew')
def crew():
    return render_template('crew.html')

@app.route('/add_crew', methods=['POST'])
def add_crew():
    try:
        db = get_db_connection()
        cursor = db.cursor()
        crew_id = request.form['crew_id']
        name = request.form['name']
        role = request.form['role']
        salary = request.form['salary']

        query = "INSERT INTO crew (crew_id, name, role, salary) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (crew_id, name, role, salary))
        db.commit()
        cursor.close()
        db.close()
        return redirect('/')  # redirects to index page
    except Exception as e:
        print(f"An error occurred: {e}")  # Log the error to the console
        return "An error occurred while adding the crew. Please try again."


@app.route('/display_crew', methods=['GET', 'POST'])
def display_crew():
    # try:
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM crew")
    crew_data = cursor.fetchall()
    cursor.close()
    db.close()
    return render_template('display_crew.html', crew_data=crew_data)
    # except Exception as e:
    #     print(f"An error occurred: {e}")
    #     return "An error occurred while fetching crew data."


@app.route('/ticket', methods=['POST'])
def ticket():
    return render_template('ticket.html')

@app.route('/add_ticket', methods=['POST'])
def add_ticket():
    try:
        db = get_db_connection()
        cursor = db.cursor()
        ticket_id = request.form['ticket_id']
        passenger_id = request.form['passenger_id']
        flight_id = request.form['flight_id']
        seat_number = request.form['seat_number']
        price = request.form['price']

        query = "INSERT INTO ticket (ticket_id, passenger_id, flight_id, seat_number, price) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (ticket_id, passenger_id, flight_id, seat_number, price))
        db.commit()
        cursor.close()
        db.close()
        return redirect('/')  # redirects to index page
    except Exception as e:
        print(f"An error occurred: {e}")  # Log the error to the console
        return "An error occurred while adding the ticket. Please try again."

@app.route('/flight')
def flight():
    return render_template('flight.html')

@app.route('/add_flight', methods=['POST'])
def add_flight():
    try:
        db = get_db_connection()
        cursor = db.cursor()
        flight_id = request.form['flight_id']
        flight_no = request.form['flight_no']
        source = request.form['source']
        destination = request.form['destination']
        airline_id = request.form['airline_id']
        departure_time = request.form['departure_time']
        arrival_time = request.form['arrival_time']
        name = request.form['name']
        capacity = request.form['capacity']

        query = "INSERT INTO flight (flight_id,flight_no, source, destination, airline_id, departure_time, arrival_time, name, capacity) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (flight_id, flight_no,source, destination, airline_id, departure_time, arrival_time, name, capacity))
        db.commit()
        cursor.close()
        db.close()
        return redirect('/')  # redirects to index page
    except Exception as e:
        print(f"An error occurred: {e}")  # Log the error to the console
        return "An error occurred while adding the flight. Please try again."


@app.route('/edit_crew/<crew_id>', methods=['GET', 'POST'])
def edit_crew(crew_id):
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    if request.method == 'POST':
        name = request.form['name']
        role = request.form['role']
        salary = request.form['salary']

        print("Updating:", name, role, salary, crew_id)  # debug log

        update_query = "UPDATE crew SET name=%s, role=%s, salary=%s WHERE crew_id=%s"
        cursor.execute(update_query, (name, role, salary, crew_id))
        db.commit()
        cursor.close()
        db.close()
        return redirect('/display-crew')

    # GET request - fetch crew member info
    cursor.execute("SELECT * FROM crew WHERE crew_id = %s", (crew_id,))
    crew = cursor.fetchone()
    cursor.close()
    db.close()
    return render_template('edit-crew.html', crew=crew)


@app.route('/delete_crew/<crew_id>', methods=['POST'])
def delete_crew(crew_id):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("DELETE FROM crew WHERE crew_id=%s", (crew_id,))
    db.commit()
    cursor.close()
    db.close()
    return redirect('/display_crew')



if __name__ == '__main__':
    app.run(debug=True)
