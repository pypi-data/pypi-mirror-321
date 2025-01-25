"""Tool for the Dappier API."""

import os
from typing import Dict, List, Literal, Optional, Type, Union

from dappier import Dappier, DappierAsync
from dappier.types import AIRecommendationsResponse
from langchain_core.callbacks import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)
from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field


class DappierInput(BaseModel):
    """Input schema for Dappier tool."""

    query: str = Field(description="search query to look up")


class DappierRealTimeSearchTool(BaseTool):  # type: ignore[override]
    """Tool that queries Dappier's Real Time AI models and returns back an answer.

    Setup:
        Install ``langchain-dappier`` and set environment variable ``DAPPIER_API_KEY``.

        .. code-block:: bash

            pip install -U langchain-dappier
            export DAPPIER_API_KEY="your-api-key"

    Instantiation:
        .. code-block:: python

            from langchain_dappier import DappierRealTimeSearchTool

            tool = DappierRealTimeSearchTool(
                # ai_model_id="am_01j06ytn18ejftedz6dyhz2b15", # overwrite default ai_model_id 
                # name="...",            # overwrite default tool name
                # description="...",     # overwrite default tool description
                # args_schema=...,       # overwrite default args_schema: BaseModel
            )

    Invocation with args:
        .. code-block:: python

            tool.invoke({'query': 'who won the last french open'})

        .. code-block:: python

            Carlos Alcaraz won the last French Open on June 9, 2024, 
            defeating Alexander Zverev in a five-set match. On the women's 
            side, Iga Świątek claimed the title by beating Jasmine 
            Paolini. 🎾🏆 What an exciting tournament!

    Invocation with ToolCall:

        .. code-block:: python

            tool.invoke({"args": {'query': 'who won the last french open'}, "type": "tool_call", "id": "foo", "name": "dappier"})

        .. code-block:: python

            ToolMessage(
                content=(
                    "Carlos Alcaraz won the last French Open on June 9, 2024, defeating "
                    "Alexander Zverev in the final. On the women's side, Iga Świątek claimed "
                    "the title by beating Jasmine Paolini. 🎾🏆 What a fantastic tournament!"
                ),
                name='dappier_real_time_search',
                tool_call_id='foo'
            )
    """  # noqa: E501

    name: str = "dappier_real_time_search"
    description: str = (
        "Access real-time Google search results, including the latest news, " 
        "weather, travel, and deals, along with up-to-date financial news, "
        "stock prices, and trades from polygon.io, all powered by AI insights "
        "to keep you informed."
    )
    args_schema: Type[BaseModel] = DappierInput

    ai_model_id: str = "am_01j06ytn18ejftedz6dyhz2b15"
    """
    The AI model ID to use for the query. The AI model ID always starts 
    with the prefix "am_".

    Defaults to "am_01j06ytn18ejftedz6dyhz2b15".

    Multiple AI model IDs are available, which can be found at:
    https://marketplace.dappier.com/marketplace
    """         

    def _run(
        self,
        query: str,
        *,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Use the tool."""
        try:
            dp_client = Dappier(api_key=os.environ["DAPPIER_API_KEY"])
            response = dp_client.search_real_time_data(
                query=query,
                ai_model_id=self.ai_model_id,
            )
            if response is None:
                raise Exception("An unknown error occurred while retrieving the response.")
            return response.message
        except Exception as e:
            raise Exception(f"Error while retrieving documents: {e}") from e

    async def _arun(
        self,
        query: str,
        *,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Use the tool asynchronously."""
        try:
            dp_client = DappierAsync(
                api_key=os.environ["DAPPIER_API_KEY"]
            )
            async with dp_client as client:
                response = await client.search_real_time_data_async(
                    query=query,
                    ai_model_id=self.ai_model_id,
                )
                if response is None:
                    raise Exception("An unknown error occurred while retrieving the response.")
                return response.message
        except Exception as e:
            raise Exception(f"Error while retrieving documents: {e}") from e


class DappierAIRecommendationTool(BaseTool):  # type: ignore[override]
    """Tool that queries Dappier's AI Recommmendation model and returns json.

    Instantiation:
        .. code-block:: python

            from langchain_dappier import DappierRealTimeSearchTool

            tool = DappierRealTimeSearchTool(
                data_model_id="dm_01j0pb465keqmatq9k83dthx34",
                similarity_top_k=3,
                ref="sportsnaut.com",
                num_articles_ref=2,
                search_algorithm="most_recent",
                # name="...",            # overwrite default tool name
                # description="...",     # overwrite default tool description
                # args_schema=...,       # overwrite default args_schema: BaseModel
            )

    Invocation with args:
        .. code-block:: python

            tool.invoke({'query': 'latest sports news'})

        .. code-block:: python

            [{
                "author": "Matt Weaver",
                "image_url": "https://images.dappier.com/dm_01j0pb465keqmatq9k83dthx34...",
                "pubdate": "Fri, 17 Jan 2025 08:04:03 +0000",
                "source_url": "https://sportsnaut.com/chili-bowl-thursday-bell-column/",
                "summary": "The article highlights the thrilling unpredictability... ",
                "title": "Thursday proves why every lap of Chili Bowl..."
            },
            {
                "author": "Matt Higgins",
                "image_url": "https://images.dappier.com/dm_01j0pb465keqmatq9k83dthx34...",
                "pubdate": "Fri, 17 Jan 2025 02:48:42 +0000",
                "source_url": "https://sportsnaut.com/new-york-mets-news-pete-alonso...",
                "summary": "The New York Mets are likely parting ways with star...",
                "title": "MLB insiders reveal New York Mets’ last-ditch..."
            },
            {
                "author": "Jim Cerny",
                "image_url": "https://images.dappier.com/dm_01j0pb465keqmatq9k83dthx34...",
                "pubdate": "Fri, 17 Jan 2025 05:10:39 +0000",
                "source_url": "https://www.foreverblueshirts.com/new-york-rangers-news...",
                "summary": "The New York Rangers achieved a thrilling 5-3 comeback... ",
                "title": "Rangers score 3 times in 3rd period for stirring 5-3..."
            }]

    Invocation with ToolCall:

        .. code-block:: python

            tool.invoke({"args": {'query': 'latest tech news'}, "type": "tool_call", "id": "foo", "name": "dappier"})

        .. code-block:: python

            ToolMessage(
                content='''[
                    {
                        "author": "Matt Weaver",
                        "image_url": "https://images.dappier.com/dm_01j0pb465keqmatq9k83dthx34...",
                        "pubdate": "Fri, 17 Jan 2025 08:04:03 +0000",
                        "source_url": "https://sportsnaut.com/chili-bowl-thursday-bell-column/",
                        "summary": "The article highlights the thrilling unpredictability... ",
                        "title": "Thursday proves why every lap of Chili Bowl..."
                    },
                    {
                        "author": "Matt Higgins",
                        "image_url": "https://images.dappier.com/dm_01j0pb465keqmatq9k83dthx34...",
                        "pubdate": "Fri, 17 Jan 2025 02:48:42 +0000",
                        "source_url": "https://sportsnaut.com/new-york-mets-news-pete-alonso...",
                        "summary": "The New York Mets are likely parting ways with star...",
                        "title": "MLB insiders reveal New York Mets’ last-ditch..."
                    },
                    {
                        "author": "Jim Cerny",
                        "image_url": "https://images.dappier.com/dm_01j0pb465keqmatq9k83dthx34...",
                        "pubdate": "Fri, 17 Jan 2025 05:10:39 +0000",
                        "source_url": "https://www.foreverblueshirts.com/new-york-rangers-news...",
                        "summary": "The New York Rangers achieved a thrilling 5-3 comeback... ",
                        "title": "Rangers score 3 times in 3rd period for stirring 5-3..."
                    }
                ]''',
                name='dappier_ai_recommendations',
                tool_call_id='foo'
            )
    """  # noqa: E501

    name: str = "dappier_ai_recommendations"
    description: str = (
        "Supercharge your AI applications with Dappier's pre-trained RAG models "
        "and natural language APIs, delivering factual and up-to-date responses "
        "from premium content providers across verticals like News, Finance, "
        "Sports, Weather, and more."
    )
    args_schema: Type[BaseModel] = DappierInput

    data_model_id: str = "dm_01j0pb465keqmatq9k83dthx34"
    """
    The data model ID to use for recommendations. Data model IDs always 
    start with the prefix "dm_". Defaults to "dm_01j0pb465keqmatq9k83dthx34"

    Multiple Data model IDs are available, which can be found at:
    https://marketplace.dappier.com/marketplace
    """

    similarity_top_k: int = 9
    """The number of top documents to retrieve based on similarity.
    Defaults to 9.
    """

    ref: Optional[str] = None
    """The site domain where AI recommendations should be displayed.
    Defaults to None.
    """

    num_articles_ref: int = 0
    """The minimum number of articles to return from the specified reference domain (`ref`).
    The remaining articles will come from other sites in the RAG model.
    Defaults to 0.
    """

    search_algorithm: Literal["most_recent", "semantic", "most_recent_semantic", "trending"] = "most_recent"
    """The search algorithm to use for retrieving articles.
    Defaults to 'most_recent'.
    """

    def _run(
        self,
        query: str,
        *,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> Union[List[Dict[str, str]], Dict[str, str]]:
        """Use the tool."""
        try:
            dp_client = Dappier(api_key=os.environ["DAPPIER_API_KEY"])
            response = dp_client.get_ai_recommendations(
                query=query,
                data_model_id=self.data_model_id,
                similarity_top_k=self.similarity_top_k,
                ref=self.ref,
                num_articles_ref=self.num_articles_ref,
                search_algorithm=self.search_algorithm,
            )

            if response is None or response.status != "success":
                raise Exception("An unknown error occurred while retrieving the response.")

            # Use the helper function to collect the relevant results
            return self._collect_relevant_results(response)

        except Exception as e:
            raise Exception(f"Error while retrieving documents: {e}") from e

    async def _arun(
        self,
        query: str,
        *,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> Union[List[Dict[str, str]], Dict[str, str]]:
        """Use the tool asynchronously."""
        try:
            dp_client = DappierAsync(
                api_key=os.environ["DAPPIER_API_KEY"]
            )
            async with dp_client as client:
                response = await client.get_ai_recommendations_async(
                    query=query,
                    data_model_id=self.data_model_id,
                    similarity_top_k=self.similarity_top_k,
                    ref=self.ref,
                    num_articles_ref=self.num_articles_ref,
                    search_algorithm=self.search_algorithm,
                )

                if response is None or response.status != "success":
                    raise Exception("An unknown error occurred while retrieving the response.")

                # Use the helper function to collect the relevant results
                return self._collect_relevant_results(response)

        except Exception as e:
            raise Exception(f"Error while retrieving documents: {e}") from e
        
    def _collect_relevant_results(self, response: AIRecommendationsResponse) -> List[Dict[str, str]]:
        """Collect only relevant information from the response."""
        return [
            {
                "author": result.author,
                "image_url": result.image_url,
                "pubdate": result.pubdate,
                "source_url": result.source_url,
                "summary": result.summary,
                "title": result.title,
            }
            for result in (
                getattr(response.response, "results", None) or []
            )
        ]
