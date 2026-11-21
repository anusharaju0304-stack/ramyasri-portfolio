# Ramyasri Portfolio — Python + Flask

A beginner-friendly portfolio website built with Python (Flask), HTML, CSS and JavaScript.

## What's included

- `app.py` — Python Flask application and editable portfolio content
- `templates/index.html` — website structure
- `static/style.css` — responsive premium styling
- `static/script.js` — mobile navigation, scroll animations and current year
- `requirements.txt` — Python dependency

## Run in VS Code (Windows)

1. Install Python 3 from https://www.python.org/downloads/ and select **Add Python to PATH** during installation.
2. Extract this ZIP file.
3. Open VS Code → **File → Open Folder** → choose the extracted `ramyasri_portfolio_python` folder.
4. Open **Terminal → New Terminal**.
5. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

6. Activate it:

   ```powershell
   .venv\Scripts\Activate
   ```

   If PowerShell blocks activation, use Command Prompt terminal and run:

   ```bat
   .venv\Scripts\activate.bat
   ```

7. Install Flask:

   ```bash
   pip install -r requirements.txt
   ```

8. Start the website:

   ```bash
   python app.py
   ```

9. Open the local address shown in the terminal, usually `http://127.0.0.1:5000`.

**Note:** Flask runs the website itself. You do not need Live Server for this Python version.

## Personalize your portfolio

Open `app.py` and edit the `PORTFOLIO` dictionary:

- Add your confirmed education details.
- Replace the sample email and LinkedIn URL with your personal professional links.
- Add your GitHub URL.
- Add technical skills, verified projects, certifications and awards.
- Update experience dates.
- Add project links where available.

The current content uses details available from prior conversations. Unknown academic details and personal achievements are placeholders, not invented claims.

## Deploy online

For a simple deployment, you can use a Python hosting service that supports Flask, such as Render:

1. Create a GitHub repository and upload this project.
2. Create a new Web Service on Render and connect the repository.
3. Build command: `pip install -r requirements.txt`
4. Start command: `gunicorn app:app`
5. Add `gunicorn` to `requirements.txt` before deploying.

For deployment, update `requirements.txt` to:

```text
Flask>=3.0,<4.0
gunicorn
```

Then redeploy. Your hosting provider will give you a public URL.

## Important

This is a portfolio starter based on the information currently available. Confirm all details before sharing it with recruiters. Add a real resume file and link it from the site if you want a working Resume download button.
