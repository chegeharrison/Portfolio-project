
---

## Django Online Course Marketplace

This is a Django-powered website designed to enable users to **sell and browse online courses**. It features a clean Bootstrap front end with cards to display each course attractively. The goal is to create a minimal, scalable e-learning platform.

---

### 🚀 Features

* User-friendly landing page styled with **Bootstrap**
* Course display using **Bootstrap cards**
* Admin panel to manage courses
* PostgreSQL database integration
* Modular Django app structure
* Environment variables managed via `.env`
* Scalable setup for production deployment

---

### 🛠 Tech Stack

* **Backend**: Django (Python)
* **Frontend**: HTML, CSS, Bootstrap
* **Database**: PostgreSQL
* **Environment management**: Python `venv`, dotenv

---

### ⚙️ Setup Instructions

1. **Clone the repo**:

   ```bash
   git clone git@github.com:chegeharrison/Portfolio-project.git
   cd Portfolio-project
   ```

2. **Create a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up `.env` file**:
   Create a `.env` file in the root directory with the following structure:

   ```env
   SECRET_KEY=your-secret-key
   DEBUG=True
   DB_ENGINE=django.db.backends.postgresql
   DB_NAME=your-db-name
   DB_USER=your-db-user
   DB_PASSWORD=your-db-password
   DB_HOST=localhost
   DB_PORT=5432
   ```

5. **Apply migrations**:

   ```bash
   python manage.py migrate
   ```

6. **Run the server**:

   ```bash
   python manage.py runserver
   ```

---

### 📸 Screenshots
 ![Website Screenshot](static/media/online%20courses.pngscreenshot.png)

 Here is the homepage and course layout using Bootstrap cards.

---

### ✅ Future Improvements

* User authentication and registration
* Course payment integration (e.g., Stripe)
* Course preview and full-page details
* Ratings and reviews
* Instructor dashboard

---

### 📄 License

MIT License — feel free to use, modify, and contribute!

