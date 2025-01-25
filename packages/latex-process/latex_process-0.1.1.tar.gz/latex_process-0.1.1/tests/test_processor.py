import shutil
import unittest
from pathlib import Path
from latex_process import LatexProcess, LatexProcessError
import logging

class TestLatexProcess(unittest.TestCase):
    def setUp(self):
        """
        Set up a LatexProcess instance for testing.
        """
        self.output_dir = Path('test_output')
        self.output_dir.mkdir(exist_ok=True)
        self.processor = LatexProcess(
            engine='pdflatex',
            bib_tool='bibtex',
            output_format='pdf',
            output_dir=self.output_dir,
            output_filename='test_document.pdf',
            log_level=logging.DEBUG
        )
        self.sample_tex = r"""
        \documentclass{article}
        \begin{document}
        Hello, World!
        \end{document}
        """
    
    def tearDown(self):
        """
        Clean up the output directory after tests.
        """
        if self.output_dir.exists():
            shutil.rmtree(self.output_dir)
    
    def test_load_from_string(self):
        """
        Test loading LaTeX code from a string.
        """
        self.processor.load_from_string(self.sample_tex)
        self.assertIn("Hello, World!", self.processor.latex_code)
    
    def test_compile_success(self):
        """
        Test successful compilation of a simple LaTeX document.
        """
        self.processor.load_from_string(self.sample_tex)
        output = self.processor.compile()
        self.assertTrue(output.exists())
        self.assertEqual(output.name, 'document.pdf')
    
    def test_compile_failure(self):
        """
        Test compilation failure with invalid LaTeX code.
        """
        invalid_tex_code = r"""
        \documentclass{article}
        \begin{document}
        This is a test document with an error
        \missingcommand % This command does not exist
        \end{document}
        """
        self.processor.load_from_string(invalid_tex_code)
        
        with self.assertRaises(LatexProcessError) as context:
            self.processor.compile()
        
        self.assertIn("Command 'pdflatex", str(context.exception))  # Check if the exception message contains the command
    
    def test_add_dependency(self):
        """
        Test adding a dependency file.
        """
        # Create a dummy dependency file
        dep_file = self.output_dir / 'image.png'
        dep_file.touch()
        self.processor.add_dependency(str(dep_file))
        self.assertIn(str(dep_file.resolve()), self.processor.dependencies)
    
    def test_render_template(self):
        """
        Test rendering LaTeX code from a Jinja2 template.
        """
        template_content = r"""
        \documentclass{article}
        \begin{document}
        Hello, {{ name }}!
        \end{document}
        """
        template_file = self.output_dir / 'template.tex'
        template_file.write_text(template_content, encoding='utf-8')
        self.processor.template = str(template_file)
        context = {'name': 'Tester'}
        self.processor.render_template(context)
        self.assertIn("Hello, Tester!", self.processor.latex_code)

if __name__ == '__main__':
    unittest.main()
