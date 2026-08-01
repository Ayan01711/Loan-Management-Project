"""
==========================================================
                LOAN MANAGEMENT SYSTEM
----------------------------------------------------------
File Name : app.py

Purpose :
Main entry point of the application.

Author : Ayan
Version : 1.0
==========================================================
"""

# ==========================================================
# Import Required Libraries
# ==========================================================

from flask import Flask, render_template

from config import Config
from extensions import db

# ==========================================================
# Create Flask Application
# ==========================================================

app = Flask(__name__)

# ==========================================================
# Load Configuration
# ==========================================================

app.config.from_object(Config)

# ==========================================================
# Initialize Database
# ==========================================================

db.init_app(app)

# ==========================================================
# Import Blueprints
# ==========================================================

# NOTE:
# These imports are placed here to avoid circular imports.
# We will create these files later.

from routes.visitor import visitor_bp
from routes.auth import auth_bp
from routes.customer import customer_bp
from routes.admin import admin_bp

# ==========================================================
# Register Blueprints
# ==========================================================

app.register_blueprint(visitor_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(customer_bp)
app.register_blueprint(admin_bp)

# ==========================================================
# Error Pages
# ==========================================================

@app.errorhandler(404)
def page_not_found(error):
    """
    Handles Page Not Found Error
    """
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(error):
    """
    Handles Internal Server Error
    """
    return render_template("500.html"), 500


# ==========================================================
# Main Function
# ==========================================================

if __name__ == "__main__":

    print("=" * 60)
    print("Loan Management System Started Successfully")
    print("URL : http://127.0.0.1:5000")
    print("=" * 60)

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )