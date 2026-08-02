"""
==========================================================
Loan Management System

File Name : bank_account.py

Purpose :
Customer Bank Account Model

Author : Ayan
==========================================================
"""

# ==========================================================
# Import Required Packages
# ==========================================================

from extensions import db


# ==========================================================
# Bank Account Model
# ==========================================================

class BankAccount(db.Model):
    """
    Stores customer bank account information.
    """

    __tablename__ = "customer_bank_accounts"

    # ------------------------------------------------------
    # Primary Key
    # ------------------------------------------------------

    bank_account_id = db.Column(
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
    # Bank Information
    # ------------------------------------------------------

    bank_name = db.Column(
        db.String(100),
        nullable=False
    )

    account_holder_name = db.Column(
        db.String(100),
        nullable=False
    )

    account_number = db.Column(
        db.String(25),
        nullable=False,
        unique=True
    )

    ifsc_code = db.Column(
        db.String(11),
        nullable=False
    )

    branch_name = db.Column(
        db.String(100)
    )

    account_type = db.Column(
        db.Enum(
            "Savings",
            "Current"
        ),
        default="Savings"
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

        return f"<BankAccount {self.bank_name}>"

    # ------------------------------------------------------
    # Dictionary
    # ------------------------------------------------------

    def to_dict(self):

        return {

            "bank_account_id": self.bank_account_id,

            "customer_id": self.customer_id,

            "bank_name": self.bank_name,

            "account_holder_name": self.account_holder_name,

            "account_number": self.account_number,

            "ifsc_code": self.ifsc_code,

            "branch_name": self.branch_name,

            "account_type": self.account_type

        }