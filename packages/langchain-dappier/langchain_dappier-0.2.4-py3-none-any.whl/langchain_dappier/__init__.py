from importlib import metadata

from langchain_dappier.retrievers import DappierRetriever
from langchain_dappier.tools import (
    DappierRealTimeSearchTool,
    DappierAIRecommendationTool
)

try:
    __version__ = metadata.version("langchain_dappier")
except metadata.PackageNotFoundError:
    # Case where package metadata is not available.
    __version__ = ""
del metadata  # optional, avoids polluting the results of dir(__package__)

__all__ = [
    "DappierRetriever",
    "DappierRealTimeSearchTool",
    "DappierAIRecommendationTool",
    "__version__",
]
