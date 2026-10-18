"""Check extraction fidelity and execute every generated notebook code cell."""

from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from audit_nltk_blocks import BLOCK, ORGANON_DIR, section
from export_dhatu_notebook import BLOCK_NAMES, build_notebook


class DhatuNotebookTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.notebook = build_notebook()

    def test_layout_and_exact_block_roundtrip(self):
        notebook = json.loads(json.dumps(self.notebook))
        self.assertEqual((notebook["nbformat"], notebook["nbformat_minor"]), (4, 5))
        self.assertEqual(len(notebook["cells"]), 148)
        self.assertEqual(len({c["id"] for c in notebook["cells"]}), 148)
        for number in range(1, 49):
            with self.subTest(verse=number):
                text = (ORGANON_DIR / "01-dhatu" / f"VAK_1.{number:02d}.md").read_text(
                    encoding="utf-8"
                )
                context, blocks, run = notebook["cells"][2 + (number - 1) * 3:5 + (number - 1) * 3]
                self.assertEqual(context["cell_type"], "markdown")
                self.assertIn(section(text, 3).strip(), "".join(context["source"]))
                namespace = {}
                exec("".join(blocks["source"]), namespace)
                for kind, body in BLOCK.findall(section(text, 4)) + BLOCK.findall(section(text, 8)):
                    self.assertEqual(namespace[BLOCK_NAMES[kind]], body)
                for cell in (blocks, run):
                    self.assertEqual(cell["outputs"], [])
                    self.assertIsNone(cell["execution_count"])

    def test_run_all_and_countermodel(self):
        namespace = {}
        with redirect_stdout(io.StringIO()):
            for cell in self.notebook["cells"]:
                if cell["cell_type"] == "code":
                    exec(compile("".join(cell["source"]), cell["id"], "exec"), namespace)
        self.assertEqual(set(namespace["studies"]), set(range(1, 49)))
        for study in namespace["studies"].values():
            self.assertEqual(study["results"]["verse"], "T")
            self.assertEqual(study["sem"].free(), set())
        self.assertIs(namespace["before"], True)
        self.assertIs(namespace["after"], False)
        self.assertNotIn(
            ("ecog_d", "sound_d"), namespace["studies"][48]["valuation"]["Knows"]
        )
        with self.assertRaisesRegex(ValueError, "grammar parse"):
            namespace["run_study"](
                namespace["fcfg_text"].replace("'pañca'", "'missing'"),
                namespace["dependency_text"],
                namespace["sem_text"],
                namespace["fol_text"],
                namespace["valuation_text"],
            )

    def test_cli_protects_existing_notebook(self):
        with tempfile.TemporaryDirectory() as folder:
            output = Path(folder) / "experiment.ipynb"
            output.write_text("my experiment", encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(Path(__file__).with_name("export_dhatu_notebook.py")),
                 "--output", str(output)],
                capture_output=True, text=True, check=False,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("already exists", result.stderr)
            self.assertEqual(output.read_text(encoding="utf-8"), "my experiment")


if __name__ == "__main__":
    unittest.main()
