#PBS -l walltime=00:30:00,nodes=1:ppn=8

cd ~/BasicCourse/Files/day1-3/cavity/20x20x1mesh

mpirun -np 8 -machinefile $PBS_NODEFILE buoyantPimpleFoam -parallel | tee -a log.std


