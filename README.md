# DepenSight: Interactive Dependency Radar

**DepenSight** is a Python static analysis tool that transforms your code's "invisible" architecture into an interactive, visual map. Unlike simple dependency lists, this tool leverages **Graph Theory** to identify critical points, redundancies, and architectural risks in your project.

---

## Why is it useful?

In software development, imports form a **Directed Acyclic Graph (DAG)**. As a project grows, this graph becomes increasingly complex. DepenSight helps you:

*   **Visualize the "Blast Radius"**: If you modify a file, which parts of the codebase are likely to break?
*   **Detect Dependency Hell**: Instantly identify circular dependencies that create maintenance nightmares.
*   **Clear the "Dead Wood"**: Find orphaned files that are never imported and clutter your repository.
*   **Centrality Analysis**: Discover which modules are the "pillars" of your architecture.
*   **Risk Assessment**: Quantify how critical each module is to your system's stability.

---

## Tech Stack

*   **Static Analysis**: Python's `ast` module to extract imports without executing code.
*   **Graph Engine**: `NetworkX` for mathematical calculations and dependency topology.
*   **Visualization**: `Pyvis` for an interactive, physics-based HTML/JavaScript interface.

---

## Understanding the Visualization

The interactive graph uses **visual encoding** to communicate risk:

| Visual Element | Meaning |
| :--- | :--- |
| **Node Size** | Larger = Higher risk score (based on PageRank × Impact Radius) |
| **Red Nodes** | Modules involved in circular dependencies (dependency cycles) |
| **Gray Nodes** | Orphaned files (never imported) |
| **Blue Nodes** | Regular local modules |
| **Node Hover** | Shows: Risk Score, Impact Radius (number of dependent files) |

---

## Core Metrics

### Risk Score Formula
$$\text{Risk Score} = (\text{PageRank} \times 100 \times 0.7) + (\text{Impact Radius} \times 0.3)$$

Where:
- **PageRank**: Measures module importance within the dependency graph
- **Impact Radius**: Number of files that depend on this module (direct + transitive)

### Betweenness Centrality
The project also calculates **Betweenness Centrality** to identify "bridge" modules:
$$C_B(v) = \sum_{s \neq v \neq t} \frac{\sigma_{st}(v)}{\sigma_{st}}$$

*Where $\sigma_{st}$ is the total shortest paths, and $\sigma_{st}(v)$ is the count passing through v.*

---

## Project Structure

| File | Responsibility |
| :--- | :--- |
| `scanner.py` | Crawls project using `pathlib` and `ast` to extract imports. |
| `graph_manager.py` | Manages nodes, edges, and graph operations. |
| `analyzer.py` | Computes risk scores, cycles, orphans, and bottlenecks. |
| `visualizer.py` | Converts graph to interactive HTML using Pyvis. |
| `main.py` | Orchestration: Scanner → Graph → Analysis → Visualization. |

---

## Quick Start

1. **Install dependencies**:
   ```bash
   pip install networkx pyvis
   ```

2. **Run analysis**:
   ```bash
   python main.py
   ```
   This generates `dependencies.html` — open in your browser.

3. **Explore the graph**:
   - **Drag** to move nodes
   - **Scroll** to zoom
   - **Hover** to see risk details
   - **Click** to highlight connections

---

## Example Output

The analysis produces:
- **Risk Scores**: Each module gets a quantified risk value
- **Circular Dependencies**: List of all detected cycles
- **Orphaned Files**: Modules with zero incoming dependencies
- **Bottlenecks**: Top 3 modules with highest betweenness centrality
