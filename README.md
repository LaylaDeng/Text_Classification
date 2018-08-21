# Text_Classification
建立模型通过长文本数据正文(article)，预测文本对应的类别(class)，完成分类。

数据集下载地址：http://www.pkbigdata.com/common/cmpt/“达观杯”文本智能处理挑战赛_赛体与数据.html



评分算法:
binary-classification
评分标准 
采用各个品类F1指标的算术平均值，它是Precision 和 Recall 的调和平均数。

![image](https://latex.codecogs.com/gif.latex?%3CF1%3E%3D%5Cfrac%7B1%7D%7Bn%7D%20%5Csum_%7Bi%7D%5E%7Bn%7DF1_i%3D%5Cfrac%7B1%7D%7Bn%7D%5Csum_%7Bi%7D%5E%7Bn%7D%5Cfrac%7B2%5Ccdot%20P_i%5Ccdot%20R_i%7D%7BP_i&plus;R_i%7D)  

其中，Pi是表示第i个种类对应的Precision， Ri是表示第i个种类对应Recall。

<================================================>


``01_try 成绩： 0.777996``  :&nbsp;使用svm.linearSVC
``02_try 成绩： 0.71``  :&nbsp;&nbsp;使用SGDClassifier
