"""
==========================================================
Loan Management System

File Name : loan.py

Purpose :
Contains LoanType and LoanApplication Models

Author : Ayan
==========================================================
"""

from extensions import db


# ==========================================================
# Loan Type Model
# ==========================================================

class LoanType(db.Model):
    """
    Stores available loan types.
    """

    __tablename__ = "loan_types"

    # Primary Key
    loan_type_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    # Loan Details
    loan_name = db.Column(
        db.String(100),
        nullable=False
    )

    interest_rate = db.Column(
        db.Numeric(5, 2),
        nullable=False
    )

    processing_fee = db.Column(
        db.Numeric(10, 2)
    )

    minimum_amount = db.Column(
        db.Numeric(12, 2)
    )

    maximum_amount = db.Column(
        db.Numeric(12, 2)
    )

    maximum_years = db.Column(
        db.Integer
    )

    status = db.Column(
        db.Enum("Active", "Inactive"),
        default="Active"
    )

    # Relationship
    loan_applications = db.relationship(
        "LoanApplication",
        backref="loan_type",
        lazy=True
    )

    def __repr__(self):
        return f"<LoanType {self.loan_name}>"

    def to_dict(self):
        return {
            "loan_type_id": self.loan_type_id,
            "loan_name": self.loan_name,
            "interest_rate": float(self.interest_rate),
            "processing_fee": float(self.processing_fee),
            "minimum_amount": float(self.minimum_amount),
            "maximum_amount": float(self.maximum_amount),
            "maximum_years": self.maximum_years,
            "status": self.status
        }


# ==========================================================
# Loan Application Model
# ==========================================================

class LoanApplication(db.Model):
    """
    Stores customer loan applications.
    """

    __tablename__ = "loan_applications"

    # Primary Key
    application_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    # Foreign Keys
    customer_id = db.Column(
        db.Integer,
        db.ForeignKey("customers.customer_id"),
        nullable=False
    )

    loan_type_id = db.Column(
        db.Integer,
        db.ForeignKey("loan_types.loan_type_id"),
        nullable=False
    )

    # Loan Information
    requested_amount = db.Column(
        db.Numeric(12, 2),
        nullable=False
    )

    duration_months = db.Column(
        db.Integer,
        nullable=False
    )

    purpose = db.Column(
        db.Text
    )

    application_status = db.Column(
        db.Enum(
            "Pending",
            "Approved",
            "Rejected"
        ),
        default="Pending"
    )

    remarks = db.Column(
        db.Text
    )

    application_date = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    approved_by = db.Column(
        db.Integer,
        db.ForeignKey("admins.admin_id")
    )

    approval_date = db.Column(
        db.DateTime
    )

    admin = db.relationship(
        "Admin",
        backref="approved_loans"
    )

    emi_schedule = db.relationship(
        "EMISchedule",
        backref="loan_application",
        lazy=True
    )

    def __repr__(self):
        return f"<LoanApplication {self.application_id}>"

    def to_dict(self):
        return {
            "application_id": self.application_id,
            "customer_id": self.customer_id,
            "loan_type_id": self.loan_type_id,
            "requested_amount": float(self.requested_amount),
            "duration_months": self.duration_months,
            "status": self.application_status
        }