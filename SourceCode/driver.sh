#!/bin/bash

docker exec -it namenode hdfs dfsadmin -safemode leave

docker exec -it namenode hdfs dfs -rm -r /user/student/output_driver_final 2>/d>

docker exec -it namenode hadoop jar /opt/hadoop-3.2.1/share/hadoop/tools/lib/ha>
  -files /tmp/miniproject/mapper.py,/tmp/miniproject/reducer.py,/tmp/miniprojec>
  -mapper "python3 mapper.py" \
  -reducer "python3 reducer.py" \
  -input "/user/student/library/tmp/*.txt" \
  -output /user/student/output_driver_final

# 4. Show the top of the combined index
echo "------------------------------------------"
echo "FINAL COMBINED INVERTED INDEX (SAMPLE)"
echo "------------------------------------------"
docker exec -it namenode hdfs dfs -cat /user/student/output_driver_final/part* >

