select_all_female_bears_return_name_and_age = """
    Write your SQL query here
    SELECT name, age
    FROM bears
    WHERE sex = 'F';
"""
        
select_all_bears_names_and_orders_in_alphabetical_order = """
    Write your SQL query here
    SELECT name
    FROM bears
    ORDER BY name;
"""

select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = """
    Write your SQL query here
    SELECT name, age
    FROM bears
    WHERE alive = TRUE
    ORDER BY age;

"""

select_oldest_bear_and_returns_name_and_age = """
    Write your SQL query here
    SELECT name, age
    FROM bears
    ORDER BY age DESC
    LIMIT 1;
"""
select_youngest_bear_and_returns_name_and_age = """
    Write your SQL query here
    SELECT name, age
    FROM bears
    ORDER BY age
    LIMIT 1;
"""