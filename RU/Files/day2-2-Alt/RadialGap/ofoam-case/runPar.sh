#PBS -l walltime=00:30:00,nodes=1:ppn=8

cd ~/BasicCourse/Files/day2-2-Alt/RadialGap/ofoam-case

mpirun -np 8 -machinefile $PBS_NODEFILE simpleFoam -parallel | tee -a log.std


