https://www.youtube.com/watch?v=P0xUb-rRxU4

https://en.wikipedia.org/wiki/Exome

https://en.wikipedia.org/wiki/DNA_microarray

https://habr.com/ru/articles/452622/
https://habr.com/ru/articles/137069/
https://habr.com/ru/companies/epam_systems/articles/337892/

https://www.genenames.org/

https://www.youtube.com/watch?v=cBDZSGf9HRE Variant Calling Format VCF

DNA Sample -> sequencing -> Raw Sequence FASFA/FANTQ -> alignment -> Aligned reads (BAM SAM) -> variant calling -> Carian Call (VCF)


https://www.youtube.com/watch?v=Kfs6xgGn6Pc ChIP-Seq files - BigWig (Wiggle) and BED/bigBed

https://habr.com/ru/articles/137082/ Практическая биоинформатика ч.2.
https://habr.com/ru/articles/137267/ Практическая биоинформатика ч.3.
https://habr.com/ru/articles/137453/ Практическая биоинформатика ч.4.
https://habr.com/ru/articles/137626/ Практическая биоинформатика ч.5.
https://habr.com/ru/articles/138486/ Алгоритмы в биоинформатике ч.1
https://habr.com/ru/articles/221813/ Сравнение биологических последовательностей

https://habr.com/ru/companies/JetBrains-education/articles/238759/

https://habr.com/ru/articles/115641/
https://habr.com/ru/articles/385865/
https://habr.com/ru/articles/48533/
https://habr.com/ru/articles/378545/

https://habr.com/ru/articles/181850/

https://rosalind.info/problems/locations/ Структура белка: введение для айтишников
https://habr.com/ru/articles/170429/  Браузеры генома
https://habr.com/ru/companies/stepic/articles/196870/

https://habr.com/ru/articles/412453/
https://bioinformaticsinstitute.ru/sites/default/files/grigorev_-_tehnologii_sekvenirovaniya_compressed.pdf
https://bioinformaticsinstitute.ru/sites/default/files/ramensky2017summer.pdf
https://bioinformaticsinstitute.ru/sites/default/files/sequoia_0.pdf 
https://habr.com/ru/articles/448376/


https://habr.com/ru/articles/443526/  От алгоритмов до рака: лекции со школы по биоинформатике
https://habr.com/ru/articles/153305/ Видеолекции по биоинформатике
https://habr.com/ru/articles/198784/ Видеолекции по биоинформатике

https://vimeo.com/30294283 Многомерный анализ microarray данных
https://vimeo.com/30295235 Технологии ChIP-seq и компьютерный анализ геномных профилей связывания

https://en.wikipedia.org/wiki/DNA_sequencing
https://en.wikipedia.org/wiki/ChIP_sequencing 
https://en.wikipedia.org/wiki/RNA-Seq
```
ДНК — это полимерная цепь, состоящая из мономеров четырех типов, называемых нуклеотидами, 
The DNA alphabet only has four letters: A, C, G and T. 

  ДНК в клетке представляет собой двойную спираль (см. рисунок), состоящую из двух цепочек комплиментарных нуклеотидов: 
  дело в том, что нуклеотиды попарно образуют между собой связи (T-A, G-C). Свойство комплиментарности заставляет одинарные цепочки ДНК,
плавающие в растворе, находить свои «пары» и объединяться с ними.

ДНК — молекула, состоящая из двух цепочек, и, хотя, последовательность нуклеотидов у них разная, последовательность одной цепочки можно однозначно восстановить,
 если известна последовательность другой. Поэтому цепочки называют комплементарными. (англ. Complement – дополнение)
Это свойство используется при копировании клетки, когда цепочки ДНК расплетаются, и, на каждой, как на матрице, синтезируется вторая,
 и каждая из двух дочерних клеток получает свою двуцепочечную ДНК. Вся последовательность ДНК организма называется геномом.
Например, геном человека состоит из 46 хромосом.

 There are 2 copies of every of 23 chromosome. 
 Самая длинная хромосома человека (первая) содержит около 250 миллионов пар оснований,
 Y chromosome is found only in males.

 в ядре клетки содержится полный хромосомный набор (те самые 23 пары). 

Ген − участок ДНК, в котором закодирован один белок.
Хромосома − одиночная молекула ДНК, которая свернута в структуру определенной формы.
С РНК сложнее, так как их несколько типов (мРНК, тРНК и др.).


. Некоторые участки ДНК называются генами, с них считывается РНК, по которой потом кодируются белки (Protein).
Белки состоят из аминокислот 20 видов (плюс пара экзотических), каждая из которых кодируется по трём нуклеотидам.

У разных методов секвенирования длина рида, которы они могут хорошо прочитать, составляет порядка десятков или сотен нуклеотидов.
Вторая заключается в том, что ДНК — это очень длинная молекула, и, при скрупулезном чтении каждой буквы друг за дружкой,
секвенирование заняло бы неприлично много времени, а в данном случае этот процесс легко распараллеливается,
и можно одновременно читать миллионы и миллиарды ридов.

 Длина полученных из аппаратуры строк составляет всего 36-50 bases (длина строки в нуклеотидах) иногда больше, но на текущий момент вроде не более 200.
Эти отрезки, полученные из секвенирующей аппаратуры и определенные, последовательностью нуклеотидов, называются ридами (от английского reads — “считывание
Стоит отметить, что риды характеризуются только последовательностью нуклеотидов, а не расположением на геноме.
Иногда эти последовательности дополнены строкой вероятностей, ставящей в соответствие позиции нуклеотида его вероятность нахождения на этой позиции.
FASTA файл — это файл без вероятностей, FASTQ — это файл с вероятностями.

 геномный ассемблер (сборщик) — это программа, которая принимает на вход короткие (несколько сотен нуклеотидов) перекрывающиеся кусочки генома,
называемые ридами (reads), и собирает их в единую последовательность.
Точнее, пытается собрать — в большинстве случаев даже для относительно небольших бактериальных геномов (несколько миллионов нуклеотидов) цельной последовательности не получается.

https://habr.com/ru/companies/JetBrains-education/articles/238759/

Когда в каком-нибудь 23andme анализируют образец вашей слюны, они занимаются строго говоря не полноценным секвенированием
(что долго и дорого, даже при идеально чистом образце, даже сейчас), а поиском уникального для вас набора полиморфизмов
(то есть, отличий в нуклеотидных последовательностях) на известном наборе фрагментов в их большой БД, что гораздо проще и дешевле,
и более чем достаточно для обычных задач генотипирования вроде установления родства или определения склонности к болезням.

Современные методы секвенирования дают огромный объем информации о полиморфизме генома, то есть отличиях индивидуальных геномов друг от друга.
 Эти отличия (варианты) возникают в результате мутаций при репликации ДНК и частично фиксируются в популяции.
Распространенность, локализация и функциональный эффект геномных вариантов сильно различаются – от полной летальности до отсутствия какого-либо влияния на индивидуальный фенотип.

Обычно геном обозначают некоторый участок ДНК, отвечающий за синтез некоторого белка (оставим в стороне множество генов, не являющихся белок-кодирующими).
ДНК сначала считывается в РНК (это зовется транскрипцией). Есть участок старта гена, зовущийся промотером.
У эукариот, как вам правильно подметили, всё сложно. Промотер чётко не выделяется и вообще стартов транскрипции у гена может быть несколько разных.
Затем альтернативный сплайсинг делает из этих РНК несколько разных изоформ — «транскриптов». И только затем РНК превращается в белок в ходе трансляции.
 Этот последний этап — единственный более-менее стандартизованный.
В генетическом коде, который используется при трансляции, есть последовательности нуклеотидов, маркирующих старт- и стоп-кодоны.
 Это наиболее похоже на то, что вы описываете, когда говорите про признаки начала и конца (называется это поиском открытой рамки считывания) — но это поиск скорее белка, чем «гена».
Но экспериментально вы можете отсеквенировать РНК и хотя бы понять, где начинается кончается область, которая транскрибируется —
так вы имеете шанс поймать границы гена и, если повезет, границы интронов (участков, которые вырезаются при сплайсинге
```
### SNP - Single Nucleotide Polymorthism

https://www.hgvs.org/ Human Genome Variation Society

https://www.encodeproject.org/

https://habr.com/ru/articles/231591/

https://thegeneticgenealogist.com/2013/09/22/what-else-can-i-do-with-my-dna-test-results/

```
Изменчивость между людьми — примерно 1 нуклеотид на тысячу. Соответственно ~3 миллиона нуклеотидов на геном.
 для каждого изменения нашей ДНК достаточно сохранить только различия от эталонного генома. Обычно они сохраняются в файле VCF (Variant Call Format).

 Обычно имеются треки с геномными вариациями, которые, например, отличают различных людей друг от друга. Часто вариации выражаются в виде точечных мутаций,
однонуклеотидных замен (Single-nucleotide polymorphism, SNP).
Многие из этих мутаций найдены при сравнении результатов секвенирования геномов разных людей и помещены в специальные базы данных (например, dbSNP)

VCF	формат	для	хранения	данных	генетических	полиморфизмов
GWAS (Genome wide association study, полигеномный поиск ассоциаций) является основой генетического анализа вариантов. Он сопоставляет вариации с данными наблюдений.
```

 https://www.bbc.com/future/article/20121102-will-we-ever-crack-lifes-code

 https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000001405.40/

 https://www.biorxiv.org/content/10.1101/2021.05.26.445798v1
```
 3.055 billion base pair (bp) sequence of a human genome
 длинна человеческой ДНК всего 3,1 млрд пар оснований

 In 2001, Celera Genomics and the International Human Genome Sequencing Consortium published their initial drafts of the human genome
```
### SEQANSWERS

https://www.seqanswers.com/articles/324199-from-algorithms-to-assemblies-an-interview-with-sequencing-analysis-experts%E2%80%94part-1

https://www.seqanswers.com/articles/324579-qc-alignment-and-mapping-recommended-tools-for-next-level-sequencing-analysis

https://www.seqanswers.com/articles/324604-variant-analysis-and-genome-assembly-recommended-tools-for-next-level-sequencing-analysis

https://www.seqanswers.com/articles/324616-differential-expression-and-data-visualization-recommended-tools-for-next-level-sequencing-analysis

### DNA File formats

https://bioinformatics.stackexchange.com/questions/1/whats-the-most-efficient-file-format-for-the-storage-of-dna-sequences

http://emboss.open-bio.org/html/use/ch05s02.html

https://linsalrob.github.io/ComputationalGenomicsManual/

https://linsalrob.github.io/ComputationalGenomicsManual/SequenceFileFormats/

The standard and the most common sequence format is FASTA for sure. You can compress it with a compressor. For the ~3GB human genome, 
gzip reduces the size to ~900MB, depending on the option in use.

Another often used format is UCSC's 2-bit format. This format keeps each A/C/G/T with 2 bits.
 
```
 Genes encode the instructions for assembling proteins, molecular machines that perform vital jobs in our cells. 
 A protein is a long chain of amino acids, and we can predict that chain with perfect precision. 
 But the chain also folds, origami-like, into a complex three-dimensional shape, and the shape dictates everything that the protein does, 
 from the chemical reactions it speeds up to the other molecules it sticks to.

 The problem is that some DNA is extremely repetitive. 
 Certain stretches of the genome repeat the same sequences over and over, sometimes for thousands of bases.

The repetitive DNA often turns up in the same bits of the genome. 
Our DNA isn't stored in one long continuous rope, but is instead split into smaller chunks called chromosomes.
These are X-shaped (apart from one Y-shaped chromosome carried by men) 
and there are 23 pairs of them in humans. 
Each has repetitive DNA at the tips of its four arms – the telomeres – and at the central cross, the centromere. Both are important.

 Some genes provide the information needed to make an enormous variety of different proteins that perform assorted functions important to life,
 while other sections of DNA have regulatory functions. 

It has turned out that most diseases are affected by hundreds of genes,


Protein-coding genes make up just 1.5% of our genome, the rest includes a lot of what is thought to be useless junk with no discernible function.
But it also contains regulatory sequences that control when, where and how our genes are used.
We need to identify these if we’re ever to predict how a genome leads to a living, breathing organism.
The technology for doing that is being developed, and the ENCODE project – the Encyclopaedia of DNA elements –
has put it to good use, compiling a catalogue of the various regulatory sequences in our own genome. But
ENCODE involved 442 scientists intensely running experiments for a decade, and even its unprecedented catalogue is incomplete.
```
https://www.goodreads.com/book/show/25660581-the-deeper-genome

https://www.quantamagazine.org/biologists-rethink-the-logic-behind-cells-molecular-signals-20210916 

https://www.quantamagazine.org/most-complete-simulation-of-a-cell-probes-lifes-hidden-rules-20220224 

https://www.quantamagazine.org/embryo-cells-set-patterns-for-growth-by-pushing-and-pulling-20220712

https://www.quantamagazine.org/most-complete-simulation-of-a-cell-probes-lifes-hidden-rules-20220224 

https://actu.epfl.ch/news/a-secret-language-of-cells-new-cell-computations-u/

https://news.ycombinator.com/item?id=32387815


### Bioinformatics

https://www.bbc.com/future/article/20230210-the-man-whose-genome-you-can-read-end-to-end

### Immune system atlas 

https://www.nature.com/articles/s41586-022-05028-x

https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-022-05028-x/MediaObjects/41586_2022_5028_MOESM1_ESM.pdf

https://news.ycombinator.com/item?id=32381790


https://www.pillar.vc/playlist/article/open-source-tools-for-computational-biology/

https://freethoughtblogs.com/pharyngula/2008/02/03/buffeted-by-the-winds-of-chanc/

https://jsomers.net/i-should-have-loved-biology/

https://news.ycombinator.com/item?id=32035054

https://news.ycombinator.com/item?id=25136422

https://www.pnas.org/doi/10.1073/pnas.1620001114

### Vitaly Vanchurin

-- видеоканал Artificial Neural Computing https://www.youtube.com/@ArtificialNeuralComputing
-- группа The World as a Neural Network в фейсбуке (основные обсуждения пока тут): https://www.facebook.com/groups/2930104110608299
-- чат в телеграме https://t.me/theworldasaneuralnetworkchat и обсуждения в зуме с 19 до 21 часа по пятницам (ссылка на зум в инфо канала)
-- канал в телеграме https://t.me/theworldasaneuralnetwork
-- вопросы, которые обсуждаются: https://docs.google.com/document/d/1xNEmpqhzt6QRp4CFkXwJJ2yfE3zofEcn0Vn5PbtLs2Q/edit
-- разговор про природу искусства: https://www.facebook.com/groups/2930104110608299/posts/3470688086549896/
-- работы Ванчурина https://scholar.google.com/citations?hl=en&user=nEEFLp0AAAAJ&view_op=list_works&sortby=pubdate
-- компания Ванчурина https://artificialneuralcomputing.com/
-- интервью Ванчурина (январь 2023) по-русски на пару часов: https://www.youtube.com/watch?v=p6mUVE6nmGY, по-английски на пять часов: https://www.youtube.com/watch?v=RIEtRGfFSGI (ноябрь 2022)


( University of Minnesota Duluth )
https://scholar.google.com/citations?hl=en&user=nEEFLp0AAAAJ&view_op=list_works&sortby=pubdate
 
 Сергей Ястребов
От атомов к древу. Введение в современную науку о жизни
 https://vsenauka.ru/knigi/vsenauchnyie-knigi/book-details.html?id=823
 
 https://www.quantamagazine.org/first-support-for-a-physics-theory-of-life-20170726/ 
 
 A Review of Mathematical and Computational Methods in Cancer Dynamics
https://arxiv.org/abs/2201.02055

System Biology MIT
https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/video_galleries/lecture-videos/

 
 https://www.quantamagazine.org/in-worms-inheritance-beyond-genes-can-help-evolution-20220419/ 
 
https://www.quantamagazine.org/most-complete-simulation-of-a-cell-probes-lifes-hidden-rules-20220224/ 
 
http://www.rasa-usa.org/en/

https://www.nature.com/collections/iahbbijjbb  2021 Top 25 Health Sciences Articles

https://arxiv.org/abs/2201.06897. The world beyond physics: how big is it?
Sauro Succi


https://probmods.org/. Probabilistic models of cognition

Михаил Цодыкс

https://www.youtube.com/watch?v=cYuepljq5vA

https://www.youtube.com/watch?v=MDj_rAH0rdM Мозг, память и корень из Пи.



Eugene Shakhnovich
https://www.uhnwidata.com/den-of-rich/eugene-shakhnovich

https://www.pnas.org/content/117/3/1485 . Cotranslational folding allows misfolding-prone proteins to circumvent deep kinetic traps


Consciousness is supported by near-critical slow cortical electrodynamics
https://www.pnas.org/content/119/7/e2024455119

https://news.ycombinator.com/item?id=30350261





Aging clocks, entropy, and the limits of age-reversal. 
  Andrei E. Tarkhov, Kirill A. Denisov,  Peter O. Fedichev
https://www.biorxiv.org/content/10.1101/2022.02.06.479300v1

Principles for the design of multicellular engineered living systems
https://aip.scitation.org/doi/pdf/10.1063/5.0076635

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6783340/  Cell modelling

Modeling Progression of Single Cell Populations Through the Cell Cycle as a Sequence of Switches

 Zinovyev1,2,3*,  Michail Sadovsky4,5,6,7,  Laurence Calzone1,2,3,  Aziz Fouché1,2,3,  Clarice S. Groeneveld8,9,  Alexander Chervov1,2,3,  Emmanuel Barillot1,2,3 and  Alexander N. Gorban7,10
 
https://www.frontiersin.org/articles/10.3389/fmolb.2021.793912/full

https://evolutionnews.org/2022/02/nuclear-pore-complex-comes-into-focus/

https://www.youtube.com/watch?v=TfYf_rPWUdY mRNA

https://habr.com/ru/company/ruvds/blog/582126/. Наш мозг не компьютер

### Vitaly Vanchurin, Yuri I. Wolf,  Eugene V. Koonin,  Mikhail I. Katsnelson
https://trv-science.ru/2022/03/vsya-nasha-zhizn-zadachi-po-optimizacii 

https://trv-science.ru/2022/02/zhizn-kak-mnogourovnevoe-obuchenie/

Thermodynamics of evolution and the origin of life
Vitaly Vanchurina,b,1, Yuri I. Wolfa , Eugene V. Koonina,1 , and Mikhail I. Katsnelsonc,1

https://www.pnas.org/content/pnas/119/6/e2120042119.full.pdf


https://arxiv.org/abs/2110.14602 Towards a Theory of Evolution as Multilevel Learning

https://www.pnas.org/content/pnas/119/6/e2120037119.full.pdf

https://www.pnas.org/content/119/6/e2120037119

https://www.pnas.org/content/119/6/e2120042119

https://habr.com/ru/company/timeweb/blog/594859/  Краткое знакомство с моделированием белков

https://condensedconcepts.blogspot.com/2021/09/nanoscale-machines-in-nature.html

https://www.nature.com/articles/d41586-021-02904-w

https://news.ycombinator.com/item?id=29123843

https://www.youtube.com/watch?v=m40UnvhT1Vg

cancer

https://habr.com/ru/post/564978/

Gene therapy (ru)
https://www.youtube.com/watch?v=QybCCXJdLn8&t=2s

### Molecular biology
МФТИ Молекулярная биология, Пупов Д. В., 22.04.2022
https://www.youtube.com/playlist?list=PLthfp5exSWEqHCSmeN7RkAGVl9ck4iDzL


<https://news.ycombinator.com/item?id=22763100>

### Окштейн И.Л., МФТИ
https://www.youtube.com/playlist?list=PLwg7NW3ZH-fX2HGMrhXNvQjJtwpE9ORTz


### Михаил Никитин. 

https://www.youtube.com/results?search_query=Faculty+of+Bioengineering+and+Bioinformatics%2C+MSU&sp=EiG4AQHCARtDaElKd19ZS1J4NU50VVlSNnpBeHg5YmZoNVk%253D


Михаил Никитин: "История фотосинтеза, или кто сделал небо голубым
https://www.youtube.com/watch?v=eXc1eXbJBIU


https://www.youtube.com/playlist?list=PLsgpsPeRv64h8d2lgoQpx-Z755m5gO4Rs

https://www.youtube.com/playlist?list=PL9Zn3Gcp2G7YWIeeIVglBXEnCtTggCIoR

https://www.youtube.com/playlist?list=PLf8iQozIdvKhwJrnksSMugsRbhRTGkJ9w

Лекция 4. Атмосфера и климат.
https://www.youtube.com/watch?v=iTKe2BMvzZM

Михаил Никитин. Лекция 5. Место возникновения жизни. 
https://www.youtube.com/watch?v=TYkkN3r8IZo

Лекция 9.
https://www.youtube.com/watch?v=0sWOhMe7DK0

Центр Архэ
https://www.youtube.com/channel/UCY41Iz96tJZMEp1qyLH-LYQ


### Molecular motors
How Molecular Motors Extract Order from Chaos(A Key Issues Review)
Peter M Hoffmann
https://cpb-us-e1.wpmucdn.com/s.wayne.edu/dist/c/2/files/2018/07/MolecMachinesv7-1cpb97f.pdf

Quantum-Classical Simulation of Molecular Motors Driven Only by Light
https://pubs.acs.org/doi/10.1021/acs.jpclett.1c00951

https://pubs.acs.org/doi/pdf/10.1021/acs.jpclett.1c00951


https://www.youtube.com/watch?v=sbFL2U7Vwls    (ru)  В.А.Твердислов "Хиральность и иерархия струкутр в биомакромолекулах. Молекулярные машины"

https://ufn.ru/ru/articles/2020/4/a/ Управление нанотранспортом с помощью рэтчет-эффекта
Ю.В. Гуляев†  а, б, А.С. Бугаев‡  а, б, В.М. Розенбаум§  в, Л.И. Трахтенберг*  б, г, д
