from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("LearnSpark").getOrCreate()
# df = spark.read.csv("fx_USDJPY.csv", encoding="cp932")


df = spark.read.format("csv")\
                  .option("encoding","cp932")\
                  .option("header","true")\
                  .option("maxRowsInMemory",1000)\
                  .option("inferSchema","false")\
                  .option("delimiter", ",")\
                  .load("fx_USDJPY.csv")
df.show()
