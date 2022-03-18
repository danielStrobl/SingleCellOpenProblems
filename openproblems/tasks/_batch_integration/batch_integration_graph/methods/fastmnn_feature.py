# from ....tools.normalize import log_cpm
from .....tools.decorators import method
from .....tools.utils import check_version

import scprep

# from scib.integration import _fastmnn_feature


_fastmnn_feature = scprep.run.RFunction(
    setup="""
            library(SingleCellExperiment)
            library(batchelor)
        """,
    args="sobj, batch, hvg=2000",
    body="""
        expr <- assay(sobj, 'counts')
        sce <- fastMNN(expr, batch = colData(sobj)[[batch]])
        assay(sobj, "counts") <- assay(sce, "reconstructed")
        sobj
        """,
)


@method(
    method_name="FastMNN feature",
    paper_name="A description of the theory behind the fastMNN algorithm",
    paper_url="https://marionilab.github.io/FurtherMNN2018/theory/description.html",
    paper_year=2019,
    code_url="https://rdrr.io/github/LTLA/batchelor/man/fastMNN.html",
    code_version=check_version("scprep"),
    image="openproblems-r-batch-integration",  # only if required
)
def fastmnn_feature_full_unscaled(adata):
    from scib.preprocessing import reduce_data

    adata = _fastmnn_feature(adata, "batch")
    reduce_data(adata, umap=False)
    # Complete the result in-place
    return adata


@method(
    method_name="FastMNN feature (hvg/unscaled)",
    paper_name="A description of the theory behind the fastMNN algorithm",
    paper_url="https://marionilab.github.io/FurtherMNN2018/theory/description.html",
    paper_year=2019,
    code_url="https://rdrr.io/github/LTLA/batchelor/man/fastMNN.html",
    code_version=check_version("scprep"),
    image="openproblems-r-batch-integration",  # only if required
)
def fastmnn_feature_hvg_unscaled(adata):
    from ._utils import hvg_batch
    from scib.preprocessing import reduce_data

    adata = hvg_batch(adata, "batch", target_genes=2000, adataOut=True)
    adata = _fastmnn_feature(adata, "batch")
    reduce_data(adata, umap=False)
    return adata


@method(
    method_name="FastMNN feature (hvg/scaled)",
    paper_name="A description of the theory behind the fastMNN algorithm",
    paper_url="https://marionilab.github.io/FurtherMNN2018/theory/description.html",
    paper_year=2019,
    code_url="https://rdrr.io/github/LTLA/batchelor/man/fastMNN.html",
    code_version=check_version("scprep"),
    image="openproblems-r-batch-integration",  # only if required
)
def fastmnn_feature_hvg_scaled(adata):
    from ._utils import hvg_batch
    from ._utils import scale_batch
    from scib.preprocessing import reduce_data

    adata = hvg_batch(adata, "batch", target_genes=2000, adataOut=True)
    adata = scale_batch(adata, "batch")
    adata = _fastmnn_feature(adata, "batch")
    reduce_data(adata, umap=False)
    return adata


@method(
    method_name="FastMNN feature (full/scaled)",
    paper_name="A description of the theory behind the fastMNN algorithm",
    paper_url="https://marionilab.github.io/FurtherMNN2018/theory/description.html",
    paper_year=2019,
    code_url="https://rdrr.io/github/LTLA/batchelor/man/fastMNN.html",
    code_version=check_version("scprep"),
    image="openproblems-r-batch-integration",  # only if required
)
def fastmnn_feature_full_scaled(adata):
    from ._utils import scale_batch
    from scib.preprocessing import reduce_data

    adata = scale_batch(adata, "batch")
    adata = _fastmnn_feature(adata, "batch")
    reduce_data(adata, umap=False)
    return adata
