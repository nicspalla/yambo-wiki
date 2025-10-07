# Rome 2023

A general description of the goal(s) of the school can be found on the
[Yambo main
website](https://www.yambo-code.eu/2023/02/18/yambo-school-2023/)

## Use CINECA computational resources {#use_cineca_computational_resources}

Yambo tutorials will be run on the MARCONI100 (M100) accelerated
cluster. You can find info about M100
[here](https://wiki.u-gov.it/confluence/display/SCAIUS/UG3.2%3A+MARCONI100+UserGuide#UG3.2:MARCONI100UserGuide).
In order to access computational resources provided by CINECA you need
your personal username and password that were sent you by the
organizers.

### Connect to the cluster using ssh {#connect_to_the_cluster_using_ssh}

You can access M100 via `ssh` protocol in different ways.

**- Connect using username and password**

Use the following command replacing your username:

`$ ssh username@login.m100.cineca.it`

However, in this way you have to type your password each time you want
to connect.

**- Connect using ssh key**

You can setup a ssh key pair to avoid typing the password each time you
want to connect to M100. To do so, go to your `.ssh` directory (usually
located in the `home` directory):

`$ cd $HOME/.ssh`

If you don\'t have this directory, you can create it with
`mkdir $HOME/.ssh`.

Once you are in the `.ssh` directory, run the `ssh-keygen` command to
generate a private/public key pair:

`$ ssh-keygen`\
`Generating public/private rsa key pair.`\
`Enter file in which to save the key: m100_id_rsa`\
`Enter passphrase (empty for no passphrase): `\
`Enter same passphrase again: `\
`Your identification has been saved in <your_.ssh_dir>/m100_id_rsa`\
`Your public key has been saved in <your_.ssh_dir>/m100_id_rsa.pub`\
`The key fingerprint is:`\
`<...>`\
`The key's randomart image is:`\
`<...>`

Now you need to copy the **public** key to M100. You can do that with
the following command (for this step you need to type your password):

`$ ssh-copy-id -i <your_.ssh_dir>/m100_id_rsa.pub ``<username>`{=html}`@login.m100.cineca.it`

Once the public key has been copied, you can connect to M100 without
having to type the password using the `-i` option:

`$ ssh -i <your_.ssh_dir>/m100_id_rsa username@login.m100.cineca.it`

To simplify even more, you can paste the following lines in a file named
`config` located inside the `.ssh` directory adjusting username and
path:

`Host m100 `\
` HostName login.m100.cineca.it`\
` User username`\
` IdentityFile <your_.ssh_dir>/m100_id_rsa`

With the `config` file setup you can connect simply with

`$ ssh m100`

### General instructions to run tutorials {#general_instructions_to_run_tutorials}

Before proceeding, it is useful to know the different workspaces you
have available on M100, which can be accessed using environment
variables. The main ones are:

- `$HOME`: it\'s the `home` directory associated to your username;
- `$WORK`: it\'s the `work` directory associated to the account where
  the computational resources dedicated to this school are allocated;
- `$CINECA_SCRATCH`: it\'s the `scratch` directory associated to your
  username.

You can find more details about storage and FileSystems
[here](https://wiki.u-gov.it/confluence/display/SCAIUS/UG2.5%3A+Data+storage+and+FileSystems).

Please don\'t forget to **run all tutorials in your scratch directory**:

`$ echo $CINECA_SCRATCH`\
`/m100_scratch/userexternal/username`\
`$ cd $CINECA_SCRATCH`

Computational resources on M100 are managed by the job scheduling system
[Slurm](https://slurm.schedmd.com/overview.html). Most part of Yambo
tutorials during this school can be run in serial, except some that need
to be executed on multiple processors. Generally, Slurm batch jobs are
submitted using a script, but the tutorials here are better understood
if run interactively. The two procedures that we will use to submit
interactive and non interactive jobs are explained below.

**- Run a job using a batch script**

This procedure is suggested for the tutorials and examples that need to
be run in parallel. In these cases you need to submit the job using a
batch script `job.sh`. Please note that the instructions in the batch
script must be compatible with the specific M100
[architecture](https://wiki.u-gov.it/confluence/display/SCAIUS/UG3.2%3A+MARCONI100+UserGuide#UG3.2:MARCONI100UserGuide-SystemArchitecture)
and
[accounting](https://wiki.u-gov.it/confluence/display/SCAIUS/UG3.2%3A+MARCONI100+UserGuide#UG3.2:MARCONI100UserGuide-Accounting)
systems. The complete list of Slurm options can be found
[here](https://slurm.schedmd.com/sbatch.html). However you will find
**ready-to-use** batch scripts in locations specified during the
tutorials.

To submit the job, use the `sbatch` command:

`$ sbatch job.sh`\
`Submitted batch job ``<JOBID>`{=html}

To check the job status, use the `squeue` command:

`$ squeue -u ``<username>`{=html}\
`             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)`\
`             <...>  m100_...      JOB username  R       0:01    ``<N>`{=html}` <...>`

If you need to cancel your job, do:

`$ scancel ``<JOBID>`{=html}` `

**- Open an interactive session**

This procedure is suggested for most of the tutorials, since the
majority of these is meant to be run in serial (relatively to MPI
parallelization) from the command line. Use the command below to open an
interactive session of 1 hour (complete documentation
[here](https://slurm.schedmd.com/salloc.html)):

`$ salloc -A tra23_Yambo -p m100_sys_test -q qos_test --reservation=s_tra_yambo --nodes=1 --ntasks-per-node=1 --cpus-per-task=4 -t 01:00:00`\
`salloc: Granted job allocation 10164647`\
`salloc: Waiting for resource configuration`\
`salloc: Nodes r256n01 are ready for job`

We ask for 4 cpus-per-task because we can exploit OpenMP parallelization
with the available resources.

With `squeue` you can see that there is now a job running:

`$ squeue -u username`\
`             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)`\
`          10164647 m100_usr_ interact username  R       0:02      1 r256n01`

To run the tutorial, `ssh` into the node specified by the job allocation
and `cd` to your scratch directory:

`username@`**`login02`**`$ ssh r256n01`\
`...`\
`username@`**`r256n01`**`$ cd $CINECA_SCRATCH`

Then, you need to manually load `yambo` as in the batch script above.
Please note that the serial version of the code is in a different
directory and does not need `spectrum_mpi`:

`$ module purge`\
`$ module load hpc-sdk/2022--binary spectrum_mpi/10.4.0--binary`\
`$ export PATH=/m100_work/tra23_Yambo/softwares/YAMBO/5.2-cpu/bin:$PATH`

Finally, set the `OMP_NUM_THREADS` environment variable to 4 (as in the
`--cpus-per-task` option):

`$ export OMP_NUM_THREADS=4`

To close the interactive session when you have finished, log out of the
compute node with the `exit` command, and then cancel the job:

`$ exit`\
`$ scancel ``<JOBID>`{=html}

**- Plot results with gnuplot**

During the tutorials you will often need to plot the results of the
calculations. In order to do so on M100, **open a new terminal window**
and connect to M100 enabling X11 forwarding with the `-X` option:

`$ ssh -X m100`

Please note that `gnuplot` can be used in this way only from the login
nodes:

`username@`**`login01`**`$ cd ``<directory_with_data>`{=html}\
`username@`**`login01`**`$ gnuplot`\
`...`\
`Terminal type is now '...'`\
`gnuplot> plot <...>`

**- Set up yambopy**

In order to run yambopy on m100, you must first setup the conda
environment (to be done only once):

`$ cd`\
`$ module load anaconda/2020.11`\
`$ conda init bash`\
`$ source .bashrc`

After this, every time you want to use yambopy you need to load its
module and environment:

`$ module load anaconda/2020.11`\
`$ conda activate /m100_work/tra23_Yambo/softwares/YAMBO/env_yambopy`

## Tutorials

Quick recap. Before every tutorial, if you run on m100, do the following
steps

`ssh m100`\
`cd $CINECA_SCRATCH`\
`mkdir YAMBO_TUTORIALS `**`(Only if you didn't before)`**\
`cd YAMBO_TUTORIALS`

At this point you can download the needed files for the tutorial. After
you can open the interactive session and login into the node

`salloc -A tra23_Yambo -p m100_sys_test -q qos_test --reservation=s_tra_yambo --nodes=1 --ntasks-per-node=1 --cpus-per-task=4 -t 04:00:00`\
`ssh `**`PUT HERE THE ASSIGNED NODE NAME AFTER salloc COMMAND`**\
`module purge`\
`module load hpc-sdk/2022--binary spectrum_mpi/10.4.0--binary`\
`export PATH=/m100_work/tra23_Yambo/softwares/YAMBO/5.2-cpu/bin:$PATH`\
`cd $CINECA_SCRATCH`\
`cd YAMBO_TUTORIALS `

### DAY 1 - Monday, 22 May {#day_1___monday_22_may}

**16:15 - 18:30 From the DFT ground state to the complete setup of a
Many Body calculation using Yambo**

To get the tutorial files needed for the following tutorials, follow
these steps:

`$ wget `[`https://media.yambo-code.eu/educational/tutorials/files/hBN.tar.gz`](https://media.yambo-code.eu/educational/tutorials/files/hBN.tar.gz)\
`$ wget `[`https://media.yambo-code.eu/educational/tutorials/files/hBN-2D.tar.gz`](https://media.yambo-code.eu/educational/tutorials/files/hBN-2D.tar.gz)\
`$ ls`\
`hBN-2D.tar.gz  hBN.tar.gz`\
`$ tar -xvf hBN-2D.tar.gz`\
`$ tar -xvf hBN.tar.gz`\
`$ ls`\
**`hBN-2D`**` `**`hBN`**` hBN-2D.tar.gz  hBN.tar.gz`

Now that you have all the files, you may open the interactive job
session with `salloc` as explained above and proceed with the tutorials.


At this point, you may learn about the python pre-postprocessing
capabilities offered by yambopy, our python interface to yambo and QE.
First of all, let\'s create a dedicated directory, download and extract
the related files.

`$ cd $CINECA_SCRATCH`\
`$ mkdir YAMBOPY_TUTORIALS`\
`$ cd YAMBOPY_TUTORIALS`\
`$ wget `[`https://media.yambo-code.eu/educational/tutorials/files/databases_yambopy.tar`](https://media.yambo-code.eu/educational/tutorials/files/databases_yambopy.tar)\
`$ tar -xvf databases_yambopy.tar`\
`$ cd databases_yambopy`

Then, follow **the first three sections** of this link, which are
related to initialization and linear response.


### DAY 2 - Tuesday, 23 May {#day_2___tuesday_23_may}

**14:00 - 16:30 A tour through GW simulation in a complex material (from
the blackboard to numerical computation: convergence, algorithms,
parallel usage)**

To get all the tutorial files needed for the following tutorials, follow
these steps:

`wget `[`https://media.yambo-code.eu/educational/tutorials/files/hBN.tar.gz`](https://media.yambo-code.eu/educational/tutorials/files/hBN.tar.gz)\
`wget `[`https://media.yambo-code.eu/educational/tutorials/files/MoS2_2Dquasiparticle_tutorial.tar.gz`](https://media.yambo-code.eu/educational/tutorials/files/MoS2_2Dquasiparticle_tutorial.tar.gz)\
`tar -xvf hBN.tar.gz`\
`tar -xvf MoS2_2Dquasiparticle_tutorial.tar.gz`\
`cd hBN`

Now you can start the first tutorial:


If you have gone through the first tutorial, pass now to the second one:

`cd $CINECA_SCRATCH`\
`cd YAMBO_TUTORIALS`\
`cd MoS2_HPC_tutorial`


To conclude, you can learn an other method to plot the band structure in
Yambo


### DAY 3 - Wednesday, 24 May {#day_3___wednesday_24_may}

**14:00 - 16:30 Bethe-Salpeter equation (BSE)** Fulvio Paleari
(CNR-Nano, Italy), Davide Sangalli (CNR-ISM, Italy)

To get the tutorial files needed for the following tutorials, follow
these steps:

`$ wget `[`https://media.yambo-code.eu/educational/tutorials/files/hBN.tar.gz`](https://media.yambo-code.eu/educational/tutorials/files/hBN.tar.gz)` # NOTE: YOU SHOULD ALREADY HAVE THIS FROM DAY 1`\
`$ wget `[`https://media.yambo-code.eu/educational/tutorials/files/hBN-convergence-kpoints.tar.gz`](https://media.yambo-code.eu/educational/tutorials/files/hBN-convergence-kpoints.tar.gz)` `\
`$ tar -xvf hBN-convergence-kpoints.tar.gz`\
`$ tar -xvf hBN.tar.gz`

Now, you may open the interactive job session with `salloc` and proceed
with the following tutorials.

Now, go into the yambopy tutorial directory to learn about python
analysis tools for the BSE:

`$ cd $CINECA_SCRATCH`\
`$ cd YAMBOPY_TUTORIALS/databases_yambopy`

**17:00 - 18:30 Bethe-Salpeter equation in real time (TD-HSEX)** Fulvio
Paleari (CNR-Nano, Italy), Davide Sangalli (CNR-ISM, Italy)

The files needed for the following tutorials can be downloaded following
these steps:

`$ wget `[`https://media.yambo-code.eu/educational/tutorials/files/hBN-2D-RT.tar.gz`](https://media.yambo-code.eu/educational/tutorials/files/hBN-2D-RT.tar.gz)\
`$ tar -xvf hBN-2D-RT.tar.gz`


### DAY 4 - Thursday, May 25 {#day_4___thursday_may_25}

**14:00 - 16:30 Real-time approach with the time dependent berry phase**
Myrta Gruning (Queen\'s University Belfast), Davide Sangalli (CNR-ISM,
Italy)

For the tutorials we will use first the `hBN-2D-RT` folder (k-sampling
10x10x1) and then the `hBN-2D` folder (k-sampling 6x6x1) You may already
have them in the `YAMBO_TUTORIALS` folder

`$ ls`\
**`hBN-2D`**` `**`hBN-2D-RT`**` hBN-2D.tar.gz  hBN-2D-RT.tar.gz`

If you need to downoload again the tutorial files, follow these steps:

`$ wget `[`https://media.yambo-code.eu/educational/tutorials/files/hBN-2D.tar.gz`](https://media.yambo-code.eu/educational/tutorials/files/hBN-2D.tar.gz)\
`$ wget `[`https://media.yambo-code.eu/educational/tutorials/files/hBN-2D-RT.tar.gz`](https://media.yambo-code.eu/educational/tutorials/files/hBN-2D-RT.tar.gz)\
`$ tar -xvf hBN-2D.tar.gz`\
`$ tar -xvf hBN-2D-RT.tar.gz`


<!-- -->


### DAY 5 - Friday, 26 May {#day_5___friday_26_may}

## Lectures

### DAY 1 - Monday, 22 May {#day_1___monday_22_may_1}

- D. Varsano, [Description and goal of the
  school](https://media.yambo-code.eu/educational/Schools/ROME2023/scuola_intro.pdf).
- G. Stefanucci, [The Many-Body Problem: Key concepts of the Many-Body
  Perturbation
  Theory](https://media.yambo-code.eu/educational/Schools/ROME2023/Stefanucci.pdf)
- M. Marsili, [Beyond the independent particle scheme: The linear
  response
  theory](https://media.yambo-code.eu/educational/Schools/ROME2023/marghe_linear_response.pdf)

### DAY 2 - Tuesday, 23 May {#day_2___tuesday_23_may_1}

- E. Perfetto, [An overview on non-equilibrium Green
  Functions](https://media.yambo-code.eu/educational/Schools/ROME2023/Talk_Perfetto.pdf)
- R. Frisenda, [ARPES spectroscopy, an experimental
  overview](https://media.yambo-code.eu/educational/Schools/ROME2023/FRISENDA%20-%20ARPES%20spectroscopy,%20an%20experimental%20overview.pdf)
- A. Marini, [The Quasi Particle concept and the GW
  method](https://media.yambo-code.eu/educational/Schools/ROME2023/GW_marini.pdf)
- A. Guandalini, [The GW method: approximations and
  algorithms](https://media.yambo-code.eu/educational/Schools/ROME2023/alberto_guandalini.pdf)
- D.A. Leon, C. Cardoso, [Frequency dependence in GW: origin, modelling
  and practical
  implementations](https://media.yambo-code.eu/educational/Schools/ROME2023/Cardoso_YamboSchool2023_Rome.pdf)

### DAY 3 - Wednesday, 24 May {#day_3___wednesday_24_may_1}

- A. Molina-Sánchez, [Modelling excitons: from 2D materials to Pump and
  Probe
  experiments](https://media.yambo-code.eu/educational/Schools/ROME2023/yambo-talk-alejandro.pdf)
- M. Palummo, [The Bethe-Salpeter equation: derivations and main
  physical
  concepts](https://media.yambo-code.eu/educational/Schools/ROME2023/Palummo_YSCHOOL2023.pdf)
- F. Paleari, [Real time approach to the Bethe-Salpeter
  equation](https://media.yambo-code.eu/educational/Schools/ROME2023/Yambo2023_FulvioPaleari.pdf)
- D. Sangalli, [TD-HSEX and real-time
  dynamics](https://www.yambo-code.eu/wiki/index.php/File:RealTime_Propagation_Lecture.pdf)

### DAY 4 - Thursday, 25 May {#day_4___thursday_25_may}

- S. Mor, [Time resolved spectroscopy: an experimental
  overview](https://media.yambo-code.eu/educational/Schools/ROME2023/Yamboschool2023_mor.pdf)
- M. Grüning, [Nonlinear optics within Many-Body Perturbation
  Theory](https://media.yambo-code.eu/educational/Schools/ROME2023/myrta_Nonlinear_Yschool.pdf)
- N. Tancogne-Dejean, [Theory and simulation of High Harmonics
  Generation](https://media.yambo-code.eu/educational/Schools/ROME2023/Yamboschool2023_NicolasTancogne-Dejean.pdf)
- Y. Pavlyukh, [Coherent electron-phonon dynamics within a time-linear
  GKBA
  scheme](https://media.yambo-code.eu/educational/Schools/ROME2023/yaroslav_Coherent_eph_dynamicsMS.pdf)
