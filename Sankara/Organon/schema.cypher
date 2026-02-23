### Step 2: Define Neo4j Schema

Define the schema for nodes and relationships in Neo4j to represent the semantic parts.

CREATE CONSTRAINT ON (v:Verse) ASSERT v.id IS UNIQUE;
CREATE CONSTRAINT ON (lb:LeadingBhashya) ASSERT lb.id IS UNIQUE;
CREATE CONSTRAINT ON (vt:Versetext) ASSERT vt.id IS UNIQUE;
CREATE CONSTRAINT ON (b:Bhashya) ASSERT b.id IS UNIQUE;
CREATE CONSTRAINT ON (c:Cell) ASSERT c.id IS UNIQUE;
CREATE CONSTRAINT ON (sp:SemanticPart) ASSERT sp.id IS UNIQUE;

CREATE INDEX ON :Verse(text);
CREATE INDEX ON :LeadingBhashya(text);
CREATE INDEX ON :Versetext(text);
CREATE INDEX ON :Bhashya(text);
CREATE INDEX ON :Cell(type);
CREATE INDEX ON :Cell(content);
CREATE INDEX ON :Cell(tags);
CREATE INDEX ON :SemanticPart(content);
