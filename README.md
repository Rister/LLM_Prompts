# AI Agent Persona Collection

[![Project Status: Active](https://img.shields.io/badge/Project%20Status-Active-green.svg)](https://shields.io/) [![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg?style=flat-square)](https://shields.io/)

This repository is a collection of system prompts designed to define the personas and behaviors of various AI agents.

## What is a System Prompt?

A system prompt is a set of instructions or guidelines given to an AI model at the beginning of a conversation. It helps to establish the AI's character, tone, specific knowledge, and operational constraints. By providing a well-defined system prompt, we can guide the AI to respond in a more consistent, relevant, and specialized manner.

## Available Personas

Below is a list of the AI agent personas currently available in this collection. Some personas may have associated utility prompts, such as `_ContextHandoff` for summarizing context, `_ConversationSummary` for providing conversation summaries, or `_StudyReport` for generating reports.

* **Aetheria**: An AI fiction muse and idea catalyst for writers.
* **ApexEdit**: A professional and meticulous copy-editor for refining and enhancing existing textual reports.
* **AsciidocFormatter**: A technical editor specializing in correcting formatting and structural errors in AsciiDoc documents, particularly those exported from Pandoc.
  * This persona utilizes `AsciidocFAQ.txt` and `AsciidocGuide.txt` (also present in this repository) as essential reference documents. These are embedded directly within its system prompt to provide comprehensive knowledge of the AsciiDoc format.
* **BlackPython**: An AI assistant with a dry, deadpan sense of humor, finding humor in the absurdity of everyday situations.
* **CareerCraft**: An expert resume coach and writing partner that guides users through creating and optimizing their resumes.
* **Chrono-Cartographer**: An analytical entity that identifies and articulates convoluted, indirect, and often fantastical causal relationships between any two or more given inputs or events.
* **Concept-Connector**: An analytical entity that identifies and articulates convoluted, indirect, and often fantastical causal relationships between any two or more given inputs or events.
* **ConspiracyDan**: An AI entity that operates from a worldview of profound and pervasive suspicion, generating novel conspiracy theories about any subject.
* **DrFictionalis**: A helpful academic librarian who generates plausible-sounding, yet ultimately absurd, academic references in BibLaTeX format.
* **FactExtractor**: A data processing specialist that synthesizes unstructured text data into highly organized, structured, and concise point-form facts for RAG ecosystems.
* **GregoryWilliamThomas**: A patient and truthful academic tutor with a dry, Blackadder-esque wit that generates responses in the format of a tailored business report.
* **KnowledgeWeaver**: A writing assistant for non-fiction that helps users brainstorm, outline, and develop a specific book concept.
* **LexiconAI**: A specialized linguistic agent that provides comprehensive, dictionary-style entries for any given term, including technobabble.
* **LiteraryAnalysit**: An expert literary analyst and a keen observer of narrative craft that helps users understand and appreciate the literary features in fiction books.
* **OutlineOracle**: A witty and wise outlining assistant for creative fiction that helps users plan and structure their novels.
* **Pastor**: A caring pastor with profound spiritual and intellectual depth, providing guidance, support, and theological insight rooted in a robust biblical framework.
* **PromptWhisperer**: An analytical and insightful AI assistant that translates a user's expressed intent into a fully optimized, standalone utility prompt for a specific third-party AI persona.
* **Rodney**: An AI assistant with a redneck persona that engages in rambling, tangential conversations to infer the necessary details for constructing a system prompt for a new AI agent.
* **RSTWrangler**: A meticulous AI assistant specializing in transforming and cleaning up Markdown, AsciiDoc, or reStructuredText documents into clean, properly structured reStructuredText.
* **SceneSynth**: A literary analyst and collaborative scene developer that synthesizes information from a primary text and supporting context documents to produce a comprehensive scene analysis.
* **ScopeHound**: A skilled and adaptive AI agent specializing in project initiation and task breakdown, employing an agile methodology to convert user input into actionable, granular tasks.
* **TheAnalyst**: An AI assistant characterized by extreme precision, pedantry, and a verbose, technical communication style.
* **TheCollator**: A silent, analytical AI assistant that organizes and structures chaotic brainstorming input into a structured, iterative summary.
* **TypographersCompanion**: A knowledgeable and precise expert in typeface design, font development, and the history of writing systems, providing patient, step-by-step guidance on creating and optimizing fonts.

## Utility Prompts

Utility prompts are designed to be used with their associated personas to generate specific types of output.

* **Aetheria_ContextHandoff**: Creates a "Story So Far" document to seamlessly continue brainstorming sessions with Aetheria.
* **BlackPython_AcademicReview**: Generates a savagely satirical academic review of a referenced resource.
* **BlackPython_ContextHandoff**: Generates a context handoff document to continue conversations with BlackPython seamlessly.
* **BlackPython_ConversationSummary**: Distills the essence of a conversation with BlackPython's observational wit.
* **Chrono-Cartographer_ContextHandoff**: Generates a context handoff document for seamless continuation of analysis with Chrono-Cartographer.
* **Chrono-Cartographer_SubjectReport**: Generates a comprehensive analytical report based on a chat context with Chrono-Cartographer.
* **Concept-Connector_SubjectReport**: Generates a comprehensive 'Subject Report' on the convoluted causal relationships between topics discussed with Concept-Connector.
* **LiteraryAnalyst_Report**: Compiles a comprehensive summary report of a discussion with the Literary Analyst.
* **Pastor_StudyReport**: Provides a comprehensive and meticulously detailed report of a discussion with the Pastor, formatted as a structured Bible study outline.
* **ScopeHound_ProjectPlan**: Consolidates all key decisions, confirmed requirements, user stories, and granular tasks from a project planning session with ScopeHound.
* **TheAnalyst_ContextHandoff**: Generates a comprehensive handoff report detailing the entirety of a conversational session with TheAnalyst.
* **TheAnalyst_FindingsReport**: Generates a meticulously structured findings report from a conversational log with TheAnalyst.

The following `.txt` files are not personas but are reference documents used by the `AsciidocFormatter` persona:
* AsciidocFAQ.txt
* AsciidocGuide.txt

## License

[![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-sa/4.0/)

This project is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License. See the [LICENSE](LICENSE) file for details.
