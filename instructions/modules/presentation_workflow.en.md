# Presentation Generation Workflow

## Complete Workflow

### Phase 1: Requirements Definition (5-10 min)
1. Gather information through user dialogue
2. Generate requirements YAML
3. User confirmation

### Phase 2: Content Design (10-15 min)
1. Propose slide structure
2. Select diagrams for each slide
3. Reflect feedback

### Phase 3: Diagram Generation (Automatic)
1. Generate all required diagrams
2. Save as image files
3. Verify size and quality

### Phase 4: PowerPoint Generation (Automatic)
1. Load template
2. Create slides
3. Place diagrams
4. Insert text

### Phase 5: Review (5-10 min)
1. Present preview
2. Accept modification requests
3. Regenerate

## Checkpoint Integration

Use AI_Instruction_Kits checkpoint system:

```bash
# Start task
checkpoint.sh start "Presentation creation: Data Space Interoperability"

# Progress reports
checkpoint.sh progress TASK-001 1 4 "Requirements definition complete"
checkpoint.sh progress TASK-001 2 4 "Slide structure determined"
checkpoint.sh progress TASK-001 3 4 "Diagram generation complete"
checkpoint.sh progress TASK-001 4 4 "PowerPoint generation complete"

# Task completion
checkpoint.sh complete TASK-001 "Presentation completed"
```

## Example: Creating Data Space Interoperability Presentation

### Step 1: Initial Dialogue
```
User: "I want to create a 15-minute presentation about international data space interoperability"

AI: "Understood. Please tell me:
1. Is the target audience engineers or business people?
2. What aspects do you want to emphasize? (e.g., security, interoperability, governance)
3. Should specific case studies be included?
4. Language: Japanese, English, or both?"

User: "For engineers, emphasizing interoperability. Include Japan-Europe cases (Ouranos and Gaia-X). In English"

AI: "Understood. I propose the following structure:"
```

### Step 2: Structure Proposal
```yaml
presentation:
  title: "Data Space International Interoperability"
  subtitle: "Japan-Europe Collaboration: Status and Prospects"
  author: "Dobachi"
  duration: 15
  language: "en"
  theme: "corporate"

slides:
  - type: title
    title: "Data Space International Interoperability"
    subtitle: "Japan-Europe Collaboration: Status and Prospects"

  - type: content
    title: "What is Data Space"
    layout: "diagram"
    content:
      diagram_type: "architecture"
      diagram_spec: "3-layer architecture"
    notes: "Explain concepts of data, service, and application layers"

  - type: content
    title: "Interoperability Challenges"
    layout: "text_with_diagram"
    bullets:
      - "Unification of technical standards"
      - "Governance harmonization"
      - "Respect for data sovereignty"
    content:
      diagram_type: "flowchart"
      diagram_spec: "challenge flow"

  - type: content
    title: "Ouranos Ecosystem (Japan)"
    layout: "diagram"
    content:
      diagram_type: "architecture"
      diagram_spec: "Ouranos architecture"
    notes: "Japanese data space implementation"

  - type: content
    title: "Gaia-X Framework (Europe)"
    layout: "diagram"
    content:
      diagram_type: "architecture"
      diagram_spec: "Gaia-X architecture"
    notes: "European data space implementation"

  - type: content
    title: "International Interoperability Model"
    layout: "diagram"
    content:
      diagram_type: "network"
      diagram_spec: "Japan-Europe connection"
    notes: "Ouranos ↔ Gaia-X interoperability"

  - type: content
    title: "Standard Protocol Mapping"
    layout: "chart"
    content:
      chart_type: "comparison_table"
      data:
        - ["Item", "Ouranos", "Gaia-X", "Common Standard"]
        - ["Authentication", "OAuth 2.0", "OAuth 2.0", "○"]
        - ["Data Format", "JSON-LD", "JSON-LD", "○"]
        - ["Metadata", "DCAT-AP JP", "DCAT-AP", "△"]

  - type: content
    title: "Adoption Trend"
    layout: "chart"
    content:
      chart_type: "line"
      data:
        x: [2020, 2021, 2022, 2023, 2024]
        y_ouranos: [10, 25, 45, 80, 120]
        y_gaiax: [30, 60, 95, 140, 200]

  - type: content
    title: "Summary"
    layout: "text"
    bullets:
      - "Japan-Europe data space interoperability is steadily advancing"
      - "Unification of standard protocols is critical"
      - "Future challenges: governance harmonization, data sovereignty"
      - "Continuous dialogue and technical cooperation needed"
```

### Step 3: Feedback and Improvement
```
User: "Make the 3-layer architecture diagram more detailed"

AI: "Understood. I'll create a detailed 3-layer architecture diagram:

- Data Layer (bottom): Metadata DB, Data Storage, Object Store
- Service Layer (middle): API Gateway, Auth Service, Data Catalog
- Application Layer (top): Various applications

I'll show connections and data flows between each. Should I use the corporate theme (blue tones)?"

User: "OK, proceed"
```

### Step 4: Implementation (Automatic Execution)
```python
# Code executed by AI
from presentation_generator import PresentationBuilder
from presentation_generator.diagrams import ArchitectureDiagram
from presentation_generator.charts import StatisticalChart

# Initialize builder
builder = PresentationBuilder(theme='corporate', language='en')

# Title slide
builder.add_title_slide(
    title="Data Space International Interoperability",
    subtitle="Japan-Europe Collaboration: Status and Prospects"
)

# Generate 3-layer architecture diagram
arch_diagram = ArchitectureDiagram(theme='corporate', language='en')
diagram_path = arch_diagram.create_three_layer_architecture(
    layers={
        'application': ['App 1', 'App 2', 'App 3'],
        'service': ['API Gateway', 'Auth Service', 'Data Catalog'],
        'data': ['Metadata DB', 'Data Storage', 'Object Store']
    }
)
builder.add_diagram_slide(
    title="What is Data Space",
    diagram_path=diagram_path
)

# ... Generate other slides similarly

# Save
builder.save('DataSpace_Interoperability.pptx')
```

### Step 5: Completion and Delivery
```
AI: "Presentation complete!

📊 Generated content:
- Slides: 9
- Diagrams: 5 (Architecture×3, Network×1, Line chart×1)
- File size: 2.3MB
- Format: PowerPoint (.pptx)

Download file: DataSpace_Interoperability.pptx

Let me know if any modifications are needed."
```

## Bilingual Support

### Japanese Presentation
```python
builder = PresentationBuilder(theme='corporate', language='ja')
builder.set_fonts(
    title_font='Meiryo',
    body_font='Meiryo',
    code_font='Consolas'
)
```

### English Presentation
```python
builder = PresentationBuilder(theme='corporate', language='en')
builder.set_fonts(
    title_font='Arial',
    body_font='Arial',
    code_font='Courier New'
)
```

### Japanese-English Mixed Presentation
```python
builder = PresentationBuilder(theme='corporate', language='ja_en')
builder.set_fonts(
    title_font='Meiryo',  # Japanese support
    body_font='Arial',    # English optimal
    code_font='Consolas'
)

# Language can be specified per slide
builder.add_title_slide(
    title="Data Space Architecture",
    subtitle="データスペースアーキテクチャ"
)
```

## Error Handling and Alternatives

### When Diagram Generation Fails
```python
try:
    diagram_path = arch_diagram.create_architecture(...)
except Exception as e:
    # Fallback: text-based description
    builder.add_text_slide(
        title="System Architecture",
        bullets=[
            "Application Layer: User-facing applications",
            "Service Layer: API, authentication, catalog services",
            "Data Layer: Database, storage"
        ]
    )
    print(f"Warning: Diagram generation failed, using text fallback. Error: {e}")
```

### When Library Not Installed
```python
try:
    from diagrams import Diagram
except ImportError:
    print("Warning: 'diagrams' library not installed")
    print("Suggestion: pip install diagrams")
    print("Alternative: Using graphviz for simpler diagrams")
```

## Performance Optimization

### Parallel Diagram Generation
```python
from concurrent.futures import ThreadPoolExecutor

diagrams_to_generate = [
    ('architecture_3layer', arch_diagram.create_three_layer_architecture, {...}),
    ('ouranos', arch_diagram.create_ouranos_architecture, {...}),
    ('gaiax', arch_diagram.create_gaiax_architecture, {...}),
]

with ThreadPoolExecutor(max_workers=3) as executor:
    futures = {executor.submit(func, **kwargs): name
               for name, func, kwargs in diagrams_to_generate}

    for future in futures:
        diagram_name = futures[future]
        diagram_path = future.result()
        print(f"Generated: {diagram_name} -> {diagram_path}")
```

### Caching
```python
import hashlib
import pickle

def cached_diagram(func):
    def wrapper(*args, **kwargs):
        # Generate cache key from arguments
        cache_key = hashlib.md5(
            pickle.dumps((args, kwargs))
        ).hexdigest()

        cache_file = f".cache/diagram_{cache_key}.png"

        if os.path.exists(cache_file):
            print(f"Using cached diagram: {cache_file}")
            return cache_file

        # Generate and save
        result = func(*args, **kwargs)
        os.makedirs('.cache', exist_ok=True)
        shutil.copy(result, cache_file)
        return result

    return wrapper

@cached_diagram
def create_architecture(...):
    # ...
```

## License
MIT License - Based on AI_Instruction_Kits framework
