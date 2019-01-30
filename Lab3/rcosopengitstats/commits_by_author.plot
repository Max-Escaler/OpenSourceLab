set terminal png transparent size 640,240
set size 1.0,1.0

set terminal png transparent size 640,480
set output 'commits_by_author.png'
set key left top
set yrange [0:]
set xdata time
set timefmt "%s"
set format x "%Y-%m-%d"
set grid y
set ylabel "Commits"
set xtics rotate
set bmargin 6
plot 'commits_by_author.dat' using 1:2 title "jakebillings" w lines, 'commits_by_author.dat' using 1:3 title "Ethan Graf" w lines, 'commits_by_author.dat' using 1:4 title "Fred Choi" w lines, 'commits_by_author.dat' using 1:5 title "Mitchell Falkow" w lines, 'commits_by_author.dat' using 1:6 title "Jake Billings" w lines
