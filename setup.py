from distutils.core import setup
setup(
  name = 'hurricane-factory',
  packages = ['hurricane-factory'], # this must be the same as the name above
  version = '0.1',
  description = 'Manage CloudFormation at Massive Scale',
  author = 'Jared Short',
  author_email = 'jaredlshort@gmail.com',
  url = 'https://github.com/trek10inc/hurricane-factory', # use the URL to the github repo
  download_url = 'https://github.com/trek10inc/hurricane-factory/archive/0.1.tar.gz', # I'll explain this in a second
  keywords = ['aws', 'cloudformation', 'management', 'orchestration'], # arbitrary keywords
  classifiers = [],
)