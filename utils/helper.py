"""
Loan Management System

Helper Functions
"""

from datetime import datetime


def current_datetime():

    return datetime.now()


def format_currency(amount):

    return "₹ {:,.2f}".format(float(amount))