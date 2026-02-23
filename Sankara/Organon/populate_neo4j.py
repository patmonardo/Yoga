# ...existing code...
from neo4j import GraphDatabase

def populate_neo4j(queries, uri="bolt://localhost:7687", user="neo4j", password="password"):
    driver = GraphDatabase.driver(uri, auth=(user, password))
    with driver.session() as session:
        for query in queries:
            session.run(query)
    driver.close()

# Example usage
populate_neo4j(queries)
# ...existing code...
