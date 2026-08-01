"""
==========================================================
Loan Management System

File Name : customer.py

Purpose :
Customer Routes

Author : Ayan
==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash
)

from services.customer_service import CustomerService
from services.loan_service import LoanService

# ==========================================================
# Blueprint
# ==========================================================

customer_bp = Blueprint(
    "customer",
    __name__,
    url_prefix="/customer"
)


# ==========================================================
# Login Required
# ==========================================================

def login_required():

    if "customer_id" not in session:

        return False

    return True


# ==========================================================
# Dashboard
# ==========================================================

@customer_bp.route("/dashboard")
def dashboard():

    if not login_required():

        return redirect(
            url_for("auth.login")
        )

    customer = CustomerService.get_customer(
        session["customer_id"]
    )

    loans = LoanService.get_customer_applications(
        session["customer_id"]
    )

    return render_template(
        "customer/dashboard.html",
        customer=customer,
        loans=loans
    )


# ==========================================================
# Profile
# ==========================================================

@customer_bp.route("/profile")
def profile():

    if not login_required():

        return redirect(
            url_for("auth.login")
        )

    customer = CustomerService.get_customer(
        session["customer_id"]
    )

    return render_template(
        "customer/profile.html",
        customer=customer
    )


# ==========================================================
# Update Profile
# ==========================================================

@customer_bp.route(
    "/update-profile",
    methods=["POST"]
)
def update_profile():

    if not login_required():

        return redirect(
            url_for("auth.login")
        )

    data = {

        "full_name": request.form.get("full_name"),

        "phone": request.form.get("phone"),

        "gender": request.form.get("gender"),

        "dob": request.form.get("dob"),

        "address": request.form.get("address"),

        "city": request.form.get("city"),

        "state": request.form.get("state"),

        "pincode": request.form.get("pincode"),

        "aadhaar_number": request.form.get(
            "aadhaar_number"
        ),

        "pan_number": request.form.get(
            "pan_number"
        ),

        "occupation": request.form.get(
            "occupation"
        ),

        "monthly_income": request.form.get(
            "monthly_income"
        )

    }

    success, message = CustomerService.update_customer(

        session["customer_id"],

        data

    )

    flash(

        message,

        "success" if success else "danger"

    )

    return redirect(

        url_for(
            "customer.profile"
        )

    )


# ==========================================================
# Apply Loan
# ==========================================================

@customer_bp.route(
    "/apply-loan",
    methods=["GET", "POST"]
)
def apply_loan():

    if not login_required():

        return redirect(
            url_for("auth.login")
        )

    if request.method == "POST":

        data = {

            "customer_id":
                session["customer_id"],

            "loan_type_id":
                request.form.get("loan_type_id"),

            "requested_amount":
                request.form.get("requested_amount"),

            "duration_months":
                request.form.get("duration_months"),

            "purpose":
                request.form.get("purpose")

        }

        success, message = LoanService.apply_loan(
            data
        )

        flash(

            message,

            "success" if success else "danger"

        )

        return redirect(

            url_for(
                "customer.loan_status"
            )

        )

    loan_types = LoanService.get_all_loan_types()

    return render_template(

        "customer/apply_loan.html",

        loan_types=loan_types

    )


# ==========================================================
# Loan Status
# ==========================================================

@customer_bp.route("/loan-status")
def loan_status():

    if not login_required():

        return redirect(

            url_for("auth.login")

        )

    loans = LoanService.get_customer_applications(

        session["customer_id"]

    )

    return render_template(

        "customer/loan_status.html",

        loans=loans

    )


# ==========================================================
# EMI Schedule
# ==========================================================

@customer_bp.route("/emi/<int:application_id>")
def emi(application_id):

    if not login_required():

        return redirect(

            url_for("auth.login")

        )

    from services.emi_service import EMIService

    emi_list = EMIService.get_customer_emi(
        application_id
    )

    return render_template(

        "customer/emi.html",

        emi_list=emi_list

    )