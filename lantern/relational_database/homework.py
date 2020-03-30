from typing import List
import psycopg2


def task_1_add_new_record_to_db(con) -> str:
    """
    Add a record for a new customer from Singapore
    {
        'customer_name': 'Thomas',
        'contactname': 'David',
        'address': 'Some Address',
        'city': 'London',
        'postalcode': '774',
        'country': 'Singapore',
    }

    Args:
        con: psycopg connection

    Returns: 92 records

    """
    # sql = """
    # INSERT INTO customers (customer_name, contactname, address, city, postalcode, country)
    # VALUES
    # (%(customer_name)s, %(contactname)s, %(address)s, %(city)s, %(postalcode)s, %(country)s),
    # {
    #     'customer_name': 'Thomas',
    #     'contactname': 'David',
    #     'address': 'Some Address',
    #     'city': 'London',
    #     'postalcode': '774',
    #     'country': 'Singapore'
    # }
    # """
    # try:
    #     cur = con.cursor()
    #     cur.execute(sql,)
    #     con.commit()
    #     cur.close()
    # except (Exception, psycopg2.DatabaseError) as error:
    #     print(error)
    # finally:
    #     if con is not None:
    #         con.close()
    sql = """
    INSERT INTO customers (customerid, customername, contactname, address, city, postalcode, country)
    VALUES
    (%s, 'Thomas', 'David', 'Some Address', 'London', '774', 'Singapore') RETURNING customerid;
    """

    cur = con.cursor()
    cur.execute("SELECT * FROM customers WHERE customerid = (SELECT MAX(customerid) FROM customers)")
    vendor_id = cur.fetchone()[0] + 1
    cur.execute(sql, (vendor_id,))
    con.commit()
    return cur.fetchmany(92)


def task_2_list_all_customers(cur) -> list:
    """
    Get all records from table Customers

    Args:
        cur: psycopg cursor

    Returns: 91 records

    """
    sql = """
    SELECT * FROM customers
    """
    cur.execute(sql)
    return cur.fetchmany(91)


def task_3_list_customers_in_germany(cur) -> list:
    """
    List the customers in Germany

    Args:
        cur: psycopg cursor

    Returns: 11 records
    """
    sql = """
    SELECT * FROM customers WHERE country = 'Germany'
    """
    cur.execute(sql)
    return cur.fetchmany(11)


def task_4_update_customer(con):
    """
    Update first customer's name (Set customername equal to  'Johnny Depp')
    Args:
        con: psycopg connection

    Returns: 91 records with updated customer

    """
    sql = """
    UPDATE customers SET customername = 'Johnny Depp' 
    WHERE customerid = (SELECT MIN(customerid) FROM customers)
    """
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    cur.execute("SELECT * FROM customers")
    return cur.fetchmany(91)


def task_5_delete_the_last_customer(con) -> None:
    """
    Delete the last customer

    Args:
        con: psycopg connection
    """
    sql = """
    DELETE FROM customers WHERE customerid = (SELECT MAX(customerid) FROM customers)
    """
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    return


def task_6_list_all_supplier_countries(cur) -> list:
    """
    List all supplier countries

    Args:
        cur: psycopg cursor

    Returns: 29 records

    """
    sql = """
    SELECT country FROM suppliers 
    """
    cur.execute(sql)
    return cur.fetchmany(29)

def task_7_list_supplier_countries_in_desc_order(cur) -> list:
    """
    List all supplier countries in descending order

    Args:
        cur: psycopg cursor

    Returns: 29 records in descending order

    """
    sql = """
    SELECT country FROM suppliers ORDER BY country DESC
    """
    cur.execute(sql)
    return cur.fetchmany(29)


def task_8_count_customers_by_city(cur):
    """
    List the number of customers in each city

    Args:
        cur: psycopg cursor

    Returns: 69 records in descending order
    Can been error due to difficalties with JSON
    """
    sql = """
    SELECT COUNT(customername), city FROM customers GROUP BY city ORDER BY city DESC
    """
    cur.execute(sql)

    return cur.fetchmany(69)


def task_9_count_customers_by_country_with_than_10_customers(cur):
    """
    List the number of customers in each country. Only include countries with more than 10 customers.

    Args:
        cur: psycopg cursor

    Returns: 3 records

    """
    sql = """
    SELECT COUNT(customername), country FROM customers GROUP BY country ORDER BY COUNT(customername) DESC, country
    """
    cur.execute(sql)
    return cur.fetchmany(3)

def task_10_list_first_10_customers(cur):
    """
    List first 10 customers from the table

    Results: 10 records
    """
    sql = """
    SELECT * FROM customers
    """
    cur.execute(sql)
    return cur.fetchmany(10)


def task_11_list_customers_starting_from_11th(cur):
    """
    List all customers starting from 11th record

    Args:
        cur: psycopg cursor

    Returns: 11 records
    """
    sql = """
    SELECT * FROM customers WHERE customerid > 11
    """
    cur.execute(sql)
    return cur.fetchall()


def task_12_list_suppliers_from_specified_countries(cur):
    """
    List all suppliers from the USA, UK, OR Japan

    Args:
        cur: psycopg cursor

    Returns: 8 records
    """
    sql = """
    SELECT supplierid, suppliername, contactname, city, country FROM suppliers WHERE Country = 'USA' or Country = 'UK' or Country = 'Japan'
    """
    cur.execute(sql)
    return cur.fetchall()


def task_13_list_products_from_sweden_suppliers(cur):
    """
    List products with suppliers from Sweden.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """
    sql = """
    SELECT products.productname FROM products, suppliers WHERE Country = 'Sweden' and  products.supplierid = suppliers.supplierid
    """
    cur.execute(sql)
    return cur.fetchmany(3)


def task_14_list_products_with_supplier_information(cur):
    """
    List all products with supplier information

    Args:
        cur: psycopg cursor

    Returns: 77 records
    ERROR CAN BEEN DUE TO NOT CORRECT DB LOCALE LC_MONETARY SETUP
    """
    sql = """
    SELECT products.productid, products.productname, products.unit, products.price, suppliers.country, suppliers.city, suppliers.suppliername 
    FROM products, suppliers WHERE products.supplierid = suppliers.supplierid
    """
    cur.execute(sql)
    return cur.fetchmany(77)


def task_15_list_customers_with_any_order_or_not(cur):
    """
    List all customers, whether they placed any order or not.

    Args:
        cur: psycopg cursor

    Returns: 213 records
      {
    "customername": "Wilman Kala",
    "contactname": "Matti Karttunen",
    "country": "Finland",
    "orderid": 1
  }
    """
    sql = """
    SELECT customers.customername, customers.contactname, customers.country, orders.orderid
    FROM customers, orders WHERE  customers.customerid = orders.customerid
    """
    cur.execute(sql)
    return cur.fetchmany(77)



def task_16_match_all_customers_and_suppliers_by_country(cur):
    """
    Match all customers and suppliers by country

    Args:
        cur: psycopg cursor

    Returns: 194 records
    """
    sql = """
    SELECT customername, customers.address as address, customers.country as customercountry, 
    suppliers.country as suppliercountry, suppliers.suppliername 
    FROM customers FULL JOIN suppliers ON customers.country = suppliers.country ORDER BY customercountry, suppliercountry
    """
    cur.execute(sql)
    return cur.fetchmany(194)
