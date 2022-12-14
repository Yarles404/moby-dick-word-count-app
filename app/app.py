from flask import Flask, render_template, request, url_for
from flask_caching import Cache
from pyspark import SparkContext, SparkConf
import re

config = {
    'DEBUG': True,
    'CACHE_TYPE': 'SimpleCache',
    'CACHE_DEFAULT_TIMEOUT': 300
}

app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)

with app.app_context():
    # create Spark context with a name
    spark = SparkContext('local', 'PySpark Moby Dick Word Count')

    # read data from moby dick and split each line into words
    words = spark.textFile('static/corpus/mobydick.txt') \
        .flatMap(lambda line: line.split(' '))
    # get stop words, excluding comments, filter out empty words
    stop_words = set(spark
                     .textFile('static/corpus/stop-words.txt')
                     .map(lambda line: '' if line and line[0] == '#' else line.lower())
                     .filter(lambda word: word)
                     .collect())

    # remove punctuation and lowercasify, filter out stop words and emtpy strings, then count words
    word_counts = words \
        .map(lambda word: re.sub(r'[^\w\s]', '', word).lower()) \
        .filter(lambda word: word not in stop_words and word) \
        .map(lambda word: (word, 1)) \
        .reduceByKey(lambda a, b: a + b) \
        .top(100, key=lambda x: x[1])


@app.route('/')
@cache.cached()
def wordcount():
    return render_template('word_count.html', word_counts=word_counts)


if __name__ == '__main__':
    app.run(debug=True)
