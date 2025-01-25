# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at

#   http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from functools import wraps

from dkg.assertion import Assertion
from dkg.asset import KnowledgeAsset
from dkg.graph import Graph
from dkg.manager import DefaultRequestManager
from dkg.module import Module
from dkg.network import Network
from dkg.node import Node
from dkg.paranet import Paranet
from dkg.providers import BlockchainProvider, NodeHTTPProvider
from dkg.types import UAL, Address, ChecksumAddress
from dkg.utils.ual import format_ual, parse_ual
from dkg.services.input_service import InputService
from dkg.services.node_service import NodeService


class DKG(Module):
    assertion: Assertion
    asset: KnowledgeAsset
    paranet: Paranet
    network: Network
    node: Node
    graph: Graph

    @staticmethod
    @wraps(format_ual)
    def format_ual(
        blockchain: str, contract_address: Address | ChecksumAddress, token_id: int
    ) -> UAL:
        return format_ual(blockchain, contract_address, token_id)

    @staticmethod
    @wraps(parse_ual)
    def parse_ual(ual: UAL) -> dict[str, str | Address | int]:
        return parse_ual(ual)

    def __init__(
        self,
        node_provider: NodeHTTPProvider,
        blockchain_provider: BlockchainProvider,
        config: dict = {},
    ):
        self.manager = DefaultRequestManager(node_provider, blockchain_provider)

        self.initialize_services(self.manager, config)

        modules = {
            "assertion": Assertion(self.manager),
            "asset": KnowledgeAsset(
                self.manager, self.input_service, self.node_service
            ),
            "paranet": Paranet(self.manager),
            "network": Network(self.manager),
            "node": Node(self.manager),
            "graph": Graph(self.manager, self.input_service, self.node_service),
        }
        self._attach_modules(modules)

        # Backwards compatibility
        self.graph.get = self.asset.get.__get__(self.asset)
        self.graph.create = self.asset.create.__get__(self.asset)

    def initialize_services(self, manager, config):
        self.input_service = InputService(manager, config)
        self.node_service = NodeService(manager)

    @property
    def node_provider(self) -> NodeHTTPProvider:
        return self.manager.node_provider

    @node_provider.setter
    def node_provider(self, node_provider: NodeHTTPProvider) -> None:
        self.manager.node_provider = node_provider

    @property
    def blockchain_provider(self) -> BlockchainProvider:
        return self.manager.blockchain_provider

    @blockchain_provider.setter
    def blockchain_provider(self, blockchain_provider: BlockchainProvider) -> None:
        self.manager.blockchain_provider = blockchain_provider
