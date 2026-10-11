# Docs Curator Instructions

## Overview

The Docs Curator is an automated tool that enforces and operates around the Diátaxis documentation framework. It ensures that documentation is categorized correctly, reviewed for style consistency, and updated in a way that adheres to the four distinct quadrants.

## Diátaxis Quadrants

| Quadrant | Target Audience / Need | Focus | Tone / Style | What it Must NOT Contain |
| :--- | :--- | :--- | :--- | :--- |
| **Tutorials** | Learning (Beginners) | Lesson-oriented | Guiding, step-by-step, reassuring | Abstract theory, alternative paths, edge cases. |
| **How-To Guides** | Problem-solving (Practitioners) | Goal-oriented | Practical, task-focused, recipe-like | Basic introductions, complete deep-dive explanations. |
| **Reference** | Information (Everyone) | Information-oriented | Concise, technical, dry, structured | Step-by-step guides, pedagogical lessons. |
| **Explanation** | Understanding (Everyone) | Understanding-oriented | Contextual, discursive, conceptual | Imperative instructions, syntax reference tables. |

## Rules for Documentation

1. **Tutorials:**
   - **Category:** `docs/tutorials`
   - **Focus:** Lesson-oriented
   - **Tone:** Guiding, step-by-step, reassuring
   - **Content:** Avoid abstract theory, alternative paths, and edge cases.

2. **How-To Guides:**
   - **Category:** `docs/how-to`
   - **Focus:** Goal-oriented
   - **Tone:** Practical, task-focused, recipe-like
   - **Content:** Avoid basic introductions and complete deep-dive explanations.

3. **Reference:**
   - **Category:** `docs/reference`
   - **Focus:** Information-oriented
   - **Tone:** Concise, technical, dry, structured
   - **Content:** Avoid step-by-step guides and pedagogical lessons.

4. **Explanation:**
   - **Category:** `docs/explanation`
   - **Focus:** Understanding-oriented
   - **Tone:** Contextual, discursive, conceptual
   - **Content:** Avoid imperative instructions and syntax reference tables.

## Scaffolding

When creating new documents, use the following templates:

- **Tutorials:** `templates/tutorial.md`
- **How-To Guides:** `templates/how-to.md`
- **Reference:** `templates/reference.md`
- **Explanation:** `templates/explanation.md`

## Example Templates

### Tutorial Template

