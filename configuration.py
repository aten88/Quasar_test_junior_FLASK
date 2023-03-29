from pathlib import Path

GET_URL = '/files/get'
TEST_EXTENSIONS = 'txt', 'csv', 'json', 'xlsx', 'jpg', 'png'
WRONG_TEST_EXTENSIONS = 'bin', 'doc', 'pic', 'exe', 'zip', 'rar'
BASE_DIR = Path(__file__).parent
TEST_FILES_DIR = BASE_DIR.joinpath('TEST_Storage')
