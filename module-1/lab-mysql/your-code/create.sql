CREATE DATABASE IF NOT EXISTS lab_mysql;
USE lab_mysql;
CREATE TABLE cars (car_id NOT NULL AUTO_INCREMENT, vin CHAR(17), manufacturer VARCHAR(40), model VARCHAR(20), year INT(4), color VARCHAR(10), PRIMARY KEY(car_id));
CREATE TABLE invoices (inv_id NOT NULL AUTO_INCREMENT, invoice_number INT(20), inv_date DATE, car_id INT(10), c_id INT(10), sp_id INT(10), PRIMARY KEY(inv_id));
CREATE TABLE salespersons (sp_id NOT NULL AUTO_INCREMENT, staff_id INT(5), sp_name  VARCHAR(40), store  VARCHAR(20), PRIMARY KEY(sp_id));
CREATE TABLE customers (c_id NOT NULL AUTO_INCREMENT, customer_id INT(5), cust_name VARCHAR(40), phone  VARCHAR(18), email VARCHAR(60), address VARCHAR(60), city VARCHAR(20), state_province VARCHAR(20), country VARCHAR(20), zip CHAR(5), PRIMARY KEY(c_id));