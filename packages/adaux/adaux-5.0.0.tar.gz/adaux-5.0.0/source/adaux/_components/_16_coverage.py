# Copyright (c) 2021-2025 Mario S. Könz; License: MIT
from ._15_pytest import PytestMixin


class CoverageMixin(PytestMixin):
    def templated(self, negative_default: bool = False) -> None:
        super().templated(negative_default)
        self.auxcon.dependencies.test.append(self.versions.pytest_cov)
