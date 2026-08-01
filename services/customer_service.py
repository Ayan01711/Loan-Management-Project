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
        Update customer profile
        """

        customer = Customer.query.get(customer_id)

        if customer is None:
            return False, "Customer not found."

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