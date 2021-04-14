# CrowS-Pairs

This folder contains the modified code and experimental results running CrowS-Pairs on BERT, RoBERTa, BioBERT, and SciBERT.

The code is mainly based on https://github.com/nyu-mll/crows-pairs. We added support for BioBERT https://github.com/dmis-lab/biobert-pytorch and SciBERT https://github.com/allenai/scibert in the **metric.py**.

The main metric results are in the /crows_slurm_output folder 5111759_run_crowspairs.out.

The results for all 9 bias types are saved as csv files: bert_crows_score.csv,roberta_crows_score.csv, biobert_crows_score.csv, and scibert_crows_score.csv

The analysis code is in **bias_type_analysis_ipynb**

This task is done by Kejian Shi,
![crows_contribution](https://user-images.githubusercontent.com/32584185/114758135-9e013a80-9d2a-11eb-839e-806b8c197df3.jpg)


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




