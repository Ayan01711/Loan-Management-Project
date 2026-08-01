"""
==========================================================
Loan Management System

File Name : admin.py

Purpose :
Admin Model

Represents the administrator of the system.

Author : Ayan
==========================================================
"""

# ==========================================================
# Import Required Packages
# ==========================================================

from extensions import db


# ==========================================================
# Admin Model
# ==========================================================

class Admin(db.Model):
    """
    Database Model for Admin
    """

    __tablename__ = "admins"

    # ------------------------------------------------------
    # Primary Key
    # ------------------------------------------------------
    admin_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    # ------------------------------------------------------
    # Login Username
    # ------------------------------------------------------
    username = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )

    # ------------------------------------------------------
    # Password (Hashed)
    # ------------------------------------------------------
    password = db.Column(
        db.String(255),
        nullable=False
    )

    # ------------------------------------------------------
    # Administrator Full Name
    # ------------------------------------------------------
    full_name = db.Column(
        db.String(100),
        nullable=False
    )

    # ------------------------------------------------------
    # Email Address
    # ------------------------------------------------------
    email = db.Column(
        db.String(100)
    )

    # ------------------------------------------------------
    # Account Creation Date
    # ------------------------------------------------------
    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    # ------------------------------------------------------
    # Object Representation
    # ------------------------------------------------------
    def __repr__(self):
        return f"<Admin {self.username}>"

    # ------------------------------------------------------
    # Convert Object To Dictionary
    # ------------------------------------------------------
    def to_dict(self):

        return {
            "admin_id": self.admin_id,
            "username": self.username,
            "full_name": self.full_name,
            "email": self.email
        }