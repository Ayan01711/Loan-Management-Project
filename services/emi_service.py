"""
==========================================================
Loan Management System

File : emi_service.py

Purpose :
EMI Business Logic

Author : Ayan
==========================================================
"""

# ==========================================================
# Import Required Packages
# ==========================================================

from datetime import date
from dateutil.relativedelta import relativedelta

from extensions import db

from models.loan import LoanApplication
from models.payment import (
    EMISchedule,
    Payment
)


class EMIService:
    """
    EMI Service Class
    """

    # ======================================================
    # EMI Calculator
    # ======================================================

    @staticmethod
    def calculate_emi(
        principal,
        annual_interest_rate,
        months
    ):
        """
        Calculate Monthly EMI

        Formula:
        EMI = P * R * (1+R)^N / ((1+R)^N - 1)
        """

        rate = annual_interest_rate / 12 / 100

        if rate == 0:

            return round(principal / months, 2)

        emi = (

            principal *

            rate *

            pow((1 + rate), months)

        ) / (

            pow((1 + rate), months) - 1

        )

        return round(emi, 2)

    # ======================================================
    # Generate EMI Schedule
    # ======================================================

    @staticmethod
    def generate_schedule(
        application_id,
        interest_rate
    ):
        """
        Generates EMI schedule after loan approval.
        """

        application = LoanApplication.query.get(
            application_id
        )

        if application is None:

            return False, "Application Not Found"

        # Prevent duplicate schedule

        existing = EMISchedule.query.filter_by(
            application_id=application_id
        ).first()

        if existing:

            return False, "EMI Already Generated"

        principal = float(
            application.requested_amount
        )

        months = application.duration_months

        emi_amount = EMIService.calculate_emi(
            principal,
            interest_rate,
            months
        )

        remaining = principal

        current_date = date.today()

        monthly_rate = interest_rate / 12 / 100

        for installment in range(1, months + 1):

            interest = remaining * monthly_rate

            principal_amount = emi_amount - interest

            remaining -= principal_amount

            emi = EMISchedule(

                application_id=application_id,

                installment_no=installment,

                due_date=current_date,

                emi_amount=round(emi_amount, 2),

                principal_amount=round(
                    principal_amount,
                    2
                ),

                interest_amount=round(
                    interest,
                    2
                )

            )

            db.session.add(emi)

            current_date = current_date + relativedelta(
                months=1
            )

        db.session.commit()

        return True, "EMI Generated Successfully"

    # ======================================================
    # Customer EMI List
    # ======================================================

    # ======================================================
    # Customer EMI List
    # ======================================================

    @staticmethod
    def get_customer_emi(application_id):
        """
        Returns EMI schedule for an application.
        """

        return (
            EMISchedule.query
            .filter_by(application_id=application_id)
            .order_by(EMISchedule.installment_no)
            .all()
        )

    # ======================================================
    # Get EMI By ID
    # ======================================================

    @staticmethod
    def get_emi_by_id(emi_id):
        """
        Returns single EMI record.
        """

        return EMISchedule.query.get(emi_id)


    # ======================================================
    # Make Payment
    # ======================================================

    @staticmethod
    def pay_emi(
        emi_id,
        payment_mode,
        transaction_id
    ):

        emi = EMISchedule.query.get(emi_id)

        if emi is None:

            return False, "Invalid EMI"

        if emi.payment_status == "Paid":

            return False, "EMI Already Paid"

        payment = Payment(

            emi_id=emi_id,

            payment_amount=emi.emi_amount,

            payment_mode=payment_mode,

            transaction_id=transaction_id,

            payment_date=date.today()

        )

        db.session.add(payment)

        emi.payment_status = "Paid"

        emi.payment_date = date.today()

        db.session.commit()

        return True, "EMI Paid Successfully"

    # ======================================================
    # Payment History
    # ======================================================

    @staticmethod
    def payment_history():

        return Payment.query.order_by(
            Payment.payment_date.desc()
        ).all()

    # ======================================================
    # Customer Payment History
    # ======================================================

    @staticmethod
    def get_payment_history(customer_id):
        """
        Returns payment history of logged in customer.
        """

        return (

            Payment.query

            .join(
                EMISchedule,
                Payment.emi_id == EMISchedule.emi_id
            )

            .join(
                LoanApplication,
                EMISchedule.application_id == LoanApplication.application_id
            )

            .filter(
                LoanApplication.customer_id == customer_id
            )

            .order_by(
                Payment.payment_date.desc()
            )

            .all()

        )
    
    # ======================================================
    # Dashboard
    # ======================================================

    @staticmethod
    def pending_emi():

        return EMISchedule.query.filter_by(
            payment_status="Pending"
        ).count()

    @staticmethod
    def paid_emi():

        return EMISchedule.query.filter_by(
            payment_status="Paid"
        ).count()