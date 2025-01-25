from pathlib import Path
from tempfile import TemporaryDirectory

import harrix_pylib as h


def test_add_author_book():
    current_folder = h.dev.get_project_root()
    md = Path(current_folder / "tests/data/add_author_book__before.md").read_text(encoding="utf8")
    md_after = Path(current_folder / "tests/data/add_author_book__after.md").read_text(encoding="utf8")

    with TemporaryDirectory() as temp_folder:
        temp_filename = Path(temp_folder) / "temp.md"
        temp_filename.write_text(md, encoding="utf-8")
        h.md.add_author_book(temp_filename)
        md_applied = temp_filename.read_text(encoding="utf8")
        md_after = md_after.replace("Name Surname", Path(temp_folder).name)

    assert md_after == md_applied


def test_add_image_captions():
    current_folder = h.dev.get_project_root()
    md = Path(current_folder / "tests/data/add_image_captions__before.md").read_text(encoding="utf8")
    md_after = Path(current_folder / "tests/data/add_image_captions__after.md").read_text(encoding="utf8")

    with TemporaryDirectory() as temp_folder:
        temp_filename = Path(temp_folder) / "temp.md"
        temp_filename.write_text(md, encoding="utf-8")
        h.md.add_image_captions(temp_filename)
        md_applied = temp_filename.read_text(encoding="utf8")

    assert md_after == md_applied


def test_get_yaml_from_markdown():
    md = Path(h.dev.get_project_root() / "tests/data/get_yaml.md").read_text(encoding="utf8")
    md_clean = h.md.get_yaml(md)
    assert len(md_clean.splitlines()) == 4


def test_remove_yaml_from_markdown():
    md = Path(h.dev.get_project_root() / "tests/data/get_yaml.md").read_text(encoding="utf8")
    md_clean = h.md.remove_yaml(md)
    assert len(md_clean.splitlines()) == 1


def test_sort_sections():
    current_folder = h.dev.get_project_root()
    md = Path(current_folder / "tests/data/sort_sections__before.md").read_text(encoding="utf8")
    md_after = Path(current_folder / "tests/data/sort_sections__after.md").read_text(encoding="utf8")

    with TemporaryDirectory() as temp_folder:
        temp_filename = Path(temp_folder) / "temp.md"
        temp_filename.write_text(md, encoding="utf-8")
        h.md.sort_sections(temp_filename)
        md_applied = temp_filename.read_text(encoding="utf8")

    assert md_after == md_applied
