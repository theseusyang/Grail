#!/bin/sh

algo="sssp"
echo "golden output"
cat "./output/"$algo"_golden.out"
echo "algo output"
cat "./output/"$algo".out"

python compareoutput.py -f output/sssp.out -F output/sssp_golden.out
ret=$?
if [ $ret -ne 0 ]; then
	echo "Discrepancy in Algorithmic Output generated by GRAIL"
	exit 1
fi
echo "Successful"
exit 0

