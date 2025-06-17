# This example demonstrates how to connect to a Neo4j database using the Neo4j
# Python driver.
# 
# It connects to the database, verifies the connection, runs a simple Cypher 
# query to count the nodes, and prints the result.

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

# Run a simple query to count nodes in the database
records, summary, keys = driver.execute_query(
    "RETURN COUNT {()} AS count"
)

# Get the first record
first = records[0]

# Print the count entry
print(first["count"])   # (3)

# Close the driver
driver.close()