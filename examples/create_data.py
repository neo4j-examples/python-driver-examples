# This example reads CSV data from examples/data/employees.csv
# and creates nodes and relationships in the Neo4j database.
# 
# It creates a graph with 3 node labels, `Person`, `Company`, 
# and `Location`, connected by `WORKS_AT` and `LIVES_IN` relationships.
#
# +-----------+         WORKS_AT         +-----------+
# |  Person   |------------------------->|  Company  |
# +-----------+                          +-----------+
#       |
#       |
#       | LIVES_IN
#       v
# +-----------+
# | Location  |
# +-----------+

import os
from dotenv import load_dotenv
load_dotenv()

import csv
from neo4j import GraphDatabase

FILE_PATH = os.path.join('examples','data','employees.csv')

# Initialize the Neo4j driver
driver = GraphDatabase.driver(
    os.getenv('NEO4J_URI'),
    auth=(
        os.getenv('NEO4J_USERNAME'), 
        os.getenv('NEO4J_PASSWORD')
    )
)

# Verify the connection
# driver.verify_connectivity()

# Cypher query to create the data
cypher_query = """
MERGE (p:Person {id: toInteger($id), name: $name, governmentId: $gov_id})
MERGE (l:Location {name: $location})
MERGE (c:Company {name: $company})
MERGE (p)-[:LIVES_IN]->(l)
MERGE (p)-[:WORKS_AT {position: $position}]->(c)
"""

# Load the CSV file
with open(FILE_PATH, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        
        # Execute the query with parameters
        records, summary, keys = driver.execute_query(
            cypher_query,
            id=row['id'],
            name=row['name'],
            gov_id=row['gov_id'],
            location=row['location'],
            company=row['company'],
            position=row['position']
        )

        # Alternatively, you can pass the row as parameters
        # records, summary, keys = driver.execute_query(
        #     cypher_query,
        #     parameters_= row
        # )

        print(summary.counters)

driver.close()