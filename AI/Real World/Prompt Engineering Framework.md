---
tags: [ai, ai/realworld, ai/prompt-engineering]
title: Prompt Engineering Framework
date created: Wednesday, February 11th 2026, 10:26:59 am
date modified: Saturday, February 28th 2026, 9:31:11 pm
parent: Real World
grand_parent: AI
---
# Prompt Engineering Framework
## The Five Step Framework
- **Task**
    - Persona: Expertise to draw from the LLM (e.g. Programmer, Artist, Writer, Scientist, etc).
    - Format: The format of the output.
- **Context**: What you need from it; constraints, background information, backstory, etc. More is better for the LLM to understand and model its output to your specification.
- **References**: Optional, but this can further shape the LLM to adhere to your expectations. Each reference is often called a shot (related: [[Explanation of LLMs Being Few-shot Learners + How Tools are Provided to LLMs]]). *2 to 5* usually yields the best results.
- **Evaluate**: Evaluate the output and determine whether the output of the LLM is what you wanted
- **Iterate**: Tweak your prompt based on what needs improvement.
    - Revisiting the prompt framework (Task, Context, References, Evaluate, Iterate), adding new things that make a better prompt. (e.g. persona, format, etc)
    - Separate the prompt into smaller instructions.
    - Paraphrasing or switching to a task that is similar but different enough to yield an altered result.
    - Introduce constraints.

==**Substance** is key.==

### For Images
Detail is more important here, asides from the things listed above, you should also add specifiers about the size, color, position, and aesthetic, or anything that may be needed to help shape the output image better.

#ai #ai/realworld #ai/prompt-engineering
