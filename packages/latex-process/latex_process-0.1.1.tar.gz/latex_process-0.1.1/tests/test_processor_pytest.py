import shutil
import pytest
from pathlib import Path
from latex_process import LatexProcess, LatexProcessError
import logging

@pytest.fixture
def processor():
    output_dir = Path('test_output_pytest')
    output_dir.mkdir(exist_ok=True)
    proc = LatexProcess(
        engine='pdflatex',
        bib_tool='bibtex',
        output_format='pdf',
        output_dir=output_dir,
        output_filename='test_document.pdf',
        log_level=logging.DEBUG
    )
    yield proc
    # Teardown
    if output_dir.exists():
        shutil.rmtree(output_dir)

def test_load_from_string(processor):
    sample_tex = r"""
    \documentclass{article}
    \begin{document}
    Hello, Pytest!
    \end{document}
    """
    processor.load_from_string(sample_tex)
    assert "Hello, Pytest!" in processor.latex_code

def test_compile_success(processor):
    sample_tex = r"""
    \documentclass{article}
    \begin{document}
    Hello, Pytest!
    \end{document}
    """
    processor.load_from_string(sample_tex)
    output = processor.compile()
    assert output.exists()
    assert output.name == 'test_document.pdf'

def test_compile_failure(processor):
    invalid_tex = r"""
    \documentclass{article}
    \begin{document}
    \helllo, Pytest! % Intentional typo to cause error
    \end{document}
    """
    processor.load_from_string(invalid_tex)
    with pytest.raises(LatexProcessError):
        processor.compile()

def test_add_dependency(processor):
    dep_file = processor.output_dir / 'image.png'
    dep_file.touch()
    processor.add_dependency(str(dep_file))
    assert str(dep_file.resolve()) in processor.dependencies

def test_render_template(processor):
    template_content = r"""
    \documentclass{article}
    \begin{document}
    Hello, {{ name }}!
    \end{document}
    """
    template_file = processor.output_dir / 'template.tex'
    template_file.write_text(template_content, encoding='utf-8')
    processor.template = str(template_file)
    context = {'name': 'Pytest'}
    processor.render_template(context)
    assert "Hello, Pytest!" in processor.latex_code
