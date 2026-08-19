---
title: "Installation"
description: "Get Reasongraph installed in under a minute."
icon: "download"
---

<Check>
  **Available on PyPI**: `pip install reasongraph` and you're ready.
</Check>

<Note>
  Python 3.8 or higher is required. Python 3.11+ is recommended.
</Note>

## System Requirements

| Component | Minimum | Recommended |
| :--------- | :------- | :----------- |
| Python | 3.8 | 3.11+ |
| OS | Windows / Linux / Mac | Linux / Mac |
| RAM | 4 GB | 16 GB+ |
| Storage | 2 GB | 20 GB+ (models and data) |


## Basic Installation

```bash
pip install reasongraph
```

With all optional dependencies:

```bash
pip install reasongraph[all]
```

### Verify

```bash
python -c "import reasongraph; print(reasongraph.__version__)"
```


## Virtual Environment (Recommended)

<Tabs>
  <Tab title="venv">
    ```bash
    python -m venv venv
    source venv/bin/activate   # Linux / Mac
    venv\Scripts\activate      # Windows
    pip install reasongraph
    ```
  </Tab>
  <Tab title="conda">
    ```bash
    conda create -n reasongraph python=3.11
    conda activate reasongraph
    pip install reasongraph
    ```
  </Tab>
</Tabs>


## Optional Dependencies

Install only what you need:

<Tabs>
  <Tab title="GPU">
    ```bash
    pip install reasongraph[gpu]
    ```
    Includes PyTorch with CUDA, FAISS GPU, and CuPy.
  </Tab>
  <Tab title="Visualization">
    ```bash
    pip install reasongraph[viz]
    ```
    Includes PyVis, Graphviz, and UMAP.
  </Tab>
  <Tab title="LLM Providers">
    ```bash
    pip install reasongraph[llm-all]       # all providers
    pip install reasongraph[llm-openai]    # OpenAI
    pip install reasongraph[llm-anthropic] # Anthropic
    pip install reasongraph[llm-gemini]    # Google Gemini
    pip install reasongraph[llm-groq]      # Groq
    pip install reasongraph[llm-ollama]    # Ollama (local)
    ```
  </Tab>
  <Tab title="Cloud">
    ```bash
    pip install reasongraph[cloud]
    ```
    Includes AWS S3, Azure Blob, and Google Cloud Storage.
  </Tab>
</Tabs>


## Install from Source

For the latest development version or to contribute:

```bash
git clone https://github.com/savsuth/Reasongraph.git
cd reasongraph

pip install -e .         # core only
pip install -e ".[all]"  # all extras
pip install -e ".[dev]"  # dev tools (pytest, black, etc.)
```

Install directly from the main branch if the PyPI release has issues:

```bash
pip install git+https://github.com/savsuth/Reasongraph.git@main
```


## Troubleshooting

<AccordionGroup>

<Accordion title="ModuleNotFoundError: No module named 'reasongraph'" icon="circle-xmark">

Make sure you're in the right virtual environment:

```bash
pip list | grep reasongraph
pip install --upgrade reasongraph
```

</Accordion>

<Accordion title="Installation fails with dependency errors" icon="triangle-exclamation">

```bash
pip install --upgrade pip
pip install build wheel
pip install reasongraph --no-deps  # install core first, then add extras
```

</Accordion>

<Accordion title="GPU dependencies fail to install" icon="bolt">

Install CPU-only first, then layer in GPU support:

```bash
pip install reasongraph
pip install reasongraph[gpu]
```

</Accordion>

<Accordion title="Permission denied" icon="lock">

```bash
pip install --user reasongraph  # or use a virtual environment
```

</Accordion>

<Accordion title="Windows [all] install fails" icon="windows">

Fixed in **v0.5.0**. Upgrade to the latest release:

```bash
pip install --upgrade reasongraph
```

</Accordion>

<Accordion title="Windows PyTorch DLL errors on startup" icon="windows">

Install the [Microsoft Visual C++ Redistributable](https://aka.ms/vs/17/release/vc_redist.x64.exe). This is a Windows system dependency, not a Reasongraph bug.

</Accordion>

</AccordionGroup>


## Next Steps

- [Getting Started](getting-started) — Understand what Reasongraph does before you build.
- [Build the Pipeline](quickstart) — Follow the end-to-end workflow with code.
- [Browse Examples](cookbook) — See notebook examples organized by use case.
