# Curriculum-knowledge-graph-demo
Visualization program of curriculum knowledge graph. Using django framework.

# Dependent environment
This porject needs following enviroment:
### [1]MySQL dataset
The following is the database connection information:
DATABASES = {
    'default':
    {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'his_question',
        'HOST': 'localhost', 
        'PORT': 3306,
        'USER': 'root', 
        'PASSWORD': '123456', 
    }
}
You can modify your database information accordingly,
or you can also modify the code in this path: "Graph/settings.py".

### [2]Neo4j dataset
The following is the database connection information:
#graph = Graph("http://localhost:7474/", auth=("neo4j", "neo4j_0336"),name="mygraph.db")
You can modify your database information accordingly,
or you can also modify the code in this path: "Graph/neo4j.py".

You need to import triple data into the database firstly.
In the process of importing triple data into the secondary database, 
please set the neo4j type of biological information as "knowledge_b", 
historical information as "knowledge_h" 
and programming as "knowledge_pd".

### [3]python_version == 3.6

# Get start
use "win + r" to start command windows
enter your project url: "...\Curriculum knowledge graph code\Graph"
Enter the following instructions: "python manage.py runserver 0.0.0.0:8000" to start django porject
after that, enter the following link in your default browser: "127.0.0.1:8000/list" to enter the system.
