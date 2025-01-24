from launch.env import get_bool_env_var, override_default

BUILD_DEPENDENCIES_PATH = override_default(
    key_name="BUILD_DEPENDENCIES_PATH",
    default=".launch",
)

BUILD_TEMP_DIR_PATH = override_default(
    key_name="BUILD_TEMP_DIR_PATH",
    default=f"{BUILD_DEPENDENCIES_PATH}/build",
)

DEFAULT_CLOUD_PROVIDER = override_default(
    key_name="DEFAULT_CLOUD_PROVIDER",
    default="aws",
)

DOCKER_FILE_DIR = override_default(
    key_name="DOCKER_FILE_DIR",
    default="source",
)

DOCKER_FILE_NAME = override_default(
    key_name="DOCKER_FILE_NAME",
    default="Dockerfile",
)

IS_PIPELINE = get_bool_env_var(env_var_name="IS_PIPELINE", default_value=False)

PLATFORM_SRC_DIR_PATH = override_default(
    key_name="PLATFORM_SRC_DIR_PATH",
    default="platform",
)

SECRET_J2_TEMPLATE_NAME = override_default(
    key_name="SECRET_J2_TEMPLATE_NAME",
    default="secret.yaml",
)

TOOL_VERSION_FILE = override_default(
    key_name="TOOL_VERSION_FILE",
    default=".tool-versions",
)

NON_SECRET_J2_TEMPLATE_NAME = override_default(
    key_name="NON_SECRET_J2_TEMPLATE_NAME",
    default="non_secret.yaml",
)
