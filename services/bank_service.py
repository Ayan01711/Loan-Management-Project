"""
==========================================================
Loan Management System

File Name : bank_service.py

Purpose :
Customer Bank Account Business Logic

Author : Ayan
==========================================================
"""

# ==========================================================
# Import Required Packages
# ==========================================================

from extensions import db

from models.bank_account import BankAccount


# ==========================================================
# Bank Service
# ==========================================================

class BankService:
    """
    Handles Customer Bank Account Operations.
    """

    # ======================================================
    # Get Bank Details
    # ======================================================

    @staticmethod
    def get_bank_details(customer_id):
        """
        Returns bank details of a customer.
        """

        return BankAccount.query.filter_by(
            customer_id=customer_id
        ).first()

    # ======================================================
    # Save Bank Details
    # ======================================================

    @staticmethod
    def save_bank_details(data):
        """
        Saves customer bank details.
        """

        existing = BankAccount.query.filter_by(
            customer_id=data["customer_id"]
        ).first()

        if existing:

            return False, "Bank details already exist."

        account_exists = BankAccount.query.filter_by(
            account_number=data["account_number"]
        ).first()

        if account_exists:

            return False, "Account number already exists."

        bank = BankAccount(

            customer_id=data["customer_id"],

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

        db.session.commit()

        return True, "Bank details saved successfully."

    # ======================================================
    # Update Bank Details
    # ======================================================

    @staticmethod
    def update_bank_details(
        customer_id,
        data
    ):
        """
        Updates customer bank details.
        """

        bank = BankAccount.query.filter_by(
            customer_id=customer_id
        ).first()

        if bank is None:

            return False, "Bank details not found."

        duplicate = BankAccount.query.filter(

            BankAccount.account_number == data[
                "account_number"
            ],

            BankAccount.customer_id != customer_id

        ).first()

        if duplicate:

            return False, "Account number already exists."

        bank.bank_name = data[
            "bank_name"
        ]

        bank.account_holder_name = data[
            "account_holder_name"
        ]

        bank.account_number = data[
            "account_number"
        ]

        bank.ifsc_code = data[
            "ifsc_code"
        ]

        bank.branch_name = data[
            "branch_name"
        ]

        bank.account_type = data[
            "account_type"
        ]

        db.session.commit()

        return True, "Bank details updated successfully."

    # ======================================================
    # Delete Bank Details
    # ======================================================

    @staticmethod
    def delete_bank_details(customer_id):
        """
        Deletes bank details.
        """

        bank = BankAccount.query.filter_by(
            customer_id=customer_id
        ).first()

        if bank is None:

            return False

        db.session.delete(bank)

        db.session.commit()

        return True

    # ======================================================
    # Validate IFSC
    # ======================================================

    @staticmethod
    def validate_ifsc(ifsc_code):
        """
        Simple IFSC validation.
        """

        if len(ifsc_code) != 11:

            return False

        return True

    # ======================================================
    # Validate Account Number
    # ======================================================

    @staticmethod
    def validate_account_number(
        account_number
    ):
        """
        Basic Account Number Validation.
        """

        if len(account_number) < 8:

            return False

        return True