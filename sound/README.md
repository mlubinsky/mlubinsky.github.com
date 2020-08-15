## Accelerometer

<https://en.wikipedia.org/wiki/High-pass_filter>

<http://www.sensorica.ru/docs/art2.shtml>

Для приложений, требующих измерений малых ускорений, лучшим решением будет использование акселерометра с высокой чувствительностью, где выходной сигнал будет выше уровня шума усилителя. Например, если ожидается уровень вибрации 0.1g, а чувствительность датчика составляет 10 мВ/g, напряжение выходного сигнала составит 1 мВ и потребуется акселерометр с более высокой чувствительностью.

В основном, используются два фильтра — высокочастотный (high-pass) и низкочастотный (low-pass). Эти фильтры можно использовать для отсеивания эффектов «дрожания»,
медленных поворотов и т.д.

Низкочастотный фильтр используется для нахождения ориентации устройства, высокочастотный — для определения тряски.


https://habr.com/ru/post/346766/.  motion detection on Android with Tensorflow

https://www.youtube.com/watch?v=qcHjDLCJxfI

https://www.youtube.com/watch?v=5022uOtWUag

https://www.youtube.com/watch?v=DUznmZvSQOU

https://www.youtube.com/watch?v=dEn2Qvh_qjc

https://www.youtube.com/watch?v=g8h2aFAVGH0

## Vibration

https://www.youtube.com/watch?v=4fDqII7ut6Y


## Microsoft Bot
<https://vc.ru/services/142989-artist-zhurnalist-hudozhnik-i-luchshiy-drug-660-mln-chelovek-pochemu-bot-microsoft-xiaoice-stal-samym-populyarnym-v-kitae?from=rss> 

## Question /Answer with python and streamit
<https://www.confetti.ai/post/deploying-a-state-of-the-art-question-answering-system-with-60-lines-of-python-and-streamlit>

## Noise supression

<https://news.ycombinator.com/item?id=23880207>  Noise supression

## CMSIS DSP and mbed
https://forums.mbed.com/t/cmsis-dsp-support-forthcoming/8465


## Keyword spotting KWS CMSIS-NN

Linker error: multiple definitions
<https://github.com/ARM-software/CMSIS_5/issues/581>

<https://link.springer.com/article/10.1186/s13636-020-00176-2>  Danish

https://github.com/PeterMS123/KWS-DS-CNN-for-embedded/blob/master/README.md

Naveen Suda:

<https://arxiv.org/abs/1711.07128>

<https://github.com/ARM-software/ML-KWS-for-MCU>

https://developer.arm.com/solutions/machine-learning-on-arm/developer-material/how-to-guides/converting-a-neural-network-for-arm-cortex-m-with-cmsis-nn/single-page


## Sound on FRDM-K66F
<https://community.nxp.com/thread/500494>

<https://os.mbed.com/docs/mbed-os/v5.13/apis/usbaudio.html>  USBAudio

<https://forums.mbed.com/t/sai-on-frdm-k66f/6041>

SAI (synchronous audio interface)

<https://forums.mbed.com/t/looking-for-frdm-k66f-code-example-for-microphone/9615>

## MFCC

<https://haythamfayek.com/2016/04/21/speech-processing-for-machine-learning.html>
```
 The mel-scale was developed by experimenting with the human ears 
 interpretation of a pitch in 1940’s.
The sole purpose
of the experiment were to describe the human auditory system on a linear scale. 
The experiment showed that the pitch is lineary perceived in the frequencyrange 0-1000hz. 
Above 1000 hz, the scale becomes logaritmic. 

MFCCs means Mel Frequency Cepstral Coefficients which are the most widely used features in speech recognition. MFCC coefficients model the spectral energy distribution in a perceptually meaningful way.
```
http://www.cs.tut.fi/~sgn14006/PDF2015/S04-MFCC.pdf

http://kom.aau.dk/group/04gr742/pdf/MFCC_worksheet.pdf

http://www.jatit.org/volumes/Vol79No1/5Vol79No1.pdf

https://www.silabs.com/content/usergenerated/asi/cloud/content/siliconlabs/en/community/projects/jcr:content/content/primary/blog/efm32_voice_recognit-0WYR.social.0.10.html

http://www.cs.tut.fi/~sgn14006/PDF2015/S04-MFCC.pdf

http://www.speech.cs.cmu.edu/15-492/slides/03_mfcc.pdf

https://www.researchgate.net/publication/220584952_Comparison_of_Different_Implementations_of_MFCC

https://www.researchgate.net/publication/254028337_Speaker_recognition_using_Mel_Frequency_Cepstral_Coefficients_MFCC_and_Vector_quantization_VQ_techniques

https://arxiv.org/pdf/1711.07128.pdf

https://arxiv.org/pdf/1003.4083.pdf

<https://medium.com/linagoralabs/computing-mfccs-voice-recognition-features-on-arm-systems-dae45f016eb6>


<https://dsp.stackexchange.com/questions/15145/mfcc-uncertain-of-my-results-and-algorithm>

## ARM NN

<https://www.arm.com/products/silicon-ip-cpu/ethos/arm-nn>

## DSP FFT

http://www.dsplib.ru/index.html

https://faultan.ru/osc/essence_of_fourier_transform/

https://github.com/capitanov/dsp-theory

https://www.amazon.com/Understanding-Digital-Signal-Processing-3rd/dp/0137027419/ref=dp_ob_title_bk

https://stackoverflow.com/questions/604453/analyze-audio-using-fast-fourier-transform


https://nuancesprog.ru/p/6713/

https://nuancesprog.ru/p/6758/


https://moluch.ru/archive/28/3171/

## FFT Window  

<http://www.dsplib.ru/content/win/win.html>

```
short-time signal processing is practically always done using windowing
in short-time signal processing, signals are cut into small pieces called frames, which are processed one at a time
frames are windowed with a window function in order to improve the frequency-domain representation
what windowing essentially means is multiplying the signal frame with the window function point-by-point
```
https://www.iguides.ru/main/other/kak_rabotaet_shazam_bystroe_preobrazovanie_fure_daunsempling_i_snizhenie_trudoemkosti/



### spectrogram
https://towardsdatascience.com/understanding-audio-data-fourier-transform-fft-spectrogram-and-speech-recognition-a4072d228520
```
Suppose you are working on a Speech Recognition task. 
You have an audio file in which someone is speaking a phrase (for example: How are you). 
Your recognition system should be able to predict these three words in the same order
(1. ‘how’, 2. ‘are’, 3. ‘you’).  
we broke our signal into its frequency values which will serve as features for our recognition system.
But when we applied FFT to our signal, it gave us only frequency values and we lost the track of time information. 
Now our system won’t be able to tell what was spoken first if we use these frequencies as features.
We need to find a different way to calculate features for our system such that it has frequency values along with the time at which they were observed. 
Here Spectrograms come into the picture.
Visual representation of frequencies of a given signal with time is called Spectrogram. 
In a spectrogram representation plot — one axis represents the time,
the second axis represents frequencies 
and the colors represent magnitude (amplitude) of the observed frequency at a particular time

```

<https://cartesiam-neai-docs.readthedocs-hosted.com/faq.html#faq>  

<https://www.Cartesiam.ai>
 
<https://www.musicdsp.org/en/latest/>

<https://forum.juce.com/>

<https://www.kvraudio.com/forum/viewforum.php?f=33>

## CMSIS DSP Cortex Microcontroller Software Interface Standard (CMSIS)

<https://developer.arm.com/solutions/machine-learning-on-arm/developer-material/how-to-guides/implement-classical-ml-with-arm-cmsis-dsp-libraries>

<https://github.com/ARM-software/ML-KWS-for-MCU/>

<https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/micro/kernels/cmsis-nn>

<http://m0agx.eu/2018/05/23/practical-fft-on-microcontrollers-using-cmsis-dsp/>


### arm_cfft_f32 example:

https://github.com/bkht/TFT_FFT_Test/blob/master/main.cpp

https://github.com/ARM-software/CMSIS_5/blob/master/CMSIS/DSP/Examples/ARM/arm_fft_bin_example/arm_fft_bin_example_f32.c

<https://cpp.hotexamples.com/examples/-/-/arm_cfft_f32/cpp-arm_cfft_f32-function-examples.html>

<http://www.eas.uccs.edu/~mwickert/ece5655/lecture_notes/ARM/ece5655_chap9.pdf>

<https://community.particle.io/t/fft-with-arm-math-cmsis-dsp/44314/7>

<https://stackoverflow.com/questions/32211401/proper-fft-length-for-arm-cmsis-dsp-fft-function>

<https://www.dsprelated.com/thread/1480/arm-cmsis-fft-does-it-produce-correct-results>

<https://www.arm.com/why-arm/technologies/cmsis>

<https://arm-software.github.io/CMSIS_5/DSP/html/index.html>

<http://openaudio.blogspot.com/2016/09/>

<https://pdfs.semanticscholar.org/ef5a/5e8e2b3eaacffc34840a57f7f4892d8547a0.pdf>. arm_fft CMSIS


## Sound 
<https://habr.com/ru/post/503786/> how analog sound digitized: sampling, quantization

## TFLite SIG-micro
<https://gitter.im/tensorflow/sig-micro>

## FFT
<https://betterexplained.com/articles/an-interactive-guide-to-the-fourier-transform/>

<https://github.com/bkht/TFT_FFT_Test>

<https://habr.com/ru/post/196374/>

it passes that data into GenerateMicroFeatures() , defined in micro_features/micro_features_generator.h . 
This is the function that performs the FFT and returns the audio frequency information. 

```
| File                         | Function              | Call                   | Input-Output|
-----------------------------------------------------------------------------------------------|
|  main_functions.cc           | loop                  | PopulateFeatureData    |              |
|  feature_provider.cc         | PopulateFeatureData   | GenerateMicroFeatures  |              |
| micro_features_generator.cc  | GenerateMicroFeatures | FrontendProcessSamples |              |
| frontend.c                   | FrontendProcessSamples | FftCompute            |              |
| fft.cc                       | FftCompute          |  kiss_fftr               |              |
| ./tools/kiss_fftr.c
```

<https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/microfrontend/lib/frontend.h>
```
struct FrontendOutput {
  const uint16_t* values;
  size_t size;
};

```
### tensorflow/lite/micro/examples/micro_speech/micro_features/micro_model_settings.h
```
 22 // The size of the input time series data we pass to the FFT to produce the
 23 // frequency information. This has to be a power of two, and since we're dealing
 24 // with 30ms of 16KHz inputs, which means 480 samples, this is the next value.
 25 constexpr int kMaxAudioSampleSize = 512;
 26 constexpr int kAudioSampleFrequency = 16000;
 27
 28 // The following values are derived from values used during model training.
 29 // If you change the way you preprocess the input, update all these constants.
 30 constexpr int kFeatureSliceSize = 40;
 31 constexpr int kFeatureSliceCount = 49;
 32 constexpr int kFeatureElementCount = (kFeatureSliceSize * kFeatureSliceCount);
 33 constexpr int kFeatureSliceStrideMs = 20;
 34 constexpr int kFeatureSliceDurationMs = 30;
 35
 36 // Variables for the model's output categories.
 37 constexpr int kSilenceIndex = 0;
 38 constexpr int kUnknownIndex = 1;
 39 // If you modify the output categories, you need to update the following values.
 40 constexpr int kCategoryCount = 4;
 41 extern const char* kCategoryLabels[kCategoryCount];
```

## file: ./micro_features/micro_features_generator.cc
bin size = (7500.0 -125) / 255

```
TfLiteStatus InitializeMicroFeatures(tflite::ErrorReporter* error_reporter) {
  FrontendConfig config;
  config.window.size_ms = kFeatureSliceDurationMs;
  config.window.step_size_ms = kFeatureSliceStrideMs;
  config.noise_reduction.smoothing_bits = 10;
  config.filterbank.num_channels = kFeatureSliceSize;
  config.filterbank.lower_band_limit = 125.0;
  config.filterbank.upper_band_limit = 7500.0;
  config.noise_reduction.smoothing_bits = 10;
  config.noise_reduction.even_smoothing = 0.025;
  config.noise_reduction.odd_smoothing = 0.06;
  config.noise_reduction.min_signal_remaining = 0.05;
  config.pcan_gain_control.enable_pcan = 1;
  config.pcan_gain_control.strength = 0.95;
  config.pcan_gain_control.offset = 80.0;
  config.pcan_gain_control.gain_bits = 21;
  config.log_scale.enable_log = 1;
  config.log_scale.scale_shift = 6;
  if (!FrontendPopulateState(&config, &g_micro_features_state,
                             kAudioSampleFrequency)) {
    TF_LITE_REPORT_ERROR(error_reporter, "FrontendPopulateState() failed");
    return kTfLiteError;
  }
  g_is_first_time = true;
  return kTfLiteOk;
}

// This is not exposed in any header, and is only used for testing, to ensure
// that the state is correctly set up before generating results.
void SetMicroFeaturesNoiseEstimates(const uint32_t* estimate_presets) {
  for (int i = 0; i < g_micro_features_state.filterbank.num_channels; ++i) {
    g_micro_features_state.noise_reduction.estimate[i] = estimate_presets[i];
  }
}

TfLiteStatus GenerateMicroFeatures(tflite::ErrorReporter* error_reporter,
                                   const int16_t* input, int input_size,
                                   int output_size, uint8_t* output,
                                   size_t* num_samples_read) {
  const int16_t* frontend_input;
  if (g_is_first_time) {
    frontend_input = input;
    g_is_first_time = false;
  } else {
    frontend_input = input + 160;
  }
  FrontendOutput frontend_output = FrontendProcessSamples(
    ========================================================
      &g_micro_features_state, frontend_input, input_size, num_samples_read);

  for (int i = 0; i < frontend_output.size; ++i) {
    // These scaling values are derived from those used in input_data.py in the
    // training pipeline.
    constexpr int32_t value_scale = (10 * 255);
    constexpr int32_t value_div = (256 * 26);
    int32_t value =
        ((frontend_output.values[i] * value_scale) + (value_div / 2)) /
        value_div;
    if (value < 0) {
      value = 0;
    }
    if (value > 255) {
      value = 255;
    }
    output[i] = value;
  }

  return kTfLiteOk;
}
```


<https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/experimental/microfrontend/lib>

 tensorflow/lite/experimental/microfrontend/lib/frontend.c   FFT is here!!!
```
struct FrontendOutput FrontendProcessSamples(struct FrontendState* state,
                                             const int16_t* samples,
                                             size_t num_samples,
                                             size_t* num_samples_read) {
  struct FrontendOutput output;
  output.values = NULL;
  output.size = 0;

  // Try to apply the window - if it fails, return and wait for more data.
  if (!WindowProcessSamples(&state->window, samples, num_samples,
                            num_samples_read)) {
    return output;
  }

  // Apply the FFT to the window's output (and scale it so that the fixed point
  // FFT can have as much resolution as possible).
  int input_shift =
      15 - MostSignificantBit32(state->window.max_abs_output_value);
  FftCompute(&state->fft, state->window.output, input_shift);
  ============================================================
  // We can re-ruse the fft's output buffer to hold the energy.
  int32_t* energy = (int32_t*)state->fft.output;

  FilterbankConvertFftComplexToEnergy(&state->filterbank, state->fft.output,
                                      energy);

  FilterbankAccumulateChannels(&state->filterbank, energy);
  uint32_t* scaled_filterbank = FilterbankSqrt(&state->filterbank, input_shift);

  // Apply noise reduction.
  NoiseReductionApply(&state->noise_reduction, scaled_filterbank);

  if (state->pcan_gain_control.enable_pcan) {
    PcanGainControlApply(&state->pcan_gain_control, scaled_filterbank);
  }

  // Apply the log and scale.
  int correction_bits =
      MostSignificantBit32(state->fft.fft_size) - 1 - (kFilterbankBits / 2);
  uint16_t* logged_filterbank =
      LogScaleApply(&state->log_scale, scaled_filterbank,
                    state->filterbank.num_channels, correction_bits);

  output.size = state->filterbank.num_channels;
  output.values = logged_filterbank;
  return output;
}
```

<https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/micro/examples/micro_speech/micro_features/micro_model_settings.h>

<https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/micro/examples/micro_speech/micro_features/micro_features_generator.cc#L70>
 
<https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/micro/examples/micro_speech/micro_features/micro_features_generator_test.cc> 



/experimental/microfrontend/lib/fft.cc
```
 19 #define FIXED_POINT 16
 20 #include "kiss_fft.h"
 21 #include "tools/kiss_fftr.h"
 22
 23 void FftCompute(struct FftState* state, const int16_t* input,
 ===================================================================
 24                 int input_scale_shift) {
 25   const size_t input_size = state->input_size;
 26   const size_t fft_size = state->fft_size;
 27
 28   int16_t* fft_input = state->input;
 29   // First, scale the input by the given shift.
 30   int i;
 31   for (i = 0; i < input_size; ++i) {
 32     fft_input[i] = static_cast<int16_t>(static_cast<uint16_t>(input[i])
 33                                         << input_scale_shift);
 34   }
 35   // Zero out whatever else remains in the top part of the input.
 36   for (; i < fft_size; ++i) {
 37     fft_input[i] = 0;
 38   }
 39
 40   // Apply the FFT.
 41   kiss_fftr(
 42       reinterpret_cast<const kiss_fftr_cfg>(state->scratch),
 43       state->input,
 44       reinterpret_cast<kiss_fft_cpx*>(state->output));
 45 }
```

What is  kiss_fftr()?  defined in ./tools/kiss_fftr.{h|c}
```
void kiss_fftr(kiss_fftr_cfg cfg,const kiss_fft_scalar *timedata,kiss_fft_cpx *freqdata);
/*
 input timedata has nfft scalar points
 output freqdata has nfft/2+1 complex points
*/
```
It accepts 3 args
1st arg 
2nd arg is the input
3rd arg is calculated: it has a type defined in ./kiss_fft.h
```
typedef struct {
    kiss_fft_scalar r;
    kiss_fft_scalar i;
}kiss_fft_cpx;
```



```

./main_functions.cc:  TfLiteStatus feature_status = feature_provider->PopulateFeatureData(

126 void loop(){
   ...
133   TfLiteStatus feature_status = feature_provider->PopulateFeatureData(
134       error_reporter, previous_time, current_time, &how_many_new_slices);
...

 find . -name "*.cc" | xargs grep GenerateMicroFeatures
 
./lite/micro/examples/micro_speech/feature_provider.cc:      TfLiteStatus generate_status = GenerateMicroFeatures(

./lite/micro/examples/micro_speech/micro_features/micro_features_generator.cc:TfLiteStatus GenerateMicroFeatures(tflite::ErrorReporter* error_reporter,

```
### ./tensorflow/lite/micro/examples/micro_speech/nxp_k66f/audio_provider.cc:
TfLiteStatus GetAudioSamples() - board-specific!!!
 
### feature_provider.cc
calls GetAudioSamples() and GenerateMicroFeatures()
```
37 TfLiteStatus FeatureProvider::PopulateFeatureData(
 ...
 ...
 71   const int slices_to_keep = kFeatureSliceCount - slices_needed;
 72   const int slices_to_drop = kFeatureSliceCount - slices_to_keep;
 73   // If we can avoid recalculating some slices, just move the existing data
 74   // up in the spectrogram, to perform something like this:
 75   // last time = 80ms          current time = 120ms
 76   // +-----------+             +-----------+
 77   // | data@20ms |         --> | data@60ms |
 78   // +-----------+       --    +-----------+
 79   // | data@40ms |     --  --> | data@80ms |
 80   // +-----------+   --  --    +-----------+
 81   // | data@60ms | --  --      |  <empty>  |
 82   // +-----------+   --        +-----------+
 83   // | data@80ms | --          |  <empty>  |
 84   // +-----------+             +-----------+
 85   if (slices_to_keep > 0) {
 86     for (int dest_slice = 0; dest_slice < slices_to_keep; ++dest_slice) {
 87       uint8_t* dest_slice_data =
 88           feature_data_ + (dest_slice * kFeatureSliceSize);
 89       const int src_slice = dest_slice + slices_to_drop;
 90       const uint8_t* src_slice_data =
 91           feature_data_ + (src_slice * kFeatureSliceSize);
 92       for (int i = 0; i < kFeatureSliceSize; ++i) {
 93         dest_slice_data[i] = src_slice_data[i];
 94       }
 95     }
... 
102     for (int new_slice = slices_to_keep; new_slice < kFeatureSliceCount;
103          ++new_slice) {
104       const int new_step = (current_step - kFeatureSliceCount + 1) + new_slice;
105       const int32_t slice_start_ms = (new_step * kFeatureSliceStrideMs);
106       int16_t* audio_samples = nullptr;
107       int audio_samples_size = 0;
108       // TODO(petewarden): Fix bug that leads to non-zero slice_start_ms
109       //printf("\n INSIDE PopulateFeatureData   -11  \n");
110       GetAudioSamples(error_reporter, (slice_start_ms > 0 ? slice_start_ms : 0),
111                       kFeatureSliceDurationMs, &audio_samples_size,
112                       &audio_samples);
113
114      // printf("\n INSIDE PopulateFeatureData   -12  \n");
115       if (audio_samples_size < kMaxAudioSampleSize) {
116         TF_LITE_REPORT_ERROR(error_reporter,
117                              "Audio data size %d too small, want %d",
118                              audio_samples_size, kMaxAudioSampleSize);
119         return kTfLiteError;
120       }
121       //printf("\n INSIDE PopulateFeatureData   -13  \n");
122       uint8_t* new_slice_data = feature_data_ + (new_slice * kFeatureSliceSize);
123       size_t num_samples_read;
124       TfLiteStatus generate_status = GenerateMicroFeatures(
           ====================================================
125           error_reporter, audio_samples, audio_samples_size, kFeatureSliceSize,
126           new_slice_data, &num_samples_read);
127       //printf("\n INSIDE PopulateFeatureData   -14  \n");
128       if (generate_status != kTfLiteOk) {
129         return generate_status;
130       }
131     }
132   }
133   //printf("\n INSIDE PopulateFeatureData   END \n");
134   return kTfLiteOk;
135 }
 
This is a 2D array with a single channel, so we can visualize it as a monochrome image. 
We’re working with 16 KHz audio sample data, so how do we get to this representation from that source?
The process is an example of what’s known as “feature generation” in machine learning, 
and the goal is to turn an input format that’s more difficult to work with 
(in this case 16,000 numerical values representing a second of audio) 

 Another aspect to this is that the generated spectrograms are a lot smaller than the sample data. 
 Each spectrogram consist of 1,960 numeric values, whereas the waveform has 16,000. 

  
The process begins by generating a Fourier transform, 
(FFT) for a given time slice in  our case 30 ms of audio data. 

This FFT is generated on data that’s been filtered with a Hann window , 
a bell-shaped function that reduces the influence of samples at either end of the 30-ms window. 
A Fourier transform produces complex numbers with real and imaginary components for every frequency, 
but all we care about is the overall energy, 
so we sum the squares of the two components and then apply a square root to get a magnitude for each frequency bucket.

Given N samples, a Fourier transform produces information on N /2 frequencies. 
30 ms at a rate of 16,000 samples per second requires 480 samples, 
and because our FFT algorithm needs a power of two input, 
we pad that with zeros to 512 samples, giving us 256 frequency buckets. 

This is larger than we need, 
so to shrink it down we average adjacent frequencies into 40 downsampled buckets. 
This downsampling isn’t linear, though; instead, 
it uses the human perception–based mel frequency 
scale to give more weight to lower frequencies so that 
there are more buckets available for them, 
and higher frequencies are merged into broader buckets. Figure 8-26 presents a diagram of that process.
  
  Figure 8-26. Diagram of the feature-generation process One unusual aspect of this feature generator is that it then includes a noise reduction step. 
  
This works by keeping a running average of the value in each frequency bucket 
and then subtracting this average from the current value.

The idea is that background noise will be fairly constant over time and show up in particular frequencies. By subtracting the running average, we have a good chance of removing some of the effect of that noise and leaving the more rapidly changing speech that we’re interested in intact. The tricky part is that the feature generator does retain state to track the running averages for each bucket, so if you’re trying to reproduce the same spectrogram output for a given input like we try to for testing you will need to reset that state to the correct values. Another part of the noise reduction that initially surprised us was its use of different coefficients for the odd and even frequency buckets.

This results in the distinctive comb-tooth patterns that you can see in the final generated feature images (Figures 8-22 through 8-25 ). Initially we thought this was a bug, but on talking to the original implementors, we learned that it was actually added deliberately to help performance. 

We then use per-channel amplitude normalization (PCAN) auto-gain to boost the signal based on the running average noise. Finally, we apply a log scale to all the bucket values, so that relatively loud frequencies don’t drown out quieter portions of the spectrum a normalization that helps the subsequent model work with the features.

This process is repeated 49 times in total, 
with a 30-ms window that’s moved forward 20 ms each time between iterations,
to cover the full one second of audio input data. 
This produces a 2D array of values that’s 40 elements wide 
(one for each frequency bucket) and 49 rows high (one row for each time slice). 

```



<https://github.com/mborgerding/kissfft>




## CMSIS-NN
<https://community.platformio.org/t/enabling-cmsis-nn-in-platformio/6505/13>

<https://community.arm.com/developer/tools-software/oss-platforms/f/machine-learning-forum/45879/re-build-tensorflow-lite-model-in-cmsis-nn>


```
gmake -f tensorflow/lite/micro/tools/make/Makefile TARGET=mbed TAGS="cmsis-nn nxp_k66f" generate_micro_speech_mbed_project

cd tensorflow/lite/micro/tools/make/gen/mbed_cortex-m4/prj/micro_speech/mbed
mbed compile --target K66F --toolchain GCC_ARM --profile release


[Error]  add.cc@18,10: arm_nnfunctions.h: No such file or directory
[Error] arm_nnsupportfunctions.h@692,39: 'Q31_MIN' was not declared in this scope
```
<https://github.com/tensorflow/tensorflow/issues/37730>

<https://github.com/ARMmbed/mbed-os/issues/12568>

<https://community.arm.com/developer/tools-software/oss-platforms/f/machine-learning-forum/45879/re-build-tensorflow-lite-model-in-cmsis-nn>



<https://github.com/ARM-software/ML-KWS-for-MCU/tree/master/Deployment>

<https://developer.arm.com/solutions/machine-learning-on-arm/developer-material/how-to-guides/build-arm-cortex-m-voice-assistant-with-google-tensorflow-lite/single-page>

<https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/micro/examples/micro_speech>

<https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/micro>


<https://github.com/tensorflow/tensorflow/issues/38778>

```
./tensorflow/lite/micro/examples/micro_speech/main.cc:int main(int argc, char* argv
```


mbed compile --target K66F --toolchain GCC_ARM --profile release --flash --sterm --baudrate 14500
```
tensorflow//lite/micro/examples/micro_speech/nxp_k66f/audio_provider.cc:  // This should only be called when the main thread notices that the latest
tensorflow//lite/micro/examples/micro_speech/nxp_k66f/audio_provider.cc:  // overwrite the data, but the assumption is that the main thread is checking
tensorflow//lite/micro/micro_interpreter.cc:  context_.recommended_num_threads = 1;
```

### FRDM-K66F

<https://github.com/ARMmbed/mbed-os-example-pelion>. 

<https://os.mbed.com/teams/NXP/code/pelion-example-frdm/>

<https://os.mbed.com/teams/NXP/code/pelion-example-frdm/docs/tip/>

<https://os.mbed.com/platforms/FRDM-K66F/>   has Digital MEMS microphone

```
./BUILD/K66F/GCC_ARM/K66F-tf.bin
./BUILD/K66F/GCC_ARM-RELEASE/K66F.bin
```
To find the device name under Mac OS X, use the command ''ls /dev/tty.usbmodem*''

<http://www.nxp.com/frdm-k66f>


ARM® Cortex®-M4 core running up to 180MHz and embedding 
```
- 2MB Flash, 
- 256KB RAM
- audio codec, 
- digital MEMS microphone
- dual-role high-speed USB
- microSD card slot 
- Ethernet port and headers for use with Bluetooth® and 2.4 GHz radio add-on modules. 
```
### FRDM-K64F

https://os.mbed.com/platforms/FRDM-K64F/


### /tensorflow/lite/micro/mbed/debug_log.cc
Original file was modified to remove the line 
```
static Serial pc(USBTX, USBRX);
```
<https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/micro/mbed/debug_log.cc>
```
#include "tensorflow/lite/micro/debug_log.h"

#include <mbed.h>

// On mbed platforms, we set up a serial port and write to it for debug logging.
extern "C" void DebugLog(const char* s) {
    printf("%s", s);
}
```

mbed_app.json
```
{
    "config": {
	"main-stack-size": {
            "value": 65536
	}
    },
    "requires": ["bare-metal"]
    ,"macros": [
        "TF_LITE_STATIC_MEMORY"
    ]
}
```
### Create a C array 
Back in “Converting to a C File” , we used the xxd command to convert a TensorFlow Lite model into a C array. We’ll do the same thing in the next cell: # Install xxd if it is not available !apt-get qq install xxd
```
# Save the file as a C source file !
xxd i /content/tiny_conv.tflite > /content/tiny_conv.cc
# Print the source file !
cat /content/tiny_conv.cc 
The final part of the output will be the file’s contents, which are a C array and an integer holding its length, as follows (the exact values you see might be slightly different):

unsigned char _content_tiny_conv_tflite [] = { 0x1c , 0x00 , 0x00 , 0x00 , 0x54 , 0x46 , 

0x4c , 0x33 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x0e , 0x00 , 0x18 , 0x00 , 0x04 , 0x00 , 0x08 , 0x00 , 0x0c , 0x00 , // ... 0x00 , 0x09 , 0x06 , 0x00 , 0x08 , 0x00 , 0x07 , 0x00 , 0x06 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x04 }; 
unsigned int _content_tiny_conv_tflite_len = 18208 ; 
```
This code is also written to a file, tiny_conv.cc , which you can download using Colab’s file browser. Because your Colab runtime will expire after 12 hours, it’s a good idea to download this file to your computer now. Next, we’ll integrate this newly trained model with the micro_speech project so that we can deploy it to some hardware . 

### Using the Model in Our Project 

To use our new model, we need to do three things:
1. in micro_features/tiny_conv_micro_feat
 micro_features/tiny_conv_micro_features_model_data.cc , replace the original model data with our new model.
 
2. Update the label names in micro_features/micro_model_settings.cc with our new “on” and “off” labels.

3. Update the device-specific command_responder.cc to take the actions we want for the new labels.


### Replacing the Model 

To replace the model, open ```micro_features/tiny_conv_micro_features_model_data.cc``` in your text editor. Note If you’re working with the Arduino example, the file will appear as a tab in the Arduino IDE. Its name will be micro_features_tiny_conv_micro_features_model_data.cpp .
If you’re working with the SparkFun Edge, you can edit the files directly in your local copy of the 
TensorFlow repository.
If you’re working with the STM32F746G, you should edit the files in your Mbed project directory. The tiny_conv_micro_features_model_data.cc file contains an array declaration that looks like this: 
```
const unsigned char g_tiny_conv_micro_features_model_data [] DATA_ALIGN_ATTRIBUTE = { 0x18 , 0x00 , 0x00 , 0x00 , 0x54 , 0x46 , 0x4c , 0x33 , 0x00 , 0x00 , 0x0e , 0x00 , 0x18 , 0x00 , 0x04 , 0x00 , 0x08 , 0x00 , 0x0c , 0x00 , 0x10 , 0x00 , 0x14 , 0x00 , //... 0x00 , 0x09 , 0x06 , 0x00 , 0x08 , 0x00 , 0x07 , 0x00 , 0x06 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x04 };
const int g_tiny_conv_micro_features_model_data_len = 18208 ; 

``` 
You’ll need to replace the contents of the array as well as the value of the constant g_tiny_conv_micro_features_model_data_len , if it has changed. To do so, open the tiny_conv.cc file that you downloaded at the end of the previous section. Copy and paste the contents of the array, but not its definition, into the array defined in tiny_conv_micro_features_model_data.cc . Make sure you are overwriting the array’s contents, but not its declaration. At the bottom of tiny_conv.cc you’ll find _content_tiny_conv_tflite_len , a variable whose value represents the length of the array.
Back in tiny_conv_micro_features_model_data.cc , replace the value of g_tiny_conv_micro_features_model_data_len with the value of this variable. 
Then save the file; you’re done updating it. 


### Updating the Labels
Next, open 
micro_features/micro_model_settings.cc . This file contains an array of class labels:
```
const char * kCategoryLabels [ kCategoryCount ] = { "silence" , "unknown" , "yes" , "no" , };
```
To adjust this for our new model, we can just swap the “yes” and “no” for “on” and “off.” We match labels with the model’s output tensor elements by order, so it’s important to list these in the same order in which they were provided to the training script. Here’s the expected code: 
```
const char * kCategoryLabels [ kCategoryCount ] = { "silence" , "unknown" , "on" , "off" , }; 
```
If you trained a model with more than two labels, just add them all to the list. We’re now done switching over the model. The only remaining step is to update any output code that uses the labels. 

### Updating command_responder.cc 

The project contains a different device-specific implementation of command_responder.cc for the Arduino, SparkFun Edge, and STM32F746G. We show how to update each of these in the following sections.

### Arduino 
The Arduino command responder, located in arduino/command_responder.cc , lights an LED for 3 seconds when it hears the word “yes.” Let’s update it to light the LED when it hears either “on” or “off.” In the file, locate the following if statement: 
```
// If we heard a "yes", switch on an LED and store the time. 
if ( found_command [ 0 ] == 'y' ) { 

last_yes_time = current_time ; digitalWrite ( LED_BUILTIN , HIGH ); }
```
The if statement tests whether the first letter of the command is “y,” for “yes.” If we change this “y” to an “o,” the LED will be lit for either “on” or “off,” because they both begin with “o”:
```
if ( found_command [ 0 ] == 'o' ) { 
  last_yes_time = current_time ; 
  digitalWrite ( LED_BUILTIN , HIGH ); 
}
```

### Project Idea 
Switching an LED on by saying “off” doesn’t make much sense. Try changing the code so that you can turn the LED on by saying “on” and off by saying “off.” You can use the second letter of each command, accessed via found_command[1] , to disambiguate between “on” and “off”:
```
if ( found_command [ 0 ] == 'o' && found_command [ 1 ] == 'n' ) { 
  
```
 After you’ve made these code changes, deploy to your device and give it a try.
 
 ### SparkFun Edge
 The SparkFun Edge command responder, located in sparkfun_edge/command_responder.cc , lights up a different LED depending on whether it heard “yes” or “no.” In the file, locate the following if statements: 
 ```
 if ( found_command [ 0 ] == 'y' ) { am_hal_gpio_output_set ( AM_BSP_GPIO_LED_YELLOW ); } 
 if ( found_command [ 0 ] == 'n' ) { am_hal_gpio_output_set ( AM_BSP_GPIO_LED_RED ); } 
 if ( found_command [ 0 ] == 'u' ) { am_hal_gpio_output_set ( AM_BSP_GPIO_LED_GREEN ); } 
```
 It’s simple to update these so that “on” and “off” each turn on different LEDs:
 ```
 if ( found_command [ 0 ] == 'o' && found_command [ 1 ] == 'n' ) { am_hal_gpio_output_set ( AM_BSP_GPIO_LED_YELLOW ); } 
 if ( found_command [ 0 ] == 'o' && found_command [ 1 ] == 'f' ) { am_hal_gpio_output_set ( AM_BSP_GPIO_LED_RED ); } 
 if ( found_command [ 0 ] == 'u' ) { am_hal_gpio_output_set ( AM_BSP_GPIO_LED_GREEN ); }
``` 
 Because both commands begin with the same letter, we need to look at their second letters to disambiguate them. Now, the yellow LED will light when “on” is spoken, and the red will light for “off.” 

Warden, Pete,Situnayake, Daniel. TinyML (Kindle Locations 4174-4185). O'Reilly Media. Kindle Edition.  
 
 

## Appendix B

The following text walks through the audio capture code from the wake-word application in Chapter 7 . Since it’s not directly related to machine learning, it’s provided as an appendix. The Arduino Nano 33 BLE Sense has an on-board microphone. To receive audio data from the microphone, we can register a callback function that is called when there is a chunk of new audio data ready. Each time this happens, we’ll write the chunk of new data to a buffer that stores a reserve of data. Because audio data takes up a lot of memory, the buffer has room for only a set amount of data. This data is overwritten when 

Whenever our program is ready to run inference, it can read the last second’s worth of data from this buffer. As long as new data keeps coming in faster than we need to access it, there’ll always be enough new data in the buffer to preprocess and feed into our model. Each cycle of preprocessing and inference is complex, and it takes some time to complete. Because of this, we’ll only be able to run inference a few times per second on an Arduino.

 This means that it will be easy for our buffer to stay full. As we saw in Chapter 7 , ```audio_provider.h``` implements these two functions: GetAudioSamples() , which provides a pointer to a chunk of raw audio data
``LatestAudioTimestamp()`` , which returns the timestamp of the most recently captured audio
The code that implements these for Arduino is located in 

``arduino/audio_provider.cc`` 

In the first part, we pull in some dependencies. The PDM.h library defines the API that we’ll use to get data from the microphone. The file micro_model_settings.h contains constants related to our model’s data requirements that will help us provide audio in the correct format:
```
#include "tensorflow/lite/micro/examples/micro_speech/ audio_provider.h " 
#include "PDM.h" 
#include "tensorflow/lite/micro/examples/micro_speech/ micro_features / micro_model_settings.h " 
```

The next chunk of code is where we set up some important variables:
```
namespace { 
bool g_is_audio_initialized = false ; 
// An internal buffer able to fit 16x our sample 
size constexpr int kAudioCaptureBufferSize = DEFAULT_PDM_BUFFER_SIZE * 16 ; 
int16_t g_audio_capture_buffer [ kAudioCaptureBufferSize ]; 
// A buffer that holds our output int16_t g_audio_output_buffer [ kMaxAudioSampleSize ]; 
// Mark as volatile so we can check in a while loop to see if 
// any samples have arrived yet. 
volatile int32_t g_latest_audio_timestamp = 0 ; 
} // namespace  
```

Boolean g_is_audio_initialized is what we’ll use to track whether the microphone has started capturing audio. Our audio capture buffer is defined by g_audio_capture_buffer and is sized to be 16 times the size of DEFAULT_PDM_BUFFER_SIZE , which is a constant defined in PDM.h that represents the amount of audio we receive from the microphone each time the callback is called. 
Having a nice big buffer means that we’re unlikely to run out of data if the program 
slows down for some reason. 
In addition to the audio capture buffer, we also keep a buffer of output audio: 
g_audio_output_buffer , 
that we’ll return a pointer to when GetAudioSamples() is called. It’s the length of kMaxAudioSampleSize , which is a constant from micro_model_settings.h that defines the number of 16-bit audio samples our preprocessing code can handle at once. 
Finally, we use g_latest_audio_timestamp to keep track of the time represented by our most recent audio sample. This won’t match up with the time on your wristwatch; it’s just the number of milliseconds relative to when audio capture began. The variable is declared as volatile , which means the processor shouldn’t attempt to cache its value. We’ll see why later on. After setting up these variables, we define the callback function that will be called every time there’s new audio data available. Here it is in its entirety: 

```
void CaptureSamples () { 
// This is how many bytes of new data we have each time this is called 
const int number_of_samples = DEFAULT_PDM_BUFFER_SIZE ; 
// Calculate what timestamp the last audio sample represents 
const int32_t time_in_ms = g_latest_audio_timestamp + ( number_of_samples / ( kAudioSampleFrequency / 1000 )); 
// Determine the index, in the history of all samples, of the last sample 
const int32_t start_sample_offset = g_latest_audio_timestamp * ( kAudioSampleFrequency / 1000 ); 
// Determine the index of this sample in our ring buffer 
const int capture_index = start_sample_offset % kAudioCaptureBufferSize ; 
// Read the data to the correct place in our buffer
PDM.read ( g_audio_capture_buffer + capture_index , DEFAULT_PDM_BUFFER_SIZE ); 
// This is how we let the outside world know that new audio data has 
arrived. g_latest_audio_timestamp = time_in_ms ; 
} 
```

This function is a bit complicated, so we’ll walk through it in chunks. Its goal is to determine the correct index in the audio capture buffer to write this new data to. First, we figure out how much new data we’ll receive each time the callback is called. We use that to determine a number in milliseconds that represents the time of the most recent audio sample in the buffer: 

```
// This is how many bytes of new data we have each time this is called 
const int number_of_samples = DEFAULT_PDM_BUFFER_SIZE ; 
// Calculate what timestamp the last audio sample represents 
const int32_t time_in_ms = g_latest_audio_timestamp + ( number_of_samples / ( kAudioSampleFrequency / 1000 )); 
```

The number of audio samples per second is kAudioSampleFrequency 
(this constant is defined in micro_model_settings.h ). 
We divide this by 1,000 to get the number of samples per millisecond. Next, we divide the number of samples per callback ( number_of_samples ) by the samples per millisecond to obtain the number of milliseconds’ worth of data we obtain each callback: 
```
(number_of_samples / (kAudioSampleFrequency / 1000)) 
```
We then add this to the timestamp of our previous most recent audio sample, g_latest_audio_timestamp , to obtain the timestamp of the most recent new audio sample. After we have this number, we can use it to obtain the index of the most recent sample in the history of all samples . 
To do this, we multiply the timestamp of our previous most recent audio sample by the number of samples per millisecond: 

```
const int32_t start_sample_offset = g_latest_audio_timestamp * ( kAudioSampleFrequency / 1000 ); 
```

Our buffer doesn’t have room to store every sample ever captured, though. 
Instead, it has room for 16 times the DEFAULT_PDM_BUFFER_SIZE . 
As soon as we have more data than that, we start overwriting the buffer with new data.
We now have the index of our new samples in the history of all samples .
Next, we need to convert this into theh samples’ proper index within our actual buffer. 
To do this, we can divide our history index by the buffer length and get the remainder. This is done using the modulo operator ( % ): 

```
// Determine the index of this sample in our ring buffer 
const int capture_index = start_sample_offset % kAudioCaptureBufferSize ; 
```


Because the buffer’s size, kAudioCaptureBufferSize , is a multiple 
of DEFAULT_PDM_BUFFER_SIZE , the new data will always fit neatly into the buffer. The modulo operator will return the index within the buffer where the new data should begin. Next, we use the PDM.read() method to read the latest audio into the audio capture buffer: 

```
// Read the data to the correct place in our buffer PDM . 
read ( g_audio_capture_buffer + capture_index , DEFAULT_PDM_BUFFER_SIZE ); 
```

The first argument accepts a pointer to a location in memory that the data should be written to. The variable g_audio_capture_buffer is a pointer to the address in memory where the audio capture buffer starts. By adding capture_index to this location, we can calculate the correct spot in memory to write our new data. The second argument defines how much data should be read, and we go for the maximum, DEFAULT_PDM_BUFFER_SIZE . 


Finally, we update g_latest_audio_timestamp : 
```
// This is how we let the outside world know that new audio data has arrived. 
g_latest_audio_timestamp = time_in_ms ; 
```

This will be exposed to other parts of the program via the LatestAudioTimestamp() method, letting them know when new data becomes available. Because g_latest_audio_timestamp is declared as volatile , its value will be looked up from memory every time it is accessed. This is important, because otherwise the variable would be cached by the processor. Because its value is set in a callback, the processor would not know to refresh the cached value, and any code accessing it would not receive its current value. You might be wondering what makes CaptureSamples() act as a callback function. How does it know when new audio is available? This, among other things, is handled in the next part of our code, which is a function that initiates audio capture: 
```
TfLiteStatus InitAudioRecording ( tflite :: ErrorReporter * error_reporter ) { 
// Hook up the callback that will be called with each sample 
PDM. onReceive ( CaptureSamples ); 
// Start listening for audio: MONO @ 16KHz with gain at 20 
PDM . begin ( 1 , kAudioSampleFrequency ); 
PDM . setGain ( 20 ); 
// Block until we have our first audio sample 
while ( ! g_latest_audio_timestamp ) {
} 
return kTfLiteOk ;
} 
```
This function will be called the first time someone calls GetAudioSamples() . It first uses the PDM library to hook up the CaptureSamples() callback, by calling PDM.onReceive() . 

Next, PDM.begin() is called with two arguments. 
The first argument indicates how many channels of audio to record; we only want mono audio, so we specify 1 . 
The second argument specifies how many samples we want to receive per second. 

Next, PDM.setGain() is used to configure the gain , which defines how much the microphone’s audio should be amplified. We specify a gain of 20 , which was chosen after some experimentation.

Finally, we loop until g_latest_audio_timestamp evaluates to true. Because it starts at 0 , this has the effect of blocking execution until some audio has been captured by the callback, since at that point g_latest_audio_timestamp will have a nonzero value. 
The two functions we’ve just explored allow us to initiate the process of capturing audio and to store the captured audio in a buffer. 
The next function, GetAudioSamples() , provides a mechanism for other parts of our code (namely, the feature provider) to obtain audio data: 
```
TfLiteStatus GetAudioSamples ( tflite :: ErrorReporter * error_reporter , 
int start_ms , int duration_ms , int * audio_samples_size , int16_t ** audio_samples ) {
// Set everything up to start receiving audio 
if ( ! g_is_audio_initialized ) { 
   TfLiteStatus init_status = InitAudioRecording ( error_reporter ); 
   if ( init_status != kTfLiteOk ) { 
      return init_status ; 
   }
   g_is_audio_initialized = true ; 
} 
```

The function is called with an ErrorReporter for writing logs, two variables that specify what audio we’re requesting ( start_ms and duration_ms ), and two pointers used to pass back the audio data ( audio_samples_size and audio_samples ). 
The first part of the function calls InitAudioRecording() . 
As we saw earlier, this blocks execution until the first samples of audio have arrived. 
We use the variable g_is_audio_initialized to ensure this setup code runs only once. 
After this point, we can assume that there’s some audio stored in the capture buffer. 
Our task is to figure out where in the buffer the correct audio data is located. 
To do this, we first determine the index in the history of all samples of the first sample that we want: 
```
const int start_offset = start_ms * ( kAudioSampleFrequency / 1000 ); 
```
Next, we determine the total number of samples that we want to grab:
```
const int duration_sample_count = duration_ms * ( kAudioSampleFrequency / 1000 ); 
```
Now that we have this information, we can figure out where in our audio capture buffer to read. 
We’ll read the data in a loop:
```
for ( int i = 0 ; i < duration_sample_count ; ++ i ) { 
// For each sample, transform its index in the history of all samples into 
// its index in g_audio_capture_buffer 
const int capture_index = ( start_offset + i ) % kAudioCaptureBufferSize ;

// Write the sample to the output 
buffer g_audio_output_buffer [ i ] = g_audio_capture_buffer [ capture_index ];
} 
```
Earlier, we saw how we can use the modulo operator to find the correct position within a buffer that only has enough space to hold the most recent samples. 
Here we use the same technique again if we divide the current index within the history of all samples by the size of the audio capture buffer, kAudioCaptureBufferSize , 
the remainder will indicate that data’s position within the buffer. 
We can then use a simple assignment to read the data from the capture buffer to the output buffer. Next, to get data out of this function, we use two pointers that were supplied as arguments. These are audio_samples_size , which points to the number of audio samples, and audio_samples , which points to the output buffer: 
```
// Set pointers to provide access to the 
audio * audio_samples_size = kMaxAudioSampleSize ;
* audio_samples = g_audio_output_buffer ; 
return kTfLiteOk ; 
} 
```
We end the function by returning kTfLiteOk , letting the caller know that the operation was successful. Then, in the final part, we define
```
LatestAudioTimestamp() : int32_t LatestAudioTimestamp () { return g_latest_audio_timestamp ; } 
```
Since this always returns the timestamp of the most recent audio, it can be checked in a loop by other parts of our code to determine if new audio data has arrived. 

That’s all for our audio provider! We’ve now ensured that our feature provider has a steady supply of fresh audio samples. 

 
   
 
 
