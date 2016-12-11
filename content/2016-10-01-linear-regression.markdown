---
Title: "Linear Regression"
Date: 2016-10-01 22:18:30 +0900
Tags: 'Machine&nbsp;Learning' 
---
#  다항식 회귀  
$$ g(x_i | w_k, \cdots, w_1, w_0) = w_k(x_i)^k + \cdots + w_2(x_i)^2 + w_1(x_i) + w_0$$  
$ \overrightarrow{z_i}= [x_i \:\:(x_i)^2 \:\cdots\: (x_i)^k] $ 를 갖는 다변의 선형 회귀라고 여기고 푼다.  

# Model Selection  
정확도를 어떻게 측정. 최대로 잘 맞는지  

# overfitting 
모델에 비해 data 가 너무 적어 noise 까지 fitting 해버리는 현상  

#알고리즘 정확도 측정 
학습에 동원되지 않은 데이터로 에러 측정  
K-folder Cross Validation \(CV\)  

## 항상 지켜야 될 원칙 
훈련에 쓰지 않는 데이터로 에러 측정 

## Dimension의 저주  
각 데이터가 10개의 속성이 있을 때 $10^{10} \:?? $

# Feature mapping 
$$ \overrightarrow{z} = \phi(\overrightarrow{x}) $$  
$$ \frac{1}{wt} = \phi(wt) \Rightarrow mpg = w_0 + w_1 \frac{1}{wt}$$  


