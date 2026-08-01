"""
==========================================================
Loan Management System

File Name : config.py

Purpose :
Application configuration settings.

Author : Ayan
==========================================================
"""

import os


class Config:
    """
    Application Configuration Class
    """

    # Secret key used for session management
    SECRET_KEY = "LoanManagementSystem@2026"

    # MySQL Database Connection
    DB_USERNAME = "root"
    DB_PASSWORD = "Ayan1711"
    DB_HOST = "localhost"
    DB_PORT = "3306"
    DB_NAME = "loan_management"

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}"
        f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Upload folder
    UPLOAD_FOLDER = os.path.join(
        os.getcwd(),
        "uploads"
    )

    # Maximum upload size (5 MB)
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024

    # Allowed document extensions
    ALLOWED_EXTENSIONS = {
        "pdf",
        "jpg",
        "jpeg",
        "png"
    }