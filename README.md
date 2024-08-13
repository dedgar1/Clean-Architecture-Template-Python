# Clean-Architecture-Template-Python
Template to use for clean architecture projects in python
## Overview
Clean architecture is composed of layers. Think of it as concentric cirles with the following layers going from core further out:
1. Entities
2. Use Cases
3. Gateway
4. External Systems

### Entities layer
The innermost layer represents the domain models.
Entities have knowledge of each other and case use one another directly. However, they know nothing about the outer layers. They therefore can't call the db, or anything in other layers

### Use cases
Most importat part of the clean architecture system. They use the domain model to work on real data. Use case exaples include
- User log in
- Searching for something
- bank transaction
Isolate small actions in spearate use cases. Use cases have full acess to the entities layer and can instanciate them directly.

### Gateway layer
Defines the interface with external systems. Doesn't implement any business rules.
An example of an itme here will be data storage interface
Gateways have access to entities and use cases so they can receive and return objects from those layers.

### External Systems layer
External systems have full access to the lower layers

### Communication between layers.
- Use Simple Structures from outside moving to the core
- Use interfaces for the core moving out

### How to run the app
- From the root folder, use `FLASK_CONFIG="development" flask run -h "0.0.0.0" -p 5050`