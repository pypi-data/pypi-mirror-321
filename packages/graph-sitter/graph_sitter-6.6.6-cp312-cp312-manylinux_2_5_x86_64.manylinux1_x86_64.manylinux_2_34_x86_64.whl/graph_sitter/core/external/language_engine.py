from abc import abstractmethod
from typing import TYPE_CHECKING

from graph_sitter.core.external.external_process import ExternalProcess
from graph_sitter.enums import ProgrammingLanguage

if TYPE_CHECKING:
    from graph_sitter.codebase.codebase_graph import CodebaseGraph
    from graph_sitter.core.interfaces.editable import Editable


class LanguageEngine(ExternalProcess):
    """Base class for all third part language engine support.

    This class provides the foundation for integrating external language analysis engines.
    It handles initialization, startup, and status tracking of the engine.
    """

    @abstractmethod
    def get_return_type(self, node: "Editable") -> str | None:
        pass


def get_language_engine(language: ProgrammingLanguage, codebase_graph: "CodebaseGraph", use_ts: bool = False, use_v8: bool = False) -> LanguageEngine | None:
    from graph_sitter.typescript.external.ts_analyzer_engine import NodeTypescriptEngine, V8TypescriptEngine

    use_ts = use_ts or codebase_graph.config.feature_flags.ts_language_engine
    use_v8 = use_v8 or codebase_graph.config.feature_flags.v8_ts_engine
    if language == ProgrammingLanguage.TYPESCRIPT:
        if use_ts and use_v8:
            # Enables with both ts_language_engine and v8_ts_engine feature flags are on
            return V8TypescriptEngine(repo_path=codebase_graph.repo_path, base_path=codebase_graph.projects[0].base_path, dependency_manager=codebase_graph.dependency_manager)
        elif use_ts:
            # Enabled with only ts_language_engine feature flag is on
            return NodeTypescriptEngine(repo_path=codebase_graph.repo_path, base_path=codebase_graph.projects[0].base_path, dependency_manager=codebase_graph.dependency_manager)

    return None
