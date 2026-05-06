# DepenSight: Interactive Dependency Radar

**DepenSight** is a Python static analysis tool that transforms your code's "invisible" architecture into an interactive, visual map. Unlike simple dependency lists, this tool leverages **Graph Theory** to identify critical points, redundancies, and architectural risks in your project.

---

## Why is it useful?

In software development, imports form a **Directed Acyclic Graph (DAG)**. As a project grows, this graph becomes increasingly complex. DepenSight helps you:
*   **Visualize the "Blast Radius"**: If you modify a file, which parts of the codebase are likely to break?
*   **Detect Dependency Hell**: Instantly identify circular dependencies that slow down builds and complicate testing.
*   **Clear the "Dead Wood"**: Find orphaned files that are never imported and are just cluttering your repository.
*   **Centrality Analysis**: Discover which modules are the "pillars" of your architecture.

---

## Tech Stack

*   **Static Analysis**: Built using Python’s `ast` (Abstract Syntax Tree) module to scan imports without executing the code.
*   **Graph Engine**: `NetworkX` for mathematical calculations and topology management.
*   **Visualization**: `Pyvis` to generate an interactive, physics-based web interface in HTML/JavaScript.

---

## Mathematical Concept: Betweenness Centrality

The project calculates **Betweenness Centrality** to determine node scaling. The more a file acts as a "bridge" for others, the larger it appears on the map.

The formula used is:
$$C_B(v) = \sum_{s \neq v \neq t} \frac{\sigma_{st}(v)}{\sigma_{st}}$$

*Where $\sigma_{st}$ is the total number of shortest paths and $\sigma_{st}(v)$ is the number of those paths passing through $v$.*

---

## Project Structure

| File | Responsibility |
| :--- | :--- |
| `scanner.py` | Crawler using `pathlib` and `ast` to extract import statements. |
| `graph_manager.py` | The brain. Manages nodes, edges, and graph-theory calculations. |
| `visualizer.py` | Converts the graph into an interactive HTML report. |
| `analyzer.py` | Generates a health report (cycles, orphaned files, risk factors). |
| `main.py` | Application entry point and orchestration logic. |

---

## Installation & Usage

1. **Clone the repo**:
   ```bash
   git clone [https://github.com/your-username/depensight.git](https://github.com/your-username/depensight.git)
