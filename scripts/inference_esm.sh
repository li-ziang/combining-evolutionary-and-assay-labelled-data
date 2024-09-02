#!/bin/bash


dataset='BLAT_ECOLX_Ranganathan2015-2500'

python src/esm_inference.py data/$dataset/seqs.fasta \
    data/$dataset/wt.fasta  results/BLAT_ECOLX_Ranganathan2015-2500/esm/\
    --model_location /nethome/zli3161/DATA-nash/PSNet/PSNet/data/Domainome/esm1b_t33_650M_UR50S.pt
    --toks_per_batch 65536