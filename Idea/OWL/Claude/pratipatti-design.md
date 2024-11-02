# OWL++ Schema Template Pattern

## I. Base Structure

### Required Prefixes
```ttl
@prefix : <http://example.org/domain#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix spin: <http://spinrdf.org/spin#> .
@prefix sp: <http://spinrdf.org/sp#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
```

## II. Core Components

### 1. SHACL Shapes Pattern
```ttl
:CoreShape a sh:NodeShape ;
    sh:targetClass :TargetClass ;
    sh:property [
        sh:path :requiredProperty ;
        sh:minCount 1 ;
        sh:message "Required property constraint message" ;
        sh:severity sh:Violation ;
    ] ;
    sh:property [
        sh:path :relationshipProperty ;
        sh:class :RelatedClass ;
        sh:message "Relationship constraint message" ;
    ] .
```

### 2. SPIN Rules Pattern
```ttl
:ProcessRule a spin:Rule ;
    rdfs:label "Process Description" ;
    spin:body [
        a sp:Construct ;
        sp:text """
            CONSTRUCT {
                ?subject :produces ?result .
                ?result :hasType ?type .
            }
            WHERE {
                ?subject a :SourceClass .
                ?subject :hasProperty ?property .
                BIND(UUID() AS ?result)
            }
        """
    ] .
```

### 3. Protocol Definition Pattern
```ttl
:QueryProtocol a :Protocol ;
    :hasQuery """
        CONSTRUCT {
            ?entity :hasState ?state .
            ?state :leadsTo ?nextState .
        }
        WHERE {
            {
                SELECT ?entity ?state ?nextState
                WHERE {
                    ?entity a :ProcessClass .
                    ?entity :currentState ?state .
                    ?state :transitions ?nextState .
                    FILTER EXISTS {
                        ?state a :ValidState .
                    }
                }
            }
        }
    """ .
```

## III. Integration Components

### 1. Processing Unit Pattern
```ttl
:ProcessingUnit a :Component ;
    :implementsShape :CoreShape ;
    :usesRule :ProcessRule ;
    :followsProtocol :QueryProtocol .
```

### 2. Validation Template Pattern
```ttl
:ValidationTemplate a spin:Template ;
    spin:body [
        a sp:Select ;
        sp:text """
            SELECT ?entity ?validation
            WHERE {
                ?entity a :TargetClass .
                ?entity :hasValidation ?validation .
                FILTER NOT EXISTS {
                    ?validation a :Invalid .
                }
            }
        """
    ] .
```

## IV. Core Class Structure

### 1. Base Classes Pattern
```ttl
:CoreClass a owl:Class ;
    rdfs:subClassOf :BaseClass ;
    :hasDescription "Core class description" .

:RelatedClass a owl:Class ;
    rdfs:subClassOf :CoreClass ;
    :hasDescription "Related class description" .
```

### 2. Operation Pattern
```ttl
:Operation a owl:Class ;
    rdfs:subClassOf spin:Function ;
    spin:constraint [
        a sh:NodeShape ;
        sh:property [
            sh:path :hasInput ;
            sh:minCount 1 ;
        ] ;
        sh:property [
            sh:path :producesOutput ;
            sh:minCount 1 ;
        ] ;
    ] .
```

## V. Implementation Guidelines

1. Core Class Definition:
   - Define base classes first
   - Establish clear hierarchy
   - Include descriptions

2. SHACL Shape Implementation:
   - Target specific classes
   - Define property constraints
   - Include validation messages

3. SPIN Rule Creation:
   - Clear rule labels
   - Specific CONSTRUCT queries
   - Proper variable binding

4. Protocol Setup:
   - Define query structure
   - Include state transitions
   - Implement filters

5. Component Integration:
   - Link shapes, rules, protocols
   - Define processing units
   - Establish validation templates

## VI. Usage Example

```ttl
# Define core class
:ExampleClass a owl:Class ;
    rdfs:subClassOf :CoreClass ;
    :hasDescription "Example implementation" .

# Create shape
:ExampleShape a sh:NodeShape ;
    sh:targetClass :ExampleClass ;
    sh:property [
        sh:path :requiredProperty ;
        sh:minCount 1 ;
    ] .

# Define rule
:ExampleRule a spin:Rule ;
    rdfs:label "Example Process" ;
    spin:body [
        a sp:Construct ;
        sp:text """
            CONSTRUCT {
                ?subject :hasResult ?result .
            }
            WHERE {
                ?subject a :ExampleClass .
                BIND(UUID() AS ?result)
            }
        """
    ] .

# Setup processing
:ExampleProcessor a :ProcessingUnit ;
    :implementsShape :ExampleShape ;
    :usesRule :ExampleRule ;
    :followsProtocol :ExampleProtocol .
```

## VII. Key Principles

1. Structural Integrity:
   - Maintain clear class hierarchy
   - Enforce property constraints
   - Validate relationships

2. Process Definition:
   - Clear rule specification
   - Proper state transitions
   - Validated outcomes

3. Integration Requirements:
   - Component linkage
   - Protocol adherence
   - Validation enforcement

4. Implementation Flow:
   - Define base structure
   - Implement constraints
   - Establish processes
   - Integrate components
