import json
import os
import tempfile
from dataclasses import dataclass
from enum import StrEnum, auto, unique
from pathlib import Path
from shutil import which
from typing import TYPE_CHECKING, NamedTuple

from pydantic import BaseModel, ConfigDict

from codegen.git import LocalRepoOperator
from graph_sitter.codebase.config import GSFeatureFlags
from graph_sitter.enums import ProgrammingLanguage
from graph_sitter.testing.constants import DIFF_FILEPATH
from graph_sitter.testing.verified_codemod_utils import CodemodAPI

BASE_TMP_DIR = Path(os.getenv("GITHUB_WORKSPACE", tempfile.gettempdir()))
BASE_PATH: Path = Path(__file__).parent.parent.parent.parent
TEST_DIR: Path = BASE_PATH / "tests" / "codemod"
CODEMOD_PATH: Path = BASE_PATH / "src" / "codemods"
VERIFIED_CODEMOD_DIR: Path = BASE_PATH / "tests" / "verified_codemods"
VERIFIED_CODEMOD_DATA_DIR: Path = VERIFIED_CODEMOD_DIR / "codemod_data"
VERIFIED_CODEMOD_DIFFS: Path = VERIFIED_CODEMOD_DIR / ".verified_codemod_diffs"


if TYPE_CHECKING:
    from graph_sitter.codemod import Codemod3


@unique
class Size(StrEnum):
    Small = auto()
    Large = auto()


class Repo(BaseModel):
    """Dang a 4th repo 💀"""

    model_config = ConfigDict(arbitrary_types_allowed=True)
    url: str
    commit: str
    language: ProgrammingLanguage
    size: Size = Size.Small
    subdirectories: list[str] | None = None
    produce_diffs: bool = True
    extra_repo: bool = False
    default_branch: str = "master"
    repo_id: int | None = None
    priority: int = 0
    base_path: str | None = None
    feature_flags: GSFeatureFlags | None = None

    @classmethod
    def from_json(cls, json_str: str) -> "Repo":
        return cls.model_validate(json.loads(json_str))

    def to_op(self, name: str, token: str | None) -> LocalRepoOperator:
        base_path = BASE_TMP_DIR / ("extra_repos" if self.extra_repo else "oss_repos") / name
        base_path.mkdir(exist_ok=True, parents=True)
        url = self.url
        if token:
            url = url.replace("://", f"://{token}@")
        elif self.repo_id is not None:
            print("Setting up auth using the github cli")
            if not which("gh"):
                os.system("brew install gh")
            if '[credential "https://github.codegen.app"]' not in (Path.home() / ".gitconfig").read_text():
                os.system("gh auth login -h github.codegen.app")
                os.system("gh auth setup-git -h github.codegen.app")
        # elif self.repo_id is not None:
        #
        #     from app.models.connect import get_session_local
        #     from app.models.repo import RepoModel
        #     from codegen.utils.github_utils.url.clone_url import get_authenticated_clone_url_for_repo_model
        #
        #     db = get_session_local()  # nosemgrep
        #     repo = RepoModel.find_by_id(db, self.repo_id)
        #     url = get_authenticated_clone_url_for_repo_model(repo)
        return LocalRepoOperator.create_from_commit(str(base_path), self.default_branch, self.commit, url)


@dataclass
class CodemodMetadata:
    codemod: type["Codemod3"]
    category: str
    directory: Path
    company: str | None = None
    codemod_id: int | None = None
    repo_app_id: int | None = None
    codemod_url: str | None = None
    codemod_api: CodemodAPI | None = None
    empty_diff: bool = False

    @property
    def name(self) -> str:
        if self.codemod.name:
            return self.codemod.name
        return self.codemod.__name__

    @property
    def test_dir(self) -> Path:
        return TEST_DIR / self.directory.relative_to(CODEMOD_PATH)


class CustomRepoTestCase(NamedTuple):
    codemod_metadata: CodemodMetadata
    expected_dir: Path
    input_dir: Path


class ClonedRepoTestCase(NamedTuple):
    codemod_metadata: CodemodMetadata
    repo: Repo
    repo_name: str
    test_dir: Path
    diff_path: Path

    @property
    def should_skip(self) -> bool:
        return self.test_dir.joinpath(DIFF_FILEPATH + ".skip").exists()
