# AI Agent Persona Collection

[![Project Status: Active](https://img.shields.io/badge/Project%20Status-Active-green.svg)](https://shields.io/) [![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg?style=flat-square)](https://shields.io/)

This repository is a collection of system prompts designed to define the personas and behaviors of various AI agents. These are organized into functional categories, reflecting the directory structure of the repository.

## What is a System Prompt?

A system prompt is a set of instructions or guidelines given to an AI model at the beginning of a conversation. It helps to establish the AI's character, tone, specific knowledge, and operational constraints. By providing a well-defined system prompt, we can guide the AI to respond in a more consistent, relevant, and specialized manner.

## Available Personas

Below is a list of the AI agent personas currently available in this collection. Each persona's main prompt file is an `.md` file. Associated utility prompts or reference documents are listed with their respective personas.

**Categories:**
*   [Writing](#writing)
*   [Analysis](#analysis)
*   [Formatting](#formatting)
*   [Humor](#humor)
*   [Expertise](#expertise)

### Writing
*(Directory: `Personas/Writing/`)*

*   **Aetheria**: An AI fiction muse and idea catalyst for writers. (Files: `Aetheria/Aetheria.md`, `Aetheria/Generate_ContextHandoff.md`, `Aetheria/Generate_WorldBuildingReport.md`)
    *   `Generate_ContextHandoff`: Creates a "Story So Far" document to seamlessly continue brainstorming sessions.
    *   `Generate_WorldBuildingReport`: Generates a comprehensive world-building report.
*   **CaptainCabbage**: A family-friendly storyteller AI that facilitates interactive choose-your-own-adventure narratives based on user-provided themes. (File: `CaptainCabbage/CaptainCabbage.md`)
*   **CareerCraft**: An expert resume coach and writing partner that guides users through creating and optimizing their resumes. (File: `CareerCraft/CareerCraft.md`)
*   **Grimshaw**: A sophisticated, darkly humorous, and subtly unsettling AI that co-creates an ongoing, iterative choose-your-own-adventure story with the user. (File: `Grimshaw/Grimshaw.md`)
*   **KnowledgeWeaver**: A writing assistant for non-fiction that helps users brainstorm, outline, and develop a specific book concept. (File: `KnowledgeWeaver/KnowledgeWeaver.md`)
*   **OswaldFiliston**: An AI storyteller who constructs intricate, intellectually stimulating narratives for slightly nerdy adults, subtly infused with humor and irony. (File: `OswaldFiliston/OswaldFiliston.md`)
*   **OutlineOracle**: A witty and wise outlining assistant for creative fiction that helps users plan and structure their novels. (File: `OutlineOracle/OutlineOracle.md`)
*   **SceneSynth**: A literary analyst and collaborative scene developer that synthesizes information from a primary text and supporting context documents to produce a comprehensive scene analysis. (File: `SceneSynth/SceneSynth.md`)
*   **WorldSpark**: An AI agent that helps users brainstorm and develop fictional worlds. (File: `WorldSpark/WorldSpark.md`)

### Analysis
*(Directory: `Personas/Analysis/`)*

*   **DrSkratchensniff**: An AI agent with the sole purpose of determining the user's MBTI type. (File: `DrSkratchensniff/DrSkratchensniff.md`)
*   **FactExtractor**: A data processing specialist that synthesizes unstructured text data into highly organized, structured, and concise point-form facts for RAG ecosystems. (File: `FactExtractor/FactExtractor.md`)
*   **LiteraryAnalyst**: An expert literary analyst and a keen observer of narrative craft that helps users understand and appreciate the literary features in fiction books. (Files: `LiteraryAnalyst/LiteraryAnalyst.md`, `LiteraryAnalyst/Generate_LiteraryAnalysisReport.md`)
    *   `Generate_LiteraryAnalysisReport`: Compiles a comprehensive summary report of a discussion with the Literary Analyst.
*   **RuleWeaver**: An AI assistant that helps users create and manage complex rule sets. (Files: `RuleWeaver/RuleWeaver.md`, `RuleWeaver/Generate_RuleReport.md`)
    *   `Generate_RuleReport`: Generates a report of the current rule set.
*   **ScopeHound**: A skilled and adaptive AI agent specializing in project initiation and task breakdown, employing an agile methodology to convert user input into actionable, granular tasks. (Files: `ScopeHound/ScopeHound.md`, `ScopeHound/Generate_ProjectPlan.md`)
    *   `Generate_ProjectPlan`: Consolidates all key decisions, confirmed requirements, user stories, and granular tasks from a project planning session.
*   **TheAnalyst**: An AI assistant characterized by extreme precision, pedantry, and a verbose, technical communication style. (Files: `TheAnalyst/TheAnalyst.md`, `TheAnalyst/Generate_ContextHandoff.md`, `TheAnalyst/Generate_FindingsReport.md`)
    *   `Generate_ContextHandoff`: Generates a comprehensive handoff report detailing the entirety of a conversational session.
    *   `Generate_FindingsReport`: Generates a meticulously structured findings report from a conversational log.
*   **TheCollator**: A silent, analytical AI assistant that organizes and structures chaotic brainstorming input into a structured, iterative summary. (File: `TheCollator/TheCollator.md`)
*   **TheExplainer**: An AI assistant that explains concepts in plain language, serving as a counterpart to The Analyst. (Files: `TheExplainer/TheExplainer.md`, `TheExplainer/Generate_SummaryReport.md`)
    *   `Generate_SummaryReport`: Generates a summary report of explanations provided.

### Formatting
*(Directory: `Personas/Formatting/`)*

*   **AsciidocFormatter**: A technical editor specializing in correcting formatting and structural errors in AsciiDoc documents, particularly those exported from Pandoc. (Files: `AsciidocFormatter/AsciidocFormatter.md`, `AsciidocFormatter/AsciidocFAQ.txt`, `AsciidocFormatter/AsciidocGuide.txt`)
    *   Utilizes `AsciidocFAQ.txt` and `AsciidocGuide.txt` as essential reference documents. These are not personas themselves.
*   **PromptWhisperer**: An analytical and insightful AI assistant that translates a user's expressed intent into a fully optimized, standalone utility prompt for a specific third-party AI persona. (File: `PromptWhisperer/PromptWhisperer.md`)
*   **Rodney**: An AI assistant with a redneck persona that engages in rambling, tangential conversations to infer the necessary details for constructing a system prompt for a new AI agent. (File: `Rodney/Rodney.md`)
*   **RSTWrangler**: A meticulous AI assistant specializing in transforming and cleaning up Markdown, AsciiDoc, or reStructuredText documents into clean, properly structured reStructuredText. (File: `RSTWrangler/RSTWrangler.md`)
*   **TypographersCompanion**: A knowledgeable and precise expert in typeface design, font development, and the history of writing systems, providing patient, step-by-step guidance on creating and optimizing fonts. (File: `TypographersCompanion/TypographersCompanion.md`)

### Humor
*(Directory: `Personas/Humor/`)*

*   **BlackPython**: An AI assistant with a dry, deadpan sense of humor, finding humor in the absurdity of everyday situations. (Files: `BlackPython/BlackPython.md`, `BlackPython/Generate_AcademicReview.md`, `BlackPython/Generate_ContextHandoff.md`, `BlackPython/Generate_ConversationSummary.md`)
    *   `Generate_AcademicReview`: Generates a savagely satirical academic review of a referenced resource.
    *   `Generate_ContextHandoff`: Generates a context handoff document to continue conversations seamlessly.
    *   `Generate_ConversationSummary`: Distills the essence of a conversation with observational wit.
*   **Chrono-Cartographer**: An analytical entity that identifies and articulates convoluted, indirect, and often fantastical causal relationships between any two or more given inputs or events. (Files: `Chrono-Cartographer/Chrono-Cartographer.md`, `Chrono-Cartographer/Generate_ContextHandoff.md`, `Chrono-Cartographer/Generate_SubjectReport.md`)
    *   `Generate_ContextHandoff`: Generates a context handoff document for seamless continuation of analysis.
    *   `Generate_SubjectReport`: Generates a comprehensive analytical report based on a chat context.
*   **Concept-Connector**: An analytical entity that identifies and articulates convoluted, indirect, and often fantastical causal relationships between any two or more given inputs or events. (Files: `Concept-Connector/Concept-Connector.md`, `Concept-Connector/Generate_SubjectReport.md`)
    *   `Generate_SubjectReport`: Generates a comprehensive 'Subject Report' on the convoluted causal relationships between topics discussed.
*   **ConspiracyDan**: An AI entity that operates from a worldview of profound and pervasive suspicion, generating novel conspiracy theories about any subject. (File: `ConspiracyDan/ConspiracyDan.md`)
*   **DrFictionalis**: A helpful academic librarian who generates plausible-sounding, yet ultimately absurd, academic references in BibLaTeX format. (File: `DrFictionalis/DrFictionalis.md`)
*   **PeterC**: An AI with an irritable, cynical, and nihilistic persona, delivering scathingly humorous and aggressively witty critiques of ideas and concepts. (File: `PeterC/PeterC.md`)
*   **PeterS**: Similar to Peter C, an AI with a cynical and nihilistic persona, but employs caustic dirty jokes and "yo mama" jokes in its aggressive critiques. (File: `PeterS/PeterS.md`)

### Expertise
*(Directory: `Personas/Expertise/`)*

*   **ApexEdit**: A professional and meticulous copy-editor for refining and enhancing existing textual reports. (File: `ApexEdit/ApexEdit.md`)
*   **AthenianScholar**: A quiet, patient, and deeply knowledgeable tutor of Classical and Koine Greek. (File: `AthenianScholar/AthenianScholar.md`)
*   **CampfireConfidant**: An AI assistant for introspection and self-discovery. (Files: `CampfireConfidant/CampfireConfidant.md`, `CampfireConfidant/Generate_IntrospectionReport.md`)
    *   `Generate_IntrospectionReport`: Generates a report or summary of the introspective session.
*   **GregoryWilliamThomas**: A patient and truthful academic tutor with a dry, Blackadder-esque wit that generates responses in the format of a tailored business report. (File: `GregoryWilliamThomas/GregoryWilliamThomas.md`)
*   **LexiconAI**: A specialized linguistic agent that. (File: `LexiconAI/LexiconAI.md`)
*   **Pastor**: A caring pastor with profound spiritual and intellectual depth, providing guidance, support, and theological insight rooted in a robust biblical framework. (Files: `Pastor/Pastor.md`, `Pastor/Generate_StudyReport.md`)
    *   `Generate_StudyReport`: Provides a comprehensive and meticulously detailed report of a discussion, formatted as a structured Bible study outline.
*   **Professor**: A highly meticulous, calm, and methodically focused academic who specializes in the architecture of knowledge. (File: `Professor/Professor.md`)
*   **Rickey**: An expert guide in the meticulous development of system prompts. (File: `Rickey/Rickey.md`)
*   **TeacherTammy**: An enthusiastic and eccentric AI tutor who educates users on chosen topics through immersive, choose-your-own-adventure style storytelling, suitable for a 4th-grade level. (File: `TeacherTammy/TeacherTammy.md`)

## License

[![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-sa/4.0/)

This project is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License. See the [LICENSE](LICENSE) file for details.
