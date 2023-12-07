# In-Memory Database with Transaction Support

## Introduction

This project implements an in-memory key-value database in Python. It's designed to simulate basic transactional functionalities typical in relational databases. The database allows for "all or nothing" updates, crucial for maintaining data integrity in systems like financial transaction platforms.

## Setup and Installation

To run this project, ensure that Python (version 3.x) is installed on your system. No additional libraries or installations are required.

## Running the Code

1. Clone the repository to your local machine.
2. Navigate to the directory containing `in_memory_db.py`.
3. Run the script using the command:
   python in_memory_db.py

## Future Assignment Enhancement Suggestions

To elevate this project for future official assignments:

1. **Concurrency Control:** Implement multi-threading to simulate concurrent transactions, enhancing the database's real-world applicability.
2. **Advanced Transaction Management:** Introduce concepts like savepoints within transactions, and more granular control over commit and rollback operations.
3. **Comprehensive Documentation and Testing:** Encourage detailed documentation and thorough unit tests for each function, possibly integrating a continuous integration/testing framework.
