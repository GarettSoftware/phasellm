from unittest import TestCase

from phasellm.agents import CodeExecutionAgent, SandboxedCodeExecutionAgent, EmailSenderAgent, NewsSummaryAgent


class TestE2ECodeExecutionAgent(TestCase):

    def test_execute_code(self):
        pass


class TestE2ESandboxedCodeExecutionAgent(TestCase):

    def test_execute_code_stream_result(self):
        code = "print('Hello, world!')\nprint('Hello again')"

        expected = ['Hello, world!\n', 'Hello again\n']
        with SandboxedCodeExecutionAgent() as fixture:
            logs = fixture.execute_code(code)
            for i, log in enumerate(logs):
                actual = log.decode('utf-8')
                self.assertTrue(actual == expected[i], f"{actual} != {expected[i]}")

    def test_execute_code_concat_result(self):
        code = "print('0')\nprint('1')"

        with SandboxedCodeExecutionAgent() as fixture:
            logs = fixture.execute_code(code)
            actual = b''.join(logs).decode('utf-8')

        expected = '0\n1\n'
        self.assertTrue(actual == expected, f"{actual} != {expected}")

    def test_execute_code_external_package(self):
        pass


class TestE2EEmailSenderAgent(TestCase):

    def test_send_plain_email(self):
        pass

    def test_send_plain_email_deprecated(self):
        pass


class TestE2ENewsSummaryAgent(TestCase):

    def test_get_query(self):
        pass

    def test_get_query_deprecated(self):
        pass
