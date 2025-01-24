# External imports
import os
import re
from pathlib import Path
import networkx as nx
import plotly

# GraphSitter imports (private)

from graph_sitter.codebase.control_flow import StopCodemodException

# GraphSitter imports (public)
from graph_sitter.codebase.flagging.enums import FlagKwargs
from graph_sitter.codebase.flagging.enums import MessageType
from graph_sitter.codebase.span import Span
from graph_sitter.core.assignment import Assignment
from graph_sitter.core.class_definition import Class
from graph_sitter.core.codebase import Codebase
from graph_sitter.core.codebase import CodebaseType
from graph_sitter.core.codebase import PyCodebaseType
from graph_sitter.core.codebase import TSCodebaseType
from graph_sitter.core.dataclasses.usage import Usage
from graph_sitter.core.dataclasses.usage import UsageKind
from graph_sitter.core.dataclasses.usage import UsageType
from graph_sitter.core.detached_symbols.argument import Argument
from graph_sitter.core.detached_symbols.code_block import CodeBlock
from graph_sitter.core.detached_symbols.decorator import Decorator
from graph_sitter.core.detached_symbols.function_call import FunctionCall
from graph_sitter.core.detached_symbols.parameter import Parameter
from graph_sitter.core.directory import Directory
from graph_sitter.core.export import Export
from graph_sitter.core.expressions.await_expression import AwaitExpression
from graph_sitter.core.expressions.binary_expression import BinaryExpression
from graph_sitter.core.expressions.boolean import Boolean
from graph_sitter.core.expressions.chained_attribute import ChainedAttribute
from graph_sitter.core.expressions.comparison_expression import ComparisonExpression
from graph_sitter.core.expressions.expression import Expression
from graph_sitter.core.expressions.generic_type import GenericType
from graph_sitter.core.expressions.multi_expression import MultiExpression
from graph_sitter.core.expressions.name import Name
from graph_sitter.core.expressions.named_type import NamedType
from graph_sitter.core.expressions.none_type import NoneType
from graph_sitter.core.expressions.number import Number
from graph_sitter.core.expressions.parenthesized_expression import ParenthesizedExpression
from graph_sitter.core.expressions.placeholder_type import PlaceholderType
from graph_sitter.core.expressions.string import String
from graph_sitter.core.expressions.subscript_expression import SubscriptExpression
from graph_sitter.core.expressions.ternary_expression import TernaryExpression
from graph_sitter.core.expressions.tuple_type import TupleType
from graph_sitter.core.expressions.type import Type
from graph_sitter.core.expressions.unary_expression import UnaryExpression
from graph_sitter.core.expressions.union_type import UnionType
from graph_sitter.core.expressions.unpack import Unpack
from graph_sitter.core.expressions.value import Value
from graph_sitter.core.external_module import ExternalModule
from graph_sitter.core.file import File
from graph_sitter.core.file import SourceFile
from graph_sitter.core.function import Function
from graph_sitter.core.import_resolution import Import
from graph_sitter.core.interfaces.callable import Callable
from graph_sitter.core.interfaces.editable import Editable
from graph_sitter.core.interfaces.exportable import Exportable
from graph_sitter.core.interfaces.has_block import HasBlock
from graph_sitter.core.interfaces.has_name import HasName
from graph_sitter.core.interfaces.has_value import HasValue
from graph_sitter.core.interfaces.importable import Importable
from graph_sitter.core.interfaces.typeable import Typeable
from graph_sitter.core.interfaces.unwrappable import Unwrappable
from graph_sitter.core.interfaces.usable import Usable
from graph_sitter.core.placeholder.placeholder import Placeholder
from graph_sitter.core.placeholder.placeholder_stub import StubPlaceholder
from graph_sitter.core.placeholder.placeholder_type import TypePlaceholder
from graph_sitter.core.statements.assignment_statement import AssignmentStatement
from graph_sitter.core.statements.attribute import Attribute
from graph_sitter.core.statements.block_statement import BlockStatement
from graph_sitter.core.statements.catch_statement import CatchStatement
from graph_sitter.core.statements.comment import Comment
from graph_sitter.core.statements.export_statement import ExportStatement
from graph_sitter.core.statements.expression_statement import ExpressionStatement
from graph_sitter.core.statements.for_loop_statement import ForLoopStatement
from graph_sitter.core.statements.if_block_statement import IfBlockStatement
from graph_sitter.core.statements.import_statement import ImportStatement
from graph_sitter.core.statements.raise_statement import RaiseStatement
from graph_sitter.core.statements.return_statement import ReturnStatement
from graph_sitter.core.statements.statement import Statement
from graph_sitter.core.statements.statement import StatementType
from graph_sitter.core.statements.switch_case import SwitchCase
from graph_sitter.core.statements.switch_statement import SwitchStatement
from graph_sitter.core.statements.symbol_statement import SymbolStatement
from graph_sitter.core.statements.try_catch_statement import TryCatchStatement
from graph_sitter.core.statements.while_statement import WhileStatement
from graph_sitter.core.symbol import Symbol
from graph_sitter.core.symbol_group import SymbolGroup
from graph_sitter.core.symbol_groups.comment_group import CommentGroup
from graph_sitter.core.symbol_groups.dict import Dict
from graph_sitter.core.symbol_groups.dict import Pair
from graph_sitter.core.symbol_groups.expression_group import ExpressionGroup
from graph_sitter.core.symbol_groups.list import List
from graph_sitter.core.symbol_groups.multi_line_collection import MultiLineCollection
from graph_sitter.core.symbol_groups.tuple import Tuple
from graph_sitter.core.type_alias import TypeAlias
from graph_sitter.python.assignment import PyAssignment
from graph_sitter.python.class_definition import PyClass
from graph_sitter.python.detached_symbols.code_block import PyCodeBlock
from graph_sitter.python.detached_symbols.decorator import PyDecorator
from graph_sitter.python.detached_symbols.parameter import PyParameter
from graph_sitter.python.expressions.chained_attribute import PyChainedAttribute
from graph_sitter.python.expressions.conditional_expression import PyConditionalExpression
from graph_sitter.python.expressions.generic_type import PyGenericType
from graph_sitter.python.expressions.named_type import PyNamedType
from graph_sitter.python.expressions.string import PyString
from graph_sitter.python.expressions.union_type import PyUnionType
from graph_sitter.python.file import PyFile
from graph_sitter.python.function import PyFunction
from graph_sitter.python.import_resolution import PyImport
from graph_sitter.python.interfaces.has_block import PyHasBlock
from graph_sitter.python.placeholder.placeholder_return_type import PyReturnTypePlaceholder
from graph_sitter.python.statements.assignment_statement import PyAssignmentStatement
from graph_sitter.python.statements.attribute import PyAttribute
from graph_sitter.python.statements.block_statement import PyBlockStatement
from graph_sitter.python.statements.break_statement import PyBreakStatement
from graph_sitter.python.statements.catch_statement import PyCatchStatement
from graph_sitter.python.statements.comment import PyComment
from graph_sitter.python.statements.comment import PyCommentType
from graph_sitter.python.statements.for_loop_statement import PyForLoopStatement
from graph_sitter.python.statements.if_block_statement import PyIfBlockStatement
from graph_sitter.python.statements.import_statement import PyImportStatement
from graph_sitter.python.statements.match_case import PyMatchCase
from graph_sitter.python.statements.match_statement import PyMatchStatement
from graph_sitter.python.statements.pass_statement import PyPassStatement
from graph_sitter.python.statements.try_catch_statement import PyTryCatchStatement
from graph_sitter.python.statements.while_statement import PyWhileStatement
from graph_sitter.python.statements.with_statement import WithStatement
from graph_sitter.python.symbol import PySymbol
from graph_sitter.python.symbol_groups.comment_group import PyCommentGroup
from graph_sitter.typescript.assignment import TSAssignment
from graph_sitter.typescript.class_definition import TSClass
from graph_sitter.typescript.detached_symbols.code_block import TSCodeBlock
from graph_sitter.typescript.detached_symbols.decorator import TSDecorator
from graph_sitter.typescript.detached_symbols.jsx.element import JSXElement
from graph_sitter.typescript.detached_symbols.jsx.expression import JSXExpression
from graph_sitter.typescript.detached_symbols.jsx.prop import JSXProp
from graph_sitter.typescript.detached_symbols.parameter import TSParameter
from graph_sitter.typescript.enum_definition import TSEnum
from graph_sitter.typescript.export import TSExport
from graph_sitter.typescript.expressions.array_type import TSArrayType
from graph_sitter.typescript.expressions.chained_attribute import TSChainedAttribute
from graph_sitter.typescript.expressions.conditional_type import TSConditionalType
from graph_sitter.typescript.expressions.expression_type import TSExpressionType
from graph_sitter.typescript.expressions.function_type import TSFunctionType
from graph_sitter.typescript.expressions.generic_type import TSGenericType
from graph_sitter.typescript.expressions.lookup_type import TSLookupType
from graph_sitter.typescript.expressions.named_type import TSNamedType
from graph_sitter.typescript.expressions.object_type import TSObjectType
from graph_sitter.typescript.expressions.query_type import TSQueryType
from graph_sitter.typescript.expressions.readonly_type import TSReadonlyType
from graph_sitter.typescript.expressions.string import TSString
from graph_sitter.typescript.expressions.ternary_expression import TSTernaryExpression
from graph_sitter.typescript.expressions.undefined_type import TSUndefinedType
from graph_sitter.typescript.expressions.union_type import TSUnionType
from graph_sitter.typescript.file import TSFile
from graph_sitter.typescript.function import TSFunction
from graph_sitter.typescript.import_resolution import TSImport
from graph_sitter.typescript.interface import TSInterface
from graph_sitter.typescript.interfaces.has_block import TSHasBlock
from graph_sitter.typescript.namespace import TSNamespace
from graph_sitter.typescript.placeholder.placeholder_return_type import TSReturnTypePlaceholder
from graph_sitter.typescript.statements.assignment_statement import TSAssignmentStatement
from graph_sitter.typescript.statements.attribute import TSAttribute
from graph_sitter.typescript.statements.block_statement import TSBlockStatement
from graph_sitter.typescript.statements.catch_statement import TSCatchStatement
from graph_sitter.typescript.statements.comment import TSComment
from graph_sitter.typescript.statements.comment import TSCommentType
from graph_sitter.typescript.statements.for_loop_statement import TSForLoopStatement
from graph_sitter.typescript.statements.if_block_statement import TSIfBlockStatement
from graph_sitter.typescript.statements.import_statement import TSImportStatement
from graph_sitter.typescript.statements.labeled_statement import TSLabeledStatement
from graph_sitter.typescript.statements.switch_case import TSSwitchCase
from graph_sitter.typescript.statements.switch_statement import TSSwitchStatement
from graph_sitter.typescript.statements.try_catch_statement import TSTryCatchStatement
from graph_sitter.typescript.statements.while_statement import TSWhileStatement
from graph_sitter.typescript.symbol import TSSymbol
from graph_sitter.typescript.symbol_groups.comment_group import TSCommentGroup
from graph_sitter.typescript.symbol_groups.dict import TSDict
from graph_sitter.typescript.symbol_groups.dict import TSPair
from graph_sitter.typescript.ts_config import TSConfig
from graph_sitter.typescript.type_alias import TSTypeAlias
# file generated by setuptools_scm
# don't change, don't track in version control
TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Tuple, Union
    VERSION_TUPLE = Tuple[Union[int, str], ...]
else:
    VERSION_TUPLE = object

version: str
__version__: str
__version_tuple__: VERSION_TUPLE
version_tuple: VERSION_TUPLE

__version__ = version = '6.6.6'
__version_tuple__ = version_tuple = (6, 6, 6)

__all__ = [
    "__version__",
    "__version_tuple__",
    "StopCodemodException",
    "Argument",
    "Assignment",
    "AssignmentStatement",
    "Attribute",
    "AwaitExpression",
    "BinaryExpression",
    "BlockStatement",
    "Boolean",
    "Callable",
    "CatchStatement",
    "ChainedAttribute",
    "Class",
    "CodeBlock",
    "Codebase",
    "CodebaseType",
    "Comment",
    "CommentGroup",
    "ComparisonExpression",
    "Decorator",
    "Dict",
    "Directory",
    "Editable",
    "Export",
    "ExportStatement",
    "Exportable",
    "Expression",
    "ExpressionGroup",
    "ExpressionStatement",
    "ExternalModule",
    "File",
    "FlagKwargs",
    "ForLoopStatement",
    "Function",
    "FunctionCall",
    "GenericType",
    "HasBlock",
    "HasName",
    "HasValue",
    "IfBlockStatement",
    "Import",
    "ImportStatement",
    "Importable",
    "JSXElement",
    "JSXExpression",
    "JSXProp",
    "List",
    "MessageType",
    "MultiExpression",
    "MultiLineCollection",
    "Name",
    "NamedType",
    "NoneType",
    "Number",
    "Pair",
    "Parameter",
    "ParenthesizedExpression",
    "Placeholder",
    "PlaceholderType",
    "PyAssignment",
    "PyAssignmentStatement",
    "PyAttribute",
    "PyBlockStatement",
    "PyBreakStatement",
    "PyCatchStatement",
    "PyChainedAttribute",
    "PyClass",
    "PyCodeBlock",
    "PyCodebaseType",
    "PyComment",
    "PyCommentGroup",
    "PyCommentType",
    "PyConditionalExpression",
    "PyDecorator",
    "PyFile",
    "PyForLoopStatement",
    "PyFunction",
    "PyGenericType",
    "PyHasBlock",
    "PyIfBlockStatement",
    "PyImport",
    "PyImportStatement",
    "PyMatchCase",
    "PyMatchStatement",
    "PyNamedType",
    "PyParameter",
    "PyPassStatement",
    "PyReturnTypePlaceholder",
    "PyString",
    "PySymbol",
    "PyTryCatchStatement",
    "PyUnionType",
    "PyWhileStatement",
    "RaiseStatement",
    "ReturnStatement",
    "SourceFile",
    "Span",
    "Statement",
    "StatementType",
    "String",
    "StubPlaceholder",
    "SubscriptExpression",
    "SwitchCase",
    "SwitchStatement",
    "Symbol",
    "SymbolGroup",
    "SymbolStatement",
    "TSArrayType",
    "TSAssignment",
    "TSAssignmentStatement",
    "TSAttribute",
    "TSBlockStatement",
    "TSCatchStatement",
    "TSChainedAttribute",
    "TSClass",
    "TSCodeBlock",
    "TSCodebaseType",
    "TSComment",
    "TSCommentGroup",
    "TSCommentType",
    "TSConditionalType",
    "TSConfig",
    "TSDecorator",
    "TSDict",
    "TSEnum",
    "TSExport",
    "TSExpressionType",
    "TSFile",
    "TSForLoopStatement",
    "TSFunction",
    "TSFunctionType",
    "TSGenericType",
    "TSHasBlock",
    "TSIfBlockStatement",
    "TSImport",
    "TSImportStatement",
    "TSInterface",
    "TSLabeledStatement",
    "TSLookupType",
    "TSNamedType",
    "TSNamespace",
    "TSObjectType",
    "TSPair",
    "TSParameter",
    "TSQueryType",
    "TSReadonlyType",
    "TSReturnTypePlaceholder",
    "TSString",
    "TSSwitchCase",
    "TSSwitchStatement",
    "TSSymbol",
    "TSTernaryExpression",
    "TSTryCatchStatement",
    "TSTypeAlias",
    "TSUndefinedType",
    "TSUnionType",
    "TSWhileStatement",
    "TernaryExpression",
    "TryCatchStatement",
    "Tuple",
    "TupleType",
    "Type",
    "TypeAlias",
    "TypePlaceholder",
    "Typeable",
    "UnaryExpression",
    "UnionType",
    "Unpack",
    "Unwrappable",
    "Usable",
    "Usage",
    "UsageKind",
    "UsageType",
    "Value",
    "WhileStatement",
    "WithStatement"
]