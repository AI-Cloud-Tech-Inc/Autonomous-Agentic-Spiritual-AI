# Agent Documentation

This document describes each AI agent in the Film Agent system.

## Overview

The system uses 6 specialized AI agents that work together autonomously:

1. **DirectorAgent** - Orchestrates all other agents
2. **ScreenwriterAgent** - Generates film scripts
3. **CinematographerAgent** - Plans visual elements
4. **EditorAgent** - Assembles final video
5. **SoundDesignerAgent** - Creates audio elements
6. **VFXAgent** - Applies visual effects

---

## DirectorAgent

### Class: `src.agents.director_agent.DirectorAgent`

The Director Agent is the orchestrator of the entire film production pipeline.

### Methods

#### `__init__(self)`

Initializes all agent dependencies.

#### `interpret_concept(self, prompt: str) -> Dict`

Transforms user concept into a cohesive creative vision.

**Parameters:**

- `prompt` (str): User's film concept/idea

**Returns:**

```python
{
    "vision": "Creative vision statement",
    "style": "cinematic",
    "genre": "drama",
    "target_duration": "5 minutes"
}
```

#### `coordinate_agents(self, vision: Dict) -> Dict`

Orchestrates the workflow of all agents.

**Parameters:**

- `vision` (Dict): Creative vision from `interpret_concept()`

**Returns:**

```python
{
    "script": {...},
    "shots": [...],
    "audio": {...},
    "effects": [...]
}
```

#### `review_output(self, output: Dict) -> Dict`

Evaluates and approves final output from other agents.

**Parameters:**

- `output` (Dict): Combined output from all agents

**Returns:**

```python
{
    "approved": True,
    "feedback": "Output meets quality standards",
    "revisions_needed": []
}
```

#### `make_artistic_decisions(self, context: Dict) -> Dict`

Makes high-level artistic decisions autonomously.

**Parameters:**

- `context` (Dict): Current production context

**Returns:**

```python
{
    "color_grading": "warm",
    "pacing": "moderate",
    "mood": "neutral"
}
```

---

## ScreenwriterAgent

### Class: `src.agents.screenwriter_agent.ScreenwriterAgent`

The Screenwriter Agent writes complete scripts with dialogue and scene descriptions.

### Methods

#### `__init__(self)`

Initializes the screenwriter agent.

#### `generate(self, prompt: str, genre: str = "drama", length: str = "short") -> Dict`

Generates a complete film script from a user prompt.

**Parameters:**

- `prompt` (str): User's story concept
- `genre` (str): Film genre (drama, comedy, sci-fi, etc.)
- `length` (str): Script length (short, medium, feature)

**Returns:**

```python
{
    "title": "Untitled Film",
    "scenes": [],
    "characters": [],
    "dialogue": [],
    "structure": {
        "act1": "Setup",
        "act2": "Confrontation",
        "act3": "Resolution"
    }
}
```

#### `develop_character(self, name: str, traits: List[str]) -> Dict`

Creates a detailed character profile.

**Parameters:**

- `name` (str): Character name
- `traits` (List[str]): List of character traits

**Returns:**

```python
{
    "name": "Character Name",
    "backstory": "Character history",
    "motivations": ["goal1", "goal2"],
    "arc": "transformation"
}
```

#### `structure_narrative(self, events: List[Dict]) -> Dict`

Organizes story events into a three-act structure.

**Parameters:**

- `events` (List[Dict]): List of story events

**Returns:**

```python
{
    "act1": {"setup": [...], "inciting_incident": [...]},
    "act2": {"rising_action": [...], "midpoint": [...]},
    "act3": {"climax": [...], "resolution": [...]}
}
```

#### `write_dialogue(self, character: str, context: str) -> str`

Generates dialogue for a character in a specific context.

**Parameters:**

- `character` (str): Character name
- `context` (str): Scene context

**Returns:**

```python
"[Character]: Generated dialogue"
```

#### `revise(self, script: Dict, feedback: str) -> Dict`

Improves script based on director feedback.

**Parameters:**

- `script` (Dict): Original script
- `feedback` (str): Director's feedback notes

**Returns:**

```python
{...}  # Revised script
```

---

## CinematographerAgent

### Class: `src.agents.cinematographer_agent.CinematographerAgent`

The Cinematographer Agent plans camera angles, movements, and compositions.

### Methods

#### `__init__(self)`

Initializes the cinematographer agent.

#### `plan_shots(self, script: Dict) -> List[Dict]`

Creates a shot list from the script.

**Parameters:**

- `script` (Dict): Script from ScreenwriterAgent

**Returns:**

```python
[
    {
        "shot_type": "wide",
        "camera_movement": "static",
        "composition": "establishing",
        "duration": 5.0
    }
]
```

#### `design_lighting(self, scene: Dict) -> Dict`

Plans lighting setup for a scene.

**Parameters:**

- `scene` (Dict): Scene description

**Returns:**

```python
{
    "key_light": {"position": "45 degrees", "intensity": "100%"},
    "fill_light": {"position": "opposite", "intensity": "50%"},
    "back_light": {"position": "behind subject", "intensity": "70%"},
    "mood": "dramatic"
}
```

#### `compose_frame(self, shot_type: str, subject: str) -> Dict`

Designs camera composition for a shot.

**Parameters:**

- `shot_type` (str): Type of shot
- `subject` (str): Main subject in frame

**Returns:**

```python
{
    "rule_of_thirds": {"x": 1/3, "y": 1/2},
    "headroom": "moderate",
    "look_room": "left",
    "depth": "shallow"
}
```

#### `create_shot_list(self, script: Dict) -> Dict`

Generates detailed shot breakdown.

**Parameters:**

- `script` (Dict): Full script

**Returns:**

```python
{
    "scenes": [...],
    "total_shots": 0,
    "est_duration": 0
}
```

#### `ensure_continuity(self, shots: List[Dict]) -> bool`

Verifies visual continuity across shots.

**Parameters:**

- `shots` (List[Dict]): List of all shots

**Returns:**

```python
True  # or False if issues found
```

---

## EditorAgent

### Class: `src.agents.editor_agent.EditorAgent`

The Editor Agent assembles scenes into cohesive narrative.

### Methods

#### `__init__(self)`

Initializes the editor agent.

#### `assemble(self, scenes: List[Dict], audio: Dict) -> Dict`

Combines scenes and audio into final assembly.

**Parameters:**

- `scenes` (List[Dict]): List of scene dictionaries
- `audio` (Dict): Audio track dictionary

**Returns:**

```python
{
    "timeline": [...],
    "duration": 0.0,
    "cuts": [...]
}
```

#### `determine_pacing(self, script: Dict) -> Dict`

Sets optimal timing and rhythm for scenes.

**Parameters:**

- `script` (Dict): Script with scene descriptions

**Returns:**

```python
{
    "tempo": "moderate",
    "timing": {...},
    "rhythm": "steady"
}
```

#### `apply_transitions(self, timeline: Dict) -> Dict`

Adds transitions between scenes.

**Parameters:**

- `timeline` (Dict): Current edit timeline

**Returns:**

```python
{...}  # Updated timeline
```

#### `make_cut_decisions(self, shots: List[Dict]) -> List[Dict]`

Determines optimal cut points between shots.

**Parameters:**

- `shots` (List[Dict]): List of available shots

**Returns:**

```python
[...]  # Selected cuts
```

#### `export_final(self, assembly: Dict, format: str = "mp4") -> Dict`

Renders and exports the final video.

**Parameters:**

- `assembly` (Dict): Final edit assembly
- `format` (str): Output format (mp4, mov, etc.)

**Returns:**

```python
{
    "file_path": "output/video.mp4",
    "format": "mp4",
    "resolution": "1920x1080"
}
```

---

## SoundDesignerAgent

### Class: `src.agents.sound_designer_agent.SoundDesignerAgent`

The Sound Designer Agent creates immersive audio experiences.

### Methods

#### `__init__(self)`

Initializes the sound designer agent.

#### `design_music(self, script: Dict) -> Dict`

Selects or generates background music for the film.

**Parameters:**

- `script` (Dict): Script with emotional beats

**Returns:**

```python
{
    "score": [...],
    "mood": "neutral",
    "tempo": 120,
    "duration": 0.0
}
```

#### `create_soundscape(self, scene: Dict) -> Dict`

Builds ambient audio environment for a scene.

**Parameters:**

- `scene` (Dict): Scene description

**Returns:**

```python
{
    "ambient": [...],
    "foley": [...],
    "spatial": "stereo"
}
```

#### `mix_audio(self, tracks: List[Dict]) -> Dict`

Balances and mixes multiple audio tracks.

**Parameters:**

- `tracks` (List[Dict]): List of audio tracks

**Returns:**

```python
{
    "levels": {...},
    "master": {"volume": 0.8},
    "dynamics": {"compression": True}
}
```

#### `sync_to_video(self, audio: Dict, video: Dict) -> Dict`

Synchronizes audio with visual beats and cuts.

**Parameters:**

- `audio` (Dict): Audio track
- `video` (Dict): Video with cut points

**Returns:**

```python
{...}  # Synced audio
```

#### `generate_voiceover(self, script: Dict, voice: str = "default") -> Dict`

Creates voice narration for the film.

**Parameters:**

- `script` (Dict): Script text for voiceover
- `voice` (str): Voice style/name

**Returns:**

```python
{
    "audio": None,
    "timing": [...],
    "subtitles": [...]
}
```

---

## VFXAgent

### Class: `src.agents.vfx_agent.VFXAgent`

The VFX Agent applies visual effects and color grading.

### Methods

#### `__init__(self)`

Initializes the VFX agent.

#### `identify_enhancements(self, shots: List[Dict]) -> List[Dict]`

Finds opportunities for visual enhancement.

**Parameters:**

- `shots` (List[Dict]): List of shots to analyze

**Returns:**

```python
[
    {
        "shot": 0,
        "suggestion": "color_grading",
        "priority": "high"
    }
]
```

#### `apply_color_grading(self, shot: Dict) -> Dict`

Adjusts color and contrast for visual consistency.

**Parameters:**

- `shot` (Dict): Shot to grade

**Returns:**

```python
{
    "lut": "cinematic",
    "adjustments": {
        "contrast": 1.1,
        "saturation": 1.0,
        "temperature": 0
    },
    "mood": "warm"
}
```

#### `integrate_cgi(self, shot: Dict) -> Dict`

Adds CGI elements to a shot.

**Parameters:**

- `shot` (Dict): Target shot

**Returns:**

```python
{
    "elements": [...],
    "lighting": {...},
    "blending": "normal"
}
```

#### `ensure_quality(self, video: Dict) -> Dict`

Technical quality check for final output.

**Parameters:**

- `video` (Dict): Rendered video

**Returns:**

```python
{
    "issues": [],
    "passed": True,
    "recommendations": []
}
```

#### `render_effects(self, shots: List[Dict]) -> List[Dict]`

Applies all VFX to shots.

**Parameters:**

- `shots` (List[Dict]): List of shots

**Returns:**

```python
[...]  # Shots with effects
```

**Parameters:**

- `scene` (Dict): Scene description

**Returns:**

```python
{
    "ambient": [...],

    "foley": [...],
    "spatial": "stereo"
}
```

#### `mix_audio(self, tracks: List[Dict]) -> Dict`

Balances and mixes multiple audio tracks.

**Parameters:**

- `tracks` (List[Dict]): List of audio tracks

**Returns:**

```python
{

    "levels": {...},
    "master": {"volume": 0.8},
    "dynamics": {"compression": True}
}
```

#### `sync_to_video(self, audio: Dict, video: Dict) -> Dict`

Synchronizes audio with visual beats and cuts.

**Parameters:**

- `audio` (Dict): Audio track

- `video` (Dict): Video with cut points

**Returns:**

```python
{...}  # Synced audio

```

#### `generate_voiceover(self, script: Dict, voice: str = "default") -> Dict`

Creates voice narration for the film.

**Parameters:**

- `script` (Dict): Script text for voiceover

- `voice` (str): Voice style/name

**Returns:**

```python
{

    "audio": None,
    "timing": [...],
    "subtitles": [...]
}
```

---

## VFXAgent

### Class: `src.agents.vfx_agent.VFXAgent`

The VFX Agent applies visual effects and color grading.

### Methods

#### `__init__(self)`

Initializes the VFX agent.

#### `identify_enhancements(self, shots: List[Dict]) -> List[Dict]`

Finds opportunities for visual enhancement.

**Parameters:**

- `shots` (List[Dict]): List of shots to analyze

**Returns:**

```python
[
    {
        "shot": 0,
        "suggestion": "color_grading",
        "priority": "high"
    }
]
```

#### `apply_color_grading(self, shot: Dict) -> Dict`

Adjusts color and contrast for visual consistency.

**Parameters:**

- `shot` (Dict): Shot to grade

**Returns:**

```python
{
    "lut": "cinematic",
    "adjustments": {
        "contrast": 1.1,
        "saturation": 1.0,
        "temperature": 0
    },
    "mood": "warm"
}
```

#### `integrate_cgi(self, shot: Dict) -> Dict`

Adds CGI elements to a shot.

**Parameters:**

- `shot` (Dict): Target shot

**Returns:**

```python
{
    "elements": [...],
    "lighting": {...},
    "blending": "normal"
}
```

#### `ensure_quality(self, video: Dict) -> Dict`

Technical quality check for final output.

**Parameters:**

- `video` (Dict): Rendered video

**Returns:**

```python
{
    "issues": [],
    "passed": True,
    "recommendations": []
}
```

#### `render_effects(self, shots: List[Dict]) -> List[Dict]`

Applies all VFX to shots.

**Parameters:**

- `shots` (List[Dict]): List of shots

**Returns:**

```python
[...]  # Shots with effects

```

Initializes the VFX agent.

#### `identify_enhancements(self, shots: List[Dict]) -> List[Dict]`

Finds opportunities for visual enhancement.

**Parameters:**

- `shots` (List[Dict]): List of shots to analyze

**Returns:**

```python
[
    {
        "shot": 0,
        "suggestion": "color_grading",
        "priority": "high"
    }
]
```

#### `apply_color_grading(self, shot: Dict) -> Dict`

Adjusts color and contrast for visual consistency.

**Parameters:**

- `shot` (Dict): Shot to grade

**Returns:**

```python
{
    "lut": "cinematic",
    "adjustments": {
        "contrast": 1.1,
        "saturation": 1.0,
        "temperature": 0
    },
    "mood": "warm"
}
```

#### `integrate_cgi(self, shot: Dict) -> Dict`

Adds CGI elements to a shot.

**Parameters:**

- `shot` (Dict): Target shot

**Returns:**

```python
{
    "elements": [...],
    "lighting": {...},
    "blending": "normal"
}
```

#### `ensure_quality(self, video: Dict) -> Dict`

Technical quality check for final output.

**Parameters:**

- `video` (Dict): Rendered video

**Returns:**

```python
{
    "issues": [],
    "passed": True,
    "recommendations": []
}
```

#### `render_effects(self, shots: List[Dict]) -> List[Dict]`

Applies all VFX to shots.

**Parameters:**

- `shots` (List[Dict]): List of shots

**Returns:**

```python
[...]  # Shots with effects
```
