# Research: Occam's Razor

## 1. Core Concept
Among competing hypotheses that explain a phenomenon equally well, the one with the fewest assumptions should be selected.

> "Pluralitas non est ponenda sine necessitate." (Plurality should not be posited without necessity.) - William of Ockham

## 2. Origins & Key Figures
*   **William of Ockham (1287–1347):** English Franciscan friar. While he did not invent the principle (it appears in Aristotle and Aquinas), he used it so frequently to slice through complex scholastic arguments that it became named after him.
*   **Ray Solomonoff (Information Theory):** Formulated "Solomonoff Induction" (1960), which mathematically formalizes Occam's Razor using a "universal prior". It proves that shorter programs (lower Kolmogorov complexity) have a higher prior probability of being correct.

## 3. Related Concepts
### Minimum Description Length (MDL)
In data compression and learning theory, the best model is the one that minimizes the sum of:
1.  The length of the model description.
2.  The length of the data encoded by the model.
*Implication:* A complex model must provide a massive improvement in data fit to justify its "cost".

### Gall's Law
"A complex system that works is invariably found to have evolved from a simple system that worked. A complex system designed from scratch never works and cannot be patched to make it work."

## 4. Application to Engineering
*   **YAGNI (You Aren't Gonna Need It):** XP principle. Don't add functionality until it is necessary.
*   **KISS (Keep It Simple, Stupid):** US Navy design principle.
*   **Worse is Better:** Richard Gabriel's essay arguing that simplicity of implementation is more important than correctness or completeness (Unix philosophy).

## 5. Sources
*   *The Sciences of the Artificial* by Herbert Simon
*   *Systemantics* by John Gall
