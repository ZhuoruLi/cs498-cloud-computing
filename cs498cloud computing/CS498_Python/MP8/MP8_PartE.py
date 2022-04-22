from pyspark import SparkContext, SQLContext
from pyspark.sql.types import StructType
from pyspark.sql.types import StructField
from pyspark.sql.types import StringType, IntegerType
from pyspark.sql import SparkSession 
import pyspark

sc = SparkContext()
#spark = SparkSession(sc)
sqlContext = SQLContext(sc)

####
# 1. Setup (10 points): Download the gbook file and write a function to load it in an RDD & DataFrame
####
# def programmatic_schema_example(spark: SparkSession) -> None:
    # Load a text file and convert each line to a Row.
lines = sc.textFile("gbooks")
parts = lines.map(lambda l: l.split("\t"))
# Each line is converted to a tuple.
books = parts.map(lambda p: (p[0].strip(), int(p[1].strip()), int(p[2].strip()), int(p[3].strip())))
# The schema is encoded in a string.
schemaString = "word count1 count2 count3"
# fields = [StructField(field_name, StringType(), True) for field_name in schemaString.split()]
fields = [StructField("word", StringType(), True),StructField("count1", IntegerType(), True),StructField("count2", IntegerType(), True),StructField("count3", IntegerType(), True)]
schema = StructType(fields)
# Apply the schema to the RDD.
schemabooks = sqlContext.createDataFrame(books, schema)
# Creates a temporary view using the DataFrame
schemabooks.createOrReplaceTempView("books")

####
# 5. Joining (10 points): The following program construct a new dataframe out of 'df' with a much smaller size.
####

df2 = schemabooks.select("word", "count1").distinct().limit(100)
df2.createOrReplaceTempView('gbooks2')

# results = sqlContext.sql("SELECT COUNT(*) FROM gbooks2, gbooks2")
results = sqlContext.sql("SELECT * FROM gbooks2 a INNER JOIN gbooks2 b ON a.count1 = b.count1")
print(results.count())

# Now we are going to perform a JOIN operation on 'df2'. Do a self-join on 'df2' in lines with the same #'count1' values and see how many lines this JOIN could produce. Answer this question via DataFrame API and #Spark SQL API
# Spark SQL API

# output: 210

