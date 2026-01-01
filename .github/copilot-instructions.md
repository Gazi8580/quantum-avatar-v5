# Copilot Instructions

## Scope
- Primary codebase is [quantum_avatar/](../quantum_avatar) (Flask app + orchestrator + modules). The [spacy-transformers/](../spacy-transformers) folder is an upstream checkout; treat it as read-only unless explicitly asked.

## Run / Dev Workflow
- Install deps: `python -m pip install -r requirements.txt`
- Run API locally: `python quantum_avatar/ui/app.py` (Flask app in [quantum_avatar/ui/app.py](../quantum_avatar/ui/app.py))
- Run orchestrator demo: `python quantum_avatar/orchestrator.py` (integration smoke-run in [quantum_avatar/orchestrator.py](../quantum_avatar/orchestrator.py))
- Docker: build from [Dockerfile](../Dockerfile) and run (container starts `quantum_avatar/ui/app.py` on port 5000).

## Tests
- Test suite uses stdlib `unittest` under [quantum_avatar/tests/](../quantum_avatar/tests).
- Run: `python -m unittest discover -s quantum_avatar/tests -p "test_*.py"`

## Architecture (Big Picture)
- Entry points:
	- [quantum_avatar/ui/app.py](../quantum_avatar/ui/app.py): HTTP API endpoints `/chat`, `/generate_image`, `/earn_points`, `/autonomous_action`.
	- [quantum_avatar/orchestrator.py](../quantum_avatar/orchestrator.py): wires modules together and uses defensive imports (optional modules fall back to `None`).
- Module boundaries (import via `quantum_avatar.<area>...`):
	- NLP: [quantum_avatar/nlp/nlp_processor.py](../quantum_avatar/nlp/nlp_processor.py) (spaCy + HF pipeline + autocorrect).
	- Vision: [quantum_avatar/vision/](../quantum_avatar/vision) (image generation + CLIP-based categorization).
	- Quantum: [quantum_avatar/quantum/quantum_calculator.py](../quantum_avatar/quantum/quantum_calculator.py) (Qiskit / Aer / QAOA).
	- Business/Autonomy/Security: [quantum_avatar/business/](../quantum_avatar/business), [quantum_avatar/autonomy/](../quantum_avatar/autonomy), [quantum_avatar/security/](../quantum_avatar/security).

## Model / Runtime Notes
- NLP/Vision use Hugging Face models that download on first run; keep calls and initialization in the relevant module classes.
- spaCy models must exist locally (e.g. `python -m spacy download en_core_web_sm`; multilingual uses `xx_ent_wiki_sm`).
- Requirements are pinned in [requirements.txt](../requirements.txt) (Python 3.13 in [Dockerfile](../Dockerfile)); keep versions compatible with torch/transformers/qiskit.

