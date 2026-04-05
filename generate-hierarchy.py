import sys
from pathlib import Path

def generate_hierarchy(vault_dir: str):
    vault_path = Path(vault_dir).resolve()
    
    dir_nav_orders = {}

    for md_file in vault_path.rglob('*.md'):
        relative_parts = md_file.parent.relative_to(vault_path).parts
        
        parent = relative_parts[-1] if len(relative_parts) >= 1 else None
        grand_parent = relative_parts[-2] if len(relative_parts) >= 2 else None

        dir_path = md_file.parent
        if dir_path not in dir_nav_orders:
            md_files_in_dir = sorted([f.name for f in dir_path.glob('*.md')])
            dir_nav_orders[dir_path] = {name: idx + 1 for idx, name in enumerate(md_files_in_dir)}
            
        nav_order = dir_nav_orders[dir_path][md_file.name]

        is_readme = md_file.name.lower() in ['readme.md', 'index.md']

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
        clean_frontmatter = []
        
        keys_to_purge = ['parent', 'grand_parent', 'nav_order']
        if is_readme:
            keys_to_purge.append('title')
        
        for line in frontmatter:
            key = line.split(':')[0].strip() if ':' in line else ""
            if key not in keys_to_purge:
                clean_frontmatter.append(line)
        
        insertions = []
        
        if is_readme:
            if grand_parent and parent:
                insertions.append(f"title: Intro — {grand_parent}/{parent}\n")
            elif parent:
                insertions.append(f"title: Intro — {parent}\n")
            else:
                insertions.append("title: Intro\n")
                
        if parent:
            insertions.append(f"parent: {parent}\n")
        if grand_parent:
            insertions.append(f"grand_parent: {grand_parent}\n")
            
        insertions.append(f"nav_order: {nav_order}\n")

        new_lines = [lines[0]] + clean_frontmatter + insertions + lines[end_idx:]

        if lines != new_lines:
            md_file.write_text(''.join(new_lines), encoding='utf-8')

if __name__ == '__main__':
    target_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    generate_hierarchy(target_dir)