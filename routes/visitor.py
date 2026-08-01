"""
==========================================================
Loan Management System

File Name : visitor.py

Purpose :
Visitor Routes

Handles public pages such as:
- Home
- About
- Contact
- Loan Types

Author : Ayan
==========================================================
"""

# ==========================================================
# Import Required Packages
# ==========================================================

from flask import (
    Blueprint,
    render_template
)

from services.loan_service import LoanService


# ==========================================================
# Blueprint Configuration
# ==========================================================

visitor_bp = Blueprint(
    "visitor",
    __name__
)


# ==========================================================
# Home Page
# ==========================================================

@visitor_bp.route("/")
def home():
    """
    Display Home Page
    """

    loan_types = LoanService.get_all_loan_types()

    return render_template(
        "index.html",
        loan_types=loan_types
    )


# ==========================================================
# Loan Types
# ==========================================================

@visitor_bp.route("/loan-types")
def loan_types():
    """
    Display Available Loan Types
    """

    loan_types = LoanService.get_all_loan_types()

    return render_template(
        "loan_types.html",
        loan_types=loan_types
    )