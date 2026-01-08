import re
import json
import os

def parse_readme(readme_path="README.md"):
    """
    Parses the README.md file to extract paper entries organized by research direction.
    Each section starts with '## SectionName' and contains a markdown table.
    Returns a dictionary: {section_name: [list of paper entries]}
    """
    try:
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: {readme_path} not found.")
        return {}

    # Find all sections starting with ## (excluding ### or more)
    # Pattern: ## SectionName followed by content until next ## or end of file
    section_pattern = r'^## ([^\n]+)\n([\s\S]*?)(?=^## |\Z)'
    sections = re.findall(section_pattern, content, re.MULTILINE)
    
    if not sections:
        print("Error: Could not find any ## sections in README.md")
        return {}
    
    all_data = {}
    
    for section_name, section_content in sections:
        section_name = section_name.strip()
        
        # Skip overview or other non-paper sections (you can customize this list)
        if section_name.lower() in ['overview']:
            continue
        
        # Find the table in this section
        # Look for the header row
        header_pattern = r"\|\s*Time\s*\|\s*Venue\s*\|\s*Paper\s*\|\s*Research Question/Idea\s*\|\s*Method\s*\|\s*Remark\s*\|\s*Bib\s*\|"
        match = re.search(header_pattern, section_content, re.IGNORECASE)
        
        if not match:
            # No table in this section, add empty list
            all_data[section_name] = []
            continue

        # Get the content after the header
        table_content = section_content[match.end():]
        
        # Process lines
        lines = table_content.strip().split('\n')
        data = []
        
        # Skip the separator line (e.g., | :--- | :--- | ...)
        start_idx = 0
        if lines and lines[0].strip().startswith('|') and '---' in lines[0]:
            start_idx = 1

        for line in lines[start_idx:]:
            line = line.strip()
            if not line.startswith('|'):
                continue
                
            # Stop if we hit a line that looks like a section separator (---)
            if line.startswith('---'):
                break

            # Remove leading/trailing pipes
            if line.startswith('|'): line = line[1:]
            if line.endswith('|'): line = line[:-1]
            
            cols = [c.strip() for c in line.split('|')]
            
            # Check if we have enough columns (Time, Venue, Paper, Question, Method, Remark, Bib)
            if len(cols) >= 6:
                # Paper column often contains [Title](Link)
                # Convert Markdown link to HTML link
                paper_md = cols[2]
                paper_html = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', paper_md)
                
                # Convert bold in question
                question_md = cols[3]
                question_html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', question_md)
                
                # Convert bold in method
                method_md = cols[4]
                method_html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', method_md)
                
                # Remark - keep as is for MathJax
                remark_md = cols[5]

                # Bib column
                bib_md = cols[6] if len(cols) > 6 else ""
                
                entry = {
                    "time": cols[0],
                    "venue": cols[1],
                    "paper": paper_html,
                    "question": question_html,
                    "method": method_html,
                    "remark": remark_md,
                    "bib": bib_md
                }
                data.append(entry)
        
        all_data[section_name] = data
    
    return all_data

def update_index_html(data, html_path="index.html"):
    """
    Updates the index.html file with the new data.
    data is a dictionary: {section_name: [list of paper entries]}
    """
    try:
        with open(html_path, "r", encoding="utf-8") as f:
            html_content = f.read()
    except FileNotFoundError:
        print(f"Error: {html_path} not found.")
        return

    # Create the new JSON string
    new_data_json = json.dumps(data, indent=4)
    
    # Regex to find the data variable definition in the script tag
    # const data = { ... };
    pattern = r"(const\s+data\s*=\s*)\{[\s\S]*?\};"
    
    # Check if pattern exists
    if not re.search(pattern, html_content):
        print("Error: Could not find 'const data = {...}' in index.html")
        return

    # Escape backslashes in the new_data_json string before using it in re.sub
    new_data_json_escaped = new_data_json.replace('\\', '\\\\')

    # Replace the old data with new data
    new_html_content = re.sub(pattern, f"\\1{new_data_json_escaped};", html_content)
    
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(new_html_content)
    
    total_papers = sum(len(papers) for papers in data.values())
    print(f"Successfully updated {html_path} with {len(data)} sections and {total_papers} total papers.")
    for section, papers in data.items():
        print(f"  - {section}: {len(papers)} papers")

if __name__ == "__main__":
    entries = parse_readme()
    if entries:
        update_index_html(entries)
