# MiniProject-BigData


---

## Project Overview

Builds a **Reverse Index** using Hadoop MapReduce + Streaming over a corpus of classic novels stored in HDFS.  


---

## Files Included

| File | Description |
|------|-------------|
| `mapper.py` | Tokenizes, lowercases, removes punctuation & stop words |
| `reducer.py` | Aggregates counts and builds the final reverse index |
| `driver.sh` | Shell script to run the full Hadoop Streaming job |
| `stopwords.txt` | List of common English words to filter out |
| `report-BigData.pdf` | Full project report with scalability analysis |

---

## Prerequisites

- Docker running with Hadoop containers: `namenode`, `datanode1–4`, `resourcemanager`
- Books uploaded to HDFS at `/user/student/library/tmp/`
- Project files copied into the namenode container at `/tmp/miniproject/`

---

## Setup: Copy Files into Container

```bash
docker cp mapper.py namenode:/tmp/miniproject/mapper.py
docker cp reducer.py namenode:/tmp/miniproject/reducer.py
docker cp stopwords.txt namenode:/tmp/miniproject/stopwords.txt
```

---

## How to Run

```bash
bash driver.sh
```

The script will:
1. Exit HDFS safe mode
2. Delete any previous output directory
3. Submit the Hadoop Streaming job
4. Print a sample of the resulting reverse index

---

## What the Script Does (driver.sh)

```bash
# exit safe mode
docker exec -it namenode hdfs dfsadmin -safemode leave
#remove old output
docker exec -it namenode hdfs dfs -rm -r /user/student/output_driver_final

# run Mapreduce job
docker exec -it namenode hadoop jar .../hadoop-streaming-*.jar \
  -files mapper.py,reducer.py,stopwords.txt \
  -mapper "python3 mapper.py" \
  -reducer "python3 reducer.py" \
  -input "/user/student/library/tmp/*.txt" \
  -output /user/student/output_driver_final
```

---

## View Output

```bash
# View sample results
docker exec -it namenode hdfs dfs -cat /user/student/output_driver_final/part* | head -50

# Search for a specific word
docker exec -it namenode hdfs dfs -cat /user/student/output_driver_final/part* | grep "happy"
```

---

## Scalability Results Summary

| Cluster | Real Time | Speedup |
|---------|-----------|---------|
| 4 nodes (baseline) | 32.165s | 1.000 |
| 3 nodes | 28.511s | 1.128 |
| 2 nodes | 29.168s | 1.102 |
| 1 node  | 28.825s | 1.116 |

