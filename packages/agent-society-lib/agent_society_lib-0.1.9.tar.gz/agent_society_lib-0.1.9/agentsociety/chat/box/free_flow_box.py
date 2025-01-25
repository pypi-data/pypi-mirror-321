from typing import Dict, Optional, Tuple, List
from dataclasses import dataclass
from enum import Enum

from agentsociety.chat.history import History, HistoryContent, HistoryDelta, HistoryArtifact, Actor, ContentType


@dataclass
class BoxResultMeta:
    new_annotations: Dict[str, str]
    new_artifacts: Dict[str, str]


@dataclass
class BoxMeta:
    unique_name: str
    aliases: List[str]


@dataclass
class ArtifactNames:
    success_artifact: str
    failure_artifact: str
    initial_artifact: str


class FreeFlowBox:
    
    def __init__(self, box_name: str) -> None:
        self.box_name: str = box_name
    
    def get_box_meta(self) -> BoxMeta:
        """
        Method to retrieve the box meta
        """
        pass
    
    def check_completion(self, history: History) -> Tuple[bool, Optional[BoxResultMeta]]:
        """
        Check the completion, possibly return some data
        """
        pass
    
    def check_failure(self, history: History) -> Tuple[bool, Optional[BoxResultMeta]]:
        """
        Check for failure, possibly return some data
        """
        pass
    
    def check_user_input(self, history: History) -> bool:
        """
        Checks if we need user input
        """
        pass
    
    def generate(self, history: History) -> HistoryContent:
        """
        Generate some content
        """
        pass

    def on_completion(self, history: History, box_meta: BoxResultMeta) -> HistoryContent:
        """
        What to generate upon completion
        """
        pass
    
    def on_failure(self, history: History, box_meta: BoxResultMeta) -> HistoryContent:
        """
        what to generate upon failure
        """
        pass
    
    def generate_system_prompt(self, history: History) -> HistoryContent:
        """
        Method to create the system prompt
        """
        pass
    
    def _prepare_system_content(self, content: str, annotations: Dict[str, str] = {}, artifacts: List[HistoryArtifact] = None) -> HistoryContent:
        return HistoryContent(
            content, Actor.SYSTEM, ContentType.UNDEFINED, annotations={**annotations, 'BOX_NAME': self.box_name}, artifacts=artifacts
        )
    
    def _last_msg_same_box(self, history: History) -> bool:
        last_msg = history.get_latest_non_user_message()
        if last_msg is None:
            return False
        return last_msg.annotations.get('BOX_NAME', 'NONE') == self.box_name
    
    def _is_agent_instruction_present(self, history: History) -> bool:
        artifact_names = self.get_artifact_names()
        instruction_flag = history.get_artifact_content(artifact_names.initial_artifact, 'false')
        
        return instruction_flag == 'true'

    def get_artifact_names(self) -> ArtifactNames:
        return ArtifactNames(
            f"{self.box_name}_COMPLETED",
            f"{self.box_name}_FAILED",
            f"{self.box_name}_INITIALIZED"
        )
    
    def _get_initialization_artifacts(self) -> List[HistoryArtifact]:
        artifact_names = self.get_artifact_names()
        return [
            HistoryArtifact(artifact_names.success_artifact, 'false'),
            HistoryArtifact(artifact_names.failure_artifact, 'false'),
            HistoryArtifact(artifact_names.initial_artifact, 'true')
        ]
    
    def _get_initialization_reset_artifact(self) -> HistoryArtifact:
        artifact_names = self.get_artifact_names()
    
        return HistoryArtifact(
            artifact_names.initial_artifact, 'false'
        )
    
    def init(self, history: History) -> HistoryContent:
        system_prompt = self.generate_system_prompt(history)
        reset_artifacts = self._get_initialization_artifacts()
        for ra in reset_artifacts:
            system_prompt.add_artifact(ra)
        return system_prompt
    
    def custom_processing_step(self, history: History) -> Tuple[bool, Optional[HistoryContent]]:
        return False, None

    def _generate_completion(self, history: History, complete_meta: BoxMeta) -> HistoryContent:
        completion_msg = self.on_completion(history, complete_meta)
        
        artifacts = self.get_artifact_names()
        
        completion_msg.add_artifact(
            HistoryArtifact(artifacts.success_artifact, "true")
        )
        
        completion_msg.add_artifact(
            self._get_initialization_reset_artifact()
        )
        
        return completion_msg

    def _generate_failure(self, history: History, failure_meta: BoxMeta) -> HistoryContent:
        failure_msg = self.on_failure(history, failure_meta)
        
        artifacts = self.get_artifact_names()
        
        failure_msg.add_artifact(
            HistoryContent(artifacts.failure_artifact, "true")
        )
        
        failure_msg.add_artifact(
            self._get_initialization_reset_artifact()
        )
        
        return failure_msg

    def step(self, history: History) -> Optional[HistoryContent]:
        if not self._is_agent_instruction_present(history):
            new_msg = self.init(history)
        else:
            complete, complete_meta = self.check_completion(history)
            if complete:
                print("LLM figured that this step was successful")
                return self._generate_completion(history, complete_meta)
            
            failed, failed_meta = self.check_failure(history)
            if failed:
                return self._generate_failure(history, failed_meta)

            has_msg, msg = self.custom_processing_step(history)

            if has_msg:
                new_msg = msg
            else:
                new_msg = self.generate(history)

        fake_history = history.clone()
        fake_history.add_content(new_msg)
        
        user_input_required = self.check_user_input(fake_history)
        
        if user_input_required:
            new_msg.user_input_required = True
            return new_msg
        return new_msg

