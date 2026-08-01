"""
==========================================================
Loan Management System

File : auth_service.py

Purpose :
Authentication Business Logic

Author : Ayan
==========================================================
"""

# ==========================================================
# Import Packages
# ==========================================================

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from extensions import db

from models.customer import Customer
from models.admin import Admin


# ==========================================================
# Authentication Service
# ==========================================================

class AuthService:
    """
    Handles all authentication operations.
    """

    # ------------------------------------------------------
    # Register Customer
    # ------------------------------------------------------

    @staticmethod
    def register_customer(data):
        """
        Register new customer.
        """

        # Check duplicate email

        customer = Customer.query.filter_by(
            email=data["email"]
        ).first()

        if customer:

            return False, "Email already exists."

        # Check duplicate phone

        customer = Customer.query.filter_by(
            phone=data["phone"]
        ).first()

        if customer:

            return False, "Phone number already exists."

        # Encrypt password

        hashed_password = generate_password_hash(
            data["password"]
        )

        # Create customer object

        new_customer = Customer(

            full_name=data["full_name"],

            email=data["email"],

            phone=data["phone"],

            password=hashed_password,

            gender=data["gender"],

            dob=data["dob"],

            address=data["address"],

            city=data["city"],

            state=data["state"],

            pincode=data["pincode"],

            aadhaar_number=data["aadhaar_number"],

            pan_number=data["pan_number"],

            occupation=data["occupation"],

            monthly_income=data["monthly_income"]

        )

        db.session.add(new_customer)

        db.session.commit()

        return True, "Registration Successful."

    # ------------------------------------------------------
    # Customer Login
    # ------------------------------------------------------

    @staticmethod
    def customer_login(email, password):
        """
        Authenticate customer.
        """

        customer = Customer.query.filter_by(
            email=email
        ).first()

        if customer is None:

            return False, "Invalid Email"

        if check_password_hash(
            customer.password,
            password
        ):

            return True, customer

        return False, "Invalid Password"

    # ------------------------------------------------------
    # Admin Login
    # ------------------------------------------------------

    @staticmethod
    def admin_login(username, password):
        """
        Authenticate administrator.
        """

        admin = Admin.query.filter_by(
            username=username
        ).first()

        if admin is None:

            return False, "Invalid Username"

        # Temporary login
        # Later we'll hash admin password from DB.

        if admin.password == password:

            return True, admin

        return False, "Invalid Password"