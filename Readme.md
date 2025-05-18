````markdown
# WebSocket Notification

This Django project demonstrates real-time notifications using WebSockets. It uses Django Channels to handle WebSocket connections and Daphne as the ASGI server.

---

## Features

- Real-time notifications via WebSocket.
- Notification popups with timestamp.
- Notifications saved in the database.
- Notifications dropdown with unread count badge.
- Backend powered by Django Channels.
- Runs with Daphne ASGI server.

---

## Requirements

- Python 3.8+
- Django
- Django Channels
- Channels Redis
- Daphne
- Redis Server (for channel layer backend)

---

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/amirhamjacse/websocketnotification.git
   cd websocketnotification
````

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Make migrations and migrate the database:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run Redis server**

   Make sure Redis is installed and running on your machine at `localhost:6379`.

---

## Running the Server

Run the server with Daphne to support ASGI and WebSockets:

```bash
daphne CONFIG.asgi:application
```

By default, Daphne runs on port 8000. You can access the app at:

```
http://localhost:8000/
```

---

## Usage

* When a notification is sent from the backend, the frontend receives it in real-time via WebSocket.
* Notifications show up in a popup and in the notification dropdown.
* Notifications are saved in the database with timestamps.
* Click the bell icon to toggle the notifications dropdown and mark notifications as read.

---

## Project Structure

* `CONFIG/` - Django project settings and ASGI configuration.
* `wesockapp/` - Django app handling notifications with models, consumers, and routing.
* `manage.py` - Django management script.
* `.gitignore` - Git ignore rules.
* `requirements.txt` - Python dependencies.

---

## Notes

* Ensure Redis server is running before starting Daphne.
* You can customize WebSocket URLs and notification logic in the `wesockapp` app.

---

## License

This project is open-source and free to use.

---

Feel free to contribute or open issues!

```