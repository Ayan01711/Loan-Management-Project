"""
==========================================================
Loan Management System

File Name : nominee_service.py

Purpose :
Customer Nominee Business Logic

Author : Ayan
==========================================================
"""

# ==========================================================
# Import Required Packages
# ==========================================================

from extensions import db

from models.nominee import Nominee


# ==========================================================
# Nominee Service
# ==========================================================

class NomineeService:
    """
    Handles Customer Nominee Operations.
    """

    # ======================================================
    # Get Nominee
    # ======================================================

    @staticmethod
    def get_nominee(customer_id):
        """
        Returns nominee details of customer.
        """

        return Nominee.query.filter_by(
            customer_id=customer_id
        ).first()

    # ======================================================
    # Save Nominee
    # ======================================================

    @staticmethod
    def save_nominee(data):
        """
        Saves nominee details.
        """

        existing = Nominee.query.filter_by(
            customer_id=data["customer_id"]
        ).first()

        if existing:

            return False, "Nominee already exists."

        nominee = Nominee(

            customer_id=data["customer_id"],

            nominee_name=data[
                "nominee_name"
            ],

            relationship=data[
                "relationship"
            ],

            nominee_phone=data[
                "nominee_phone"
            ],

            nominee_email=data[
                "nominee_email"
            ]

        )

        db.session.add(nominee)

        db.session.commit()

        return True, "Nominee added successfully."

    # ======================================================
    # Update Nominee
    # ======================================================

    @staticmethod
    def update_nominee(
        customer_id,
        data
    ):
        """
        Updates nominee details.
        """

        nominee = Nominee.query.filter_by(
            customer_id=customer_id
        ).first()

        if nominee is None:

            return False, "Nominee not found."

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

        return True, "Nominee updated successfully."

    # ======================================================
    # Delete Nominee
    # ======================================================

    @staticmethod
    def delete_nominee(customer_id):
        """
        Deletes nominee.
        """

        nominee = Nominee.query.filter_by(
            customer_id=customer_id
        ).first()

        if nominee is None:

            return False

        db.session.delete(nominee)

        db.session.commit()

        return True