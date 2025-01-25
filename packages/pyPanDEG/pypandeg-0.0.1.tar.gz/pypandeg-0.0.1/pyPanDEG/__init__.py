# __init__.py

from .dataset_downloader import download_data
from .rna_seq_processor import process_rna_seq
from .cds_downloader import download_cds
from .gene_clusterer import merge_fasta_files, run_mmseqs_clustering, relabel_tabular_files
from .genecount_modifier import process_counts_file
from .deg_analyzer import run_deg_analysis

# 패키지 외부에서 사용 가능한 함수 목록 정의
__all__ = [
    "download_data",
    "process_rna_seq",
    "download_cds",
    "merge_fasta_files",
    "run_mmseqs_clustering",
    "relabel_tabular_files",
    "process_counts_file",
    "run_deg_analysis",
]
