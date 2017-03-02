#!/bin/bash

function PF(){
echo $1$2
  for i in `seq 1 $1`
  do
     echo $i
     tracePF $i $2
  done

}

function CM(){
echo $1
  for i in `seq 1 $1`
  do
     traceCM $i $2
  done
}

function INST(){
echo $1
  for i in `seq 1 $1`  
  do
     traceINST $i $2
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

  ./inline -$2 
  lttng stop
  lttng destroy
}

function traceCM (){

  a='output=/tmp/ust-traces-'
  b=$2
  c='-cm-'
  d=$a$b$c
  e=$d$1

  lttng create $1 --$e
  lttng enable-event -u -a
  #./opencv_example 
  #lttng add-context -u -t perf:thread:page-fault
  lttng enable-event -u sched_switch
  lttng add-context -u -t perf:thread:cache-misses
  #lttng add-context -u -t perf:thread:instructions 

  lttng start

  ./inline -$2
  lttng stop
  lttng destroy

}

function traceINST (){
 
  a='output=/tmp/ust-traces-'
  b=$2
  c='-init'
  d=$a$2$c
  e=$d$1

  lttng create $1 --$e
  lttng enable-event -u -a
  #./opencv_example 
  #lttng add-context -u -t perf:thread:page-fault
  #lttng add-context -u -t perf:thread:cache-misses 
  lttng add-context -u -t perf:thread:instructions 

  lttng start

  ./inline -$2
  lttng stop
  lttng destroy

};


function par(){

 echo $1

};

function show(){

 a='PF'
 b='world'
 c=$a$b;
 par $c

};

echo $1
if [ "$#" -eq 0 ];
then
   echo '-all for all tests';
fi

if [ "$1" = "-a" ];
then 
   echo 'All';
   echo 'inline';

   qtd=3
   inline='i'

   PF $qtd $inline
   CM $qtd $inline
   INST $qtd $inline 
  
   echo 'not inline';
   inline='n'
 
   PF $qtd $inline
   CM $qtd $inline
   INST $qtd $inline

fi


echo Enter quantity of tests:
read qtd

echo Enter the type:
read type

echo 'With or without inline (y = i / n = n)'
read inline

if [ $type = "P" ]; 
then
       PF $qtd $inline
fi

if [ $type = "C" ]; 
then
       CM $qtd $inline
fi

if [ $type = "I" ]; 
then
       INST $qtd $inline
fi

if [ $type = "S" ];
then
       show
fi


