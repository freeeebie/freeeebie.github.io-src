---
Title: End-to-End Speech Recognition - 작성중
Date: 2017-06-24 20:11:07 +0900
Tags: "Machine&nbsp;Learning"
---

해당 글은 "Towards End-to-End Speech Recognition with Recurrent Neural Networks" 를 기반하여 공부한 내용을 작성하였다. 

기존에 Neural Network을 적용한 음성 인식 모델은 여러 단계 중 하나의 단계, 즉 classify 를 위하여 NN 을 사용하였다. 

기존 모델의 동작 파이프라인을 개략적으로 나타내면 아래와 같다. 

1. Feature extraction : MFCC 와 같은 단계를 의미한다. 
2. Speaker Normalization : Vocal tract length normalization 
3. Neural Network : Accoustic data 의 개별 프레임을 분류하기 위해 사용
4. Output distirbution : HMM 을 위한 것

이러한 모델의 단점은 우선  Pronouncation dictionary 가 필요하다는 것이다. Speech recognition system 을 트레인 시키기 위하여 사용되는 transcription 은 어휘인데 반해 네트워크가 제시하는 것은 음소이다. 그러므로 단어들을 음소의 모음으로 매핑 시키기 위해서 pronunciation dictionary 가 필요하다. 즉, '한강' 이라는 단어를 train 한다면 나오는 결과가 'ㅎ ㅏ ㄴ ㄱ ㅏ ㅇ' 인 음소의 나열이 나온다는 의미로 보인다. 이것을 원래 단어와 매핑 시키기 위하여 사전이 필요하다는 것이고 이것은 사람이 일일이 만들어야 하는 수고가 필요하다는 것이다.  

또한 language model (https://en.wikipedia.org/wiki/Language_model)이 필요하다는 것이다. HMM 에 의해 산출된 accoustic score 는 text corpus 를 train 한 language model 과 결합된다. 이러한 약점들을 극복하기 위하여 하나의 네트워크로 음성 인식이 가능한 End-to-end Speech Recognition 이 출현하게 된 것이다. 

음성 인식 문서를 읽다보면 자주 나오는 용어들이 있다. 여기서 잠시 용어를 정리하면,  

- phonetic, phoneme : 음소. 더 이상 작게 나눌 수 없는 음운론상의 최소 단위라고 한다. 낱소리라고도 한다.   한국어에서는 쉽게 자음과 모음이라고 생각하면 된다. 
- lexical, lexicon : lexical 은 어휘라는 뜻이고, lexicon은 사전이란 뜻으로 음성인식에서는 어휘 목록이라는 의미로 사용된다. 
- text corpus
- transcription : 구술된 내용을 글로 옯김. 



 

이 논문에서는  Spectrogram 을 최소한의 preprocession scheme 으로 사용하였다. Spectrogram 은 신호를 x축은 시간, y축은 주파수로 설정하고, 진폭의 차이에 따라 농도나 색상으로 나타내는 것을 의미한다.  

## Network architecture

이 논문을 이해하려고 한다면 선행적으로 RNN 과 LSTM 에 대한 이해를 해야 한다. 

RNN 은 아래에 잘 설명이 되어 있다. 

http://aikorea.org/blog/rnn-tutorial-1/


