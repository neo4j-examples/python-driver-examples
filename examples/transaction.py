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

# Create a session to run a transaction
with driver.session() as session:

    # Create a work unit for the transaction
    def create_person(tx, name, age):
        result = tx.run("""
        CREATE (p:Person {name: $name, age: $age})
        RETURN p
        """, name=name, age=age)

        return result.consume()

    # Execute transaction function
    summary = session.execute_write(create_person, name='Alice', age=30)

    print(summary.counters.nodes_created, 'node(s) created.')

# Close the driver
driver.close()