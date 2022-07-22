https://github.com/averkij/mstu-nlp-course Обзор современного машинного обучения

https://stepik.org/org/dlschool  Школа глубокого обучения МФТИ

https://ods.ai/tracks/nlp-course-spring-22 

https://ods.ai/

https://www.fast.ai/2022/07/21/dl-coders-22/. Practical Deep Learning for Coders 2022

### Classes 
https://burlachenkok.github.io/Courses-at-Stanford-relative-to-AI/

https://huggingface.co/course/chapter1/1

https://github.com/huggingface/course

Topic modeling:
https://www.toptal.com/python/topic-modeling-python

Transfer learning
https://www.toptal.com/deep-learning/exploring-pre-trained-models

Embedding
https://www.toptal.com/machine-learning/embeddings-in-machine-learning


### Transformer

https://jalammar.github.io/illustrated-transformer/

https://amatriain.net/blog/transformer-models-an-introduction-and-catalog-2d1e9039f376/

https://web.stanford.edu/class/cs25/

http://nlp.seas.harvard.edu/annotated-transformer/

https://arxiv.org/abs/2207.09238 Formal Algorithms for Transformers

https://data-science-blog.com/blog/2020/12/30/transformer/ 

https://habr.com/ru/post/657443/ Hugging Face (стартап, стоящий за библиотекой transformers)

https://github.com/huggingface/transformers

Transformers: https://habr.com/ru/search/?q=%D0%A2%D1%80%D0%B0%D0%BD%D1%81%D1%84%D0%BE%D1%80%D0%BC%D0%B5%D1%80&target_type=posts&order=relevance


### BERT
https://habr.com/ru/search/?q=BERT&target_type=posts&order=relevance

https://habr.com/ru/post/677512/ Мультиклассовая классификация текста

https://habr.com/ru/hub/natural_language_processing/
```
1. It reads all the words at once rather than left-to-right or right-to-left
2. 15% of the words are randomly selected to be “masked” (literally replaced with the [MASK] token) during training time
   - 10% of the randomly selected words are left unchanged
   - 10% of the masked words are replaced with random words
   - (a) and (b) work together to force the model to predict every word in the sentence (models are lazy)

3. BERT then attempts to predict all the words in the sentence, 
and only the masked words contribute to the loss function - inclusive of the unchanged and randomly replaced words
The model fine-tuned on next-sentence-prediction. 
In this step, the model tries to determine if a given sentence is the next sentence in the text

Convergence is slow, and BERT takes a long time to train. However, it learns the contextual relationships in text far better. 
Word vectors are very shallow representations that limit the complexity 
that they can model—BERT does not have this limitation.
```
