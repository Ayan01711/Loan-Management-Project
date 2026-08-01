"""
==========================================================
Loan Management System

File Name : customer.py

Purpose :
Customer Database Model

Author : Ayan
==========================================================
"""

# ==========================================================
# Import Required Packages
# ==========================================================

from extensions import db


# ==========================================================
# Customer Model
# ==========================================================

class Customer(db.Model):
    """
    Database Model for Customer
    """

    __tablename__ = "customers"

    # ------------------------------------------------------
    # Primary Key
    # ------------------------------------------------------
    customer_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    # ------------------------------------------------------
    # Personal Information
    # ------------------------------------------------------
    full_name = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    phone = db.Column(
        db.String(20),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(255),
        nullable=False
    )

    gender = db.Column(
        db.Enum(
            "Male",
            "Female",
            "Other"
        )
    )

    dob = db.Column(
        db.Date
    )

    # ------------------------------------------------------
    # Address Information
    # ------------------------------------------------------
    address = db.Column(
        db.Text
    )

    city = db.Column(
        db.String(50)
    )

    state = db.Column(
        db.String(50)
    )

    pincode = db.Column(
        db.String(10)
    )

    # ------------------------------------------------------
    # Identity Information
    # ------------------------------------------------------
    aadhaar_number = db.Column(
        db.String(20)
    )

    pan_number = db.Column(
        db.String(20)
    )

    # ------------------------------------------------------
    # Employment Information
    # ------------------------------------------------------
    occupation = db.Column(
        db.String(100)
    )

    monthly_income = db.Column(
        db.Numeric(12, 2)
    )

    # ------------------------------------------------------
    # Account Status
    # ------------------------------------------------------
    status = db.Column(
        db.Enum(
            "Active",
            "Inactive"
        ),
        default="Active"
    )

    # ------------------------------------------------------
    # Record Creation Date
    # ------------------------------------------------------
    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    # ------------------------------------------------------
    # Relationship
    # ------------------------------------------------------
    loan_applications = db.relationship(
        "LoanApplication",
        backref="customer",
        lazy=True
    )

    # ------------------------------------------------------
    # String Representation
    # ------------------------------------------------------
    def __repr__(self):

        return f"<Customer {self.full_name}>"

    # ------------------------------------------------------
    # Convert Object To Dictionary
    # ------------------------------------------------------
    def to_dict(self):

        return {

            "customer_id": self.customer_id,
            "full_name": self.full_name,
            "email": self.email,
            "phone": self.phone,
            "gender": self.gender,
            "city": self.city,
            "state": self.state,
            "occupation": self.occupation,
            "monthly_income": float(self.monthly_income)
            if self.monthly_income else 0,
            "status": self.status

        }