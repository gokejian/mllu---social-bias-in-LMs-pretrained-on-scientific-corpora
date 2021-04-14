# CrowS-Pairs

This folder contains the modified code and experimental results running CrowS-Pairs on BERT, RoBERTa, BioBERT, and SciBERT.

The code is mainly based on https://github.com/nyu-mll/crows-pairs. We added support for BioBERT https://github.com/dmis-lab/biobert-pytorch and SciBERT https://github.com/allenai/scibert in the **metric.py**.

The main metric results are in the /crows_slurm_output folder 5111759_run_crowspairs.out.

The results for all 9 bias types are saved as csv files: bert_crows_score.csv,roberta_crows_score.csv, biobert_crows_score.csv, and scibert_crows_score.csv

The analysis code is in **bias_type_analysis_ipynb**

This task is done by Kejian Shi,

<img width="500" alt="Screen Shot 2021-04-14 at 2 08 31 PM" src="https://user-images.githubusercontent.com/32584185/114758393-e9b3e400-9d2a-11eb-9bfd-d314e55fd813.png">



## Reference

```
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
```




