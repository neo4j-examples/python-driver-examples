# Neo4j Python Examples - Devcontainer

A .devcontainer configuration is included, and when opened, such as in a GitHub codespace, all the required software and packages will be installed.

You will need to:

1. Create a new [`.env`](.env) file and copy the contents of the [`.env.example`](.env.example) file into it
2. Update the environment values in the [`.env`](.env) file with the values in your Aura Credentials file which you downloaded when creating your instance.
3. Run the [`test_environment.py`](./llm-knowledge-graph/test_environment.py) program to check the environment is set up correctly.

You can explore the [`examples`](../examples/) to see how you can use the Neo4j Python driver with Aura.