#!/bin/bash
​
​
countToTwenty() {
  n=1
  while [ $n -le 20 ]
  do
    echo "Count: $n"
    n=$(($n + 1))
  done
}
​
countToTwenty