# Master's Thesis - Learning what to learn: Generating Language Lessons using BERT
This repository has work done regarding my master's thesis at KU Leuven. In summary, the goal of the thesis was to devise a method to partially automate the process of creating language skill trees such as the ones present in language learning apps. Portuguese was chosen as a case study language for this task. The main goal was subdivided into further tasks. The first task was to make a method to automatically classify the difficulty of text. The second task was to devise a method to classify texts by semantical topic. More details can be found in the [thesis text](./Text%20and%20Defense/Master's%20Thesis%20Text.pdf). Since Github does not support very large files, the models will be hosted elsewhere.

## Task 1 - Proficiency classification
Work regarding the first task, namely fine-tuning a BERTimbau model for classifying Portuguese text difficulty in the CEFR scale, can be found [here](./Task%201%20-%20Proficiency%20classification/). A BERTimbau model was fine-tuned on the COPLE2 corpus for the task of classifying text in Portuguese by difficulty in the CEFR system. The model can be accessed at the [Hugging Face Model Hub](https://huggingface.co/joaoDossena/BERTimbau-CEFR).

## Task 1.5 - Classifying Tatoeba sentences by difficulty
In between the two tasks, an intermediate difficulty classification of Tatoeba sentences was done. It can be found [here](./Task%201.5%20-%20Classify%20Tatoeba%20sentences%20by%20difficulty/).

## Task 2 - Topic modeling
Finally, topic modeling was done, which can be found [here](./Task%202%20-%20Topic%20Modeling%20(VSC)/). Topic modeling was done with BERTopic with default parameters and with the Tatoeba sentences in Portuguese as documents. The model can be accessed at the [Hugging Face Model Hub](https://huggingface.co/joaoDossena/BERTopic-Tatoeba-PT)


