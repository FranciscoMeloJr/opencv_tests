#!/bin/bash

S1='800'
S2='400'
S3='700'

function x {
	
	for i in `seq 1 $1`
	do
	      ./OpenCvProject $2
	     echo " "
	done

};

function y {         
	echo $1

	x 1000 $1 >> "$2"

	echo "end"
}
if [[ "$1" ==  $S1 ]]; then
	x 1000 ../data/800x800.png > ../results/test800.csv
fi
if [[ "$1" ==  $S2 ]]; then
        x 1000 ../data/400x400.png > ../results/test400.csv
fi
if [[ "$1" ==  $S3 ]]; then
        x 1000 ../data/700x700.png > ../results/test700.csv
fi

if [[ "$1" ==  '1' ]]; then
	p4="../results/testTotal.csv";
       
	v1="../data/700x700.png";
        p2="../data/400x400.png";
        p3="../data/800x800.png";

        y $v1 $p4;
	sleep 1;
	y $p2 $p4;
	sleep 1;
	y $p3 $p4;
	sleep 1;
fi





