import pytest

from flask.testing import FlaskClient

from app.main.quasar_junior_flask_server import app
from configuration import TEST_FILES_DIR, TEST_EXTENSIONS

# Материал по работе с фикстурами взят из этих статей:
# https://ru.hexlet.io/courses/python-advanced-testing/lessons/files/theory_unit
# https://docs.pytest.org/en/7.1.x/how-to/tmp_path.html#the-tmp-path-fixture


@pytest.fixture()
def app_test():
    """ Create test app. """
    app.config.update({
        "TESTING": True,
        "UPLOAD_FOLDER": TEST_FILES_DIR
    })

    yield app


@pytest.fixture()
def client(app_test) -> FlaskClient:
    """ Create test client. """
    return app_test.test_client()


@pytest.fixture()
def runner(app_test):
    return app_test.test_cli_runner()


@pytest.fixture(scope='session', autouse=True)
def return_filename():
    """ Create test directory and test files. """
    if TEST_FILES_DIR.exists():
        for file in TEST_FILES_DIR.iterdir():
            file.unlink()
        TEST_FILES_DIR.rmdir()
    TEST_FILES_DIR.mkdir(exist_ok=True)
    for extension in TEST_EXTENSIONS:
        file_path = TEST_FILES_DIR.joinpath(f'Тест.{extension}')
        file_path.touch(exist_ok=True)
        with file_path.open('w', encoding='utf-8') as f:
            f.write(f'Тест.{extension}')
