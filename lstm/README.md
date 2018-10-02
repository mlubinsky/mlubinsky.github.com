<http://neuralnetworksanddeeplearning.com/index.html> .  book

<https://medium.com/mlreview/understanding-lstm-and-its-diagrams-37e2f46f1714>

<https://towardsdatascience.com/illustrated-guide-to-lstms-and-gru-s-a-step-by-step-explanation-44e9eb85bf21>

## LSTM
```
 The feed-forward network with a single hidden layer containing a finite number of neurons can approximate 
 continuous functions on compact subsets of R^n.
ANNs are universal function approximators. 
RNNs take it a step further, though; they can compute/describe programs. 
In fact, some RNNs with proper weights and architecture qualify as Turing Complete.
  
Why do we need recurrent neural networks when we already have the beloved ANNs (and CNNs) in all their glory?
It boils down to a few things:

ANNs can’t deal with sequential or “temporal” data
ANNs lack memory
ANNs have a fixed architecture  


RNNs are being used heavily in NLP; they retain context by having memory. ANNs have no memory.
The constraint with ANNs is that they have a fixed number of computation/processing steps (because, once again, 
the number of hidden layers is a hyperparameter). 
With RNNs, we can have much more dynamic processing since we operate over vectors. 
Each neuron in an RNN is almost like an entire layer in an ANN; 

LSTM Has 3 Gates:
1) The Forget Gate: Chooses which information to remove from the state
2) The Input Gate: Chooses which information to add to the state
3) The Output Gate: Prepares what to output from this cell

The input gate contains two networks instead of one, giving an LSTM a total of 4 sets of weights that have to be trained.
 
vanishing gradients: due to the backprop in time causing weights to grow (or decrease) exponentially (multiplication at each time step). LSTM and GRU nets get around this by having an internal memory which is clamped between 0-1 (or maybe -1 and 1). This avoids exploding/vanishing weight values when backpropping in time. 
 
``` 
<https://www.youtube.com/watch?v=WCUNPb-5EYI>


<https://www.youtube.com/watch?v=QuELiw8tbx8&index=9&list=PL3FW7Lu3i5Jsnh1rnUwq_TcylNr7EkRe6> Stanford
<https://www.youtube.com/watch?v=6_MO12fPC-0&list=PL3FW7Lu3i5Jsnh1rnUwq_TcylNr7EkRe6&index=12> Standord

<https://www.altumintelligence.com/articles/a/Time-Series-Prediction-Using-LSTM-Deep-Neural-Networks>

<https://machinelearningmastery.com/multivariate-time-series-forecasting-lstms-keras/> 
 
<https://ayearofai.com/rohan-lenny-3-recurrent-neural-networks-10300100899b>

<https://www.reddit.com/r/datascience/comments/79hjzn/how_good_is_lstm_for_time_series_forecasting/>

<https://talwarabhimanyu.github.io/blog/2018/07/31/rnn-backprop>

<https://talwarabhimanyu.github.io/blog/2018/08/12/lstm-backprop>

<https://www.youtube.com/watch?v=EQ-JE38e8XE> ru

<https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi>

<https://www.asozykin.ru/courses/nnpython> 
<https://tproger.ru/translations/neural-network-zoo-2/>

<https://uzclip.net/video/1DNcYIN0aaA/%D0%BA%D0%B2%D0%B0%D1%80%D1%82%D0%B8%D1%80%D0%BD%D0%B8%D0%BA-deep-learning-%D0%BD%D0%B0-%D0%BF%D0%B0%D0%BB%D1%8C%D1%86%D0%B0%D1%85.html>

<http://mechanoid.kiev.ua/>

http://www.machinelearning.ru/wiki/images/7/78/2017_417_DrapakSN.pdf

<https://en.wikipedia.org/wiki/Long_short-term_memory>

<https://neural.wtf/floyd.html>

http://library.eltech.ru/files/vkr/2017/bakalavri/3382/2017%D0%92%D0%9A%D0%A0338212%D0%A4%D0%90%D0%9D%D0%98%D0%A4%D0%90%D0%A2%D0%AC%D0%95%D0%92%D0%90.pdf


<https://blog.heuritech.com/2016/01/20/attention-mechanism/> attention
