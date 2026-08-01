"""
==========================================================
Loan Management System

File : admin_service.py

Purpose :
Admin Business Logic

Author : Ayan
==========================================================
"""

from extensions import db

from models.admin import Admin
from models.customer import Customer
from models.loan import (
    LoanType,
    LoanApplication
)


class AdminService:
    """
    Admin Service Class
    """

    # ======================================================
    # Dashboard Statistics
    # ======================================================

    @staticmethod
    def dashboard_statistics():
        """
        Returns dashboard statistics.
        """

        return {

            "total_customers":
                Customer.query.count(),

            "active_customers":
                Customer.query.filter_by(
                    status="Active"
                ).count(),

            "inactive_customers":
                Customer.query.filter_by(
                    status="Inactive"
                ).count(),

            "total_loans":
                LoanApplication.query.count(),

            "pending_loans":
                LoanApplication.query.filter_by(
                    application_status="Pending"
                ).count(),

            "approved_loans":
                LoanApplication.query.filter_by(
                    application_status="Approved"
                ).count(),

            "rejected_loans":
                LoanApplication.query.filter_by(
                    application_status="Rejected"
                ).count()

        }

    # ======================================================
    # Admin Details
    # ======================================================

    @staticmethod
    def get_admin(admin_id):
        """
        Returns Admin object.
        """

        return Admin.query.get(admin_id)

    # ======================================================
    # Customer Management
    # ======================================================

    @staticmethod
    def get_all_customers():
        """
        Returns all customers.
        """

        return Customer.query.order_by(
            Customer.customer_id.desc()
        ).all()

    @staticmethod
    def activate_customer(customer_id):
        """
        Activate Customer
        """

        customer = Customer.query.get(customer_id)

        if customer is None:

            return False

        customer.status = "Active"

        db.session.commit()

        return True

    @staticmethod
    def deactivate_customer(customer_id):
        """
        Deactivate Customer
        """

        customer = Customer.query.get(customer_id)

        if customer is None:

            return False

        customer.status = "Inactive"

        db.session.commit()

        return True

    # ======================================================
    # Loan Types
    # ======================================================

    @staticmethod
    def get_all_loan_types():

        return LoanType.query.order_by(
            LoanType.loan_name
        ).all()

    @staticmethod
    def create_loan_type(data):
        """
        Add New Loan Type
        """

        loan = LoanType(

            loan_name=data["loan_name"],

            interest_rate=data["interest_rate"],

            processing_fee=data["processing_fee"],

            minimum_amount=data["minimum_amount"],

            maximum_amount=data["maximum_amount"],

            maximum_years=data["maximum_years"]

        )

        db.session.add(loan)

        db.session.commit()

        return True

    @staticmethod
    def update_loan_type(
        loan_type_id,
        data
    ):
        """
        Update Loan Type
        """

        loan = LoanType.query.get(
            loan_type_id
        )

        if loan is None:

            return False

        loan.loan_name = data["loan_name"]
        loan.interest_rate = data["interest_rate"]
        loan.processing_fee = data["processing_fee"]
        loan.minimum_amount = data["minimum_amount"]
        loan.maximum_amount = data["maximum_amount"]
        loan.maximum_years = data["maximum_years"]

        db.session.commit()

        return True

    @staticmethod
    def delete_loan_type(
        loan_type_id
    ):
        """
        Delete Loan Type
        """

        loan = LoanType.query.get(
            loan_type_id
        )

        if loan is None:

            return False

        db.session.delete(loan)

        db.session.commit()

        return True

    # ======================================================
    # Loan Applications
    # ======================================================

    @staticmethod
    def get_pending_loans():

        return LoanApplication.query.filter_by(
            application_status="Pending"
        ).all()

    @staticmethod
    def get_approved_loans():

        return LoanApplication.query.filter_by(
            application_status="Approved"
        ).all()

    @staticmethod
    def get_rejected_loans():

        return LoanApplication.query.filter_by(
            application_status="Rejected"
        ).all()