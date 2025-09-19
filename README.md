# Neo4j Python Examples

This repository contains code examples to use Python with Neo4j Aura.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new/neo4j-examples/python-driver-examples)

> [!IMPORTANT]  
> To use GitHub Codespaces you will need to login with a GitHub account. 
> You can use the [GitHub Codespaces free monthly usage](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts) to view these examples.

## Install

Install the [`neo4j` Python pakage](https://neo4j.com/docs/python-manual/current/).

```bash
pip install neo4j
```

## Examples

- [`connect.py` - Connect to a Neo4j Graph Database](examples/connect.py)
- [`run_cypher.py` - Run a Cypher statement](examples/run_cypher.py)
- [`create_data.py` - Read data from a CSV file and create nodes and relationships](examples/create_data.py)
- [`transaction.py` - Execute cypher in a transaction](examples/transaction.py)
- [`export_to_dataframe.py` - Export data to a Pandas DataFrame ](examples/export_to_dataframe.py)

## Run

To run the examples on your environment, you will need to:

1. Install the required packages including the [`neo4j` Python driver](https://neo4j.com/docs/python-manual/current/).:
    ```bash
    pip install -r requirements.txt
    ```
1. Create a new [`.env`](.env) file and copy the contents of the [`.env.example`](.env.example) file into it
1. Update the environment values in the [`.env`](.env) file with the values in your Aura Credentials file which you downloaded when creating your instance.
1. Run the [`test_environment.py`](./llm-knowledge-graph/test_environment.py) program to check the environment is set up correctly.
