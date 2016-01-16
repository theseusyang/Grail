Grail
============================
Code for the Grail method described in: http://pages.cs.wisc.edu/~jignesh/publ/Grail.pdf

At a high level, you load graph data into the `vertex` and the `edge` tables below, and then run the code here to generate SQL to analyze the graphs. The code here generates T-SQL (for Microsoft SQL Server, which we had used in the original paper). 
If you are interested in making this work with other databases, please let us know! 

How to run Grail?
-----------------------------------------------------------

1. Clone the git Grail repository into your local machine using one of the following commands:
  * `git clone https://github.com/adalbertgerald/Grail.git` (or)
  * `git clone git@github.com:adalbertgerald/Grail.git`

2. Change your current working directory to `Grail`.
  * `cd Grail`

3. Change directory to "src" to browse through the code or to compile and run the code.
  * `cd src`

4. Compile the java code using the following command. Note you will need to [install Java](https://java.com/en/download/help/index_installing.xml "Java Install Page") on your machine.
  * `javac *.java`

5. Run the Grail code, in any of the following ways: (`config.txt` is used as the default configuration file, if no config file is given)
  * `java Grail` (uses the default configuration file `config.txt`)
  * `java Grail configs/pagerank.txt` (to generate the T-SQL for a pagerank graph program)
  * `java Grail configs/sssp.txt` (to generate the T-SQL for a Single Source Shortest Path(SSSP) graph program)
  * `java Grail configs/wcc.txt` (to generate the T-SQL for a Weakly Connected Component(WCC) graph program)

6. Execute the SQL statements generated by Grail (i.e. output of step 5) in a Microsoft SQL Server Database.

Basic Tables
---------------------------
We have two basic tables: `vertex` and `edge`.

The vertex table is created in SQL as:

```sql
    CREATE TABLE vertex {
      vertex_id INT
    }
```

The edge table is created as:
```sql
    CREATE TABLE edge {
      src_id INT,
      dest_id INT
    }
```

Additional primary key, indices and other constraints can also be added to the schema creating commands above.

You will have to load your graph data into these two tables. 

The basic idea is that a graph analytics program(e.g. Shortest Path/PageRank/Connected Component) can be implemented in SQL database by using SQL joins, aggregations, and updates on relational tables. We want to provide a user-friendly way to generate SQL for graph analytics. The user inputs a configuration file that specifies the computation, and this program generates the corresponding (t-)SQL. See the original paper (link above) for more details.

Example configuration files
---------------------------
pagerank.txt -- page rank algorithm

sssp.txt -- single source shortest path algorithm

wcc.txt -- weakly connected component algorithm

Here is a description of the attributes in the configuration file 
------------------------------------------
1. VertexValueType: The type of value that a vertex represents. It should be one of the types supported by the RDBMS. Examples: int, float, etc.
2. MessageValueType: The type of messages that a vertex can send and receive. It should also be one of the types supported by the RDBMS. Examples: int, float, etc.
3. InitiateVal: The initial value of the vertices. For example, if the vertices have int value, the initial value could be zero.
4. Initial Message: The initial messages to all or specific vertices. (ALL, value) and (some_vertex_id, value) is used for sendind the initial message to all vertices and to a specific vertex respectively.
5. CombineMessage: The way to do aggregation on messages. The message will be automatically grouped on the destination vertex id. The aggregation should be supported by the RDBMS. It can be MIN, MAX, or UDAF. The UDAF should be defined first.
6. UpdateAndSend: The updateandsend part can be a combination of one or more of the following actions: mutate values, send messages, and flow control.
7. End: NO_MESSAGE or (ITER, max_iterations) - NO_MESSAGE terminates the graph computation, when there are no more messages remaining to be processed. (ITER, max_iterations) terminates the program after max_iterations number of iterations.

