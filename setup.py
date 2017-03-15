from distutils.core import setup

setup(
    name='gitDICE',
    version='0.2.2',
    packages=['src', 'src.misc', 'src.misc.fab', 'src.envDICE.lib.python2.7.distutils',
              'src.envDICE.lib.python2.7.encodings', 'src.envDICE.lib.python2.7.site-packages.pip',
              'src.envDICE.lib.python2.7.site-packages.pip.vcs', 'src.envDICE.lib.python2.7.site-packages.pip._vendor',
              'src.envDICE.lib.python2.7.site-packages.pip._vendor.distlib',
              'src.envDICE.lib.python2.7.site-packages.pip._vendor.distlib._backport',
              'src.envDICE.lib.python2.7.site-packages.pip._vendor.colorama',
              'src.envDICE.lib.python2.7.site-packages.pip._vendor.html5lib',
              'src.envDICE.lib.python2.7.site-packages.pip._vendor.html5lib.trie',
              'src.envDICE.lib.python2.7.site-packages.pip._vendor.html5lib.filters',
              'src.envDICE.lib.python2.7.site-packages.pip._vendor.html5lib.serializer',
              'src.envDICE.lib.python2.7.site-packages.pip._vendor.html5lib.treewalkers',
              'src.envDICE.lib.python2.7.site-packages.pip._vendor.html5lib.treeadapters',
              'src.envDICE.lib.python2.7.site-packages.pip._vendor.html5lib.treebuilders',
              'src.envDICE.lib.python2.7.site-packages.pip._vendor.requests',
              'src.envDICE.lib.python2.7.site-packages.pip._vendor.requests.packages',
              'src.envDICE.lib.python2.7.site-packages.pip._vendor.requests.packages.chardet',
              'src.envDICE.lib.python2.7.site-packages.pip._vendor.requests.packages.urllib3',
              'src.envDICE.lib.python2.7.site-packages.pip._vendor.requests.packages.urllib3.util',
              'src.envDICE.lib.python2.7.site-packages.pip._vendor.requests.packages.urllib3.contrib',
              'src.envDICE.lib.python2.7.site-packages.pip._vendor.requests.packages.urllib3.packages',
              'src.envDICE.lib.python2.7.site-packages.pip._vendor.requests.packages.urllib3.packages.ssl_match_hostname',
              'src.envDICE.lib.python2.7.site-packages.pip._vendor._markerlib',
              'src.envDICE.lib.python2.7.site-packages.pip.commands',
              'src.envDICE.lib.python2.7.site-packages.pip.backwardcompat',
              'src.envDICE.lib.python2.7.site-packages.mako', 'src.envDICE.lib.python2.7.site-packages.mako.ext',
              'src.envDICE.lib.python2.7.site-packages.ecdsa', 'src.envDICE.lib.python2.7.site-packages.flask',
              'src.envDICE.lib.python2.7.site-packages.flask.ext',
              'src.envDICE.lib.python2.7.site-packages.flask.testsuite',
              'src.envDICE.lib.python2.7.site-packages.flask.testsuite.test_apps.lib.python2.5.site-packages.site_package',
              'src.envDICE.lib.python2.7.site-packages.flask.testsuite.test_apps.path.installed_package',
              'src.envDICE.lib.python2.7.site-packages.flask.testsuite.test_apps.flaskext',
              'src.envDICE.lib.python2.7.site-packages.flask.testsuite.test_apps.flaskext.oldext_package',
              'src.envDICE.lib.python2.7.site-packages.flask.testsuite.test_apps.moduleapp',
              'src.envDICE.lib.python2.7.site-packages.flask.testsuite.test_apps.moduleapp.apps',
              'src.envDICE.lib.python2.7.site-packages.flask.testsuite.test_apps.moduleapp.apps.admin',
              'src.envDICE.lib.python2.7.site-packages.flask.testsuite.test_apps.moduleapp.apps.frontend',
              'src.envDICE.lib.python2.7.site-packages.flask.testsuite.test_apps.blueprintapp',
              'src.envDICE.lib.python2.7.site-packages.flask.testsuite.test_apps.blueprintapp.apps',
              'src.envDICE.lib.python2.7.site-packages.flask.testsuite.test_apps.blueprintapp.apps.admin',
              'src.envDICE.lib.python2.7.site-packages.flask.testsuite.test_apps.blueprintapp.apps.frontend',
              'src.envDICE.lib.python2.7.site-packages.flask.testsuite.test_apps.flask_broken',
              'src.envDICE.lib.python2.7.site-packages.flask.testsuite.test_apps.config_package_app',
              'src.envDICE.lib.python2.7.site-packages.flask.testsuite.test_apps.subdomaintestmodule',
              'src.envDICE.lib.python2.7.site-packages.flask.testsuite.test_apps.flask_newext_package',
              'src.envDICE.lib.python2.7.site-packages.cm_api',
              'src.envDICE.lib.python2.7.site-packages.cm_api.endpoints',
              'src.envDICE.lib.python2.7.site-packages.Crypto', 'src.envDICE.lib.python2.7.site-packages.Crypto.Hash',
              'src.envDICE.lib.python2.7.site-packages.Crypto.Util',
              'src.envDICE.lib.python2.7.site-packages.Crypto.Cipher',
              'src.envDICE.lib.python2.7.site-packages.Crypto.Random',
              'src.envDICE.lib.python2.7.site-packages.Crypto.Random.OSRNG',
              'src.envDICE.lib.python2.7.site-packages.Crypto.Random.Fortuna',
              'src.envDICE.lib.python2.7.site-packages.Crypto.Protocol',
              'src.envDICE.lib.python2.7.site-packages.Crypto.SelfTest',
              'src.envDICE.lib.python2.7.site-packages.Crypto.SelfTest.Hash',
              'src.envDICE.lib.python2.7.site-packages.Crypto.SelfTest.Util',
              'src.envDICE.lib.python2.7.site-packages.Crypto.SelfTest.Cipher',
              'src.envDICE.lib.python2.7.site-packages.Crypto.SelfTest.Random',
              'src.envDICE.lib.python2.7.site-packages.Crypto.SelfTest.Random.OSRNG',
              'src.envDICE.lib.python2.7.site-packages.Crypto.SelfTest.Random.Fortuna',
              'src.envDICE.lib.python2.7.site-packages.Crypto.SelfTest.Protocol',
              'src.envDICE.lib.python2.7.site-packages.Crypto.SelfTest.PublicKey',
              'src.envDICE.lib.python2.7.site-packages.Crypto.SelfTest.Signature',
              'src.envDICE.lib.python2.7.site-packages.Crypto.PublicKey',
              'src.envDICE.lib.python2.7.site-packages.Crypto.Signature',
              'src.envDICE.lib.python2.7.site-packages.fabric',
              'src.envDICE.lib.python2.7.site-packages.fabric.contrib',
              'src.envDICE.lib.python2.7.site-packages.jinja2',
              'src.envDICE.lib.python2.7.site-packages.jinja2.testsuite',
              'src.envDICE.lib.python2.7.site-packages.jinja2.testsuite.res',
              'src.envDICE.lib.python2.7.site-packages.alembic', 'src.envDICE.lib.python2.7.site-packages.alembic.ddl',
              'src.envDICE.lib.python2.7.site-packages.alembic.autogenerate',
              'src.envDICE.lib.python2.7.site-packages.fabfile', 'src.envDICE.lib.python2.7.site-packages.wtforms',
              'src.envDICE.lib.python2.7.site-packages.wtforms.ext',
              'src.envDICE.lib.python2.7.site-packages.wtforms.ext.csrf',
              'src.envDICE.lib.python2.7.site-packages.wtforms.ext.i18n',
              'src.envDICE.lib.python2.7.site-packages.wtforms.ext.django',
              'src.envDICE.lib.python2.7.site-packages.wtforms.ext.django.templatetags',
              'src.envDICE.lib.python2.7.site-packages.wtforms.ext.dateutil',
              'src.envDICE.lib.python2.7.site-packages.wtforms.ext.appengine',
              'src.envDICE.lib.python2.7.site-packages.wtforms.ext.sqlalchemy',
              'src.envDICE.lib.python2.7.site-packages.wtforms.csrf',
              'src.envDICE.lib.python2.7.site-packages.wtforms.fields',
              'src.envDICE.lib.python2.7.site-packages.wtforms.widgets',
              'src.envDICE.lib.python2.7.site-packages.cm_shell', 'src.envDICE.lib.python2.7.site-packages.paramiko',
              'src.envDICE.lib.python2.7.site-packages.werkzeug',
              'src.envDICE.lib.python2.7.site-packages.werkzeug.debug',
              'src.envDICE.lib.python2.7.site-packages.werkzeug.contrib',
              'src.envDICE.lib.python2.7.site-packages.werkzeug.testsuite',
              'src.envDICE.lib.python2.7.site-packages.werkzeug.testsuite.contrib',
              'src.envDICE.lib.python2.7.site-packages.flask_wtf',
              'src.envDICE.lib.python2.7.site-packages.flask_wtf.recaptcha',
              'src.envDICE.lib.python2.7.site-packages._markerlib',
              'src.envDICE.lib.python2.7.site-packages.markupsafe',
              'src.envDICE.lib.python2.7.site-packages.setuptools',
              'src.envDICE.lib.python2.7.site-packages.setuptools.tests',
              'src.envDICE.lib.python2.7.site-packages.setuptools.command',
              'src.envDICE.lib.python2.7.site-packages.sqlalchemy',
              'src.envDICE.lib.python2.7.site-packages.sqlalchemy.ext',
              'src.envDICE.lib.python2.7.site-packages.sqlalchemy.ext.declarative',
              'src.envDICE.lib.python2.7.site-packages.sqlalchemy.orm',
              'src.envDICE.lib.python2.7.site-packages.sqlalchemy.sql',
              'src.envDICE.lib.python2.7.site-packages.sqlalchemy.util',
              'src.envDICE.lib.python2.7.site-packages.sqlalchemy.event',
              'src.envDICE.lib.python2.7.site-packages.sqlalchemy.engine',
              'src.envDICE.lib.python2.7.site-packages.sqlalchemy.testing',
              'src.envDICE.lib.python2.7.site-packages.sqlalchemy.testing.suite',
              'src.envDICE.lib.python2.7.site-packages.sqlalchemy.testing.plugin',
              'src.envDICE.lib.python2.7.site-packages.sqlalchemy.dialects',
              'src.envDICE.lib.python2.7.site-packages.sqlalchemy.dialects.mssql',
              'src.envDICE.lib.python2.7.site-packages.sqlalchemy.dialects.mysql',
              'src.envDICE.lib.python2.7.site-packages.sqlalchemy.dialects.oracle',
              'src.envDICE.lib.python2.7.site-packages.sqlalchemy.dialects.sqlite',
              'src.envDICE.lib.python2.7.site-packages.sqlalchemy.dialects.sybase',
              'src.envDICE.lib.python2.7.site-packages.sqlalchemy.dialects.drizzle',
              'src.envDICE.lib.python2.7.site-packages.sqlalchemy.dialects.firebird',
              'src.envDICE.lib.python2.7.site-packages.sqlalchemy.dialects.postgresql',
              'src.envDICE.lib.python2.7.site-packages.sqlalchemy.databases',
              'src.envDICE.lib.python2.7.site-packages.sqlalchemy.connectors',
              'src.envDICE.lib.python2.7.site-packages.flask_script',
              'src.envDICE.lib.python2.7.site-packages.flask_migrate',
              'src.envDICE.lib.python2.7.site-packages.flask_bootstrap',
              'src.envDICE.lib.python2.7.site-packages.flask_sqlalchemy', 'dice-experiments.spark',
              'dice-experiments.dmonES', 'dice-experiments.dmonCmf', 'dice-experiments.preprocessing'],
    url='https://github.com/dice-project/DICE-Monitoring',
    license='Apache 2.0',
    author='Gabriel Iuhasz',
    author_email='iuhasz.gabriel@e-uvt.ro',
    description='DICE Monitoring Platform'
)