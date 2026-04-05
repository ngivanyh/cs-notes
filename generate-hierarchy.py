import sys
from pathlib import Path

def generate_hierarchy(vault_dir: str):
    vault_path = Path(vault_dir).resolve()
    
    for md_file in vault_path.rglob('*.md'):
        relative_parts = md_file.parent.relative_to(vault_path).parts
        
        if not relative_parts:
            continue

        parent = relative_parts[-1]
        grand_parent = relative_parts[-2] if len(relative_parts) > 1 else None

        content = md_file.read_text(encoding='utf-8')
        lines = content.splitlines(keepends=True)
        
        if not lines or lines[0].strip() != '---':
            continue 
            
        end_idx = -1
        for i, line in enumerate(lines[1:], start=1):
            if line.strip() == '---':
                end_idx = i
                break
        
        if end_idx == -1:
            continue

        frontmatter = lines[1:end_idx]
        
        existing_keys = [line.split(':')[0].strip() for line in frontmatter if ':' in line]
        
        insertions = []
        if 'parent' not in existing_keys and parent:
            insertions.append(f"parent: {parent}\n")
        if 'grand_parent' not in existing_keys and grand_parent:
            insertions.append(f"grand_parent: {grand_parent}\n")

        if insertions:
            lines[end_idx:end_idx] = insertions
            md_file.write_text(''.join(lines), encoding='utf-8')

if __name__ == '__main__':
    target_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    generate_hierarchy(target_dir)