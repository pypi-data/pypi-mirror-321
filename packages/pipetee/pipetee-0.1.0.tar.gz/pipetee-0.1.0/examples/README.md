# Pipeline-Tee Examples

This directory contains example pipelines demonstrating various features of Pipeline-Tee.

## Examples Overview

### 1. Visualization Demo (`visualization_demo.py`)

Demonstrates the pipeline visualization features with a data processing pipeline that includes:

- Branching based on data values
- Conditional execution
- Different processing paths
- Timeline visualization
- Multiple output formats (PNG, SVG, PDF)

To run the visualization demo:

1. Install system dependencies:

```bash
# macOS (using Homebrew)
brew install graphviz

# Linux (Ubuntu/Debian)
sudo apt-get install graphviz

# Windows (using Chocolatey)
choco install graphviz
```

2. Install Python dependencies:

```bash
# Install visualization dependencies
pip install -e ".[viz]"

# Verify Graphviz installation
dot -V
```

3. Run the demo:

```bash
python examples/visualization_demo.py
```

The demo will:

1. Create a pipeline that processes random data
2. Branch between high-value and low-value processing paths
3. Generate visualizations in multiple formats:
   - PNG (good for quick viewing)
   - SVG (good for web/documentation)
   - PDF (good for printing)

The visualizations will be saved in the `pipeline_visualizations` directory:

- `demo_pipeline_png_structure.png` - Pipeline structure diagram showing stages and connections
- `demo_pipeline_png_timeline.png` - Execution timeline showing stage durations
- (Similar files for SVG and PDF formats)

### 2. Complex Pipeline Demo (`complex_pipeline_demo.py`)

Shows how to build complex data processing pipelines with:

- Multiple processing stages
- Conditional branching
- Error handling
- State tracking

### 3. Complex Branching Pipeline (`complex_branching_pipeline.py`)

Demonstrates advanced flow control features:

- Multiple branch conditions
- Skip conditions
- Dynamic path selection

## Requirements

1. **Python Dependencies**:

```bash
# Core package with development tools
pip install -e ".[dev]"

# Visualization dependencies (matplotlib, graphviz)
pip install -e ".[viz]"
```

2. **System Dependencies**:

- **Graphviz** (required for pipeline structure diagrams):
  ```bash
  # macOS
  brew install graphviz

  # Linux (Ubuntu/Debian)
  sudo apt-get install graphviz

  # Windows
  choco install graphviz
  ```
- **Python 3.8+**
- **pip** (for package installation)

## Running the Examples

After installing all dependencies, you can run any example:

```bash
python examples/visualization_demo.py
python examples/complex_pipeline_demo.py
python examples/complex_branching_pipeline.py
```

## Example Pipeline Structure

The visualization demo creates a pipeline with the following structure:

```
generate_data -> validate -> [high_value_processing or low_value_processing] -> enrich -> export
```

Features demonstrated:
- Data generation and validation
- Conditional branching based on data values
- Data enrichment with skip conditions
- Export stage with detailed logging
- Comprehensive visualization of pipeline structure and execution timeline

## Visualization Features

The demo showcases two types of visualizations:

1. **Pipeline Structure** (using Graphviz):
   - Shows all stages and their connections
   - Color-coded nodes based on stage status:
     - 🔄 Gray: Pending
     - ⚡ Orange: Running
     - ✅ Green: Completed
     - ⏭️ Light Blue: Skipped
     - ❌ Red: Failed
   - Solid lines for default sequence
   - Dashed lines for conditional branches
   - Requires system Graphviz installation

2. **Execution Timeline** (using Matplotlib):
   - Shows when each stage started and ended
   - Color-coded bars for stage status
   - Duration of each stage
   - Status icons and stage names
   - Time-based axis

## Troubleshooting

1. **Structure diagram not generating** (`failed to execute PosixPath('dot')`):
   - This means the system Graphviz executables are not installed or not in PATH
   - Install Graphviz using the commands above for your OS
   - Verify installation with `dot -V`

2. **Missing status icons** in timeline:
   - This is a font issue and doesn't affect functionality
   - The timeline will still show stage status through color coding
