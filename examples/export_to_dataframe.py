# This example demonstrates how to run a Cypher query and export the results to a 
# Pandas DataFrame.
# 
# You can add the expected data to the database using the `examples/create_data.py` 
# example.

import os
from dotenv import load_dotenv
load_dotenv()

from neo4j import GraphDatabase, Result

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
RETURN 
    p.name as name, 
    c.name as company, 
    w.position as position, 
    l.name as location
"""

# Execute the query using the Result transformer 
df = driver.execute_query(
    cypher_query,
    result_transformer_=Result.to_df,
    location='London'
)

# Print the DataFrame
print(df)

# Close the driver
driver.close()