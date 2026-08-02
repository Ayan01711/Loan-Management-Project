"""
==========================================================
Loan Management System

File Name : auth.py

Purpose :
Authentication Routes

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
    flash,
    session
)

from services.auth_service import AuthService

# ==========================================================
# Blueprint
# ==========================================================

auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth"
)


# ==========================================================
# Register Customer
# ==========================================================

@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        data = {

    # ----------------------------------
    # Customer Details
    # ----------------------------------

    "full_name": request.form.get("full_name"),

    "email": request.form.get("email"),

    "phone": request.form.get("phone"),

    "password": request.form.get("password"),

    "gender": request.form.get("gender"),

    "dob": request.form.get("dob"),

    "address": request.form.get("address"),

    "city": request.form.get("city"),

    "state": request.form.get("state"),

    "pincode": request.form.get("pincode"),

    "aadhaar_number": request.form.get("aadhaar_number"),

    "pan_number": request.form.get("pan_number"),

    "occupation": request.form.get("occupation"),

    "monthly_income": request.form.get("monthly_income"),

    # ----------------------------------
    # Bank Details
    # ----------------------------------

    "bank_name": request.form.get("bank_name"),

    "account_holder_name": request.form.get(
        "account_holder_name"
    ),

    "account_number": request.form.get(
        "account_number"
    ),

    "ifsc_code": request.form.get(
        "ifsc_code"
    ),

    "branch_name": request.form.get(
        "branch_name"
    ),

    "account_type": request.form.get(
        "account_type"
    ),

    # ----------------------------------
    # Nominee Details
    # ----------------------------------

    "nominee_name": request.form.get(
        "nominee_name"
    ),

    "relationship": request.form.get(
        "relationship"
    ),

    "nominee_phone": request.form.get(
        "nominee_phone"
    ),

    "nominee_email": request.form.get(
        "nominee_email"
    )

}

        success, message = AuthService.register_customer(
            data
        )

        if success:

            flash(
                message,
                "success"
            )

            return redirect(
                url_for("auth.login")
            )

        flash(
            message,
            "danger"
        )

    return render_template(
        "register.html"
    )


# ==========================================================
# Login
# ==========================================================

@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        login_type = request.form.get("login_type")

        # -----------------------------
        # Customer Login
        # -----------------------------

        if login_type == "customer":

            email = request.form.get("email")

            password = request.form.get("password")

            success, result = AuthService.customer_login(
                email,
                password
            )

            if success:

                session["customer_id"] = result.customer_id

                session["customer_name"] = result.full_name

                flash(
                    "Login Successful",
                    "success"
                )

                return redirect(
                    url_for(
                        "customer.dashboard"
                    )
                )

            flash(
                result,
                "danger"
            )

        # -----------------------------
        # Admin Login
        # -----------------------------

        elif login_type == "admin":

            username = request.form.get("username")

            password = request.form.get("password")

            success, result = AuthService.admin_login(
                username,
                password
            )

            if success:

                session["admin_id"] = result.admin_id

                session["admin_name"] = result.username

                flash(
                    "Welcome Administrator",
                    "success"
                )

                return redirect(
                    url_for(
                        "admin.dashboard"
                    )
                )

            flash(
                result,
                "danger"
            )

    return render_template(
        "login.html"
    )


# ==========================================================
# Logout
# ==========================================================

@auth_bp.route("/logout")
def logout():

    session.clear()

    flash(
        "Logged Out Successfully.",
        "info"
    )

    return redirect(
        url_for(
            "visitor.home"
        )
    )