set title "Benchmarks"
C = "#99ffff"; Cpp = "#4671d5";
set auto x
set yrange [0:1000]
set style data histogram
set style histogram cluster gap 1
set style fill solid border -1
set boxwidth 0.9
set xtic scale 0
# 2, 3, 4, 5 are the indexes of the columns; 'fc' stands for 'fillcolor'
plot 'languages.data' using 2:xtic(1) ti col fc rgb C, '' u 3 ti col fc rgb Cpp
set term png 
set output "printme.png"
replot
