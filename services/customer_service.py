"""
==========================================================
Loan Management System

File : customer_service.py

Purpose :
Customer Business Logic

Author : Ayan
==========================================================
"""

from extensions import db
from models.customer import Customer

from models.bank_account import BankAccount
from models.nominee import Nominee
from models.loan import LoanApplication
from models.payment import EMISchedule
from sqlalchemy import func


class CustomerService:

    @staticmethod
    def get_customer(customer_id):
        """
        Get customer by ID
        """
        return Customer.query.get(customer_id)

    @staticmethod
    def get_all_customers():
        """
        Get all customers
        """
        return Customer.query.order_by(
            Customer.customer_id.desc()
        ).all()

    @staticmethod
    def get_customer_by_email(email):
        """
        Get customer using email
        """
        return Customer.query.filter_by(
            email=email
        ).first()

    @staticmethod
    def update_customer(customer_id, data):
        """
        Update customer profile,
        bank details and nominee details.
        """

        customer = Customer.query.get(customer_id)

        if customer is None:

            return False, "Customer not found."

        # ==================================================
        # Customer Information
        # ==================================================

        customer.full_name = data["full_name"]

        customer.phone = data["phone"]

        customer.gender = data["gender"]

        customer.dob = data["dob"]

        customer.address = data["address"]

        customer.city = data["city"]

        customer.state = data["state"]

        customer.pincode = data["pincode"]

        customer.aadhaar_number = data["aadhaar_number"]

        customer.pan_number = data["pan_number"]

        customer.occupation = data["occupation"]

        customer.monthly_income = data["monthly_income"]

        # ==================================================
        # Bank Details
        # ==================================================

        bank = BankAccount.query.filter_by(
            customer_id=customer_id
        ).first()

        if bank is None:

            bank = BankAccount(
                customer_id=customer_id
            )

            db.session.add(bank)

        bank.bank_name = data["bank_name"]

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

        # ==================================================
        # Nominee Details
        # ==================================================

        nominee = Nominee.query.filter_by(
            customer_id=customer_id
        ).first()

        if nominee is None:

            nominee = Nominee(
                customer_id=customer_id
            )

            db.session.add(nominee)

        nominee.nominee_name = data[
            "nominee_name"
        ]

        nominee.relationship = data[
            "relationship"
        ]

        nominee.nominee_phone = data[
            "nominee_phone"
        ]

        nominee.nominee_email = data[
            "nominee_email"
        ]

        db.session.commit()

        return True, "Profile Updated Successfully."

    @staticmethod
    def delete_customer(customer_id):
        """
        Delete customer
        """

        customer = Customer.query.get(customer_id)

        if customer is None:
            return False

        db.session.delete(customer)
        db.session.commit()

        return True

    @staticmethod
    def total_customers():
        """
        Return total customers
        """
        return Customer.query.count()

    @staticmethod
    def active_customers():
        """
        Return active customers
        """
        return Customer.query.filter_by(
            status="Active"
        ).count()

    @staticmethod
    def inactive_customers():
        """
        Return inactive customers
        """
        return Customer.query.filter_by(
            status="Inactive"
        ).count()

    @staticmethod
    def activate_customer(customer_id):

        customer = Customer.query.get(customer_id)

        if customer:

            customer.status = "Active"

            db.session.commit()

            return True

        return False

    @staticmethod
    def deactivate_customer(customer_id):

        customer = Customer.query.get(customer_id)

        if customer:

            customer.status = "Inactive"

            db.session.commit()

            return True

        return False
    
    # ======================================================
    # Customer Dashboard Statistics
    # ======================================================

    @staticmethod
    def get_dashboard_statistics(customer_id):
        """
        Returns dashboard statistics for a customer.
        """

        loans = LoanApplication.query.filter_by(
            customer_id=customer_id
        ).all()

        total_loans = len(loans)

        approved_loans = sum(
            1 for loan in loans
            if loan.application_status == "Approved"
        )

        pending_loans = sum(
            1 for loan in loans
            if loan.application_status == "Pending"
        )

        rejected_loans = sum(
            1 for loan in loans
            if loan.application_status == "Rejected"
        )

        application_ids = [
            loan.application_id
            for loan in loans
        ]

        paid_emi = 0
        pending_emi = 0
        outstanding_amount = 0
        next_emi_date = None

        if application_ids:

            emi_records = EMISchedule.query.filter(
                EMISchedule.application_id.in_(application_ids)
            ).all()

            paid_emi = sum(
                1 for emi in emi_records
                if emi.payment_status == "Paid"
            )

            pending_emi = sum(
                1 for emi in emi_records
                if emi.payment_status == "Pending"
            )

            outstanding_amount = sum(
                float(emi.emi_amount)
                for emi in emi_records
                if emi.payment_status == "Pending"
            )

            pending_dates = sorted([
                emi.due_date
                for emi in emi_records
                if emi.payment_status == "Pending"
            ])

            if pending_dates:
                next_emi_date = pending_dates[0]

        return {

            "total_loans": total_loans,

            "approved_loans": approved_loans,

            "pending_loans": pending_loans,

            "rejected_loans": rejected_loans,

            "paid_emi": paid_emi,

            "pending_emi": pending_emi,

            "outstanding_amount": round(
                outstanding_amount,
                2
            ),

            "next_emi_date": next_emi_date

        }