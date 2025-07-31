
# ✈ Airline Reservation System

The **Airline Reservation System** is a database-driven web application designed to automate and streamline airline ticket booking, flight management, and passenger information handling. It is built using **Python (Flask)** for the backend and **MySQL** as the relational database system, with HTML/CSS for the frontend interface.

## Features

- **Passenger Module**
  - User registration and login
  - View available flights
  - Book tickets and manage reservations
  - Cancel tickets and view booking history

- **Admin Module**
  - Add, update, or delete flight details
  - View and manage crew and booking data
  - Assign crew members to flights

- **Crew Module**
  - Secure login
  - Access to relevant flight assignment information

## Tech Stack

- **Frontend**: HTML, CSS
- **Backend**: Python with Flask
- **Database**: MySQL
- **Tools**: MySQL Workbench, VS Code

## Database Design

The system uses a normalized relational schema with the following key entities:
- `Airline`
- `Airport`
- `Flight`
- `Passenger`
- `Crew`
- `Ticket`
- `Uses` (Flights and Airports)
- `AssignedTo` (Flights and Crew)

ER diagrams, schema definitions, and SQL table creation scripts are provided in the source files.

## Limitations

- No real-time payment gateway integration
- No dynamic seat selection or live seat map
- Single-user access (no concurrent multi-user control)
- Basic security (data encryption not implemented)

## Future Enhancements

- Secure payment integration (e.g. Razorpay, Stripe)
- Multi-user concurrency and session handling
- Enhanced admin dashboard
- Passenger loyalty program
- Analytics and visualization dashboards

## Project Structure

```
├── app.py                  # Flask backend
├── templates/              # HTML files
├── static/                 # CSS files
├── schema.sql              # SQL table creation scripts
└── README.md
```

## How to Run

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/airline-reservation-system.git
   cd airline-reservation-system
   ```

2. Set up a MySQL database and import `schema.sql`.

3. Install dependencies and run the Flask server:
   ```bash
   pip install flask mysql-connector-python
   python app.py
   ```

4. Open your browser and visit `http://localhost:5000`.
