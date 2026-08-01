"""
Loan Management System

Validators
"""

import re


def validate_email(email):

    pattern=r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

    return re.match(pattern,email)


def validate_phone(phone):

    return phone.isdigit() and len(phone)==10


def validate_pan(pan):

    pattern=r'^[A-Z]{5}[0-9]{4}[A-Z]$'

    return re.match(pattern,pan)


def validate_aadhaar(aadhaar):

    return aadhaar.isdigit() and len(aadhaar)==12