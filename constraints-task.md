
1.	Create database
2.	Create table accounts
3.	Columns account_no, user_name,bank_name,email,balance,created_on, customer_id
4.	Create table customer details
5.	Customer_id, first_name, last_name, DOB, address
6.	Add column phone_number to customer details and it should accept only 10 numbers, not more than or less than 10 numbers. (apply this on existing table)
7.	Apply default as currenttime on created_on field from accounts table(apply on existing table)
8.	Create a new parent and child table with 5 records in it. Batch B02(python,DE)
9. Display customer_id,bank_name,email,phone_number(use joins)
10. Use without joins

Sometimes while creating table, you are not able to update or delete rows and columns as safe mode is enable. Disable safe mode by:

```
SET SQL_SAFE_UPDATES = 0;
```
