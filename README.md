
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
![Website Screenshot](static/media/online%20courses.png)

 Here is the homepage and course layout using Bootstrap cards.

---
## 🚀 Deploying on Render

Follow these steps to deploy your Django project on Render:

### 1. Create a Render Account
- Visit [Render](https://portfolio-jxhc.onrender.com/) and sign up for a free account.

### 2. Set Up the Project
- Push your project to GitHub or GitLab.
- In your Render dashboard, click **New** > **Web Service** and connect your GitHub/GitLab account.
- Select the repository for your project.
- Set the **Build Command** to `pip install -r requirements.txt`.
- Set the **Start Command** to `gunicorn Portfolio-project.wsgi`.

### 3. Configure Environment Variables
- In your Render dashboard, go to **Environment Variables** and add:
  - `SECRET_KEY=your-django-secret-key`
  - `DATABASE_URL=your-database-url-from-render`
  - You can find the `DATABASE_URL` in the **Databases** section of Render.

### 4. Deploy
- Click **Create Web Service** to start the deployment process.
- Once complete, Render will give you a URL (e.g., `Portfolio-project.onrender.com`), where your site will be live!
 Visit my site [here](https://portfolio-jxhc.onrender.com)

---

### 🔧 Future Improvements
- User authentication and registration
- Course payment integration (e.g., Stripe)
- Course preview and full-page details
- Ratings and reviews
- Instructor dashboard

### 📄 License

MIT License — feel free to use, modify, and contribute!

