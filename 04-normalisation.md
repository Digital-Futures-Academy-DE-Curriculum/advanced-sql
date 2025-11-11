# ![Digital Futures](https://github.com/digital-futures-academy/DataScienceMasterResources/blob/main/Resources/datascience-notebook-header.png?raw=true)

## Learner Stories

```txt
As a DATA PROFESSIONAL,  
I want to be able to design normalised database schemas,  
so that I can ensure data consistency and avoid redundancy

As a DATA PROFESSIONAL,  
I want to be able to create and manage primary and foreign key relationships,  
so that I can ensure data integrity across tables
```

## What is Normalisation?

Normalisation is the process of organising data in a database to reduce redundancy and improve data integrity. This involves creating tables and establishing relationships between them according to certain rules designed both to protect the data and to make the database more flexible by eliminating redundancy and inconsistent dependency.

---

## Why Normalise?

- **Data Consistency**:
  - Normalisation helps to ensure that data is consistent across the database. This is important because inconsistencies can lead to errors and make it difficult to maintain and update the database.
- **Avoid Redundancy**:
  - Normalisation helps to avoid redundancy by breaking down data into smaller, more manageable pieces. This can help to reduce the amount of storage space required and improve the performance of the database.
- **Data Integrity**:
  - Normalisation helps to maintain data integrity by enforcing constraints on the data. This can help to prevent errors and ensure that the data is accurate and reliable.
- **Flexibility**:
  - Normalisation makes it easier to modify the database structure and add new data without having to make extensive changes to the existing data. This can help to make the database more flexible and adaptable to changing requirements.
- **Efficiency**:
  - Normalisation can improve the efficiency of the database by reducing the amount of redundant data and making it easier to retrieve and update data. This can help to improve the performance of the database and reduce the time required to process queries.
- **Scalability**:
  - Normalisation can help to improve the scalability of the database by making it easier to add new data and expand the database as needed. This can help to ensure that the database can grow with the needs of the organisation and handle increasing amounts of data.
- **Data Quality**:
  - Normalisation can help to improve the quality of the data by reducing errors and inconsistencies. This can help to ensure that the data is accurate and reliable and can be used effectively for decision-making and analysis.
- **Data Security**:
  - Normalisation can help to improve data security by reducing the risk of data loss or corruption. This can help to protect the data from unauthorised access or modification and ensure that it is stored and managed securely.
- **Data Modelling**:
  - Normalisation can help to improve data modelling by providing a clear and consistent structure for the database. This can help to make it easier to understand and work with the data and ensure that it is well-organised and easy to manage.
- **Data Analysis**:
  - Normalisation can help to improve data analysis by providing a more structured and consistent view of the data. This can help to make it easier to analyse and interpret the data and identify patterns and trends that can be used to make informed decisions.
- **Data Integration**:
  - Normalisation can help to improve data integration by providing a common structure for the data that can be shared and used across different systems and applications. This can help to ensure that the data is consistent and accurate and can be easily exchanged and integrated with other data sources.
- **Data Governance**:
  - Normalisation can help to improve data governance by providing a clear and consistent framework for managing and controlling the data. This can help to ensure that the data is well-managed and protected and that it complies with relevant regulations and standards.
- **Data Compliance**:
  - Normalisation can help to improve data compliance by ensuring that the data is stored and managed in a way that complies with relevant regulations and standards. This can help to reduce the risk of non-compliance and ensure that the data is handled in a legal and ethical manner.
- **Data Privacy**:
  - Normalisation can help to improve data privacy by reducing the risk of unauthorised access or disclosure of sensitive information. This can help to protect the privacy and confidentiality of the data and ensure that it is handled securely and responsibly.

---

## When would Normalisation be used?

Normalisation is typically used in the following scenarios:

- **Database Design**:
  - Normalisation is used during the design phase of a database to create an efficient and well-organised structure for storing and managing data. This can help to ensure that the database is easy to use and maintain and that the data is consistent and reliable.
- **Data Modelling**:
  - Normalisation is used in data modelling to create a clear and consistent representation of the data that can be used to analyse and interpret the data. This can help to ensure that the data is well-organised and easy to work with and that it can be used effectively for decision-making and analysis.
- **Data Integration**:
  - Normalisation is used in data integration to provide a common structure for the data that can be shared and used across different systems and applications. This can help to ensure that the data is consistent and accurate and can be easily exchanged and integrated with other data sources.
- **Data Transformation**:
  - Normalisation is used in data transformation to convert data from one format to another and ensure that it is well-organised and easy to work with. This can help to ensure that the data is accurate and reliable and can be used effectively for analysis and reporting.

---

## How is Normalisation achieved?

Normalisation is achieved by following a set of rules known as normal forms. There are several normal forms, each with its own set of rules and requirements. The most common normal forms are:

- **First Normal Form (1NF)**:
  - In 1NF, each table must have a primary key and all columns must be atomic (indivisible). This means that each column must contain a single value and cannot be further divided.
- **Second Normal Form (2NF)**:
  - In 2NF, a table must be in 1NF and all non-key attributes must be fully functionally dependent on the primary key. This means that each non-key attribute must be dependent on the entire primary key, not just part of it.
- **Third Normal Form (3NF)**:
  - In 3NF, a table must be in 2NF and all non-key attributes must be dependent only on the primary key. This means that each non-key attribute must be dependent on the primary key and not on other non-key
- **Boyce-Codd Normal Form (BCNF)**:
  - BCNF is a stricter form of 3NF that requires that every determinant be a candidate key. This means that there are no non-trivial functional dependencies between candidate keys.

> **Note**: There are additional normal forms beyond BCNF, such as Fourth Normal Form (4NF), Fifth Normal Form (5NF), and Domain-Key Normal Form (DKNF), but these are less commonly used in practice.

---

> Data should be dependent on the primary key, the whole primary key, and nothing but the primary key, so help me Codd!

---

## Normalisation Example

### Denormalised Dataset

Let's start with the following denormalized dataset:

| OrderID | CustomerName | CustomerAddress | ProductName | Quantity | Price | OrderDate  |
|---------|--------------|-----------------|-------------|----------|-------|------------|
| 1       | Alice        | 123 Maple St    | Widget A    | 2        | 10.00 | 2023-01-01 |
| 2       | Bob          | 456 Oak St      | Widget B    | 1        | 20.00 | 2023-01-02 |
| 3       | Alice        | 123 Maple St    | Widget C    | 1        | 30.00 | 2023-01-03 |
| 4       | Charlie      | 789 Pine St     | Widget A    | 3        | 10.00 | 2023-01-04 |

***NOTE***: In this dataset, `Price` relates to the price of a single produce, and `Quantity` relates to the number of that product ordered.  No totals are stored as they can be calculated on demand.

---

### Step-by-Step Normalisation

#### Step 1: First Normal Form (1NF)

**Requirement**: Eliminate repeating groups and ensure each column contains atomic values.

**1NF Table**:

<details>
| OrderID | CustomerName | CustomerAddress | ProductName | Quantity | Price | OrderDate  |
|---------|--------------|-----------------|-------------|----------|-------|------------|
| 1       | Alice        | 123 Maple St    | Widget A    | 2        | 10.00 | 2023-01-01 |
| 2       | Bob          | 456 Oak St      | Widget B    | 1        | 20.00 | 2023-01-02 |
| 3       | Alice        | 123 Maple St    | Widget C    | 1        | 30.00 | 2023-01-03 |
| 4       | Charlie      | 789 Pine St     | Widget A    | 3        | 10.00 | 2023-01-04 |

In this table, each column contains atomic values, and there are no repeating groups. However, there is redundancy in the CustomerName and CustomerAddress columns. To eliminate this redundancy, we need to move the customer information to a separate table.

</details>

---

#### Step 2: Second Normal Form (2NF)

**Requirement**: Ensure the table is in 1NF and move partial dependencies to separate tables.

**2NF Tables**:

<details>
**Orders Table**:

| OrderID | CustomerID | OrderDate  |
|---------|------------|------------|
| 1       | 1          | 2023-01-01 |
| 2       | 2          | 2023-01-02 |
| 3       | 1          | 2023-01-03 |
| 4       | 3          | 2023-01-04 |

The Orders table now contains only the OrderID, CustomerID, and OrderDate columns. OrderID is the primary key, and CustomerID is a foreign key that references the Customers table.  This table is now abstracted from any customer information and is anonymised unless you have access to the Customers table.

**Customers Table**:

| CustomerID | CustomerName | CustomerAddress |
|------------|--------------|-----------------|
| 1          | Alice        | 123 Maple St    |
| 2          | Bob          | 456 Oak St      |
| 3          | Charlie      | 789 Pine St     |

The Customers table contains the CustomerID, CustomerName, and CustomerAddress columns. CustomerID is the primary key, and it is referenced by the CustomerID column in the Orders table.  This data is now abstracted from any orders as a stand-alone table.

**OrderDetails Table**:

| OrderID | ProductID | Quantity |
|---------|-----------|----------|
| 1       | 1         | 2        |
| 2       | 2         | 1        |
| 3       | 3         | 1        |
| 4       | 1         | 3        |

The OrderDetails table contains the OrderID, ProductID, and Quantity columns. OrderID and ProductID together form the composite primary key for this table. ProductID is a foreign key that references the Products table.  The totals for each order line and product are not stored as they can be calculated on demand.  There is no direct relationship between the OrderDetails and the customer information, as the Orders table acts as a bridge between them.

**Products Table**:

| ProductID | ProductName | Price |
|-----------|-------------|-------|
| 1         | Widget A    | 10.00 |
| 2         | Widget B    | 20.00 |
| 3         | Widget C    | 30.00 |

</details>
---

#### Step 3: Third Normal Form (3NF)

**Requirement**: Ensure the table is in 2NF and remove transitive dependencies.

**3NF Tables**:

The tables from 2NF are already in 3NF as there are no transitive dependencies.

---

---

## Normalisation Practice

Now, it's your turn to practice normalisation. Here is a denormalized dataset for you to normalize to 3NF:

| InvoiceID | CustomerName | CustomerEmail       | ProductName | Quantity | UnitPrice | InvoiceDate |
|-----------|--------------|---------------------|-------------|----------|-----------|-------------|
| 101       | Dave         | <dave@example.com>  | Gadget X    | 1        | 50.00     | 2023-02-01  |
| 102       | Eve          | <eve@example.com>   | Gadget Y    | 2        | 75.00     | 2023-02-02  |
| 103       | Dave         | <dave@example.com>  | Gadget Z    | 1        | 50.00     | 2023-02-03  |
| 104       | Frank        | <frank@example.com> | Gadget X    | 3        | 100.00    | 2023-02-04  |

### Instructions

1. **First Normal Form (1NF)**: Ensure each column contains atomic values and eliminate repeating groups.
2. **Second Normal Form (2NF)**: Ensure the table is in 1NF and move partial dependencies to separate tables.
3. **Third Normal Form (3NF)**: Ensure the table is in 2NF and remove transitive dependencies.

---

### Add your Normalised Tables here

---

### Potential Solution

Here is a potential solution for the practice dataset:

**Invoices Table**:

<details>
| InvoiceID | CustomerID | InvoiceDate |
|-----------|------------|-------------|
| 101       | 1          | 2023-02-01  |
| 102       | 2          | 2023-02-02  |
| 103       | 1          | 2023-02-03  |
| 104       | 3          | 2023-02-04  |

</details>

**Customers Table**:

<details>
| CustomerID | CustomerName | CustomerEmail        |
|------------|--------------|----------------------|
| 1          | Dave         | <dave@example.com>   |
| 2          | Eve          | <eve@example.com>    |
| 3          | Frank        | <frank@example.com>  |
</details>

**InvoiceDetails Table**:

<details>
| InvoiceID | ProductID | Quantity |
|-----------|-----------|----------|
| 101       | 1         | 1        |
| 102       | 2         | 2        |
| 103       | 3         | 1        |
| 104       | 1         | 3        |
</details>

**Products Table**:

<details>
| ProductID | ProductName | UnitPrice |
|-----------|-------------|-----------|
| 1         | Gadget X    | 50.00     |
| 2         | Gadget Y    | 75.00     |
| 3         | Gadget Z    | 100.00    |
</details>

---

### Conclusion

In this workshop, we learned about data normalisation and stepped through the process of normalizing a dataset to the third normal form (3NF). You also had the opportunity to practice normalisation on a different dataset. Normalisation helps reduce redundancy and improve data integrity in your database designs.

Feel free to ask any questions or seek clarification on any of the steps!

---

---
