# from ....tools.normalize import log_cpm
from .....tools.decorators import method
from .....tools.utils import check_version


@method(
    method_name="BBKNN",
    paper_name="BBKNN: fast batch alignment of single cell transcriptomes",
    paper_url="https://academic.oup.com/bioinformatics/article/36/3/964/5545955",
    paper_year=2020,
    code_url="",
    code_version=check_version("bbknn"),
    image="openproblems-python-batch-integration",  # only if required
)
def bbknn_full_unscaled(adata):
    # Normalize the data
    from scIB.integration import runBBKNN

    adata = runBBKNN(adata, "batch")
    # Complete the result in-place
    return adata


@method(
    method_name="BBKNN (hvg,unscaled)",
    paper_name="BBKNN: fast batch alignment of single cell transcriptomes",
    paper_url="https://academic.oup.com/bioinformatics/article/36/3/964/5545955",
    paper_year=2020,
    code_url="",
    code_version=check_version("bbknn"),
    image="openproblems-python-batch-integration",  # only if required
)
def bbknn_hvg_unscaled(adata):
    from ._hvg import hvg_batch
    from scIB.integration import runBBKNN

    adata = hvg_batch(adata, "batch", target_genes=2000, adataOut=True)
    adata = runBBKNN(adata, "batch")
    # Complete the result in-place
    return adata


@method(
    method_name="BBKNN (hvg,scaled)",
    paper_name="BBKNN: fast batch alignment of single cell transcriptomes",
    paper_url="https://academic.oup.com/bioinformatics/article/36/3/964/5545955",
    paper_year=2020,
    code_url="",
    code_version=check_version("bbknn"),
    image="openproblems-python-batch-integration",  # only if required
)
def bbknn_hvg_scaled(adata):
    from ._hvg import hvg_batch
    from scIB.integration import runBBKNN
    from scIB.preprocessing import scale_batch

    adata = hvg_batch(adata, "batch", target_genes=2000, adataOut=True)
    adata = scale_batch(adata, "batch")
    adata = runBBKNN(adata, "batch")
    # Complete the result in-place
    return adata


@method(
    method_name="BBKNN (full/scaled)",
    paper_name="BBKNN: fast batch alignment of single cell transcriptomes",
    paper_url="https://academic.oup.com/bioinformatics/article/36/3/964/5545955",
    paper_year=2020,
    code_url="",
    code_version=check_version("bbknn"),
    image="openproblems-python-batch-integration",  # only if required
)
def bbknn_full_scaled(adata):
    from scIB.integration import runBBKNN
    from scIB.preprocessing import scale_batch

    adata = scale_batch(adata, "batch")
    adata = runBBKNN(adata, "batch")
    # Complete the result in-place
    return adata
