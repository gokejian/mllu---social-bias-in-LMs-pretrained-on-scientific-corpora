# mllu - social bias in LMs pretrained on scientific corpora
 
This is the group project from Chuwei Xu, Leyi Yan, Kejian Shi for NYU MLLU class Sp21

Our project has two axes: Bias Detection and NLU Performance.For our bias detection experiments, we already have the full results. These are done by modifying the codes from (Nangia et al.,2020). Also we coded our own data analysis script to extract the score for different bias types for the CrowS-Pairs benchmark. 
Here is the result:
![Screen Shot 2021-04-26 at 5 57 51 PM](https://user-images.githubusercontent.com/32584185/116156047-f801e880-a6b8-11eb-8e0d-ea4093d17cf5.png )

The codes can be found in the ./bert_base_7_tasks and ./RoBRETa_Large_7_Task.

---

For NLU performance experiments, we already have baseline results for BERT and RoBERTa, and we are working on modifying jiant (Phang et al.,2020) to support our scientific models (BioBERT, SciBERT, ClinicalBERT). 
Here is the baseline result (code ):

![Screen Shot 2021-04-26 at 5 57 55 PM](https://user-images.githubusercontent.com/32584185/116156530-9beb9400-a6b9-11eb-9768-07a16c940a57.png )

The codes can be found in the ./wino_stereo and ./crows_pairs


## Reference 

@inproceedings{nangia2020crows,
    title = "{CrowS-Pairs: A Challenge Dataset for Measuring Social Biases in Masked Language Models}",
    author = "Nangia, Nikita  and
      Vania, Clara  and
      Bhalerao, Rasika  and
      Bowman, Samuel R.",
    booktitle = "Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics"
}


@misc{phang2020jiant,
    author = {Jason Phang and Phil Yeres and Jesse Swanson and Haokun Liu and Ian F. Tenney and Phu Mon Htut and Clara Vania and Alex Wang and Samuel R. Bowman},
    title = {\texttt{jiant} 2.0: A software toolkit for research on general-purpose text understanding models},
    howpublished = {\url{http://jiant.info/}},
    year = {2020}
}
