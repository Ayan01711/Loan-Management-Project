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
from models.bank_account import BankAccount
from models.nominee import Nominee


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
        Register new customer with
        Bank Details and Nominee.
        """

        # ----------------------------------------------
        # Duplicate Email
        # ----------------------------------------------

        customer = Customer.query.filter_by(
            email=data["email"]
        ).first()

        if customer:

            return False, "Email already exists."

        # ----------------------------------------------
        # Duplicate Phone
        # ----------------------------------------------

        customer = Customer.query.filter_by(
            phone=data["phone"]
        ).first()

        if customer:

            return False, "Phone number already exists."

        # ----------------------------------------------
        # Duplicate Account Number
        # ----------------------------------------------

        account = BankAccount.query.filter_by(
            account_number=data["account_number"]
        ).first()

        if account:

            return False, "Bank account already exists."

        try:

            # ------------------------------------------
            # Encrypt Password
            # ------------------------------------------

            hashed_password = generate_password_hash(
                data["password"]
            )

            # ------------------------------------------
            # Customer
            # ------------------------------------------

            customer = Customer(

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

            db.session.add(customer)

            # ------------------------------------------
            # Get Customer ID
            # ------------------------------------------

            db.session.flush()

            # ------------------------------------------
            # Bank Account
            # ------------------------------------------

            bank = BankAccount(

                customer_id=customer.customer_id,

                bank_name=data["bank_name"],

                account_holder_name=data[
                    "account_holder_name"
                ],

                account_number=data[
                    "account_number"
                ],

                ifsc_code=data[
                    "ifsc_code"
                ],

                branch_name=data[
                    "branch_name"
                ],

                account_type=data[
                    "account_type"
                ]

            )

            db.session.add(bank)

            # ------------------------------------------
            # Nominee
            # ------------------------------------------

            nominee = Nominee(

                customer_id=customer.customer_id,

                nominee_name=data[
                    "nominee_name"
                ],

                relationship=data[
                    "relationship"
                ],

                nominee_phone=data[
                    "nominee_phone"
                ],

                nominee_email=data[
                    "nominee_email"
                ]

            )

            db.session.add(nominee)

            # ------------------------------------------
            # Commit Everything
            # ------------------------------------------

            db.session.commit()

            return True, "Registration Successful."

        except Exception as e:

            db.session.rollback()

            print(e)

            return False, "Registration Failed."

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

        if admin.password == password:

            return True, admin

        return False, "Invalid Password"