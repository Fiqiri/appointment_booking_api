# Appointment Booking API

## Overview
This project is an appointment booking system built using Django and Django REST Framework. The API allows for the management of doctors and appointments, including features for scheduling, recurring appointments, and checking availability.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/appointment_system.git
   cd appointment_system
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   - If you want to use SQLite, you can skip this step, as it requires no additional configuration.
   - If you prefer to use another SQL-based database (e.g., PostgreSQL), configure your database settings in `settings.py` with your database credentials.


5. Run database migrations:
   ```bash
   python manage.py migrate
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Doctors
- **List Doctors**: `GET /doctors/`
- **Create Doctor**: `POST /doctors/create/`
  - Example payload:
    ```json
    {
      "name": "Dr. John",
      "start_time": "09:00",
      "end_time": "17:00"
    }
    ```
- **Get Doctor Details**: `GET /doctors/<id>/`
- **Get Doctor Availability**: `GET /doctors/<id>/availability/?start=YYYY-MM-DD&end=YYYY-MM-DD`

### Appointments
- **Create Appointment**: `POST /appointments/create/`
  - Example payload:
    ```json
    {
      "doctor": 1,
      "start_datetime": "2024-09-30T10:00:00Z",
      "end_datetime": "2024-09-30T10:30:00Z"
    }
    ```

## Running Tests

To run tests, use the following command:

```bash
python manage.py test
```