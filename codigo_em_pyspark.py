# -*- coding: utf-8 -*-
"""Codigo em Pyspark

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14WN5nLm9nslKN-KaOkwOWTVVlPW79gah
"""

!apt-get install openjdk-8-jdk-headless -qq > /dev/null
!wget -q https://archive.apache.org/dist/spark/spark-3.1.2/spark-3.1.2-bin-hadoop2.7.tgz
!tar xf spark-3.1.2-bin-hadoop2.7.tgz

import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["SPARK_HOME"] ="/content/spark-3.1.2-bin-hadoop2.7"
!pip install -q findspark
import findspark
findspark.init()
from pyspark.sql import SparkSession
sc = SparkSession.builder.master('local[*]').getOrCreate()
sc

!wget --continue https://github.com/jonates/opendata/blob/master/WorldCup/WorldCups.csv

WorldCups = sc.read.csv(
    path = "/content/WorldCups.csv",
    inferSchema = True,
    header = True,
    sep =';',
    encoding = "UTF-8"
)

type(WorldCups)

from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

data = [
    (1930, "Uruguay", "Uruguay", "Argentina", "USA", "Yugoslavia", 70, 13, 18, 434000, 24139),
    (1934, "Italy", "Italy", "Czechoslovakia", "Germany", "Austria", 70, 16, 17, 395000, 23235),
    (1938,'France','Italy','Hungary','Brazil','Sweden',84,15,18,483000,26833),
    (1950,'Brazil','Uruguay','Brazil','Sweden','Spain',88,13,22,1337000,60773),
    (1954,'Switzerland','Germany FR','Hungary','Austria','Uruguay',140,16,26,943000,36269),
    (1958,'Sweden','Brazil','Sweden','France','Germany FR',126,16,35,868000,24800),
    (1962,'Chile','Brazil','Czechoslovakia','Chile','Yugoslavia',89,16,32,776000,24250),
    (1966,'England','England','Germany FR','Portugal','Soviet Union',89,16,32,1614677,50459),
    (1970,'Mexico','Brazil','Italy','Germany FR','Uruguay',95,16,32,1673975,52312),
    (1974,'Germany','Germany FR','Netherlands','Poland','Brazil',97,16,38,1774022,46685),
    (1978,'Argentina','Argentina','Netherlands','Brazil', 'Italy' , 102, 16, 38, 1610215, 42374),
    (1982,'Spain','Italy','Germany FR','Poland', 'France' , 146, 24, 52, 1856277, 35698),
    (1986,'Mexico','Argentina','Germany FR','France','Belgium', 132, 24, 52, 2407431 , 46297),
    (1990,'Italy','Germany FR','Argentina','Italy','England', 115, 24, 52, 2527348, 48411),
    (1994,'USA','Brazil','Italy','Sweden','Bulgaria', 141, 24, 52, 3568567, 68626),
    (1998,'France','France','Brazil','Croatia','Netherlands', 171, 32, 64, 2859234, 44676),
    (2002,'Korea/Japan','Brazil','Germany','Turkey','Korea Republic', 161, 32, 64, 2724604, 42571),
    (2006,'Germany','Italy','France','Germany','Portugal', 147, 32, 64, 3367000, 52609),
    (2010,'South Africa','Spain','Netherlands','Germany','Uruguay', 145, 32, 64, 3167984, 49499),
    (2014,'Brazil','Germany','Argentina','Netherlands','Brazil', 171, 32, 64, 3441450, 53772),
    (2018,'Russia','France','Croatia','Belgium','England', 169, 32, 64, 3031768, 47371),


]

df = spark.createDataFrame(data, ["Year", "Country", "Winner", "Runners-Up", "Third", "Fourth", "GoalsScored", "QualifiedTeams", "MatchesPlayed", "Attendance", "Attendance_per_Matches"])

df.show()