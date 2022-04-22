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
lines = sc.textFile("gbooks.txt")
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
# SQL can be run over DataFrames that have been registered as a table.
# results = sqlContext.sql("SELECT word FROM books LIMIT 15")
# results.show()
schemabooks.printSchema()
# RDD API
# Columns:
# 0: place (string), 1: count1 (int), 2: count2 (int), 3: count3 (int)

# Spark SQL - DataFrame API



