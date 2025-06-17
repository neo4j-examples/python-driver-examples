# This example demonstrates how to run a Cypher query using the Neo4j Python driver.
# Query parameters are used to run the query, and the result is printed.
# 
# You can add the expected data to the database using the `examples/create_data.py` 
# example.

import os
from dotenv import load_dotenv
load_dotenv()

from neo4j import GraphDatabase

# Initialize the Neo4j driver
driver = GraphDatabase.driver(
    os.getenv('NEO4J_URI'),
    auth=(
        os.getenv('NEO4J_USERNAME'), 
        os.getenv('NEO4J_PASSWORD')
    )
)

# Verify the connection
driver.verify_connectivity()

# Define the query
cypher_query = """
MATCH (p:Person)-[:LIVES_IN]->(l:Location)
MATCH (p)-[w:WORKS_AT]->(c:Company)
WHERE l.name = $location
RETURN p.name as name, c.name as company, w.position as position
"""

# Execute the query with a parameter
records, summary, keys = driver.execute_query(
    cypher_query,
    location='London'
)

# When only reading data, you can optimize performance by setting the 
# routing_ parameter to READ mode.

# records, summary, keys = driver.execute_query(
#     cypher_query,
#     routing_='r',
#     location='London'
# )

# Parse the result
for record in records:
    # Print the return values
    print(f"Name: {record['name']}, Company: {record['company']}, Position: {record['position']}")

# Close the driver
driver.close()