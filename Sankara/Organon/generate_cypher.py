# ...existing code...
def generate_cypher_queries(data):
    queries = []
    for item in data:
        queries.append(f"CREATE (v:Verse {{id: '{item['id']}', text: '{item['text']}'}})")
        if item['leading_bhashya']:
            queries.append(f"CREATE (lb:LeadingBhashya {{id: '{item['id']}_LB', text: '{item['leading_bhashya']}'}})")
            queries.append(f"MATCH (v:Verse {{id: '{item['id']}'}}), (lb:LeadingBhashya {{id: '{item['id']}_LB'}}) CREATE (v)-[:HAS_LEADING_BHASHYA]->(lb)")
        if item['versetext']:
            queries.append(f"CREATE (vt:Versetext {{id: '{item['id']}_VT', text: '{item['versetext']}'}})")
            queries.append(f"MATCH (v:Verse {{id: '{item['id']}'}}), (vt:Versetext {{id: '{item['id']}_VT'}}) CREATE (v)-[:HAS_VERSETEXT]->(vt)")
        if item['bhashya']:
            queries.append(f"CREATE (b:Bhashya {{id: '{item['id']}_B', text: '{item['bhashya']}'}})")
            queries.append(f"MATCH (v:Verse {{id: '{item['id']}'}}), (b:Bhashya {{id: '{item['id']}_B'}}) CREATE (v)-[:HAS_BHASHYA]->(b)")
    return queries

queries = generate_cypher_queries(verses)

for query in queries:
    print(query)
# ...existing code...
