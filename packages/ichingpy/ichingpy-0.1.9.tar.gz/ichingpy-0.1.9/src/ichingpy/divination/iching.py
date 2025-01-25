# %%
import importlib.resources
import json

from ichingpy.divination.base import DivinationEngineBase
from ichingpy.enum.language import Language
from ichingpy.model.hexagram import Hexagram
from ichingpy.model.interpretation.hexagram.iching_hexagram import IChingHexagramInterp


class IChingDivinationEngine(DivinationEngineBase):

    def __init__(self):
        self._load_interpretation_data()

    def _load_interpretation_data(self) -> None:
        from ichingpy.model.interpretation.line.iching_line import IChingLineInterp

        match IChingLineInterp.display_language:

            case Language.CHINESE:
                file_name = "iching_zh.json"
            case Language.ENGLISH:
                file_name = "iching_en.json"

        with importlib.resources.files("ichingpy.data").joinpath(file_name).open(encoding="utf8") as f:
            self._data = json.load(f)["hexagrams"]

    def execute(self, hexagram: Hexagram) -> None:
        hexagram.interpretation = self._execute_inner(hexagram)
        hexagram.interpretation.transformed = self._execute_inner(hexagram.transformed)

    def _execute_inner(self, hexagram: Hexagram) -> IChingHexagramInterp:
        key = str(tuple([v % 2 for v in hexagram.values]))
        interp = IChingHexagramInterp.model_validate(self._data[key])
        for line, line_interp in zip(hexagram.lines, interp.lines):
            line_interp.status = line.status
        return interp
