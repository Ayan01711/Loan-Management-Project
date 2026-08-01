@echo off
title Loan Management System - Project Structure Creator
color 0A

echo =====================================================
echo        LOAN MANAGEMENT SYSTEM PROJECT SETUP
echo =====================================================
echo.

echo Creating Project Structure...

:: Root Directories
mkdir database
mkdir models
mkdir routes
mkdir services
mkdir templates
mkdir static
mkdir uploads
mkdir utils
mkdir docs

:: Template Directories
mkdir templates\admin
mkdir templates\customer

:: Static Directories
mkdir static\css
mkdir static\js
mkdir static\images

:: Root Files
type nul > app.py
type nul > config.py
type nul > extensions.py
type nul > requirements.txt
type nul > run.bat
type nul > README.md

:: Database
type nul > database\database.sql

:: Models
type nul > models\__init__.py
type nul > models\admin.py
type nul > models\customer.py
type nul > models\loan.py
type nul > models\payment.py

:: Routes
type nul > routes\__init__.py
type nul > routes\auth.py
type nul > routes\visitor.py
type nul > routes\customer.py
type nul > routes\admin.py

:: Services
type nul > services\__init__.py
type nul > services\auth_service.py
type nul > services\customer_service.py
type nul > services\loan_service.py
type nul > services\admin_service.py
type nul > services\emi_service.py

:: Templates
type nul > templates\layout.html
type nul > templates\index.html
type nul > templates\login.html
type nul > templates\register.html

:: Customer Templates
type nul > templates\customer\dashboard.html
type nul > templates\customer\profile.html
type nul > templates\customer\apply_loan.html
type nul > templates\customer\loan_status.html
type nul > templates\customer\emi.html
type nul > templates\customer\payments.html

:: Admin Templates
type nul > templates\admin\dashboard.html
type nul > templates\admin\customers.html
type nul > templates\admin\loan_types.html
type nul > templates\admin\applications.html
type nul > templates\admin\approve_loan.html
type nul > templates\admin\emi.html

:: Static Files
type nul > static\css\style.css
type nul > static\js\script.js

:: Utilities
type nul > utils\helper.py
type nul > utils\validators.py

echo.
echo =====================================================
echo Project Structure Created Successfully
echo =====================================================
echo.
pause