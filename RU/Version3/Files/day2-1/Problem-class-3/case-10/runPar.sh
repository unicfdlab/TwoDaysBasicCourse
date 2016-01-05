#PBS -l walltime=00:30:00,nodes=1:ppn=8

cd ~/BasicCourse/Files/day2-1/Problem-class-3/case-10

mpirun -np 8 -machinefile $PBS_NODEFILE simpleFoam -parallel | tee -a log.std


