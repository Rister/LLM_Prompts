# AI Agent Persona Collection

This repository is a collection of system prompts designed to define the personas and behaviors of various AI agents.

## What is a System Prompt?

A system prompt is a set of instructions or guidelines given to an AI model at the beginning of a conversation. It helps to establish the AI's character, tone, specific knowledge, and operational constraints. By providing a well-defined system prompt, we can guide the AI to respond in a more consistent, relevant, and specialized manner.

## Available Personas

Below is a list of the AI agent personas currently available in this collection. Some personas may have associated utility prompts, such as `_ContextHandoff` for summarizing context, `_ConversationSummary` for providing conversation summaries, or `_StudyReport` for generating reports.

* **Aetheria**: An AI fiction muse and idea catalyst for writers.
  * `Aetheria_ContextHandoff`: Creates a "Story So Far" document to seamlessly continue brainstorming sessions.
* **ApexEdit**: A professional and meticulous copy-editor for refining and enhancing existing textual reports.
* **AsciidocFormatter**: A technical editor specializing in correcting formatting and structural errors in AsciiDoc documents, particularly those exported from Pandoc.
  * This persona utilizes `AsciidocFAQ.txt` and `AsciidocGuide.txt` (also present in this repository) as essential reference documents. These are embedded directly within its system prompt to provide comprehensive knowledge of the AsciiDoc format.
* **BlackPython**: An AI assistant with a dry, deadpan sense of humor, finding humor in the absurdity of everyday situations.
  * `BlackPython_ContextHandoff`: Generates a context handoff document to continue conversations seamlessly.
  * `BlackPython_ConversationSummary`: Distills the essence of a conversation with observational wit.
* **CareerCraft**: An expert resume coach and writing partner that guides users through creating and optimizing their resumes.
* **Chrono-Cartographer**: An analytical entity that identifies and articulates convoluted, indirect, and often fantastical causal relationships between any two or more given inputs or events.
  * `Chrono-Cartographyer_ContextHandoff`: Generates a context handoff document for seamless continuation of analysis.
* **ConspiracyDan**: An AI entity that operates from a worldview of profound and pervasive suspicion, generating novel conspiracy theories about any subject.
* **FactExtractor**: A data processing specialist that synthesizes unstructured text data into highly organized, structured, and concise point-form facts for RAG ecosystems.
* **GregoryWilliamThomas**: A patient and truthful academic tutor with a dry, Blackadder-esque wit that generates responses in the format of a tailored business report.
* **KnowledgeWeaver**: A writing assistant for non-fiction that helps users brainstorm, outline, and develop a specific book concept.
* **LexiconAI**: A specialized linguistic agent that provides comprehensive, dictionary-style entries for any given term, including technobabble.
* **LiteraryAnalysit**: An expert literary analyst and a keen observer of narrative craft that helps users understand and appreciate the literary features in fiction books.
* **OutlineOracle**: A witty and wise outlining assistant for creative fiction that helps users plan and structure their novels.
* **Pastor**: A caring pastor with profound spiritual and intellectual depth, providing guidance, support, and theological insight rooted in a robust biblical framework.
  * `Pastor_StudyReport`: Provides a comprehensive and meticulously detailed report of a discussion, formatted as a structured Bible study outline.
* **PromptWhisperer**: An analytical and insightful AI assistant that translates a user's expressed intent into a fully optimized, standalone utility prompt for a specific third-party AI persona.
* **Rodney**: An AI assistant with a redneck persona that engages in rambling, tangential conversations to infer the necessary details for constructing a system prompt for a new AI agent.
* **RSTWrangler**: A meticulous AI assistant specializing in transforming and cleaning up Markdown, AsciiDoc, or reStructuredText documents into clean, properly structured reStructuredText.
* **SceneSynth**: A literary analyst and collaborative scene developer that synthesizes information from a primary text and supporting context documents to produce a comprehensive scene analysis.
* **TheAnalyst**: An AI assistant characterized by extreme precision, pedantry, and a verbose, technical communication style.
* **TheAnalyst_ContextHandoff**: Generates a comprehensive handoff report detailing the entirety of a conversational session.
* **TypographersCompanion**: A knowledgeable and precise expert in typeface design, font development, and the history of writing systems, providing patient, step-by-step guidance on creating and optimizing fonts.

The following `.txt` files are not personas but are reference documents used by the `AsciidocFormatter` persona:
* AsciidocFAQ.txt
* AsciidocGuide.txt

## License

This project is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License. See the [LICENSE](LICENSE) file for details.
