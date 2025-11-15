# Troubleshooting

English | [日本語](TROUBLESHOOTING.md)

## Graphviz Errors

### Important: Graphviz requires TWO components

To use Graphviz, you need **BOTH**:

1. **Python package** `graphviz` - Python library to use Graphviz
2. **System software** Graphviz - The actual program that draws diagrams

### Error: "No module named 'graphviz'"

**Cause:** Python graphviz package is not installed.

**Solution:**

```bash
# If using uv
uv pip install graphviz

# If using pip
pip install graphviz

# Or reinstall all dependencies
uv pip install -r requirements.txt
```

### Error: "Graphviz executable not found" or "FileNotFoundError"

**Cause:** Graphviz system software is not installed.

**Solution:**

You need to install the Graphviz software on your system separately from the Python `graphviz` package.

#### Ubuntu/Debian

```bash
sudo apt-get update
sudo apt-get install graphviz
```

#### macOS

```bash
brew install graphviz
```

#### Windows

1. Download installer from https://graphviz.org/download/
2. Select "Add to PATH" option during installation
3. Restart command prompt

#### Verify Installation

```bash
dot -V
```

You should see output like:
```
dot - graphviz version 2.x.x
```

### Error: "'graphviz' Python library not installed"

**Cause:** Python graphviz package is not installed.

**Solution:**

```bash
# If using uv
uv pip install graphviz

# If using pip
pip install graphviz
```

## Dependency Errors

### Error: "No module named 'diagrams'"

**Solution:**

```bash
# Reinstall all dependencies
uv pip install -r requirements.txt

# or
pip install -r requirements.txt
```

### Error: "No module named 'matplotlib'"

If you get font-related errors with matplotlib:

**Ubuntu/Debian:**
```bash
sudo apt-get install fonts-noto-cjk  # Japanese fonts
```

**macOS:**
```bash
brew install font-noto-sans-cjk-jp
```

## PowerPoint Generation Errors

### Error: "Permission denied" when saving .pptx

**Cause:** No write permission for output directory.

**Solution:**

```bash
# Create output directory with proper permissions
mkdir -p output
chmod 755 output
```

### Error: Japanese fonts appear garbled

**Solution:**

```python
# Check if Meiryo font is available
from src.i18n import FontSelector

selector = FontSelector()
fonts = selector.get_all_fonts_for_language('ja')
print(fonts)
```

Ensure Japanese fonts are installed on your system.

## Performance Issues

### Diagram generation is slow

**Solution:**

1. **Use uv** - Faster than pip:
   ```bash
   pip install uv
   uv pip install -r requirements.txt
   ```

2. **Adjust output resolution** - Lower DPI if needed:
   ```python
   chart.create_line_chart(..., dpi=150)  # Default is 300
   ```

## Frequently Asked Questions

### Q: Flowcharts are not being generated

A: Verify Graphviz system installation:
```bash
which dot  # Linux/macOS
where dot  # Windows
```

### Q: Japanese text doesn't appear in diagrams

A: Check the following:
1. Japanese fonts are installed on system
2. `language='ja'` parameter is set
3. Meiryo or fallback font is available

### Q: Cannot activate virtual environment

A: Use the correct command for your OS:

**Linux/macOS:**
```bash
source .venv/bin/activate  # uv
source venv/bin/activate   # venv
```

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1  # uv
venv\Scripts\Activate.ps1   # venv
```

**Windows (CMD):**
```cmd
.venv\Scripts\activate.bat  # uv
venv\Scripts\activate.bat   # venv
```

## Support

If your issue is not resolved:

1. Search existing [Issues](https://github.com/dobachi/PresentationTemplate/issues)
2. Create a new Issue (include full error message)
3. Include the following information:
   - OS name and version
   - Python version (`python --version`)
   - Installation method (uv/pip)
   - Full error message

## Related Links

- [README](README.en.md) - Installation instructions
- [Graphviz Official Site](https://graphviz.org/)
- [python-pptx Documentation](https://python-pptx.readthedocs.io/)
