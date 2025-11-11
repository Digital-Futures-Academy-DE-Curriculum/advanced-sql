import sqlite3
import pandas as pd

# ===== DATABASE SETUP =====
# This mimics your original table structure
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Create the employees table (same structure as your example)
cursor.execute('''
CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY,
    name TEXT,
    manager_id INTEGER
)
''')

# Insert the exact data from your example
employees = [
    (1, 'Alice', None),   # CEO - no manager (this is our "anchor" row)
    (2, 'Bob', 1),        # Reports to Alice
    (3, 'Charlie', 1),    # Reports to Alice  
    (4, 'David', 2),      # Reports to Bob
    (5, 'Eve', 2),        # Reports to Bob
    (6, 'Frank', 3),      # Reports to Charlie
    (7, 'Grace', 4),      # Reports to David
]

cursor.executemany('INSERT INTO employees (employee_id, name, manager_id) VALUES (?, ?, ?)', employees)

print("=== ORIGINAL DATA ===")
# Show the complete table that the CTE will traverse
original_data = pd.read_sql("SELECT * FROM employees ORDER BY employee_id", conn)
print(original_data)

print("\n=== STEP 1: Base Case (Anchor) ===")
print("This is the FIRST part of your CTE - the non-recursive anchor query")
print("It finds employees with no manager (WHERE manager_id IS NULL)")
base_query = """
SELECT employee_id, manager_id, 1 as level
FROM employees
WHERE manager_id IS NULL
"""
base_result = pd.read_sql(base_query, conn)
print(base_result)
print("→ This gives us the starting point for recursion (Alice, the CEO)")

print("\n=== STEP 2: First Recursion ===")
print("This simulates the FIRST iteration of the recursive part")
print("It finds employees whose manager_id matches employee_id from Step 1 (Alice=1)")
first_recursion = """
SELECT e.employee_id, e.manager_id, 2 as level
FROM employees e
WHERE e.manager_id IN (1)
"""
first_result = pd.read_sql(first_recursion, conn)
print(first_result)
print("→ This finds Alice's direct reports (Bob and Charlie)")

print("\n=== STEP 3: Second Recursion ===")
print("This simulates the SECOND iteration of the recursive part")
print("It finds employees whose manager_id matches employee_ids from Step 2 (Bob=2, Charlie=3)")
second_recursion = """
SELECT e.employee_id, e.manager_id, 3 as level
FROM employees e
WHERE e.manager_id IN (2, 3)
"""
second_result = pd.read_sql(second_recursion, conn)
print(second_result)
print("→ This finds reports of Bob (David, Eve) and Charlie (Frank)")

print("\n=== STEP 4: Third Recursion ===")
print("This simulates the THIRD iteration of the recursive part")
print("It finds employees whose manager_id matches employee_ids from Step 3 (David=4, Eve=5, Frank=6)")
third_recursion = """
SELECT e.employee_id, e.manager_id, 4 as level
FROM employees e
WHERE e.manager_id IN (4, 5, 6)
"""
third_result = pd.read_sql(third_recursion, conn)
print(third_result)
print("→ This finds David's report (Grace). Eve and Frank have no reports.")

print("\n=== FINAL RESULT: Complete Hierarchy ===")
print("This is what your original recursive CTE produces automatically")
print("It combines the anchor (Step 1) with all recursive iterations (Steps 2-4) using UNION ALL")
final_query = """
WITH RECURSIVE employee_hierarchy AS (
    -- ANCHOR: Same as Step 1
    SELECT employee_id, manager_id, 1 as level
    FROM employees
    WHERE manager_id IS NULL
    UNION ALL
    -- RECURSIVE PART: Automatically does Steps 2, 3, 4, etc. until no more matches
    SELECT e.employee_id, e.manager_id, eh.level + 1
    FROM employees e
    JOIN employee_hierarchy eh ON e.manager_id = eh.employee_id
)
SELECT * FROM employee_hierarchy ORDER BY level, employee_id
"""
final_result = pd.read_sql(final_query, conn)
print(final_result)
print("\n→ The CTE stops recursing when no more employees are found (Step 5 would be empty)")

print("\n=== HOW THE RECURSIVE CTE WORKS ===")
print("1. Start with anchor query (employees with no manager)")
print("2. Join employees table with previous CTE results")
print("3. Add new matches to the result set")
print("4. Repeat step 2-3 until no new matches found")
print("5. Return all accumulated results")

conn.close()