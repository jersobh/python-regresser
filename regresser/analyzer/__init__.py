from regresser.analyzer import pil_analyzer, wand_analyzer

class Compare:

    def __init__(self, version):
        pil_analyzer.Compare(version=version)
        wand_analyzer.Compare(version=version)
