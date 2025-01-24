import csv
import json
import uuid
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from typing import Callable, Dict, List, Optional

from pydantic import ValidationError

from swarms.structs.agent import Agent
from swarms.utils.loguru_logger import logger
from cachetools import LRUCache
from cachetools import cached

# Using cachetools for more control
agent_cache = LRUCache(maxsize=1000)


class AgentRegistry:
    """
    A class for managing a registry of agents with improved organization.

    Attributes:
        name (str): The name of the registry
        description (str): A description of the registry
        return_json (bool): Whether to return data in JSON format
        auto_save (bool): Whether to automatically save changes
        agent_store (Dict[str, Dict]): Main storage structure for agents with format:
            {
                "agent_id": {
                    "name": str,
                    "agent": Agent,
                    "metadata": Dict
                }
            }
    """

    def __init__(
        self,
        id: str = uuid.uuid4().hex,
        name: str = "Agent Registry",
        description: str = "A registry for managing agents.",
        return_json: bool = True,
        auto_save: bool = False,
        *args,
        **kwargs,
    ):
        self.id = id
        self.name = name
        self.description = description
        self.return_json = return_json
        self.auto_save = auto_save
        self.agent_store: Dict[str, Dict] = {}

    def _get_timestamp(self) -> str:
        """Get current UTC timestamp in ISO format."""
        return datetime.now(timezone.utc).isoformat()

    def _create_agent_entry(self, agent: Agent) -> Dict:
        """Creates a standardized agent entry dictionary."""
        timestamp = self._get_timestamp()
        return {
            "name": agent.agent_name,
            "agent": agent,
            "agent_dict": agent.to_dict(),
            "metadata": {
                "created_at": timestamp,
                "last_updated": timestamp,
                "status": "active",
            },
        }

    def add(self, agent: Agent) -> None:
        """
        Adds a new agent to the registry.

        Args:
            agent (Agent): The agent to add

        Raises:
            ValueError: If agent with same ID already exists
            ValidationError: If agent data is invalid
        """
        agent_id = agent.agent_name  # Using agent_name as ID for now

        if agent_id in self.agent_store:
            logger.error(f"Agent with ID {agent_id} already exists.")
            raise ValueError(
                f"Agent with ID {agent_id} already exists."
            )

        try:
            self.agent_store[agent_id] = self._create_agent_entry(
                agent
            )
            logger.info(f"Agent {agent_id} added successfully.")
        except ValidationError as e:
            logger.error(f"Validation error: {e}")
            raise

    def add_many(self, agents: List[Agent]) -> None:
        """
        Adds multiple agents to the registry concurrently.

        Args:
            agents (List[Agent]): List of agents to add

        Raises:
            ValueError: If any agent ID already exists
            ValidationError: If any agent data is invalid
        """
        with ThreadPoolExecutor() as executor:
            futures = {
                executor.submit(self.add, agent): agent
                for agent in agents
            }
            for future in as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    logger.error(f"Error adding agent: {e}")
                    raise

    def get(self, agent_id: str) -> Agent:
        """
        Retrieves an agent from the registry.

        Args:
            agent_id (str): ID of the agent to retrieve

        Returns:
            Agent: The requested agent

        Raises:
            KeyError: If agent_id doesn't exist
        """
        try:
            agent_entry = self.agent_store[agent_id]
            logger.info(f"Agent {agent_id} retrieved successfully.")
            return agent_entry["agent"]
        except KeyError:
            logger.error(f"Agent {agent_id} not found.")
            raise

    def update_agent(self, new_agent: Agent) -> None:
        """
        Updates an existing agent in the registry.

        Args:
            new_agent (Agent): Updated agent instance

        Raises:
            KeyError: If agent doesn't exist
            ValidationError: If new agent data is invalid
        """
        agent_id = new_agent.agent_name

        if agent_id not in self.agent_store:
            logger.error(f"Agent with ID {agent_id} does not exist.")
            raise KeyError(
                f"Agent with ID {agent_id} does not exist."
            )

        try:
            self.agent_store[agent_id]["agent"] = new_agent
            self.agent_store[agent_id]["name"] = new_agent.agent_name
            self.agent_store[agent_id][
                "agent_dict"
            ] = new_agent.to_dict()
            self.agent_store[agent_id]["metadata"][
                "last_updated"
            ] = self._get_timestamp()
            logger.info(f"Agent {agent_id} updated successfully.")

            self.clear_cache()
        except ValidationError as e:
            logger.error(f"Validation error: {e}")
            raise

    def delete(self, agent_id: str) -> None:
        """
        Deletes an agent from the registry.

        Args:
            agent_id (str): ID of the agent to delete

        Raises:
            KeyError: If agent_id doesn't exist
        """
        try:
            del self.agent_store[agent_id]
            logger.info(f"Agent {agent_id} deleted successfully.")
        except KeyError:
            logger.error(f"Agent {agent_id} not found.")
            raise

    def list_agents(self) -> List[str]:
        """
        Lists all agent IDs in the registry.

        Returns:
            List[str]: List of all agent IDs
        """
        try:
            agent_ids = list(self.agent_store.keys())
            logger.info("Listed all agents successfully.")
            return agent_ids
        except Exception as e:
            logger.error(f"Error listing agents: {e}")
            raise

    def return_all_agents(self) -> List[Agent]:
        """
        Returns all agent instances from the registry.

        Returns:
            List[Agent]: List of all agent instances
        """
        try:
            agents = [
                entry["agent"] for entry in self.agent_store.values()
            ]
            logger.info("Retrieved all agents successfully.")
            return agents
        except Exception as e:
            logger.error(f"Error retrieving agents: {e}")
            raise

    def clear_cache(self):
        """Clears the agent cache."""
        agent_cache.clear()
        logger.info("Agent cache cleared.")

    @cached(agent_cache)
    def query(
        self, condition: Optional[Callable[[Agent], bool]] = None
    ) -> List[Agent]:
        """
        Queries agents based on a condition, with caching.

        Args:
            condition (Optional[Callable[[Agent], bool]]): Function to filter agents.

        Returns:
            List[Agent]: List of agents meeting the condition.
        """
        try:
            if condition is None:
                return self.return_all_agents()

            agents = [
                entry["agent"]
                for entry in self.agent_store.values()
                if condition(entry["agent"])
            ]
            logger.info("Query executed successfully and cached.")
            return agents
        except Exception as e:
            logger.error(f"Error querying agents: {e}")
            raise

    @cached(agent_cache)
    def find_agent_by_name(self, agent_name: str) -> Optional[Agent]:
        """
        Finds an agent by its name, with caching.

        Args:
            agent_name (str): Name of the agent to find.

        Returns:
            Optional[Agent]: The found agent or None if not found.
        """
        try:
            for entry in self.agent_store.values():
                if entry["name"] == agent_name:
                    logger.info(
                        f"Agent {agent_name} retrieved from registry."
                    )
                    return entry["agent"]
            logger.warning(f"Agent {agent_name} not found.")
            return None
        except Exception as e:
            logger.error(f"Error finding agent: {e}")
            raise

    def _auto_save_export(self, file_name: str, content: str) -> None:
        """Automatically saves export metadata if auto_save is enabled."""
        if self.auto_save:
            logger.info(
                f"Auto-saving metadata for export: {file_name}"
            )
            metadata_file = f"{file_name}_metadata.json"
            metadata = {
                "exported_at": self._get_timestamp(),
                "file_name": file_name,
                "uuid": self._generate_uuid(),
                "content_summary": {
                    "agents_count": len(self.agent_store),
                },
            }
            with open(metadata_file, "w") as file:
                json.dump(metadata, file, indent=4)
            logger.info(f"Export metadata saved to {metadata_file}")

    def _generate_uuid(self):
        return uuid.uuid4().hex

    def return_agents_as_list(self) -> List[Agent]:
        """
        Returns all agents in the registry as a list.

        Returns:
            List[Agent]: A list of all Agent objects in the registry.
        """
        try:
            agents_list = [
                entry["metadata"]
                for entry in self.agent_store.values()
            ]
            logger.info(
                "Successfully retrieved all agents as a list."
            )
            return agents_list
        except Exception as e:
            logger.error(
                f"Error while returning agents as a list: {e}"
            )
            raise

    def export_to_json(self, file_name: Optional[str] = None) -> None:
        """
        Exports all agents to a JSON file.

        Args:
            file_name (Optional[str]): Name of the JSON file. Defaults to a UUID.
        """
        try:
            if not file_name:
                file_name = (
                    f"agents_export_{self._generate_uuid()}.json"
                )

            data = {
                agent_id: entry["agent_dict"]
                for agent_id, entry in self.agent_store.items()
            }
            with open(file_name, "w") as file:
                json.dump(data, file, indent=4)

            logger.info(f"Exported agents to JSON: {file_name}")
            self._auto_save_export(file_name, data)
        except Exception as e:
            logger.error(f"Error exporting to JSON: {e}")
            raise

    def export_to_csv(self, file_name: Optional[str] = None) -> None:
        """
        Exports all agents to a CSV file.

        Args:
            file_name (Optional[str]): Name of the CSV file. Defaults to a UUID.
        """
        try:
            if not file_name:
                file_name = (
                    f"agents_export_{self._generate_uuid()}.csv"
                )

            with open(file_name, "w", newline="") as csvfile:
                fieldnames = [
                    "agent_id",
                    "name",
                    "created_at",
                    "last_updated",
                    "status",
                ]
                writer = csv.DictWriter(
                    csvfile, fieldnames=fieldnames
                )

                writer.writeheader()
                for agent_id, entry in self.agent_store.items():
                    writer.writerow(
                        {
                            "agent_id": agent_id,
                            "name": entry["name"],
                            "created_at": entry["metadata"][
                                "created_at"
                            ],
                            "last_updated": entry["metadata"][
                                "last_updated"
                            ],
                            "status": entry["metadata"]["status"],
                        }
                    )

            logger.info(f"Exported agents to CSV: {file_name}")
            self._auto_save_export(file_name, "CSV")
        except Exception as e:
            logger.error(f"Error exporting to CSV: {e}")
            raise
