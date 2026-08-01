"""
==========================================================
Loan Management System

File Name : admin.py

Purpose :
Administrator Routes

Author : Ayan
==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    session,
    flash,
    request
)

from services.admin_service import AdminService
from services.loan_service import LoanService
from services.emi_service import EMIService


# ==========================================================
# Blueprint
# ==========================================================

admin_bp = Blueprint(
    "admin",
    __name__,
    url_prefix="/admin"
)


# ==========================================================
# Admin Login Required
# ==========================================================

def admin_login_required():

    return "admin_id" in session


# ==========================================================
# Dashboard
# ==========================================================

@admin_bp.route("/dashboard")
def dashboard():

    if not admin_login_required():

        return redirect(
            url_for("auth.login")
        )

    statistics = AdminService.dashboard_statistics()

    return render_template(
        "admin/dashboard.html",
        statistics=statistics
    )


# ==========================================================
# Customers
# ==========================================================

@admin_bp.route("/customers")
def customers():

    if not admin_login_required():

        return redirect(
            url_for("auth.login")
        )

    customers = AdminService.get_all_customers()

    return render_template(
        "admin/customers.html",
        customers=customers
    )


# ==========================================================
# Loan Types
# ==========================================================

@admin_bp.route("/loan-types")
def loan_types():

    if not admin_login_required():

        return redirect(
            url_for("auth.login")
        )

    loan_types = AdminService.get_all_loan_types()

    return render_template(
        "admin/loan_types.html",
        loan_types=loan_types
    )


# ==========================================================
# Loan Applications
# ==========================================================

@admin_bp.route("/applications")
def applications():

    if not admin_login_required():

        return redirect(
            url_for("auth.login")
        )

    applications = LoanService.get_all_applications()

    return render_template(
        "admin/applications.html",
        applications=applications
    )


# ==========================================================
# Approve Loan
# ==========================================================

@admin_bp.route(
    "/approve/<int:application_id>",
    methods=["POST"]
)
def approve(application_id):

    if not admin_login_required():

        return redirect(
            url_for("auth.login")
        )

    remarks = request.form.get(
        "remarks",
        ""
    )

    success, message = LoanService.approve_loan(

        application_id,

        session["admin_id"],

        remarks

    )

    if success:

        application = LoanService.get_application(
            application_id
        )

        loan_type = LoanService.get_loan_type(
            application.loan_type_id
        )

        EMIService.generate_schedule(

            application_id,

            float(loan_type.interest_rate)

        )

    flash(

        message,

        "success" if success else "danger"

    )

    return redirect(

        url_for(
            "admin.applications"
        )

    )


# ==========================================================
# Reject Loan
# ==========================================================

@admin_bp.route(
    "/reject/<int:application_id>",
    methods=["POST"]
)
def reject(application_id):

    if not admin_login_required():

        return redirect(
            url_for("auth.login")
        )

    remarks = request.form.get(
        "remarks",
        ""
    )

    success, message = LoanService.reject_loan(

        application_id,

        session["admin_id"],

        remarks

    )

    flash(

        message,

        "success" if success else "danger"

    )

    return redirect(

        url_for(
            "admin.applications"
        )

    )


# ==========================================================
# EMI List
# ==========================================================

@admin_bp.route("/emi")
def emi():

    if not admin_login_required():

        return redirect(
            url_for("auth.login")
        )

    history = EMIService.payment_history()

    return render_template(

        "admin/emi.html",

        history=history

    )