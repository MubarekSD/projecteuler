#!/usr/bin/env bash
sum=0
for i in {1..1000}
do
	if [ $((i % 3)) -eq 0 ] || [ $((i % 5)) -eq 0 ]
	then
		((sum = sum + i))
	fi
done

echo $sum
