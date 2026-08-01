"""
==========================================================
Loan Management System

File Name : extensions.py

Purpose :
Initializes all Flask extensions used throughout
the application.

Author : Ayan
==========================================================
"""

from flask_sqlalchemy import SQLAlchemy


# ==========================================================
# SQLAlchemy Database Object
# ==========================================================

db = SQLAlchemy()