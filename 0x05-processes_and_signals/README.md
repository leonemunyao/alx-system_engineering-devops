0x05. Processes and signals

PID Defination - A PID (i.e Process Identification Number) is an identification number that is automalically assigned to each project when its created on a Unix-like Operating System. A process is an executing instance of a program. Each process is guaranteed a unique PID, which is always a non-negative number.The process init is the only process that will always have the same PID and that PID is 1

This is because init is always the first process on the system and is the ancestor of all other processes.

The default maximum PID is 32,767. This maximum is important because its essentially the maximum number of processes that can exists simultaneosly on a system
