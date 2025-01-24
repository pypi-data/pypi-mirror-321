#!/usr/bin/env python3

import yaml

from provisioner_shared.components.remote.domain.config import RemoteConfig, RunEnvironment
from provisioner_shared.components.remote.remote_opts import CliRemoteOpts
from provisioner_shared.components.runtime.infra.remote_context import RemoteContext

TEST_DATA_ENVIRONMENT: RunEnvironment = RunEnvironment.Local
TEST_DATA_SSH_HOSTNAME_1 = "test-hostname-1"
TEST_DATA_SSH_HOSTNAME_2 = "test-hostname-2"
TEST_DATA_SSH_IP_ADDRESS_1 = "test-ip-address-1"
TEST_DATA_SSH_IP_ADDRESS_2 = "test-ip-address-2"
TEST_DATA_REMOTE_NODE_USERNAME_1 = "test-user-1"
TEST_DATA_REMOTE_NODE_USERNAME_2 = "test-user-2"
TEST_DATA_REMOTE_NODE_PASSWORD_1 = "test-pass-1"
TEST_DATA_REMOTE_NODE_PASSWORD_2 = "test-pass-2"
TEST_DATA_REMOTE_SSH_PRIVATE_KEY_FILE_PATH_1 = "test-ssh-private-key-1"
TEST_DATA_REMOTE_SSH_PRIVATE_KEY_FILE_PATH_2 = "test-ssh-private-key-2"
TEST_DATA_REMOTE_IP_DISCOVERY_RANGE = "1.1.1.1/32"

# TEST_REMOTE_HOSTS_DICT = {
#     TEST_DATA_SSH_HOSTNAME_1: {
#         'name': TEST_DATA_SSH_HOSTNAME_1,
#         'address': TEST_DATA_SSH_IP_ADDRESS_1,
#         'auth': {
#             'username': TEST_DATA_REMOTE_NODE_USERNAME_1,
#             # Mutually exclusive with ssh_private_key_file_path
#             'password': TEST_DATA_REMOTE_NODE_PASSWORD_1,
#         },
#     },
#     TEST_DATA_SSH_HOSTNAME_2: {
#         'name': TEST_DATA_SSH_HOSTNAME_2,
#         'address': TEST_DATA_SSH_IP_ADDRESS_2,
#         'auth': {
#             'username': TEST_DATA_REMOTE_NODE_USERNAME_2,
#             # Mutually exclusive with node_password
#             'ssh_private_key_file_path': TEST_DATA_REMOTE_SSH_PRIVATE_KEY_FILE_PATH_2,
#         },
#     },
# }

TEST_REMOTE_CFG_YAML_TEXT = f"""
remote:
  hosts:
    - name: {TEST_DATA_SSH_HOSTNAME_1}
      address: {TEST_DATA_SSH_IP_ADDRESS_1}
      auth:
        username: {TEST_DATA_REMOTE_NODE_USERNAME_1}
        password: {TEST_DATA_REMOTE_NODE_PASSWORD_1}

    - name: {TEST_DATA_SSH_HOSTNAME_2}
      address: {TEST_DATA_SSH_IP_ADDRESS_2}
      auth:
        username: {TEST_DATA_REMOTE_NODE_USERNAME_2}
        ssh_private_key_file_path: {TEST_DATA_REMOTE_SSH_PRIVATE_KEY_FILE_PATH_2}

  lan_scan:
    ip_discovery_range: {TEST_DATA_REMOTE_IP_DISCOVERY_RANGE}
"""


class TestDataRemoteOpts:
    @staticmethod
    def create_fake_remote_cfg() -> RemoteConfig:
        cfg_dict = yaml.safe_load(TEST_REMOTE_CFG_YAML_TEXT)
        return RemoteConfig(cfg_dict["remote"])

    @staticmethod
    def create_fake_cli_remote_opts(
        remote_context: RemoteContext = None,
        environment: RunEnvironment = TEST_DATA_ENVIRONMENT,
    ) -> CliRemoteOpts:
        return CliRemoteOpts(
            environment=environment,
            node_username=TEST_DATA_REMOTE_NODE_USERNAME_1,
            node_password=TEST_DATA_REMOTE_NODE_PASSWORD_1,
            ssh_private_key_file_path=TEST_DATA_REMOTE_SSH_PRIVATE_KEY_FILE_PATH_1,
            ip_discovery_range=TEST_DATA_REMOTE_IP_DISCOVERY_RANGE,
            remote_hosts=TestDataRemoteOpts.create_fake_remote_cfg().to_hosts_dict(),
            remote_context=remote_context,
        )
