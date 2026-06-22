## Group Theory

An **abelian group** is a group in which the operation is **commutative**.

That is, for all elements (a) and (b),

[
a b = b a.
]

The name comes from the Norwegian mathematician **Niels Henrik Abel**.

### Definition

A set (G) with an operation (\cdot) is an abelian group if:

1. **Closure**:
   [
   a,b\in G \implies a\cdot b\in G
   ]

2. **Associativity**:
   [
   (a\cdot b)\cdot c = a\cdot(b\cdot c)
   ]

3. **Identity element** (e):
   [
   a\cdot e = e\cdot a = a
   ]

4. **Inverse element**:
   [
   \forall a\in G,\ \exists a^{-1}\in G,\quad
   a\cdot a^{-1}=a^{-1}\cdot a=e
   ]

5. **Commutativity**:
   [
   a\cdot b=b\cdot a.
   ]

### Examples

#### Integers under addition

[
(\mathbb Z,+)
]

* Identity: (0)
* Inverse of (n): (-n)
* Commutative because

[
m+n=n+m.
]

#### Real numbers under addition

[
(\mathbb R,+)
]

is abelian.

#### Nonzero real numbers under multiplication

[
(\mathbb R^\times,\cdot)
]

is abelian.

#### Circle group

[
S^1={z\in\mathbb C:|z|=1}
]

under complex multiplication is abelian.

### Non-example

The group of invertible matrices

[
GL(n,\mathbb R)
]

for (n\ge 2) is generally **not** abelian because matrix multiplication does not commute:

[
AB \ne BA.
]

For example,

[
A=
\begin{pmatrix}
1&1\
0&1
\end{pmatrix},
\quad
B=
\begin{pmatrix}
1&0\
1&1
\end{pmatrix}
]

satisfy (AB\neq BA).

### Why abelian groups matter

Abelian groups are the simplest and most completely understood groups. They appear everywhere:

* vector spaces (under addition),
* Fourier analysis,
* algebraic topology (homology groups),
* number theory,
* quantum mechanics.

In fact, every finite abelian group can be decomposed into cyclic pieces. This is the **Fundamental Theorem of Finite Abelian Groups**:

[
G \cong \mathbb Z_{n_1}\times \mathbb Z_{n_2}\times\cdots\times \mathbb Z_{n_k}.
]

For example,

[
\mathbb Z_{12}
\cong
\mathbb Z_3 \times \mathbb Z_4.
]

A useful way to think about it:

* **Abelian group** = "addition-like" behavior ((a+b=b+a)).
* **Non-abelian group** = "rotation-like" behavior, where the order of operations matters. For example, rotations of a cube in 3D form a non-abelian group.


A **compact group** is a group that is also a **compact topological space**.

More precisely:

* A **group** is a set with an operation satisfying closure, associativity, identity, and inverses.
* A **topological group** is a group equipped with a topology such that:

  * multiplication ((x,y)\mapsto xy) is continuous, and
  * inversion (x\mapsto x^{-1}) is continuous.
* A **compact group** is a topological group whose underlying topological space is compact.

In simple terms, compactness means the space is “finite in extent” in a topological sense.

### Examples

1. **Finite groups**

   * Any finite group with the discrete topology is compact.

2. The **circle group**
   [
   S^1={z\in \mathbb{C}: |z|=1}
   ]
   under complex multiplication.

   S^1={z\in\mathbb{C}:|z|=1}

3. The group of orthogonal matrices
   [
   O(n)={A\in M_n(\mathbb{R}) : A^TA=I}
   ]
   which is compact inside (\mathbb{R}^{n^2}).

   O(n)={A\in M_n(\mathbb{R}):A^TA=I}

4. The unitary group
   [
   U(n)={A\in M_n(\mathbb{C}) : A^*A=I}
   ]

### Non-examples

* ((\mathbb{R},+)) is not compact.
* ((\mathbb{Z},+)) with the discrete topology is not compact.

### Why compact groups are important

Compact groups play a central role in:

* harmonic analysis,
* representation theory,
* quantum physics,
* Lie theory.

A key property is the existence of a unique translation-invariant probability measure called the **Haar measure**.

If you'd like, I can also explain:

* compact Lie groups,
* why (O(n)) is compact,
* Haar measure,
* or the difference between compact and locally compact groups.


## Теория групп. (Алексей Савватеев)

<https://teach-in.ru/course/group-theory-manukhov>

https://www.youtube.com/playlist?list=PLsdv2rpSb41YX3GXvKg7YQOwl-MVNkz9H


https://www.youtube.com/watch?v=ihoATq9jSlQ  Лекция 1 

https://www.youtube.com/watch?v=cEC7gPN441w  Лекция 2

https://www.youtube.com/watch?v=m0Fz88VtTKc 3

https://www.youtube.com/watch?v=OgQSmqZABVY 4 

https://www.youtube.com/watch?v=OraV8VbFzrQ 5 

https://www.youtube.com/watch?v=obXICujbJMw 6

https://www.youtube.com/watch?v=ytRgMCC2DN0 7 

### Основы высшей алгебры и теории кодирования (1 курс, весна 2022) - Лектор: Вялый М.Н.


https://www.youtube.com/watch?v=aF0amljoZk4&list=PL4_hYwCyhAvZQoUsDe17ZGXIxcG3O84RG

https://publications.hse.ru/mirror/pubs/share/direct/433420486.pdf


### Lie groups in physics
https://arxiv.org/pdf/2012.00834.pdf

https://www.youtube.com/watch?v=w-HygD3yLho

## Lie Group

A **Lie group** (pronounced *"Lee group"*, after Sophus Lie) is a mathematical object that is simultaneously:

1. A **group** (it has a multiplication, identity, inverses), and
2. A **smooth manifold** (locally it looks like (\mathbb{R}^n), and you can do calculus on it).

Moreover, the group operations must be smooth:

[
(x,y)\mapsto xy
]

and

[
x\mapsto x^{-1}
]

are differentiable maps.

---

## Intuition

A Lie group describes **continuous symmetries**.

Examples:

* Rotations of a circle
* Rotations of 3D space
* Translations of space
* Lorentz transformations in relativity
* Gauge symmetries in particle physics

Whenever a symmetry depends on continuously varying parameters, a Lie group is usually involved.

---

## Example 1: Circle group (U(1))

The set

[
U(1)={e^{i\theta}: \theta\in\mathbb{R}}
]

forms a group under multiplication.

Geometrically it is a circle:

[
S^1.
]

Each element is determined by one parameter (\theta).

So:

* Group structure: multiplication of complex numbers.
* Manifold structure: a 1-dimensional circle.

Therefore (U(1)) is a 1-dimensional Lie group.

![Image](https://images.openai.com/static-rsc-4/R1C5O9B-uVYDxApln1y1NLZ-7w1tdj-hWenMg-pTTtelMaDrgic-YoErjQySiqNhOPpnRKra_g0oC_69F4v4yJeZnRPDINsQpsapltOg2bmBqGs-482TKqpLPM7j7tgBJHRibhD-bQ3z11rHBFc9CheLJ68f77J7m21B6k_MzVE-ffih9ZpSV88ZmwClIRAf?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/ssh1mkSp4ej0s7hBgL-lDvjrxbYPdo2GgEOLfvvJaaW3LJzt98ww2Kch-7j8Dpv4uCmTw4Qwu9YQrlOZ3ifwUEYNfPs2VOaO_AeehdRqvA1eqjqictYmocxXIR1DtR5Ee-cIxRC8DGIEJT4gofIgfoML-m04yVOUsXOzm4QjPulaOoVQPfL19cnlNjefasbs?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/yznlhqWL2FINYn2ka_naxpvNtY3sUxJzIM-4Wjk0e6cdnB2u-amwa8flVzwrId-3gVzrD0uyWL-wrS1MpGQ_Miq4bxFoSZydnu1TzZfIUml2J4nmKJEa69A3nK1LzNLkUnKbmmAEqKekD4p_Hqe8J8uMVrQRer6luSa6H0Rx85fhAUm2Anb5MnWDGnnMK_O4?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/_yow6aWBwp4IJ5BB9H1AS__qjook1vXuWauzFWnSuxHNnvD-RYWjUu2Jq5iNAH3KYkyPUqv0S2CvqWm1vsWTeoH6Ag0ZeJ8pGcB26N8OCL7U82TGtbFO5p1F827dEVb0fdXPTOyIOjt2p0I6P2_ZozAdUU19YD6BhaqvEHBe94vX9Wf-gV_gHhhrDpbTNFF5?purpose=fullsize)

---

## Example 2: Rotations in the plane

Every rotation can be written as

[
R(\theta)=
\begin{pmatrix}
\cos\theta & -\sin\theta\
\sin\theta & \cos\theta
\end{pmatrix}.
]

The set of all such matrices is

[
SO(2).
]

This is also a 1-dimensional Lie group.

---

## Example 3: Rotations in 3D

The group

[
SO(3)
]

consists of all (3\times3) rotation matrices.

Each rotation depends on three independent parameters.

Thus:

[
\dim SO(3)=3.
]

This group describes the rotational symmetry of ordinary space.

![Image](https://images.openai.com/static-rsc-4/i4S2kdVPaa10_K6RdMfNvddXkaiC42m_XkC4X40Ttg4YasGNVWUih6q_gLaIjbr7LIcvGwg7YPOckPeJ0xxkSGPmrYL5Qvz1Heu7XmcGBlX7wvizTjlvfq6JWABpT4-ARCsRE6Bh5fFHURomirRbBC1B3ss9HMsEtfBnHxNWqrhRtmjAlQ0sVqwH-5GKebDi?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/6Uz2y9pgMo4bx4OOJIr0QDa276YqSgMcslF2RMa_cI4yRkhu7zPTz7BQs75rXnxYVugMBLp9VB740eX6al9xKgHGJpYW0OMHRaQosxzquMwC48to4eqPGW28DOBW6CEo33jYN7jCJnzMdmiKaF2qgeuDVbduAt9979l2pQp_GrWuTYDds9Wz_y8-u89Ymc5p?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/cajxgOc7ahfL0thWN8-VVVsqZyEPobsbI1nu0wx6U_mikwj8fAR465PuLwPU4JHTTyeLXzT68qB0apwcSw5hnwep1F3aoq_AqexTqgLL8hL1N3lbBu_nlB1DM-q8jHKV2pz93ftAW2Ndn2fFiIOnP5CEaiwo3CM2aYsgK7Liq2ihoh5Glnh3k0c699ABAtfY?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/tjk2VbGUHvMWilSkk3UyQmfpY25tby8sbDeuAEZxwjxXX-Xra6owdd5EWqImGZPa9m4ksmscqxPARRclQOCyT56Nou_9NmFa_h3vJGsAGsoW-tak8ebYn4jNgZIfh2AzfNsIz20xCZUluaNzwfuBq3L9-Fnp_qKBesFU3G-eibmAcxQnrm5kYo_88EO_qIcd?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/7_Og9s7uwoOroFKbZh4f_lMpcnxfzh96QOlqxHC1rgaBjpRtaq7epSybLYHXBDwS1n-PUyQdyH-ibEomB9ul8znw64MtxfUDbDu60CNq7rOjTz5Lr67wE-DMU9eFiS_VQDT0saeNR1JNmje7oCmEBxRWXn_pYixJAv0L3apjRu6xV8CQp37tp8kQzEuJpfdD?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/oLugUY5il2ymuH1novu0E1CHCKAP_Ko6YRqDw51aZfYF8v4JpPqrX08VEAKpKyFLBJhQyJc-7p5vv_uEIjNra7wolB5Iu5MjmY_SzQHyUfb49krvR0LsXlD2CnZUL05Z_dxaLthCUQ5knJ_9gDeSpLlUeXxlgkeDjzQLT58EqfnNeCeyFOKx6U2XGsepvXEE?purpose=fullsize)

---

## Matrix Lie Groups

Many important Lie groups are groups of matrices:

| Group             | Meaning                  | Dimension  |
| ----------------- | ------------------------ | ---------- |
| (GL(n,\mathbb R)) | invertible real matrices | (n^2)      |
| (SL(n,\mathbb R)) | determinant (1) matrices | (n^2-1)    |
| (O(n))            | orthogonal matrices      | (n(n-1)/2) |
| (SO(n))           | rotations                | (n(n-1)/2) |
| (U(n))            | unitary matrices         | (n^2)      |
| (SU(n))           | special unitary matrices | (n^2-1)    |

---

## Lie Algebra

One of Lie's great discoveries was that a Lie group can be studied by looking at its behavior near the identity element.

The infinitesimal version of a Lie group is its **Lie algebra**.

For example:

[
SO(3)
]

has Lie algebra

[
\mathfrak{so}(3),
]

which describes infinitesimal rotations.

Physicists often work with generators rather than full group elements.

For rotations:

[
R(\theta)
=========

e^{\theta J}
]

where (J) is a generator.

This is analogous to

[
e^{itH}
]

in quantum mechanics.

---

## Why Lie groups matter in physics

They describe nearly every fundamental symmetry:

| Physics            | Lie Group      |
| ------------------ | -------------- |
| Electromagnetism   | (U(1))         |
| Weak interaction   | (SU(2))        |
| Strong interaction | (SU(3))        |
| Rotations          | (SO(3))        |
| Relativity         | Lorentz group  |
| Quantum states     | Unitary groups |

The Standard Model gauge symmetry is

[
SU(3)\times SU(2)\times U(1).
]

---

## Compact vs Non-compact Lie Groups

Examples of **compact** Lie groups:

* (U(1))
* (SO(3))
* (SU(2))

Examples of **non-compact** Lie groups:

* ((\mathbb R,+))
* (GL(n,\mathbb R))
* Lorentz group

Compact Lie groups have finite volume (with Haar measure) and especially nice representation theory.

### One-sentence summary

A **Lie group** is a group of continuous symmetries that is also a smooth geometric space, allowing algebra and calculus to be used together. It is the mathematical language of symmetry in geometry, physics, and differential equations.


The phrase **"free parameters"** is not a standard concept in abstract group theory, but it appears in several related contexts.

### 1. Free parameters in a Lie group

For continuous groups (Lie groups), the elements can be described by a certain number of continuous parameters.

Examples:

* The circle group (U(1)):
  [
  e^{i\theta}
  ]
  has **one free parameter** (\theta).

* The rotation group (SO(3)):
  every rotation can be described by an axis (2 parameters) and an angle (1 parameter), so it has **3 free parameters**.

* The unitary group (U(n)) has (n^2) real parameters.

In this context, "free parameters" means the number of independent continuous coordinates needed to specify a group element.

---

### 2. Free generators in a free group

Perhaps you mean a **free group**.

A free group on generators

[
F(a,b,c)
]

has no relations except those required by the group axioms.

The generators (a,b,c) are sometimes informally called "free parameters" because they can be combined arbitrarily.

Example:

[
a^2 b^{-1} c a
]

is a valid element of (F(a,b,c)).

The only simplifications are things like

[
a a^{-1} = e.
]

---

### 3. Parameters in a group presentation

A group may be defined by generators and relations:

[
G = \langle a,b \mid a^2=e,\ b^3=e \rangle.
]

Here (a) and (b) are generators, and the relations constrain them.

If there are fewer relations, there is more "freedom."

---

### 4. Degrees of freedom in matrix groups

Consider

[
SO(2)=
\left{
\begin{pmatrix}
\cos\theta & -\sin\theta\
\sin\theta & \cos\theta
\end{pmatrix}
\right}.
]

A (2\times2) matrix has 4 entries, but the orthogonality conditions force all entries to depend on a single parameter (\theta).

So (SO(2)) has **one free parameter**.

Similarly:

| Group   | Number of free parameters |
| ------- | ------------------------- |
| (SO(2)) | 1                         |
| (SO(3)) | 3                         |
| (SU(2)) | 3                         |
| (U(n))  | (n^2)                     |
| (SU(n)) | (n^2-1)                   |

---

If your question comes from physics (Lie groups, gauge theory, quantum mechanics), then "free parameters" usually means **the dimension of the Lie group**—the number of independent continuous variables needed to specify an element. If it comes from algebra, you may be referring to **free groups** and **free generators**.


### LightCone

https://www.youtube.com/watch?v=wA8Wa2zAJ3E&list=PLnbH8YQPwKblIpRi0ARO2VadnMwntvF51&pp=iAQB


https://www.youtube.com/watch?v=wTdO_N0qGg4


https://www.youtube.com/watch?v=ajkof5THayg Лекция №1 по Теории групп. Смежные классы. Теорема Лагранжа. Богданов И.И.

https://www.youtube.com/watch?v=ajkof5THayg



https://www.youtube.com/playlist?list=PLi01XoE8jYoi3SgnnGorR_XOW3IcK-TP6
