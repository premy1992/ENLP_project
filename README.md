# A Short Answer Grader

This is an automatic short answer grading system written in Python. Given a question, a correct reference answer and a student response, it computes a real-valued score for the student response based on its semantic similarity with the correct answer.


### Prerequisites

What things you need to install the software and how to install them

```
1) NLTK  
2) Scikit-learn
3) Wang2vec  
```

## Installing

NLTK 
```
sudo pip install -U nltk
```
Scikit-learn
```
pip install -U scikit-learn
``` 
Wang2vec:

https://github.com/nathanshartmann/portuguese_word_embeddings



## Running the tests

Instructions To execute Short Answer Grading Project First Run Wang2Vec Model using following command from the wang2vec-master folder $ ./word2vec -train input_file -output embedding_file -type 0 -size 50 -window 5 -negative 10 -nce 0 -hs 0 -sample 1e-4 -threads 1 -binary 1 -iter 5 -cap 0
The -type argument is a integer that defines the architecture to use. These are the possible parameters: 0 - cbow 1 - skipngram 2 - cwindow (see below) 3 - structured skipngram(see below) 4 - collobert's senna context window model (still experimental)
./word2vec -train answers.txt -output embedding_file.bin -type 0 -size 50 -window 5 -negative 10 -nce 0 -hs 0 -sample 1e-4 -threads 1 -binary 1 -iter 5 -cap 0
From terp-master use terp.py file supply sourcefile = "train.csv" and run the command $ python terp.py supply sourcefile = "test.csv" and run the command $ python terp.py
copy and paste these 2 files in wang2vec-master folder $ python ModelTest.py for sourcefile = "train.csv" and sourcefile = "test.csv" $ python KerasModel.py


## Project Directory

* [Source_Directry](https://drive.google.com/drive/folders/0B_qaDpCt_ckYdU5wdlBjYmlNTnc)


