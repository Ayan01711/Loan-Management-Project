"""
==========================================================
Loan Management System

File : loan_service.py

Purpose :
Loan Business Logic

Author : Ayan
==========================================================
"""

from extensions import db

from models.loan import (
    LoanType,
    LoanApplication
)


class LoanService:
    """
    Loan Service
    """

    # ======================================================
    # Loan Types
    # ======================================================

    @staticmethod
    def get_all_loan_types():
        """
        Return all active loan types.
        """

        return LoanType.query.filter_by(
            status="Active"
        ).all()

    @staticmethod
    def get_loan_type(loan_type_id):
        """
        Return loan type by ID.
        """

        return LoanType.query.get(
            loan_type_id
        )

    # ======================================================
    # Loan Application
    # ======================================================

    @staticmethod
    def apply_loan(data):
        """
        Create new loan application.
        """

        application = LoanApplication(

            customer_id=data["customer_id"],

            loan_type_id=data["loan_type_id"],

            requested_amount=data["requested_amount"],

            duration_months=data["duration_months"],

            purpose=data["purpose"]

        )

        db.session.add(application)

        db.session.commit()

        return True, "Loan Application Submitted Successfully."

    @staticmethod
    def get_application(application_id):
        """
        Return application by ID.
        """

        return LoanApplication.query.get(
            application_id
        )

    @staticmethod
    def get_customer_applications(customer_id):
        """
        Return applications of customer.
        """

        return LoanApplication.query.filter_by(
            customer_id=customer_id
        ).order_by(
            LoanApplication.application_date.desc()
        ).all()

    @staticmethod
    def get_all_applications():
        """
        Return all applications.
        """

        return LoanApplication.query.order_by(
            LoanApplication.application_date.desc()
        ).all()

    # ======================================================
    # Loan Approval
    # ======================================================

    @staticmethod
    def approve_loan(
        application_id,
        admin_id,
        remarks=""
    ):
        """
        Approve loan application.
        """

        application = LoanApplication.query.get(
            application_id
        )

        if application is None:

            return False, "Application Not Found."

        application.application_status = "Approved"

        application.approved_by = admin_id

        application.remarks = remarks

        db.session.commit()

        return True, "Loan Approved Successfully."

    @staticmethod
    def reject_loan(
        application_id,
        admin_id,
        remarks=""
    ):
        """
        Reject loan application.
        """

        application = LoanApplication.query.get(
            application_id
        )

        if application is None:

            return False, "Application Not Found."

        application.application_status = "Rejected"

        application.approved_by = admin_id

        application.remarks = remarks

        db.session.commit()

        return True, "Loan Rejected Successfully."

    # ======================================================
    # Dashboard Statistics
    # ======================================================

    @staticmethod
    def total_applications():

        return LoanApplication.query.count()

    @staticmethod
    def pending_applications():

        return LoanApplication.query.filter_by(
            application_status="Pending"
        ).count()

    @staticmethod
    def approved_applications():

        return LoanApplication.query.filter_by(
            application_status="Approved"
        ).count()

    @staticmethod
    def rejected_applications():

        return LoanApplication.query.filter_by(
            application_status="Rejected"
        ).count()