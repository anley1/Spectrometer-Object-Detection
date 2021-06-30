

# if not getattr(pycocotools, '__version__', '0') >= '12.0.2':
#     raise AssertionError(
#         'Incompatible version of pycocotools is installed. '
#         'Run pip uninstall pycocotools first. Then run pip '
#         'install mmpycocotools to install open-mmlab forked '
#         'pycocotools.')

try:
    import pycocotools
    if not hasattr(pycocotools, '__sphinx_mock__'):  # for doc generation
        assert pycocotools.__version__ >= '12.0.2'
except AssertionError:
    raise AssertionError('Incompatible version of pycocotools is installed. '
                         'Run pip uninstall pycocotools first. Then run pip '
                         'install mmpycocotools to install open-mmlab forked '
                         'pycocotools.')
