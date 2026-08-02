/*
==========================================================
Loan Management System
Database : loan_management

Author : Ayan

Purpose :
Creates all required database tables.

==========================================================
*/

-- ========================================================
-- Create Database
-- ========================================================

DROP DATABASE IF EXISTS loan_management;

CREATE DATABASE loan_management;

USE loan_management;

-- ========================================================
-- Admin Table
-- ========================================================

CREATE TABLE admins(

    admin_id INT AUTO_INCREMENT PRIMARY KEY,

    username VARCHAR(50) NOT NULL UNIQUE,

    password VARCHAR(255) NOT NULL,

    full_name VARCHAR(100) NOT NULL,

    email VARCHAR(100),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

INSERT INTO admins
(
username,
password,
full_name,
email
)

VALUES
(
'admin',
'admin123',
'System Administrator',
'admin@loan.com'
);

-- ========================================================
-- Customer Table
-- ========================================================

CREATE TABLE customers(

    customer_id INT AUTO_INCREMENT PRIMARY KEY,

    full_name VARCHAR(100) NOT NULL,

    email VARCHAR(100) UNIQUE NOT NULL,

    phone VARCHAR(20) UNIQUE NOT NULL,

    password VARCHAR(255) NOT NULL,

    gender ENUM('Male','Female','Other'),

    dob DATE,

    address TEXT,

    city VARCHAR(50),

    state VARCHAR(50),

    pincode VARCHAR(10),

    aadhaar_number VARCHAR(20),

    pan_number VARCHAR(20),

    occupation VARCHAR(100),

    monthly_income DECIMAL(12,2),

    status ENUM('Active','Inactive')
    DEFAULT 'Active',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

-- ========================================================
-- Customer Bank Accounts
-- ========================================================

CREATE TABLE customer_bank_accounts(

    bank_account_id INT AUTO_INCREMENT PRIMARY KEY,

    customer_id INT NOT NULL UNIQUE,

    bank_name VARCHAR(100) NOT NULL,

    account_holder_name VARCHAR(100) NOT NULL,

    account_number VARCHAR(25) NOT NULL UNIQUE,

    ifsc_code VARCHAR(11) NOT NULL,

    branch_name VARCHAR(100),

    account_type ENUM(
        'Savings',
        'Current'
    ) DEFAULT 'Savings',


    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

FOREIGN KEY(customer_id)
REFERENCES customers(customer_id)
ON DELETE CASCADE

);

-- ========================================================
-- Customer Nominees
-- ========================================================

CREATE TABLE customer_nominees(

    nominee_id INT AUTO_INCREMENT PRIMARY KEY,

    customer_id INT NOT NULL UNIQUE,

    nominee_name VARCHAR(100) NOT NULL,

    relationship ENUM(

        'Father',
        'Mother',
        'Brother',
        'Sister',
        'Spouse',
        'Son',
        'Daughter',
        'Other'

    ) NOT NULL,

    nominee_phone VARCHAR(20),
    nominee_email VARCHAR(100),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

FOREIGN KEY(customer_id)
REFERENCES customers(customer_id)
ON DELETE CASCADE

);


-- ========================================================
-- Loan Types
-- ========================================================

CREATE TABLE loan_types(

    loan_type_id INT AUTO_INCREMENT PRIMARY KEY,

    loan_name VARCHAR(100) NOT NULL,

    interest_rate DECIMAL(5,2) NOT NULL,

    processing_fee DECIMAL(10,2),

    minimum_amount DECIMAL(12,2),

    maximum_amount DECIMAL(12,2),

    maximum_years INT,

    status ENUM('Active','Inactive')
    DEFAULT 'Active'

);

INSERT INTO loan_types
(
loan_name,
interest_rate,
processing_fee,
minimum_amount,
maximum_amount,
maximum_years
)

VALUES

('Personal Loan',10.50,1000,10000,500000,5),

('Home Loan',8.25,5000,500000,10000000,30),

('Vehicle Loan',9.50,2500,50000,2000000,7),

('Education Loan',7.25,1000,25000,3000000,10);

-- ========================================================
-- Loan Applications
-- ========================================================

CREATE TABLE loan_applications(

    application_id INT AUTO_INCREMENT PRIMARY KEY,

    customer_id INT NOT NULL,

    loan_type_id INT NOT NULL,

    requested_amount DECIMAL(12,2) NOT NULL,

    duration_months INT NOT NULL,

    purpose TEXT,

    application_status
    ENUM(
    'Pending',
    'Approved',
    'Rejected'
    )
    DEFAULT 'Pending',

    remarks TEXT,

    application_date TIMESTAMP
    DEFAULT CURRENT_TIMESTAMP,

    approved_by INT,

    approval_date DATETIME,

    FOREIGN KEY(customer_id)
    REFERENCES customers(customer_id),

    FOREIGN KEY(loan_type_id)
    REFERENCES loan_types(loan_type_id),

    FOREIGN KEY(approved_by)
    REFERENCES admins(admin_id)

);

-- ========================================================
-- EMI Schedule
-- ========================================================

CREATE TABLE emi_schedule(

    emi_id INT AUTO_INCREMENT PRIMARY KEY,

    application_id INT,

    installment_no INT,

    due_date DATE,

    emi_amount DECIMAL(12,2),

    principal_amount DECIMAL(12,2),

    interest_amount DECIMAL(12,2),

    payment_status
    ENUM(
    'Pending',
    'Paid'
    )
    DEFAULT 'Pending',

    payment_date DATE,

    FOREIGN KEY(application_id)
    REFERENCES loan_applications(application_id)

);

-- ========================================================
-- Payments
-- ========================================================

CREATE TABLE payments(

    payment_id INT AUTO_INCREMENT PRIMARY KEY,

    emi_id INT,

    payment_amount DECIMAL(12,2),

    payment_mode
    ENUM(
    'Cash',
    'UPI',
    'Card',
    'Net Banking'
    ),

    transaction_id VARCHAR(100),

    payment_date TIMESTAMP
    DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(emi_id)
    REFERENCES emi_schedule(emi_id)

);

-- ========================================================
-- Contact Messages
-- ========================================================

CREATE TABLE contact_messages(

    message_id INT AUTO_INCREMENT PRIMARY KEY,

    name VARCHAR(100),

    email VARCHAR(100),

    subject VARCHAR(150),

    message TEXT,

    submitted_at TIMESTAMP
    DEFAULT CURRENT_TIMESTAMP

);