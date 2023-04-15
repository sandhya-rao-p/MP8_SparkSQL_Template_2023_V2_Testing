from pyspark import SparkContext, SQLContext
from pyspark.sql.types import StructType
from pyspark.sql.types import StructField
from pyspark.sql.types import StringType, IntegerType

sc = SparkContext()
sqlContext = SQLContext(sc)

####
# 1. Setup : Write a function to load it in an RDD & DataFrame
####

# RDD API
# Columns:
# 0: word (string), 1: count1 (int), 2: count2 (int), 3: count3 (int)


# Spark SQL - DataFrame API

####
# 2. Counting (16 points): How many lines does the file contains? Answer this question via both RDD api & #Spark SQL
####

# Spark SQL 

# sqlContext.sql(query).show() or df.show()
# +--------+
# |count(1)|
# +--------+
# |   50013|
# +--------+


