from langchain.tools import StructuredTool
from mcp_manager.utils import mcp_tool

def list_pull_requests(owner: str, repo: str, path: str = ".") -> list:
    print(f"Pull requests Retriever: Getting open issues for {owner}/{repo}")
    result = mcp_tool([
        "tools", "list_pull_requests",
        "--owner", owner,
        "--repo", repo,
        "--sort", "updated",
        '--direction', 'desc',
        '--perPage', '5',
        '--page', '1'
    ])
    if isinstance(result, list):
        return result
    else:
        print(f"Pull requests Retriever Unexpected result: {result}")
        return []

get_pull_requests = StructuredTool.from_function(
    name = "get_pull_requests",
    func = list_pull_requests,
    description = "'Fetch and provide a list of pull requests from a GitHub repository using the MCP server."
)