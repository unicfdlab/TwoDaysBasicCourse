#PBS -l walltime=00:30:00,nodes=1:ppn=8

cd ~/BasicCourse/Files/day1-3/motorBike

#mpirun -np 8 -machinefile $PBS_NODEFILE pisoFoam -parallel | tee -a log.std


