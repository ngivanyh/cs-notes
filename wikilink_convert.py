import re
from sys import argv
from pathlib import Path
from os.path import relpath

WIKILINK_REGEX = re.compile(
    r"\[\[(?:(?P<file>[^#|\]]+))?(?:#(?P<header>[^|\]]+))?(?:\|(?P<alias>[^\]]+))?\]\]",
    re.IGNORECASE
)

def convert(vault_dir: str):
    vault_path = Path(vault_dir).resolve()
    file_map = {f.stem: f for f in vault_path.rglob("*.md")}

    current_note = None

    def replace_link(wikilink: re.Match[str]):
        if not wikilink["file"] or wikilink["file"] not in file_map:
            return wikilink.group(0)

        linked_note = file_map[wikilink["file"]]

        if linked_note.parent == current_note.parent:
            path = linked_note.name
        else:
            path = relpath(str(linked_note), str(current_note.parent))

        return "[{name}{header}]({path})".format(
            name = wikilink["alias"] if wikilink["alias"] else wikilink["file"],
            header = f" ({wikilink["header"]})" if wikilink["header"] else "",
            path = path
        )

    for note in vault_path.rglob("*.md"):
        content = note.read_text(encoding='utf-8')
        current_note = note

        updated_content = re.sub(WIKILINK_REGEX, replace_link, content)

        if updated_content != content:
            note.write_text(updated_content, encoding="utf-8")

if __name__ == "__main__":
    convert(argv[1] if len(argv) > 1 else ".")