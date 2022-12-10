# sql_practice 

from sqlite3 import connect 

#build your remote database 
connection = connect("worm_genome.sqlite")
cursor = connection.cursor()

#create the first table: features table 
create_features = '''

CREATE TABLE IF NOT EXISTS features (
    feature_id  INTEGER PRIMARY KEY AUTOINCREMENT, 
    seq_id TEXT NOT NULL, 
    source TEXT NOT NULL, 
    type_id TEXT NOT NULL, 
    start BIGINT NOT NULL, 
    end BIGINT NOT NULL, 
    score TEXT NOT NULL, --score REAL VALUE HERE (no need to include NOT NULL)
    strand TEXT NOT NULL, 
    phase TEXT NOT NULL --don't include the comma if you are towards the end. 
);

'''
#test cases to override the "DatabaseError"
try:
    cursor.execute(create_features)
except connection.DatabaseError:
    print("Creating the features table resulted in a database error!")
    connection.rollback()
    raise 
else:
    connection.commit
finally:
    print("done")

#check to ensure features table exists 
select_master = "SELECT name, type FROM sqlite_master;"
cursor.execute(select_master)
cursor.fetchall()

#create attributes table 
create_attributes = '''
CREATE TABLE IF NOT EXISTS attributes (
    attr_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    feature_id INTEGER NOT NULL, 
    attr_name TEXT NOT NULL, 
    value TEXT NOT NULL,   
    FOREIGN KEY (feature_id) REFERENCES features (feature_id)
)



'''








create_attributes = '''
CREATE TABLE IF NOT EXISTS attributes (
    attr_id INTEGER PRIMARY KEY AUTOINCREMENT,
    feature_id INTEGER NOT NULL,
    attr_name TEXT NOT NULL, 
    value TEXT NOT NULL, 
    FOREIGN KEY (feature_id) REFERENCES features (feature_id)
    );
'''

try:
    cursor.execute(create_attributes)
except connection.DatabaseError:
    print("Creating the attributes table resulted in a database error!")
    connection.rollback()
    raise
else:
    connection.commit()
finally:
    print("done!")