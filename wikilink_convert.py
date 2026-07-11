import re
from sys import argv
from pathlib import Path
from os.path import relpath

WIKILINK_REGEX = re.compile(
    r"\[\[(?:(?P<file>[^#|\]]+))?(?:#(?P<header>[^|\]]+))?(?:\|(?P<alias>[^\]]+))?\]\]",
    re.IGNORECASE
)
IMAGE_WIKILINK_REGEX = re.compile(
    r"!\[\[(?:(?P<image>[^#|\]]+))\]\]",
    re.IGNORECASE
)

def convert(vault_dir: str):
    vault_path = Path(vault_dir).resolve()

    # Wikilink for markdown files
    md_file_map = {f.stem: f for f in vault_path.rglob("*.md")}
    current_note = None

    def replace_md_wikilink(wikilink: re.Match[str]):
        if not wikilink["file"] or wikilink["file"] not in md_file_map:
            return wikilink.group(0)

        linked_note = md_file_map[wikilink["file"]]

        if linked_note.parent == current_note.parent:
            path = linked_note.name
        else:
            path = relpath(str(linked_note), str(current_note.parent))

        return "[{name}{header}]({path})".format(
            name = wikilink["alias"] if wikilink["alias"] else wikilink["file"],
            header = f" ({wikilink["header"]})" if wikilink["header"] else "",
            path = path
        )

    image_map = {f.name: f for f in vault_path.rglob("*") if f.is_file()}

    def replace_img_wikilink(wikilink: re.Match[str]):
        if not wikilink["image"] or wikilink["image"] not in image_map:
            return wikilink.group(0)

        linked_image = image_map[wikilink["image"]]
        path = relpath(str(linked_image), str(current_note.parent))

        return "![{name}]({path})".format(
            name = linked_image.stem,
            path = path
        )

    for note in vault_path.rglob("*.md"):
        content = note.read_text(encoding='utf-8')
        current_note = note

        updated_content = re.sub(WIKILINK_REGEX, replace_md_wikilink, content)
        updated_content = re.sub(IMAGE_WIKILINK_REGEX, replace_img_wikilink, updated_content)

        if updated_content != content:
            note.write_text(updated_content, encoding="utf-8")

if __name__ == "__main__":
    convert(argv[1] if len(argv) > 1 else ".")