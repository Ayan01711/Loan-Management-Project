"""
==========================================================
Loan Management System

File Name : payment.py

Purpose :
Contains EMI Schedule and Payment Models

Author : Ayan
==========================================================
"""

from extensions import db


# ==========================================================
# EMI Schedule Model
# ==========================================================

class EMISchedule(db.Model):
    """
    Stores EMI schedule for approved loans.
    """

    __tablename__ = "emi_schedule"

    # ------------------------------------------------------
    # Primary Key
    # ------------------------------------------------------

    emi_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    # ------------------------------------------------------
    # Foreign Key
    # ------------------------------------------------------

    application_id = db.Column(
        db.Integer,
        db.ForeignKey("loan_applications.application_id"),
        nullable=False
    )

    # ------------------------------------------------------
    # EMI Details
    # ------------------------------------------------------

    installment_no = db.Column(
        db.Integer,
        nullable=False
    )

    due_date = db.Column(
        db.Date,
        nullable=False
    )

    emi_amount = db.Column(
        db.Numeric(12, 2),
        nullable=False
    )

    principal_amount = db.Column(
        db.Numeric(12, 2),
        nullable=False
    )

    interest_amount = db.Column(
        db.Numeric(12, 2),
        nullable=False
    )

    payment_status = db.Column(
        db.Enum(
            "Pending",
            "Paid"
        ),
        default="Pending"
    )

    payment_date = db.Column(
        db.Date
    )

    # ------------------------------------------------------
    # Relationship
    # ------------------------------------------------------

    payments = db.relationship(
        "Payment",
        backref="emi",
        lazy=True
    )

    # ------------------------------------------------------
    # String Representation
    # ------------------------------------------------------

    def __repr__(self):

        return f"<EMI {self.emi_id}>"

    # ------------------------------------------------------
    # Dictionary
    # ------------------------------------------------------

    def to_dict(self):

        return {

            "emi_id": self.emi_id,
            "application_id": self.application_id,
            "installment_no": self.installment_no,
            "emi_amount": float(self.emi_amount),
            "payment_status": self.payment_status

        }


# ==========================================================
# Payment Model
# ==========================================================

class Payment(db.Model):
    """
    Stores customer payment history.
    """

    __tablename__ = "payments"

    # ------------------------------------------------------
    # Primary Key
    # ------------------------------------------------------

    payment_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    # ------------------------------------------------------
    # Foreign Key
    # ------------------------------------------------------

    emi_id = db.Column(
        db.Integer,
        db.ForeignKey("emi_schedule.emi_id"),
        nullable=False
    )

    # ------------------------------------------------------
    # Payment Information
    # ------------------------------------------------------

    payment_amount = db.Column(
        db.Numeric(12, 2),
        nullable=False
    )

    payment_mode = db.Column(
        db.Enum(
            "Cash",
            "UPI",
            "Card",
            "Net Banking"
        )
    )

    transaction_id = db.Column(
        db.String(100)
    )

    payment_date = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    # ------------------------------------------------------
    # String Representation
    # ------------------------------------------------------

    def __repr__(self):

        return f"<Payment {self.payment_id}>"

    # ------------------------------------------------------
    # Dictionary
    # ------------------------------------------------------

    def to_dict(self):

        return {

            "payment_id": self.payment_id,
            "emi_id": self.emi_id,
            "payment_amount": float(self.payment_amount),
            "payment_mode": self.payment_mode,
            "transaction_id": self.transaction_id

        }