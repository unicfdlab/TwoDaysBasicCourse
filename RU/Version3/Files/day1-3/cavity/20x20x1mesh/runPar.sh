#PBS -l walltime=00:30:00,nodes=1:ppn=8
cd /unicluster/home/matvey.kraposhin/UniCourses/BasicCourse/trunk/Files/day1-3/cavity/20x20x1mesh
#cd ~/BasicCourse/Files/day1-3/cavity/20x20x1mesh

mpirun -np 8 -machinefile $PBS_NODEFILE icoFoam -parallel | tee -a log.std


