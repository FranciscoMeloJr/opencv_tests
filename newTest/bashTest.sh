#!/bin/bash

function PF(){
echo $1$2
  for i in `seq 1 $1`
  do
     echo $i
     tracePF $i $2
  done

}

function tracePF(){

  a='output=/tmp/ust-traces-'
  b=$2
  c='-pf-'
  d=$a$b$c
  e=$d$1

  lttng create $1 --$e
  lttng enable-event -u -a
  #./opencv_example 
  lttng enable-event -u sched_switch
  lttng add-context -u -t perf:thread:page-fault
  #lttng add-context -u -t perf:thread:cache-misses 
  #lttng add-context -u -t perf:thread:instructions 

  lttng start

   LD_PRELOAD=/usr/local/lib/liblttng-ust-fork.so ./opencv $2
  lttng stop
  lttng destroy
}


if [ "$1" = "-a" ];
then
   echo 'All';
   echo 'inline';

   qtd=1
   data="../data/500x500.jpg"

   PF $qtd $data
   
fi

