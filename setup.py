from setuptools import setup, find_packages

setup(
    name = "spSeudoMap",
    version = "1.0.0",
    description = "Cell type mapping of spatial transcriptomics using unmatched single-cell RNA-seq data",
    url = "https://github.com/ayanadyg/spSeudoMap.git",
    packages = find_packages(include=['spSeudoMap', 'spSeudoMap.*']),
    author = "Sungwoo Bae, Hongyoon Choi",
    install_requires = ["scanpy==1.9.1","pandas==1.3.5","numpy==1.22.0",
                        "h5py==3.9.0", "jupyter",
                        "keras==2.12.0", "tensorflow==2.12.0"]
)
