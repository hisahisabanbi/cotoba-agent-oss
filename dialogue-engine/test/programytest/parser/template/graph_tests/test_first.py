"""
Copyright (c) 2020 COTOBA DESIGN, Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import xml.etree.ElementTree as ET

from programy.parser.template.nodes.base import TemplateNode
from programy.parser.template.nodes.first import TemplateFirstNode
from programy.parser.template.nodes.word import TemplateWordNode
from programytest.parser.template.graph_tests.graph_test_client import TemplateGraphTestClient


class TemplateGraphFirstTests(TemplateGraphTestClient):

    def test_first(self):
        template = ET.fromstring("""
            <template>
                <first>one two three four</first>
            </template>
            """)
        ast = self._graph.parse_template_expression(template)
        self.assertIsNotNone(ast)
        self.assertIsInstance(ast, TemplateNode)
        self.assertEqual(1, len(ast.children))

        first_node = ast.children[0]
        self.assertIsNotNone(first_node)
        self.assertIsInstance(first_node, TemplateFirstNode)

        self.assertIsNotNone(first_node.children)
        self.assertEqual(1, len(first_node.children))
        self.assertIsInstance(first_node.children[0], TemplateWordNode)

        self.assertEqual(ast.resolve(self._client_context), "one")

    def test_first_one_word(self):
        template = ET.fromstring("""
            <template>
                <first>one</first>
            </template>
            """)
        ast = self._graph.parse_template_expression(template)

        self.assertEqual(ast.resolve(self._client_context), "one")

    def test_first_empty(self):
        template = ET.fromstring("""
            <template>
                <first></first>
            </template>
            """)
        ast = self._graph.parse_template_expression(template)

        self.assertEqual(ast.resolve(self._client_context), "unknown")
