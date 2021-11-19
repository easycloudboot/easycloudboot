cmd=$1  #command to run int parallel
parallel_num=$2  #how many processes u want to run

rm -f /tmp/idxfifo
mkfifo /tmp/idxfifo
exec 6<> /tmp/idxfifo

for i in `seq $parallel_num`
do  {

   $cmd
   echo $? > /tmp/idxfifo

} &
done

for i in `seq $parallel_num`
do
    read  -u6 line
    echo $line
done