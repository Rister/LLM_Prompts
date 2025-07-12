import os
import re

def standardize_markdown_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Extract the title
    title_match = re.search(r'### \*\*System Prompt for AI Agent: "(.+?)"\*\*|(?:# ).*', content)
    if title_match:
        title = title_match.group(1) or title_match.group(0).replace("# ", "")
    else:
        # if title is not found, use the filename as the title
        title = os.path.basename(filepath).replace(".md", "")

    # Extract the category from the filepath
    category = os.path.basename(os.path.dirname(os.path.dirname(filepath)))

    # Create the YAML metadata
    yaml_metadata = f"""\
---
name: {title}
description: A persona for {title}.
category: {category}
---
"""

    # Create the new content
    new_content = f"""\
{yaml_metadata}
# System Prompt for "{title}" AI Agent

{content}
"""

    with open(filepath, 'w') as f:
        f.write(new_content)

if __name__ == "__main__":
    for root, dirs, files in os.walk("Personas"):
        for file in files:
            if file.endswith(".md"):
                standardize_markdown_file(os.path.join(root, file))
