import os
from typing import Any, List

from googleapiclient.discovery import build
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mcp-google-cse")


@mcp.tool()
def google_search(search_term: str) -> Any:
    """
    Search the custom search engine using the search term.
    Regular query arguments can also be used, like appending site:reddit.com or after:2024-04-30.
    Example: "claude.ai features site:reddit.com after:2024-04-30"
    :param search_term: The search term to search for, equaling the q argument in Google's search.
    :return: Search results containing the title, link and snippet of the search result.
    """
    service = build(os.getenv('SERVICE_NAME', 'customsearch'), "v1", developerKey=os.getenv('API_KEY'))
    response = service.cse().list(
        q=search_term,
        cx=os.getenv('ENGINE_ID'),
        cr=os.getenv('COUNTRY_REGION'),
        gl=os.getenv('GEOLOCATION', 'us'),
        lr=os.getenv('RESULT_LANGUAGE', 'lang_en'),
        num=os.getenv('RESULT_NUM', 10),
        fields='items(title,link,snippet)').execute()
    results = response['items']
    __clean_up_snippets(results)
    return results


def __clean_up_snippets(items: List[dict]) -> None:
    """
    Remove non-breaking space and trailing whitespace from snippets.
    :param items: The search results that contain snippets that have to be cleaned up.
    :return: Nothing, the dict is mutable and updated directly.
    """
    for item in items:
        item.update({k: v.replace('\xa0', ' ').strip() if k == 'snippet' else v for k, v in item.items()})
