#PBS -l walltime=00:30:00,nodes=1:ppn=8

cd ~/BasicCourse/Files/day2-1/Problem-class-4/case-11-anim

mpirun -np 8 -machinefile $PBS_NODEFILE pisoFoam -parallel | tee -a log.std


