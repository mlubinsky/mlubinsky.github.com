![look](Romain_Langlois_FTT.jpeg)


## Comp physics
http://polybook.ru/comma/

https://docs.pybinding.site/en/stable/tutorial/lattice.html

## QuTiP QuTiP: Quantum Toolbox in Python

http://qutip.org/docs/latest/index.html
conda create -n qutip-env
```
# To activate this environment, use
#
#     $ conda activate qutip-env
#
# To deactivate an active environment, use
#
#     $ conda deactivate

(base) [~]$ conda env list
# conda environments:
#
base                  *  /Users/mlubinsky/opt/anaconda3
qutip-env                /Users/mlubinsky/opt/anaconda3/envs/qutip-env

(base) [~]$ conda activate qutip-env


(qutip-env) [~]$ conda config --add channels conda-forge
(qutip-env) [~]$ conda install qutip
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /Users/mlubinsky/opt/anaconda3/envs/qutip-env

  added / updated specs:
    - qutip


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    ca-certificates-2020.6.20  |       hecda079_0         146 KB  conda-forge
    certifi-2020.6.20          |   py38h32f6830_0         151 KB  conda-forge
    libblas-3.8.0              |      17_openblas          11 KB  conda-forge
    libcblas-3.8.0             |      17_openblas          11 KB  conda-forge
    libcxx-10.0.1              |       h5f48129_0         1.0 MB  conda-forge
    libffi-3.2.1               |    hb1e8313_1007          42 KB  conda-forge
    libgfortran-4.0.0          |                3          16 KB  conda-forge
    libgfortran4-7.5.0         |       h1565451_3         776 KB  conda-forge
    liblapack-3.8.0            |      17_openblas          11 KB  conda-forge
    libopenblas-0.3.10         |openmp_h63d9170_4         8.2 MB  conda-forge
    llvm-openmp-10.0.1         |       h28b9765_0         265 KB  conda-forge
    ncurses-6.2                |       hb1e8313_1         902 KB  conda-forge
    numpy-1.19.1               |   py38h8ccc501_2         5.1 MB  conda-forge
    openssl-1.1.1g             |       haf1e3a3_1         1.9 MB  conda-forge
    pip-20.2.3                 |             py_0         1.1 MB  conda-forge
    python-3.8.5               |hfc71d35_7_cpython        12.1 MB  conda-forge
    python_abi-3.8             |           1_cp38           4 KB  conda-forge
    qutip-4.5.2                |   py38hcebb5e4_0         4.4 MB  conda-forge
    readline-8.0               |       h0678c8f_2         255 KB  conda-forge
    scipy-1.5.2                |   py38h1402333_0        19.2 MB  conda-forge
    setuptools-49.6.0          |   py38h32f6830_0         955 KB  conda-forge
    sqlite-3.33.0              |       h960bd1c_0         1.7 MB  conda-forge
    tk-8.6.10                  |       hb0a8c7a_0         3.3 MB  conda-forge
    wheel-0.35.1               |     pyh9f0ad1d_0          29 KB  conda-forge
    xz-5.2.5                   |       haf1e3a3_1         228 KB  conda-forge
    zlib-1.2.11                |    h7795811_1009         102 KB  conda-forge
    ------------------------------------------------------------
                                           Total:        61.8 MB

The following NEW packages will be INSTALLED:

  ca-certificates    conda-forge/osx-64::ca-certificates-2020.6.20-hecda079_0
  certifi            conda-forge/osx-64::certifi-2020.6.20-py38h32f6830_0
  libblas            conda-forge/osx-64::libblas-3.8.0-17_openblas
  libcblas           conda-forge/osx-64::libcblas-3.8.0-17_openblas
  libcxx             conda-forge/osx-64::libcxx-10.0.1-h5f48129_0
  libffi             conda-forge/osx-64::libffi-3.2.1-hb1e8313_1007
  libgfortran        conda-forge/osx-64::libgfortran-4.0.0-3
  libgfortran4       conda-forge/osx-64::libgfortran4-7.5.0-h1565451_3
  liblapack          conda-forge/osx-64::liblapack-3.8.0-17_openblas
  libopenblas        conda-forge/osx-64::libopenblas-0.3.10-openmp_h63d9170_4
  llvm-openmp        conda-forge/osx-64::llvm-openmp-10.0.1-h28b9765_0
  ncurses            conda-forge/osx-64::ncurses-6.2-hb1e8313_1
  numpy              conda-forge/osx-64::numpy-1.19.1-py38h8ccc501_2
  openssl            conda-forge/osx-64::openssl-1.1.1g-haf1e3a3_1
  pip                conda-forge/noarch::pip-20.2.3-py_0
  python             conda-forge/osx-64::python-3.8.5-hfc71d35_7_cpython
  python_abi         conda-forge/osx-64::python_abi-3.8-1_cp38
  qutip              conda-forge/osx-64::qutip-4.5.2-py38hcebb5e4_0
  readline           conda-forge/osx-64::readline-8.0-h0678c8f_2
  scipy              conda-forge/osx-64::scipy-1.5.2-py38h1402333_0
  setuptools         conda-forge/osx-64::setuptools-49.6.0-py38h32f6830_0
  sqlite             conda-forge/osx-64::sqlite-3.33.0-h960bd1c_0
  tk                 conda-forge/osx-64::tk-8.6.10-hb0a8c7a_0
  wheel              conda-forge/noarch::wheel-0.35.1-pyh9f0ad1d_0
  xz                 conda-forge/osx-64::xz-5.2.5-haf1e3a3_1
  zlib               conda-forge/osx-64::zlib-1.2.11-h7795811_1009
```

## Dynamic systems

https://habr.com/ru/company/mailru/blog/513016/

https://habr.com/ru/post/249429/

https://habr.com/ru/company/hsespb/blog/517838/. in C++

##

https://habr.com/ru/post/516206/. QM article

https://habr.com/ru/post/342654/ Autolokebaiya

<https://youtu.be/rO6KySrM1IY> ru

## So you want to learm physics

<https://vk.com/wall-49014451?own=1> books

<https://news.ycombinator.com/item?id=24078420>

<https://news.ycombinator.com/item?id=24088985>


<https://ium.mccme.ru/index.php>

<https://www.youtube.com/watch?v=4zcoOzXtlAo&fbclid=IwAR1c0VXp2Mljpy-5Wj-N7Gq36uuKKZhT4nKjOwlpCuWYfnQiqzPxLGbpiyM>

<https://elementy.ru/nauchno-populyarnaya_biblioteka/zhurnaly>

<https://teach-in.ru/lecture/02-13-Stepanyants>

<https://www.youtube.com/watch?v=skN0WCiNeaI> Dima Shepelyansky

<https://www.youtube.com/watch?v=TGlI3kazeuk>  Методы математической физики. Д. А. Шапиро

<https://www.youtube.com/watch?v=uyPi24Qrj64>

MFTI
<https://www.youtube.com/c/%D0%A4%D0%90%D0%9B%D0%A2%D0%9C%D0%A4%D0%A2%D0%98/playlists> 

<https://arxiv.org/list/physics.ed-ph/recent>

<https://arxiv.org/abs/2002.12118> Simple Relativity Approach to Special Relativity

<https://arxiv.org/abs/1001.1778> Understanding Quaternions and the Dirac Belt Trick

<https://news.ycombinator.com/item?id=23153778>

<https://physics.stackexchange.com/questions/148370/how-to-understand-non-associative-composition-of-velocities-in-str>

<https://physicstravelguide.com/>

<https://demystifyingscience.com/>

<https://www.quantumfieldtheory.info/>

https://news.ycombinator.com/item?id=23690788.  Modelica

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4382372/.  Virus modeling

### QM
<https://habr.com/ru/post/501858/>

<https://nautil.us/issue/83/intelligence/how-to-make-sense-of-quantum-physics>

<https://www.quantamagazine.org/mathematicians-prove-batchelors-law-of-turbulence-20200204/> Turbulence

<https://www.fermatslibrary.com/s/feynmans-proof-of-the-maxwell-equations#email-newsletter>


<https://arxiv.org/abs/2001.04797> Solid state physics


<http://www.damtp.cam.ac.uk/user/tong/kintheory/one.pdf> .  Kinetic Theory

## Maxwell

<https://github.com/photonlines/Intuitive-Guide-to-Maxwells-Equations>

<https://news.ycombinator.com/item?id=23700295>

<https://www.damtp.cam.ac.uk/user/tong/em/dyson.pdf>

<https://news.ycombinator.com/item?id=22810867>

## Chaos
<https://youtu.be/ovJcsL7vyrk>

<https://gereshes.com/2020/01/13/attracted-to-attractors/>

## youtube

https://www.youtube.com/watch?v=ovJcsL7vyrk

https://www.youtube.com/user/EugeneKhutoryansky

https://www.youtube.com/watch?v=WVSWzRdpIHs

https://www.youtube.com/results?search_query=best+physics+channel

https://www.youtube.com/user/MIT


## QED

<https://medium.com/cantors-paradise/when-feynman-met-dirac-fe9cca0006df>

<https://arxiv.org/abs/hep-th/9702027>

## QM

<https://arxiv.org/abs/quant-ph/0702225>

<https://arxiv.org/pdf/quant-ph/0702225.pdf>
