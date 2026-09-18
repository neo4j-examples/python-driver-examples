# This example reads CSV data from examples/data/employees.csv
# and creates nodes and relationships in the Neo4j database in batches.
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
from itertools import islice
from neo4j import GraphDatabase

FILE_PATH = os.path.join('examples','data','employees.csv')
BATCH_SIZE = 1000

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

# Cypher query to create the data in batches
cypher_query = """
UNWIND $rows AS row
MERGE (p:Person {id: toInteger(row.id), name: row.name, governmentId: row.gov_id})
MERGE (l:Location {name: row.location})
MERGE (c:Company {name: row.company})
MERGE (p)-[:LIVES_IN]->(l)
MERGE (p)-[:WORKS_AT {position: row.position}]->(c)
"""


def batched(reader, batch_size):
    while batch := list(islice(reader, batch_size)):
        yield batch


# Load the CSV file
with open(FILE_PATH, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for batch in batched(reader, BATCH_SIZE):

        # Execute the query once for each batch
        records, summary, keys = driver.execute_query(
            cypher_query,
            database_=os.getenv('NEO4J_DATABASE'),
            rows=batch
        )

        print(summary.counters)

driver.close()