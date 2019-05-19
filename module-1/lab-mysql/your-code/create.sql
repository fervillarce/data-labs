CREATE DATABASE lab_mysql;
USE lab_mysql;
CREATE TABLE cars (car_id INT(10), vin CHAR(17), manufacturer VARCHAR(40), model VARCHAR(20), year INT(4), color VARCHAR(10));
CREATE TABLE invoices (inv_id INT(10), invoice_number INT(20), inv_date DATE, car_id INT(10), c_id INT(10), sp_id INT(10));
CREATE TABLE salespersons (sp_id INT(10), staff_id INT(5), sp_name  VARCHAR(40), store  VARCHAR(20));
CREATE TABLE customers (c_id INT(10), customer_id INT(5), cust_name VARCHAR(40), phone  VARCHAR(18), email VARCHAR(60), address VARCHAR(60), city VARCHAR(20), state_province VARCHAR(20), country VARCHAR(20), zip CHAR(5));