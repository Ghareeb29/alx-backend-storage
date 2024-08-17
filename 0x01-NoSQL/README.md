# 0x01-NoSQL

## Task 12

This script does the following:

1. It uses `pymongo` to connect to the MongoDB database `logs` and the collection `nginx`.

2. It counts the total number of documents in the collection using `count_documents({})`.

3. It then counts the number of documents for each HTTP method (GET, POST, PUT, PATCH, DELETE) using `count_documents()` with a filter for each method.

4. Finally, it counts the number of status checks, which are documents with method "GET" and path "/status".

5. The results are printed in the exact format specified in your requirements.
