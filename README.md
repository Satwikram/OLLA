# OLLA

**OLLA** is a screen-reader-accessible interaction layer for computer-use agents (CUAs), designed to support blind users in completing desktop tasks through natural-language commands and nonvisual feedback.

This repository accompanies our **EMNLP 2026 Main Conference** paper:

> **Are We There Yet? Assessing Computer-Use Agents for Blind Users' Accessible Interaction with Desktop Applications**  
> Satwik Ram Kodandaram, Monalika Padma Reddy, Xiaojun Bi, Jiawei Zhou, I. Ramakrishnan, and Vikas Ashok  
> *The 2026 Conference on Empirical Methods in Natural Language Processing (EMNLP 2026), Main Conference*  
> **Budapest, Hungary · October 24–29, 2026 · HUNGEXPO**

**Paper:** OpenReview  
**Conference:** EMNLP 2026

## Citation

If you use OLLA in your research, please cite:

```bibtex
@inproceedings{kodandaram2026arewethereyet,
  title     = {Are We There Yet? Assessing Computer-Use Agents for Blind Users' Accessible Interaction with Desktop Applications},
  author    = {Kodandaram, Satwik Ram and Padma Reddy, Monalika and Bi, Xiaojun and Zhou, Jiawei and Ramakrishnan, I. and Ashok, Vikas},
  booktitle = {Proceedings of the 2026 Conference on Empirical Methods in Natural Language Processing},
  year      = {2026},
  address   = {Budapest, Hungary},
  publisher = {Association for Computational Linguistics}
}
```

The citation will be updated with the final ACL Anthology identifier and page numbers after publication.

---

## Overview

Computer-use agents combine language-based reasoning with interface grounding to interact with graphical user interfaces. However, most existing CUAs assume visually mediated interaction, requiring users to monitor screenshots, interface changes, or agent actions.

OLLA provides an accessibility layer that enables blind screen-reader users to interact with CUAs nonvisually. Users can issue natural-language commands, receive spoken feedback about agent actions, and interact with desktop applications without directly monitoring the graphical interface.

OLLA is **not a new CUA reasoning architecture**. Instead, it provides an accessible interaction and execution layer around an underlying computer-use agent while preserving the agent's reasoning process.

The current implementation integrates:

- natural-language and speech-based task input;
- Microsoft UI Automation for observing desktop interfaces;
- language-model-based interface reasoning;
- structured UI-action generation;
- programmatic action execution using `pywinauto`;
- interaction history across execution steps; and
- text-to-speech feedback for nonvisual interaction.

In the accompanying study, OLLA supported a three-week longitudinal deployment with **8 blind screen-reader users**, yielding **1,258 participant-issued commands across 12 desktop applications**.

---

## System Architecture

OLLA follows an iterative **observe–reason–act** interaction loop:

```text
Participant Command
        ↓
Current Application State
        ↓
Microsoft UI Automation Tree
        ↓
LLM Solver
        ↓
Structured UI Action
        ↓
Action Execution
        ↓
Updated Application State
        ↓
Task Complete?
   ↙           ↘
 No             Yes
 ↓               ↓
Observe again    Stop
```

At each execution step:

1. OLLA observes the current desktop interface using Microsoft UI Automation.
2. The current UI tree, participant-issued command, and recent interaction history are provided to the solver.
3. The solver reasons over the observed application state and identifies a relevant interface control.
4. The solver generates a structured action.
5. OLLA executes the action through the UI Automation layer.
6. The resulting application state is observed again.
7. The loop continues until the solver determines that the task has been completed.

OLLA also includes an auxiliary reviewer module that can verify solver-selected actions against the current interface state and interaction history.

---

## Repository Structure

```text
OLLA-main/
├── main.py
├── llm.py
├── reviewer.py
├── utils.py
│
├── agents/
│   ├── solver/
│   │   ├── prompt.py
│   │   ├── few_shot_examples.py
│   │   ├── output.py
│   │   └── ui_tree.py
│   │
│   └── reviewer/
│       └── prompt.py
│
├── ui_automation/
│   └── ui_manager.py
│
├── speech/
│   ├── stt.py
│   ├── tts.py
│   └── hotkey.py
│
├── package/
│   ├── tray.py
│   └── build.txt
│
├── assets/
│   ├── olla_tray.ico
│   └── speech/
│       └── models/
│           └── small/
│
├── pyproject.toml
├── poetry.lock
└── README.md
```

### Core Modules

| Module | Description |
|---|---|
| `main.py` | Main OLLA orchestration loop. Coordinates speech input, interface observation, model inference, action execution, and task progression. |
| `llm.py` | Initializes the solver model and manages interaction history using LangChain/LangGraph. |
| `reviewer.py` | Implements the optional action-verification agent. |
| `agents/solver/prompt.py` | Defines the system prompt used to ground model reasoning in the observed desktop interface. |
| `agents/solver/few_shot_examples.py` | Contains examples of UI-grounded interaction for the solver. |
| `agents/reviewer/prompt.py` | Defines the reviewer prompt used to examine generated actions. |
| `ui_automation/ui_manager.py` | Connects to desktop applications using Microsoft UI Automation, extracts UI-tree information, captures screenshots, and executes actions. |
| `speech/stt.py` | Implements local speech recognition using Faster-Whisper. |
| `speech/tts.py` | Provides nonvisual spoken feedback using text-to-speech. |
| `speech/hotkey.py` | Implements global keyboard hotkey handling. |
| `package/tray.py` | Provides the optional Windows system-tray interface. |

---

## Requirements

OLLA currently targets **Windows desktop applications** because its interface-observation and execution layer relies on Microsoft UI Automation.

### System Requirements

- Windows 10 or Windows 11
- Python `>=3.11,<3.15`
- Poetry
- A working microphone for speech input
- An OpenAI API key for the current model backend
- A target application that exposes controls through Microsoft UI Automation

The current speech-recognition implementation uses a locally stored Faster-Whisper model located under:

```text
assets/speech/models/small/
```

---

## Installation

### 1. Clone the Repository

```bash
git clone <YOUR-REPOSITORY-URL>
cd OLLA-main
```

### 2. Install Dependencies

OLLA uses Poetry for Python dependency management.

```bash
poetry install
```

---

## Environment Configuration

OLLA loads environment variables from a `.env` file using `python-dotenv`.

Create a file named:

```text
.env
```

in the root of the repository.

### Required Configuration

```env
OPENAI_API_KEY=your_openai_api_key
MODEL=your_model_identifier
SPEECH_MODEL=small
```

### Environment Variables

| Variable | Required | Used By | Description |
|---|---:|---|---|
| `OPENAI_API_KEY` | Yes | OpenAI/LangChain integration | API key used to authenticate requests to the configured OpenAI model. |
| `MODEL` | Yes | `llm.py`, `reviewer.py` | Model identifier passed to the model initialization logic for the solver and reviewer. |
| `SPEECH_MODEL` | Optional | `main.py` | Speech-model configuration passed when initializing speech recognition. |

For example:

```env
OPENAI_API_KEY=sk-...
MODEL=<model-id>
SPEECH_MODEL=small
```

### Important Note About `SPEECH_MODEL`

Although `main.py` currently reads the `SPEECH_MODEL` environment variable, the speech-recognition implementation in `speech/stt.py` directly loads the bundled Faster-Whisper checkpoint from:

```text
assets/speech/models/small/
```

Therefore, changing:

```env
SPEECH_MODEL=...
```

does **not currently change the underlying Faster-Whisper checkpoint** unless the model-loading logic in `speech/stt.py` is also modified.

### Protecting API Credentials

Do not commit your `.env` file to GitHub.

Add the following to `.gitignore`:

```gitignore
.env
```

We recommend including a safe `.env.example` file in the repository:

```env
OPENAI_API_KEY=
MODEL=
SPEECH_MODEL=small
```

Users can then create their local environment configuration from this template.

On Windows:

```powershell
copy .env.example .env
```

---

## Running OLLA

Start OLLA with:

```bash
poetry run python main.py
```

The current `UIManager` connects to the active Windows application.

Before starting OLLA, bring the desktop application you want OLLA to interact with to the foreground.

---

## Using OLLA

### Voice Interaction

The current implementation uses **F9** to control speech recording.

1. Bring the target application to the foreground.
2. Start OLLA.
3. Press and release **F9** to begin recording.
4. Speak a natural-language task.
5. Press and release **F9** again to stop recording.
6. OLLA transcribes the command locally.
7. OLLA extracts the current UI Automation tree.
8. The solver reasons over the current interface state and generates an action.
9. OLLA provides spoken feedback and executes the selected action.
10. If the task is incomplete, OLLA observes the updated interface and continues execution.

Example request:

```text
Change the font size to 10.
```

---

## Interface Observation

OLLA uses Microsoft UI Automation to construct a structured representation of the active application.

The UI tree provides information about available controls, including properties such as:

- control name;
- control type;
- interface hierarchy;
- bounding rectangle; and
- other UI Automation properties exposed by the application.

This representation allows the model to reason about interface state without relying exclusively on visual pixel information.

The repository also supports screenshot capture through `UIManager`. The default execution loop in `main.py` currently grounds solver actions primarily in the Microsoft UI Automation representation.

---

## Structured Agent Output

The solver generates one structured JSON action at each execution step.

An example output is:

```json
{
  "found": "Yes",
  "control_type": "Edit",
  "title": "Font Size",
  "value": "10",
  "rect": {
    "left": 0,
    "top": 0,
    "right": 0,
    "bottom": 0
  },
  "reason": "The Font Size edit control is the relevant control for changing the requested formatting property.",
  "complete": "Yes"
}
```

### Output Fields

| Field | Description |
|---|---|
| `found` | Indicates whether the solver identified an appropriate interface control. |
| `control_type` | Microsoft UI Automation control type associated with the target. |
| `title` | Name or label of the selected interface control. |
| `value` | Text or value to enter when required by the action. |
| `rect` | Bounding rectangle associated with the selected control. |
| `reason` | Solver rationale for selecting the target control. |
| `complete` | Indicates whether the solver considers the participant's task complete. |

The generated information is passed to the action-execution layer.

For editable controls, OLLA can focus the selected interface element and enter the requested value. Other supported controls can be activated through UI Automation operations such as `click_input()`.

---

## Interaction History

OLLA maintains recent interaction history across execution steps.

This allows the solver to reason over:

- the participant's original command;
- actions already attempted;
- previously selected controls;
- resulting interface states; and
- whether additional actions are required.

The execution process therefore operates as a multi-step interaction rather than treating each interface action independently.

---

## Reviewer Module

The repository also contains a reviewer agent implemented in:

```text
reviewer.py
```

The reviewer can inspect the solver-selected action together with the current UI state and recent interaction history.

Its role is to support verification of proposed actions, including identifying:

- potentially incorrect control selections;
- redundant actions;
- repeated interaction patterns; and
- non-progressing behavior.

The reviewer is implemented as a separate module from the primary solver.

---

## Speech Recognition

Speech-to-text functionality is implemented in:

```text
speech/stt.py
```

OLLA uses **Faster-Whisper** for local speech recognition.

The bundled speech model is stored under:

```text
assets/speech/models/small/
```

Because recognition occurs locally, recorded speech does not need to be sent to the language-model provider as audio.

The transcribed text is subsequently used as the participant's natural-language task command.

---

## Text-to-Speech Feedback

Nonvisual spoken feedback is implemented in:

```text
speech/tts.py
```

OLLA uses text-to-speech to communicate system information and agent actions to the user.

This enables blind users to monitor interaction without visually inspecting the application or OLLA interface.

---

## Building the Windows Executable

The repository includes the PyInstaller configuration used to create a standalone Windows executable in:

```text
package/build.txt
```

A representative build command is:

```powershell
poetry run pyinstaller `
  --name OLLA `
  --onefile `
  --noconsole `
  --hidden-import=pythoncom `
  --hidden-import=pywintypes `
  --collect-all faster_whisper `
  --collect-all ctranslate2 `
  --collect-all numpy `
  --collect-binaries sounddevice `
  --collect-binaries soundfile `
  --exclude-module numpy.f2py.tests `
  --add-data "speech/models;speech/models" `
  --add-data "assets;assets" `
  --icon "assets/olla_tray.ico" `
  main.py
```

The generated executable is written to:

```text
dist/OLLA.exe
```

---

## Research Context

OLLA was developed to enable the study of computer-use agents under authentic nonvisual desktop interaction.

The accompanying EMNLP 2026 paper investigates three questions:

1. How effectively do computer-use agents support blind users in completing everyday, real-world computer tasks?
2. Where do CUAs break down during nonvisual task execution, and what do these breakdowns reveal about current agent limitations?
3. How do blind users envision CUAs supporting everyday computer use beyond end-to-end automation?

We conducted an IRB-approved three-week longitudinal deployment with **8 blind screen-reader users**.

Participants used OLLA during their regular desktop activities rather than completing only predefined laboratory tasks.

The deployment yielded:

- **1,258 participant-issued commands**
- **12 desktop applications**
- **304 normalized task intents**
- screenshots;
- Microsoft UI Automation trees;
- model responses;
- generated actions; and
- interaction histories.

The paper additionally evaluates the participant-issued commands across multiple computer-use models under controlled conditions.

Please refer to the paper for the full study protocol, model configurations, annotation methodology, statistical analysis, and empirical findings.

---

## Accessibility

OLLA was designed specifically to support nonvisual interaction with computer-use agents.

The system incorporates mechanisms including:

- screen-reader-compatible interaction;
- keyboard-based activation;
- natural-language commands;
- speech input;
- audio feedback; and
- nonvisual monitoring of agent execution.

These accessibility mechanisms enable blind users to interact with the underlying CUA but do not modify the reasoning process of the underlying model.

---

## Privacy and Safety

OLLA is a **research prototype** and should not be treated as a production automation system.

Agent-generated actions can modify:

- application state;
- documents;
- application settings;
- files; and
- other interface content.

We recommend evaluating OLLA first on reversible tasks and non-sensitive data.

Depending on the configured model backend, information provided to the model can include:

- the participant's natural-language command;
- UI Automation control names;
- interface structure;
- document or application text exposed through UI Automation; and
- recent interaction history.

UI Automation trees can contain sensitive information such as filenames, document content, control labels, and application data.

Researchers and users should therefore review the privacy requirements of their deployment environment and configured model provider before using OLLA with sensitive information.

Speech recognition is performed locally using Faster-Whisper in the current implementation.

---

## Authors

**Satwik Ram Kodandaram**  
Stony Brook University

**Monalika Padma Reddy**  
Stony Brook University

**Xiaojun Bi**  
Stony Brook University

**Jiawei Zhou**  
Stony Brook University

**I. Ramakrishnan**  
Stony Brook University

**Vikas Ashok**  
Old Dominion University

---

## License

This project is released under the license specified in the repository.

---

## Acknowledgments

We thank the blind participants who contributed their time and experiences to this research.

OLLA builds on open-source tools and libraries including:

- LangChain;
- LangGraph;
- `pywinauto`;
- Faster-Whisper;
- `pyttsx3`; and
- Microsoft UI Automation.
