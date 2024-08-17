# 0x01-NoSQL

## Task 2:

```javascript
db.school.insert({ name: "Holberton school" })
```

Now, let me break down this script and explain how it works:

1. `db`: This refers to the current database. When you run the script with `mongo my_db`, it automatically connects to the `my_db` database, so `db` will refer to `my_db`.

2. `school`: This is the name of the collection. If it doesn't exist, MongoDB will create it automatically.

3. `insert()`: This is a MongoDB method used to insert documents into a collection.

4. `{ name: "Holberton school" }`: This is the document we're inserting. It's in JSON format, with one field named "name" and its value set to "Holberton school".

When you run this script, it will:
    1. Connect to the specified database (passed as an option to the `mongo` command)
    2. Create the `school` collection if it doesn't exist
    3. Insert a new document into the `school` collection with the field `name` set to "Holberton school"

The output `WriteResult({ "nInserted" : 1 })` indicates that one document was successfully inserted.
