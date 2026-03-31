# Research: Rubber Duck Debugging

## Origin
**Source:** "The Pragmatic Programmer" by Andrew Hunt and David Thomas (1999).
**Story:** A programmer carried a rubber duck and would debug by explaining code to the duck line by line.

## Core Mechanism
Verbalization forces structured, slower analysis. The act of translating code into natural language:
1.  **Exposes Assumptions:** You must articulate what you *think* the code does.
2.  **Reveals Gaps:** If you cannot explain a line, you do not understand it.
3.  **Activates Different Brain Regions:** Speaking/writing uses different neural pathways than reading.

## Why It Works for AI Agents
LLMs are fundamentally language models. They are better at natural language reasoning than formal logic.
*   **Code:** Pattern-matched structure. Can produce syntactically correct but semantically wrong output.
*   **English:** Closer to the model's training distribution. Semantic errors are more obvious.

By forcing a translation from Code -> English, we leverage the agent's strength (language) to validate its weakness (logic).

## Application Protocol
1.  **Identify:** Complex code block (loops, conditionals).
2.  **Translate:** One English sentence per logical step.
3.  **Check:** Does the English description match the User's Goal?
4.  **Decide:** If mismatch, fix the code *before* running.

## Resources & Verified References
*   [Wikipedia: Rubber Duck Debugging](https://en.wikipedia.org/wiki/Rubber_duck_debugging)
*   [FreeCodeCamp: Rubber Duck Debugging](https://www.freecodecamp.org/news/rubber-duck-debugging/)
*   [Coursera: Rubber Duck Debugging Explained](https://www.coursera.org/articles/rubber-duck-debugging)
