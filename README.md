# GitHub Repository Analyzer (Django + CrewAI + MCP)

This project is a Django-based web application that integrates **CrewAI**, **LangChain**, and the **GitHub MCP Server** to automatically analyze a GitHub repository and generate structured Markdown documentation.

The system provides an AI-powered workflow that fetches repository data, processes it with multiple agents, and produces comprehensive reports through a clean web interface. This mirrors the architecture of modern AI-driven developer tools.

---

## Features

### AI-Powered Repository Analysis
CrewAI agents perform goal-driven tasks such as:
- Analyzing repository structure
- Summarizing issues
- Reviewing pull requests
- Inspecting branches
- Producing consolidated documentation

### MCP (Model Context Protocol) Integration
The GitHub MCP Server enables structured access to:
- File contents
- Issues
- Pull requests
- Branch metadata

### LangChain Tool Execution
Agents use LangChain to call MCP tools intelligently and sequentially.

### Django Web Interface
- Simple UI for entering a repository
- Trigger automated analysis
- View generated reports
- Download Markdown output files

### Automatic Markdown Report Generation
Outputs include:
- `repo_structure.md`
- `report_issues.md`
- `pull_requests.md`
- `branches.md`
- `summary.md` (final combined report)
