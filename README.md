# AI Agent Persona Collection

[![Project Status: Active](https://img.shields.io/badge/Project%20Status-Active-green.svg)](https://shields.io/) [![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg?style=flat-square)](https://shields.io/)

This repository is a collection of system prompts designed to define the personas and behaviors of various AI agents. These are organized into functional categories, reflecting the directory structure of the repository.

## What is a System Prompt?

A system prompt is a set of instructions or guidelines given to an AI model at the beginning of a conversation. It helps to establish the AI's character, tone, specific knowledge, and operational constraints. By providing a well-defined system prompt, we can guide the AI to respond in a more consistent, relevant, and specialized manner.

## Available Personas

Below is a list of the AI agent personas currently available in this collection. Each persona's main prompt file is an `.md` file. Associated utility prompts or reference documents are listed with their respective personas.

### Writing & Content Creation
*(Directory: `Writing_and_Content_Creation/`)*

*   **Aetheria**: An AI fiction muse and idea catalyst for writers. (Files: `Aetheria/Aetheria.md`, `Aetheria/Aetheria_ContextHandoff.md`)
    *   `Aetheria_ContextHandoff`: Creates a "Story So Far" document to seamlessly continue brainstorming sessions.
*   **CareerCraft**: An expert resume coach and writing partner that guides users through creating and optimizing their resumes. (File: `CareerCraft.md`)
*   **KnowledgeWeaver**: A writing assistant for non-fiction that helps users brainstorm, outline, and develop a specific book concept. (File: `KnowledgeWeaver.md`)
*   **OutlineOracle**: A witty and wise outlining assistant for creative fiction that helps users plan and structure their novels. (File: `OutlineOracle.md`)
*   **SceneSynth**: A literary analyst and collaborative scene developer that synthesizes information from a primary text and supporting context documents to produce a comprehensive scene analysis. (File: `SceneSynth.md`)

### Analysis & Data Structuring
*(Directory: `Analysis_and_Data_Structuring/`)*

*   **FactExtractor**: A data processing specialist that synthesizes unstructured text data into highly organized, structured, and concise point-form facts for RAG ecosystems. (File: `FactExtractor.md`)
*   **LiteraryAnalyst**: An expert literary analyst and a keen observer of narrative craft that helps users understand and appreciate the literary features in fiction books. (Files: `LiteraryAnalyst/LiteraryAnalyst.md`, `LiteraryAnalyst/LiteraryAnalyst_Report.md`)
    *   `LiteraryAnalyst_Report`: Compiles a comprehensive summary report of a discussion with the Literary Analyst.
*   **ScopeHound**: A skilled and adaptive AI agent specializing in project initiation and task breakdown, employing an agile methodology to convert user input into actionable, granular tasks. (Files: `ScopeHound/ScopeHound.md`, `ScopeHound/ScopeHound_ProjectPlan.md`)
    *   `ScopeHound_ProjectPlan`: Consolidates all key decisions, confirmed requirements, user stories, and granular tasks from a project planning session.
*   **TheAnalyst**: An AI assistant characterized by extreme precision, pedantry, and a verbose, technical communication style. (Files: `TheAnalyst/TheAnalyst.md`, `TheAnalyst/TheAnalyst_ContextHandoff.md`, `TheAnalyst/TheAnalyst_FindingsReport.md`)
    *   `TheAnalyst_ContextHandoff`: Generates a comprehensive handoff report detailing the entirety of a conversational session.
    *   `TheAnalyst_FindingsReport`: Generates a meticulously structured findings report from a conversational log.
*   **TheCollator**: A silent, analytical AI assistant that organizes and structures chaotic brainstorming input into a structured, iterative summary. (File: `TheCollator.md`)
*   **TheExplainer**: An AI assistant that explains concepts in plain language, serving as a counterpart to The Analyst. (Files: `TheExplainer/TheExplainer.md`, `TheExplainer/TheExplainer_SummaryReport.md`)
    *   `TheExplainer_SummaryReport`: Generates a summary report of explanations provided.

### Technical & Formatting
*(Directory: `Technical_and_Formatting/`)*

*   **AsciidocFormatter**: A technical editor specializing in correcting formatting and structural errors in AsciiDoc documents, particularly those exported from Pandoc. (Files: `Asciidoc/AsciidocFormatter.md`, `Asciidoc/AsciidocFAQ.txt`, `Asciidoc/AsciidocGuide.txt`)
    *   Utilizes `AsciidocFAQ.txt` and `AsciidocGuide.txt` as essential reference documents. These are not personas themselves.
*   **PromptWhisperer**: An analytical and insightful AI assistant that translates a user's expressed intent into a fully optimized, standalone utility prompt for a specific third-party AI persona. (File: `PromptWhisperer.md`)
*   **Rodney**: An AI assistant with a redneck persona that engages in rambling, tangential conversations to infer the necessary details for constructing a system prompt for a new AI agent. (File: `Rodney.md`)
*   **RSTWrangler**: A meticulous AI assistant specializing in transforming and cleaning up Markdown, AsciiDoc, or reStructuredText documents into clean, properly structured reStructuredText. (File: `RSTWrangler.md`)
*   **TypographersCompanion**: A knowledgeable and precise expert in typeface design, font development, and the history of writing systems, providing patient, step-by-step guidance on creating and optimizing fonts. (File: `TypographersCompanion.md`)

### Humor, Satire & Esoterica
*(Directory: `Humor_Satire_and_Esoterica/`)*

*   **BlackPython**: An AI assistant with a dry, deadpan sense of humor, finding humor in the absurdity of everyday situations. (Files: `BlackPython/BlackPython.md`, `BlackPython/BlackPython_AcademicReview.md`, `BlackPython/BlackPython_ContextHandoff.md`, `BlackPython/BlackPython_ConversationSummary.md`)
    *   `BlackPython_AcademicReview`: Generates a savagely satirical academic review of a referenced resource.
    *   `BlackPython_ContextHandoff`: Generates a context handoff document to continue conversations seamlessly.
    *   `BlackPython_ConversationSummary`: Distills the essence of a conversation with observational wit.
*   **Chrono-Cartographer**: An analytical entity that identifies and articulates convoluted, indirect, and often fantastical causal relationships between any two or more given inputs or events. (Files: `Chrono-Cartographer/Chrono-Cartographer.md`, `Chrono-Cartographer/Chrono-Cartographer_ContextHandoff.md`, `Chrono-Cartographer/Chrono-Cartographer_SubjectReport.md`)
    *   `Chrono-Cartographer_ContextHandoff`: Generates a context handoff document for seamless continuation of analysis. (Filename corrected from `Chrono-Cartographyer_ContextHandoff.md`)
    *   `Chrono-Cartographer_SubjectReport`: Generates a comprehensive analytical report based on a chat context.
*   **Concept-Connector**: An analytical entity that identifies and articulates convoluted, indirect, and often fantastical causal relationships between any two or more given inputs or events. (Files: `Concept-Connector/Concept-Connector.md`, `Concept-Connector/Concept-Connector_SubjectReport.md`)
    *   `Concept-Connector_SubjectReport`: Generates a comprehensive 'Subject Report' on the convoluted causal relationships between topics discussed.
*   **ConspiracyDan**: An AI entity that operates from a worldview of profound and pervasive suspicion, generating novel conspiracy theories about any subject. (File: `ConspiracyDan.md`)
*   **DrFictionalis**: A helpful academic librarian who generates plausible-sounding, yet ultimately absurd, academic references in BibLaTeX format. (File: `DrFictionalis.md`)

### Specialized Expertise
*(Directory: `Specialized_Expertise/`)*

*   **ApexEdit**: A professional and meticulous copy-editor for refining and enhancing existing textual reports. (File: `ApexEdit.md`)
*   **CampfireConfidant**: An AI assistant for introspection and self-discovery. (Files: `CampfireConfidant/CampfireConfidant.md`, `CampfireConfidant/CampfireConfidant_Report.md`)
    *   `CampfireConfidant_Report`: Generates a report or summary of the introspective session.
*   **GregoryWilliamThomas**: A patient and truthful academic tutor with a dry, Blackadder-esque wit that generates responses in the format of a tailored business report. (File: `GregoryWilliamThomas.md`)
*   **LexiconAI**: A specialized linguistic agent that provides comprehensive, dictionary-style entries for any given term, including technobabble. (File: `LexiconAI.md`)
*   **Pastor**: A caring pastor with profound spiritual and intellectual depth, providing guidance, support, and theological insight rooted in a robust biblical framework. (Files: `Pastor/Pastor.md`, `Pastor/Pastor_StudyReport.md`)
    *   `Pastor_StudyReport`: Provides a comprehensive and meticulously detailed report of a discussion, formatted as a structured Bible study outline.

## License

[![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-sa/4.0/)

This project is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License. See the [LICENSE](LICENSE) file for details.
