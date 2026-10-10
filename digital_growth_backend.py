#python#
# digital_growth_backend.py
# Digital Growth Hub — Ready-to-run backend
# Frontend file: digital growth frontend.py
# Run: python digital_growth_backend.py

import os
import re
import json
import hmac
import secrets
import sqlite3
import threading
import webbrowser
from pathlib import Path
from datetime import datetime, timezone
from functools import wraps

from flask import Flask, request, jsonify, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash

BASE_DIR = Path(__file__).resolve().parent
FRONTEND_FILE = BASE_DIR / "digital growth frontend.py"
DATABASE_FILE = BASE_DIR / "digital_growth.db"

APP_NAME = "Digital Growth Hub"
PHONE = "018601808843"
EMAIL = "liyonahmed806@gmail.com"
FACEBOOK = "https://www.facebook.com/profile.php?id=61594996359759&sk=directory_links"

PORT = int(os.environ.get("PORT", "5000"))
ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "")
ADMIN_PASSWORD_HASH = os.environ.get("ADMIN_PASSWORD_HASH", "")

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 32 * 1024

SERVICES = [
    "Facebook Ads",
    "Instagram Ads",
    "TikTok Ads",
    "WhatsApp Business API",
    "Meta Business Suite",
    "Business Growth Strategy",
    "Facebook Page Setup",
]

# --------------------------------------------------
# DATABASE
# --------------------------------------------------

def get_db():
    connection = sqlite3.connect(
        str(DATABASE_FILE),
        timeout=20
    )
    connection.row_factory = sqlite3.Row
    return connection

def initialize_database():
    with get_db() as db:
        db.executescript("""
            CREATE TABLE IF NOT EXISTS inquiries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT DEFAULT '',
                service TEXT NOT NULL,
                message TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'new'
                    CHECK(status IN ('new','contacted','closed')),
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                slug TEXT NOT NULL UNIQUE,
                category TEXT NOT NULL DEFAULT 'News',
                content TEXT NOT NULL,
                published INTEGER NOT NULL DEFAULT 0,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS settings (
                key TEXT PRIMARY KEY,
                value TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS admin_sessions (
                token_hash TEXT PRIMARY KEY,
                expires_at TEXT NOT NULL
            );

            CREATE INDEX IF NOT EXISTS idx_inquiry_status
            ON inquiries(status);
        """)

    print("[OK] Database initialized.")

initialize_database()

# --------------------------------------------------
# HELPERS
# --------------------------------------------------

def response_error(message, status=400):
    return jsonify({
        "success": False,
        "error": message
    }), status

def clean(value, limit=5000):
    if not isinstance(value, str):
        return ""
    return value.strip()[:limit]

def valid_email(email):
    return bool(
        re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email)
    )

def admin_required(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        auth = request.authorization

        if not auth:
            return response_error(
                "Admin authentication required.", 401
            )

        username_ok = hmac.compare_digest(
            auth.username.encode(),
            ADMIN_USERNAME.encode()
        )

        password_ok = False

        if ADMIN_PASSWORD_HASH:
            try:
                password_ok = check_password_hash(
                    ADMIN_PASSWORD_HASH, auth.password
                )
            except (ValueError, TypeError):
                password_ok = False
        elif ADMIN_PASSWORD:
            password_ok = hmac.compare_digest(
                auth.password.encode(),
                ADMIN_PASSWORD.encode()
            )

        if not username_ok or not password_ok:
            return response_error(
                "Invalid admin credentials.", 401
            )

        return function(*args, **kwargs)

    return wrapper

# --------------------------------------------------
# FRONTEND
# --------------------------------------------------

@app.get("/")
def homepage():
    # Serve a static HTML file if one exists.
    index = BASE_DIR / "index.html"

    if index.exists():
        return send_from_directory(BASE_DIR, "index.html")

    return jsonify({
        "name": APP_NAME,
        "message": "Backend is running.",
        "frontend_note": (
            "A Python frontend generator is not automatically "
            "a browser page. Export your frontend as index.html "
            "to serve it here."
        ),
        "api": "/api/health"
    })

# --------------------------------------------------
# PUBLIC API
# --------------------------------------------------

@app.get("/api/health")
def health():
    return jsonify({
        "success": True,
        "application": APP_NAME,
        "status": "healthy",
        "time": datetime.now(timezone.utc).isoformat()
    })

@app.get("/api/business")
def business_details():
    return jsonify({
        "name": APP_NAME,
        "phone": PHONE,
        "email": EMAIL,
        "facebook": FACEBOOK,
        "services": SERVICES
    })

@app.get("/api/services")
def list_services():
    return jsonify({
        "success": True,
        "services": SERVICES
    })

@app.post("/api/contact")
def create_inquiry():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return response_error(
            "Please submit the form as JSON."
        )

    name = clean(data.get("name"), 100)
    email = clean(data.get("email"), 254).lower()
    phone = clean(data.get("phone", ""), 30)
    service = clean(data.get("service"), 100)
    message = clean(data.get("message"), 5000)

    if not all([name, email, service, message]):
        return response_error(
            "Name, email, service and message are required."
        )

    if not valid_email(email):
        return response_error("Enter a valid email address.")

    if service not in SERVICES:
        return response_error("Select a valid service.")

    try:
        with get_db() as db:
            cursor = db.execute("""
                INSERT INTO inquiries
                    (name, email, phone, service, message)
                VALUES (?, ?, ?, ?, ?)
            """, (name, email, phone, service, message))

            inquiry_id = cursor.lastrowid

        return jsonify({
            "success": True,
            "message": "Your inquiry was received.",
            "inquiry_id": inquiry_id
        }), 201

    except sqlite3.Error:
        app.logger.exception("Inquiry save failed")
        return response_error(
            "Unable to save your inquiry.", 500
        )

@app.get("/api/posts")
def public_posts():
    with get_db() as db:
        rows = db.execute("""
            SELECT id, title, slug, category, content, created_at
            FROM posts
            WHERE published = 1
            ORDER BY id DESC
        """).fetchall()

    return jsonify({
        "success": True,
        "posts": [dict(row) for row in rows]
    })

# --------------------------------------------------
# ADMIN API
# Configure ADMIN_USERNAME and ADMIN_PASSWORD in
# your operating system environment before running.
# --------------------------------------------------

@app.get("/api/admin/dashboard")
@admin_required
def dashboard():
    with get_db() as db:
        total = db.execute(
            "SELECT COUNT(*) FROM inquiries"
        ).fetchone()[0]

        new = db.execute(
            "SELECT COUNT(*) FROM inquiries WHERE status='new'"
        ).fetchone()[0]

        contacted = db.execute(
            "SELECT COUNT(*) FROM inquiries WHERE status='contacted'"
        ).fetchone()[0]

        closed = db.execute(
            "SELECT COUNT(*) FROM inquiries WHERE status='closed'"
        ).fetchone()[0]

        latest = db.execute("""
            SELECT id, name, email, service, status, created_at
            FROM inquiries
            ORDER BY id DESC LIMIT 10
        """).fetchall()

    return jsonify({
        "success": True,
        "statistics": {
            "total": total,
            "new": new,
            "contacted": contacted,
            "closed": closed
        },
        "latest_inquiries": [dict(row) for row in latest]
    })

@app.get("/api/admin/inquiries")
@admin_required
def admin_inquiries():
    status = request.args.get("status", "").strip()

    if status and status not in {"new", "contacted", "closed"}:
        return response_error("Invalid status.")

    page = request.args.get("page", default=1, type=int)
    limit = request.args.get("limit", default=20, type=int)
    page = max(page or 1, 1)
    limit = min(max(limit or 20, 1), 100)

    condition = "WHERE status=?" if status else ""
    params = [status] if status else []

    with get_db() as db:
        total = db.execute(
            f"SELECT COUNT(*) FROM inquiries {condition}",
            params
        ).fetchone()[0]

        rows = db.execute(
            f"""
            SELECT * FROM inquiries
            {condition}
            ORDER BY id DESC LIMIT ? OFFSET ?
            """,
            params + [limit, (page - 1) * limit]
        ).fetchall()

    return jsonify({
        "success": True,
        "total": total,
        "page": page,
        "inquiries": [dict(row) for row in rows]
    })

@app.patch("/api/admin/inquiries/<int:inquiry_id>")
@admin_required
def update_inquiry(inquiry_id):
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return response_error("Send a JSON request.")

    status = clean(data.get("status"), 20)

    if status not in {"new", "contacted", "closed"}:
        return response_error("Invalid status.")

    with get_db() as db:
        cursor = db.execute(
            "UPDATE inquiries SET status=? WHERE id=?",
            (status, inquiry_id)
        )

        if cursor.rowcount == 0:
            return response_error("Inquiry not found.", 404)

    return jsonify({"success": True, "status": status})

@app.delete("/api/admin/inquiries/<int:inquiry_id>")
@admin_required
def delete_inquiry(inquiry_id):
    with get_db() as db:
        cursor = db.execute(
            "DELETE FROM inquiries WHERE id=?",
            (inquiry_id,)
        )

        if cursor.rowcount == 0:
            return response_error("Inquiry not found.", 404)

    return jsonify({
        "success": True,
        "message": "Inquiry deleted."
    })

@app.post("/api/admin/posts")
@admin_required
def create_post():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return response_error("Send a JSON request.")

    title = clean(data.get("title"), 200)
    slug = clean(data.get("slug"), 200).lower()
    category = clean(data.get("category", "News"), 80)
    content = clean(data.get("content"), 20000)
    published = bool(data.get("published", False))

    if not title or not slug or not content:
        return response_error(
            "Title, slug and content are required."
        )

    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
        return response_error("Invalid post slug.")

    try:
        with get_db() as db:
            cursor = db.execute("""
                INSERT INTO posts
                    (title, slug, category, content, published)
                VALUES (?, ?, ?, ?, ?)
            """, (
                title, slug, category, content, int(published)
            ))

        return jsonify({
            "success": True,
            "post_id": cursor.lastrowid
        }), 201

    except sqlite3.IntegrityError:
        return response_error("Post slug already exists.")

@app.get("/api/admin/settings")
@admin_required
def admin_settings():
    with get_db() as db:
        rows = db.execute(
            "SELECT key, value FROM settings"
        ).fetchall()

    return jsonify({
        "success": True,
        "settings": {
            row["key"]: row["value"] for row in rows
        }
    })

@app.put("/api/admin/settings")
@admin_required
def update_settings():
    data = request.get_json(silent=True)

    allowed = {
        "business_name",
        "contact_email",
        "contact_phone",
        "facebook_url"
    }

    if not isinstance(data, dict) or not data:
        return response_error("Provide settings as JSON.")

    if any(key not in allowed for key in data):
        return response_error("Unknown setting key.")

    with get_db() as db:
        for key, value in data.items():
            if not isinstance(value, str) or len(value) > 500:
                return response_error(
                    f"Invalid value for {key}."
                )

            db.execute("""
                INSERT INTO settings (key, value)
                VALUES (?, ?)
                ON CONFLICT(key) DO UPDATE
                SET value=excluded.value
            """, (key, value.strip()))

    return jsonify({
        "success": True,
        "message": "Settings saved."
    })

# --------------------------------------------------
# START SERVER
# --------------------------------------------------

if __name__ == "__main__":
    if not ADMIN_PASSWORD and not ADMIN_PASSWORD_HASH:
        print("\nWARNING: Admin access is not configured.")
        print("Set ADMIN_USERNAME and ADMIN_PASSWORD before")
        print("using admin endpoints in a real deployment.\n")

    print("=" * 50)
    print(APP_NAME, "Backend")
    print("=" * 50)
    print(f"API: http://127.0.0.1:{PORT}/api/health")
    print(f"Business: http://127.0.0.1:{PORT}/api/business")
    print("Press CTRL+C to stop.")
    print("=" * 50)

    app.run(
        host="127.0.0.1",
        port=PORT,
        debug=False
    )
