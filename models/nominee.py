"""
==========================================================
Loan Management System

File Name : nominee.py

Purpose :
Customer Nominee Model

Author : Ayan
==========================================================
"""

# ==========================================================
# Import Required Packages
# ==========================================================

from extensions import db


# ==========================================================
# Nominee Model
# ==========================================================

class Nominee(db.Model):
    """
    Stores customer nominee information.
    """

    __tablename__ = "customer_nominees"

    # ------------------------------------------------------
    # Primary Key
    # ------------------------------------------------------

    nominee_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    # ------------------------------------------------------
    # Foreign Key
    # ------------------------------------------------------

    customer_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "customers.customer_id",
            ondelete="CASCADE"
        ),
        nullable=False,
        unique=True
    )

    # ------------------------------------------------------
    # Nominee Information
    # ------------------------------------------------------

    nominee_name = db.Column(
        db.String(100),
        nullable=False
    )

    relationship = db.Column(
        db.Enum(
            "Father",
            "Mother",
            "Brother",
            "Sister",
            "Spouse",
            "Son",
            "Daughter",
            "Other"
        ),
        nullable=False
    )

    nominee_phone = db.Column(
        db.String(20)
    )

    nominee_email = db.Column(
        db.String(100)
    )

    # ------------------------------------------------------
    # Record Creation Date
    # ------------------------------------------------------

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    # ------------------------------------------------------
    # String Representation
    # ------------------------------------------------------

    def __repr__(self):

        return f"<Nominee {self.nominee_name}>"

    # ------------------------------------------------------
    # Dictionary
    # ------------------------------------------------------

    def to_dict(self):

        return {

            "nominee_id": self.nominee_id,

            "customer_id": self.customer_id,

            "nominee_name": self.nominee_name,

            "relationship": self.relationship,

            "nominee_phone": self.nominee_phone,

            "nominee_email": self.nominee_email

        }