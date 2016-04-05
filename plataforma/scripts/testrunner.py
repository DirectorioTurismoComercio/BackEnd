import django.test.runner
from django_jenkins.runner import CITestSuiteRunner

class NoDbTestRunner(django.test.runner.DiscoverRunner):
  """ A test runner to test without database creation """

  def setup_databases(self, **kwargs):
    """ Override the database creation defined in parent class """
    pass

  def teardown_databases(self, old_config, **kwargs):
    """ Override the database teardown defined in parent class """
    pass


class NoopTestRunner(CITestSuiteRunner):
    """
    Dummy test runner to avoid django-jenkins to actually run tests.
    We just want static code quality analysis.
    """

   
    def setup_databases(self):
        return None, None

    def teardown_databases(self, old_config, **kwargs):
        return None, None
