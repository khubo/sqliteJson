# sqliteJson

Convert sqlite query results to json consumable python dicts.

## Install 
      
        pip install sqliteJson

### example
  
        import sqlite3
        from sqliteJson import json_serializer
                  
        db = sqlite3.connect('example.db')
        cur = db.execute('Select * from table ')
        result_dict = json_serializer(cur)

                                      
