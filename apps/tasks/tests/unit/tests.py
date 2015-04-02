import django.test

client = django.test.Client()

### Test cases
class TaskTestCase(django.test.TestCase):
  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_unicode(self):
    pass
