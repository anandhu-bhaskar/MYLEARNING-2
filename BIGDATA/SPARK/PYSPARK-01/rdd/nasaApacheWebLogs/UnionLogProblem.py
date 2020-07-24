from pyspark import SparkContext, SparkConf

def isNotHeader(line: str):
    return not (line.startswith("host") and "bytes" in line)


if __name__ == "__main__":
    conf = SparkConf().setAppName("unionLogs").setMaster("local[*]")
    sc = SparkContext(conf = conf)

    julyLogs = sc.textFile("in/nasa_19950701.tsv")
    augustLogs = sc.textFile("in/nasa_19950801.tsv")

    aggregatedLogs = julyLogs.union(augustLogs)

    cleanLog = aggregatedLogs.filter(isNotHeader)
    sample = cleanLog.sample(withReplacement = True, fraction = 0.1)

    sample.saveAsTextFile("out/sample_nasa_log.csv")