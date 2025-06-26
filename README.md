# AI Agent Persona Collection

This repository is a collection of system prompts designed to define the personas and behaviors of various AI agents.

## What is a System Prompt?

A system prompt is a set of instructions or guidelines given to an AI model at the beginning of a conversation. It helps to establish the AI's character, tone, specific knowledge, and operational constraints. By providing a well-defined system prompt, we can guide the AI to respond in a more consistent, relevant, and specialized manner.

## Available Personas

Below is a list of the AI agent personas currently available in this collection. Some personas may have associated utility prompts, such as `_ContextHandoff` for summarizing context, `_ConversationSummary` for providing conversation summaries, or `_StudyReport` for generating reports.

* Aetheria
  * Aetheria_ContextHandoff
* ApexEdit
* AsciidocFormatter
  * This persona utilizes `AsciidocFAQ.txt` and `AsciidocGuide.txt` (also present in this repository) as essential reference documents. These are embedded directly within its system prompt to provide comprehensive knowledge of the AsciiDoc format.
* BlackPython
  * BlackPython_ContextHandoff
  * BlackPython_ConversationSummary
* CareerCraft
* Chrono-Cartographer
  * Chrono-Cartographyer_ContextHandoff
* ConspiracyDan
* FactExtractor
* GregoryWilliamThomas
* KnowledgeWeaver
* LexiconAI
* LiteraryAnalysit
* OutlineOracle
* Pastor
  * Pastor_StudyReport
* PromptWhisperer
* Rodney
* SceneSynth
* TheAnalyst
  * TheAnalyst_ContextHandoff
* TypographersCompanion

The following `.txt` files are not personas but are reference documents used by the `AsciidocFormatter` persona:
* AsciidocFAQ.txt
* AsciidocGuide.txt
