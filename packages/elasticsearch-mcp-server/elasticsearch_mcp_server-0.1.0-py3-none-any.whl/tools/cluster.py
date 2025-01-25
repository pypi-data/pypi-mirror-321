from typing import Any
from mcp.types import TextContent
from .base import BaseTools

class ClusterTools(BaseTools):
    def register_tools(self, mcp: Any):
        """Register cluster-related tools."""
        
        @mcp.tool(description="Get cluster health status")
        async def get_cluster_health() -> list[TextContent]:
            """
            Get health status of the Elasticsearch cluster.
            Returns information about the number of nodes, shards, etc.
            """
            self.logger.info("Getting cluster health")
            try:
                response = self.es_client.cluster.health()
                return [TextContent(type="text", text=str(response))]
            except Exception as e:
                self.logger.error(f"Error getting cluster health: {e}")
                return [TextContent(type="text", text=f"Error: {str(e)}")]

        @mcp.tool(description="Get cluster statistics")
        async def get_cluster_stats() -> list[TextContent]:
            """
            Get statistics from a cluster wide perspective. 
            The API returns basic index metrics (shard numbers, store size, memory usage) and information 
            about the current nodes that form the cluster (number, roles, os, jvm versions, memory usage, cpu and installed plugins).
            https://www.elastic.co/guide/en/elasticsearch/reference/8.17/cluster-stats.html
            """
            self.logger.info("Getting cluster stats")
            try:
                response = self.es_client.cluster.stats()
                return [TextContent(type="text", text=str(response))]
            except Exception as e:
                self.logger.error(f"Error getting cluster stats: {e}")
                return [TextContent(type="text", text=f"Error: {str(e)}")]
