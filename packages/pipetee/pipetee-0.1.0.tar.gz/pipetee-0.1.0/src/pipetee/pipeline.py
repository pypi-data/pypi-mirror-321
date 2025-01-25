"""
Core pipeline components for building data processing pipelines.
"""

import asyncio
import json
import logging
from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path
from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar, Union

from pipetee.models.checkpoint import PipelineCheckpoint
from pipetee.models.stage import InputType, OutputType, StageDecision, StageResult
from pipetee.models.visual import StageVizInfo
from pipetee.utils.logging_config import setup_logger


class DateTimeEncoder(json.JSONEncoder):
    """Custom JSON encoder for datetime objects."""

    def default(self, obj: Any) -> Any:
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)


# Type definitions
ProcessorType = TypeVar("ProcessorType")
ConditionFunc = Callable[[Any], Union[bool, asyncio.Future[bool]]]
ProcessorFunc = Callable[
    [ProcessorType], Union[ProcessorType, asyncio.Future[ProcessorType]]
]


class PipelineVisualizer:
    """Handles pipeline visualization"""

    def __init__(self, pipeline: "Pipeline") -> None:
        self.pipeline = pipeline
        self.viz_data: Dict[str, StageVizInfo] = {}
        self._status_icons = {
            "pending": "🔄",
            "running": "⚡",
            "completed": "✅",
            "skipped": "⏭️",
            "failed": "❌",
        }

    def update_stage_status(self, stage_name: str, status: str, **kwargs: Any) -> None:
        """Update status and info for a stage"""
        if stage_name not in self.pipeline.stages:
            raise ValueError(f"Invalid stage name: {stage_name}")

        if stage_name not in self.viz_data:
            self.viz_data[stage_name] = StageVizInfo(
                name=stage_name,
                status=status,
                error=None,
                metrics=None,
                start_time=kwargs.get("start_time"),
                end_time=kwargs.get("end_time"),
            )

        stage_info = self.viz_data[stage_name]
        stage_info.status = status

        for key, value in kwargs.items():
            setattr(stage_info, key, value)

    def reset(self) -> None:
        """Clear visualization data"""
        self.viz_data.clear()

    def generate_mermaid_diagram(self) -> str:
        """Generate Mermaid.js diagram showing pipeline structure and status"""
        diagram = ["graph LR"]

        # Add nodes with escaped names and labels
        for stage_name, stage_info in self.viz_data.items():
            safe_name = self._escape_mermaid_string(stage_name)
            icon = self._status_icons.get(stage_info.status, "")
            # Include both stage name and status in the node label
            diagram.append(
                f'    {safe_name}["{icon} {stage_name} ({stage_info.status})"]'
            )

        # Add connections
        for i in range(len(self.pipeline.default_sequence) - 1):
            current = self._escape_mermaid_string(self.pipeline.default_sequence[i])
            next_stage = self._escape_mermaid_string(
                self.pipeline.default_sequence[i + 1]
            )
            diagram.append(f"    {current} --> {next_stage}")

        # Add branch connections
        for stage_name, stage in self.pipeline.stages.items():
            safe_name = self._escape_mermaid_string(stage_name)
            for condition, target in stage.branch_conditions.items():
                safe_target = self._escape_mermaid_string(target)
                safe_condition = self._escape_mermaid_string(condition.name)
                diagram.append(f"    {safe_name} -->|{safe_condition}| {safe_target}")

        return "\n".join(diagram)

    def generate_execution_timeline(self) -> str:
        """Generate Mermaid.js timeline diagram of execution"""
        diagram = [
            "gantt",
            "    dateFormat  HH:mm:ss",
            "    axisFormat  %H:%M:%S",
            "    title Pipeline Execution Timeline",
        ]

        for stage_name, stage_info in self.viz_data.items():
            if not (stage_info.start_time and stage_info.end_time):
                continue

            status_icon = self._status_icons.get(stage_info.status, "🔄")
            safe_name = self._escape_mermaid_string(stage_name)

            try:
                diagram.append(f"    section {safe_name}")
                diagram.append(
                    f"    {status_icon} {safe_name} : "
                    f"{stage_info.start_time.strftime('%H:%M:%S')}, "
                    f"{stage_info.end_time.strftime('%H:%M:%S')}"
                )
            except AttributeError:
                continue  # Skip if datetime formatting fails

        return "\n".join(diagram)

    @staticmethod
    def _escape_mermaid_string(text: str) -> str:
        """Escape special characters for Mermaid.js"""
        return text.replace(" ", "_").replace("-", "_")


class Condition:
    """Class for defining pipeline conditions with async support"""

    def __init__(self, name: str, condition_func: ConditionFunc):
        self.name = name
        self.condition_func = condition_func

    async def evaluate(self, data: Any) -> bool:
        """Evaluate condition with async support"""
        result = self.condition_func(data)
        if asyncio.iscoroutine(result):
            return await result
        return bool(result)


class PipelineStage(ABC, Generic[InputType, OutputType]):
    """Enhanced pipeline stage with conditions and async support"""

    def __init__(self, log_level: int = logging.INFO):
        self.skip_conditions: List[Condition] = []
        self.branch_conditions: Dict[Condition, str] = {}
        self.post_processors: List[ProcessorFunc[OutputType]] = []
        self.logger = setup_logger(
            logger_name=self.__class__.__name__, log_level=log_level
        )
        self.logger.info("Initializing %s", self.__class__.__name__)

    def add_skip_condition(
        self, condition: Condition
    ) -> "PipelineStage[InputType, OutputType]":
        """Add condition that determines if stage should be skipped"""
        self.logger.info("Adding skip condition: %s", condition.name)
        self.skip_conditions.append(condition)
        return self

    def add_branch_condition(
        self, condition: Condition, next_stage: str
    ) -> "PipelineStage[InputType, OutputType]":
        """Add condition that determines branching"""
        self.logger.info(
            "Adding branch condition: %s -> %s", condition.name, next_stage
        )
        self.branch_conditions[condition] = next_stage
        return self

    def add_post_processor(
        self, processor: ProcessorFunc[OutputType]
    ) -> "PipelineStage[InputType, OutputType]":
        """Add post-processing function with async support"""
        self.logger.info(
            "Adding post-processor: %s", getattr(processor, "__name__", str(processor))
        )
        self.post_processors.append(processor)
        return self

    @abstractmethod
    async def process(self, data: InputType) -> StageResult[OutputType]:
        """
        Process the input data with async support.
        Implementation should include appropriate logging.
        Example:
            self.logger.info("Starting processing")
            try:
                # ... processing logic ...
                self.logger.debug("Processing details: %s", details)
                return StageResult(success=True, data=result)
            except Exception as e:
                self.logger.error("Processing failed", exc_info=True)
                return StageResult(success=False, data=None, error=str(e))
        """
        pass


class Pipeline:
    """Pipeline with advanced flow control and async support"""

    def __init__(self) -> None:
        self.stages: Dict[str, PipelineStage[Any, Any]] = {}
        self.default_sequence: List[str] = []
        self.global_conditions: List[Condition] = []
        self.state: Dict[str, Any] = {}
        self.metrics: Dict[str, List[float]] = {}
        self.visualizer = PipelineVisualizer(self)
        self.logger = setup_logger(logger_name=self.__class__.__name__)
        self.logger.info("Initializing new pipeline")
        self._checkpoint_dir = Path(".pipeline_checkpoints")
        self._checkpoint_dir.mkdir(parents=True, exist_ok=True)

    def add_stage(self, name: str, stage: PipelineStage[Any, Any]) -> "Pipeline":
        """Add a stage to the pipeline"""
        self.logger.info("Adding stage: %s", name)
        self.stages[name] = stage
        self.default_sequence.append(name)
        return self

    def add_global_condition(self, condition: Condition) -> "Pipeline":
        """Add a global condition checked before each stage"""
        self.logger.info("Adding global condition: %s", condition.name)
        self.global_conditions.append(condition)
        return self

    async def should_skip_stage(self, stage_name: str, data: Any) -> bool:
        """Check if stage should be skipped based on conditions"""
        self.logger.debug("Checking skip conditions for stage: %s", stage_name)
        stage = self.stages[stage_name]

        # Check global conditions
        for condition in self.global_conditions:
            if await condition.evaluate(data):
                self.logger.info("Global condition triggered skip: %s", condition.name)
                return True

        # Check stage-specific conditions
        for condition in stage.skip_conditions:
            if await condition.evaluate(data):
                self.logger.info("Stage condition triggered skip: %s", condition.name)
                return True

        return False

    async def get_next_stage(self, current_stage: str, data: Any) -> Optional[str]:
        """Determine next stage based on branching conditions"""
        stage = self.stages[current_stage]
        self.logger.debug("Determining next stage after: %s", current_stage)

        # Check branching conditions
        for condition, next_stage in stage.branch_conditions.items():
            if await condition.evaluate(data):
                self.logger.info(
                    "Branch condition triggered: %s -> %s", condition.name, next_stage
                )
                return next_stage

        # Return next stage in default sequence
        try:
            current_index = self.default_sequence.index(current_stage)
            if current_index < len(self.default_sequence) - 1:
                next_stage = self.default_sequence[current_index + 1]
                self.logger.debug("Moving to next stage in sequence: %s", next_stage)
                return next_stage
        except ValueError:
            self.logger.warning(
                "Current stage not found in default sequence: %s", current_stage
            )

        self.logger.debug("No next stage found, pipeline will terminate")
        return None

    async def create_checkpoint(
        self, current_stage: str, current_data: Any, input_data: Any
    ) -> PipelineCheckpoint:
        """Create a checkpoint of the current pipeline state."""
        self.logger.info("Creating pipeline checkpoint at stage: %s", current_stage)

        checkpoint = PipelineCheckpoint(
            current_stage=current_stage,
            stage_states=self.state.copy(),
            execution_path=list(self.visualizer.viz_data.keys()),
            metadata={
                "metrics": self.metrics,
                "visualization": {
                    name: stage_info.model_dump()
                    for name, stage_info in self.visualizer.viz_data.items()
                },
            },
            input_data=input_data,
            current_data=current_data,
        )

        # Save checkpoint to disk
        checkpoint_path = self._checkpoint_dir / f"{checkpoint.checkpoint_id}.json"
        with open(checkpoint_path, "w") as f:
            json.dump(checkpoint.model_dump(), f, indent=2, cls=DateTimeEncoder)

        self.logger.info("Checkpoint saved: %s", checkpoint.checkpoint_id)
        return checkpoint

    async def restore_from_checkpoint(self, checkpoint_id: str) -> Optional[Any]:
        """Restore pipeline state from a checkpoint and continue execution."""
        checkpoint_path = self._checkpoint_dir / f"{checkpoint_id}.json"

        if not checkpoint_path.exists():
            self.logger.error("Checkpoint not found: %s", checkpoint_id)
            return None

        try:
            with open(checkpoint_path, "r") as f:
                checkpoint_data = json.load(f)
                checkpoint = PipelineCheckpoint.model_validate(checkpoint_data)

            self.logger.info("Restoring from checkpoint: %s", checkpoint_id)

            # Restore pipeline state
            self.state = checkpoint.stage_states
            self.metrics = checkpoint.metadata.get("metrics", {})

            # Restore visualization state
            viz_data = checkpoint.metadata.get("visualization", {})
            self.visualizer.viz_data = {
                name: StageVizInfo.model_validate(info)
                for name, info in viz_data.items()
            }

            # Continue pipeline execution from checkpoint
            if checkpoint.current_stage:
                # Process the current stage first
                stage = self.stages[checkpoint.current_stage]
                result = await stage.process(checkpoint.current_data)
                if not result.success:
                    return None

                # Then continue with remaining stages
                next_stage = await self.get_next_stage(
                    checkpoint.current_stage, result.data
                )
                if next_stage:
                    final_result = await self.process(
                        result.data, start_from_stage=next_stage
                    )
                    return final_result.data if final_result.success else None
                return result.data

            return None

        except Exception as e:
            self.logger.error("Failed to restore checkpoint: %s", str(e))
            return None

    async def process(
        self, input_data: Any, start_from_stage: Optional[str] = None
    ) -> StageResult[Any]:
        """Process data through the pipeline with flow control and visualization"""
        self.logger.info("Starting pipeline processing")
        current_data = input_data
        current_stage_name: Optional[str] = start_from_stage or (
            self.default_sequence[0] if self.default_sequence else None
        )
        metadata: Dict[str, Any] = {
            "pipeline_start": datetime.now(),
            "execution_path": [],
            "skipped_stages": [],
        }

        # Initialize visualization for all stages
        if not start_from_stage:
            self.visualizer.reset()  # Only reset if starting fresh
            for stage_name in self.stages:
                self.visualizer.update_stage_status(stage_name, "pending")

        try:
            while current_stage_name:
                self.logger.debug("Processing stage: %s", current_stage_name)

                # Check if we should skip this stage
                if await self.should_skip_stage(current_stage_name, current_data):
                    self.logger.info("Skipping stage: %s", current_stage_name)
                    metadata["skipped_stages"].append(current_stage_name)
                    self.visualizer.update_stage_status(
                        current_stage_name,
                        "skipped",
                        start_time=datetime.now(),
                        end_time=datetime.now(),
                    )
                    current_stage_name = await self.get_next_stage(
                        current_stage_name, current_data
                    )
                    continue

                # Update stage status to running
                self.visualizer.update_stage_status(
                    current_stage_name,
                    "running",
                    start_time=datetime.now(),
                )

                # Process the stage
                stage = self.stages[current_stage_name]
                result = await stage.process(current_data)

                # Store state and update metadata
                if result.success:
                    self.state[current_stage_name] = result.data
                    current_data = (
                        result.data
                    )  # Update current_data with processed result
                metadata["execution_path"].append(current_stage_name)

                # Update visualization based on result
                self.visualizer.update_stage_status(
                    current_stage_name,
                    "failed" if not result.success else "completed",
                    end_time=datetime.now(),
                    error=result.error if not result.success else None,
                    metrics=result.metadata.get("metrics") if result.metadata else None,
                )

                if not result.success:
                    # Create checkpoint on failure for recovery
                    await self.create_checkpoint(
                        current_stage_name, current_data, input_data
                    )
                    self.logger.error("Stage processing failed: %s", current_stage_name)
                    return StageResult(
                        success=False, data=None, error=result.error, metadata=metadata
                    )

                # Apply post-processors
                for processor in stage.post_processors:
                    try:
                        self.logger.debug(
                            "Applying post-processor: %s",
                            getattr(processor, "__name__", str(processor)),
                        )
                        processed_result = processor(result.data)
                        if asyncio.iscoroutine(processed_result):
                            result.data = await processed_result
                        else:
                            result.data = processed_result
                    except Exception as e:
                        self.logger.error("Post-processor failed: %s", str(e))
                        return StageResult(
                            success=False,
                            data=None,
                            error=f"Post-processor failed: {str(e)}",
                        )

                # Handle stage decision
                if result.decision == StageDecision.CONTINUE:
                    # Get next stage in default sequence
                    try:
                        current_index = self.default_sequence.index(current_stage_name)
                        if current_index < len(self.default_sequence) - 1:
                            # Only proceed to next stage if it's in the original sequence
                            next_stage = self.default_sequence[current_index + 1]
                            if next_stage in self.stages:
                                current_stage_name = next_stage
                                continue
                        current_stage_name = None
                    except ValueError:
                        current_stage_name = None
                elif result.decision == StageDecision.SKIP_NEXT:
                    self.logger.info("Skipping next stage as per stage decision")
                    try:
                        current_index = self.default_sequence.index(current_stage_name)
                        if current_index < len(self.default_sequence) - 2:
                            current_stage_name = self.default_sequence[
                                current_index + 2
                            ]
                            self.logger.debug(
                                "Jumping to stage: %s", current_stage_name
                            )
                        else:
                            current_stage_name = None
                    except ValueError:
                        current_stage_name = None
                elif result.decision in (
                    StageDecision.JUMP_TO,
                    StageDecision.BRANCH_TO,
                ):
                    if result.next_stage not in self.stages:
                        error_msg = f"Invalid {result.decision.value} target: {result.next_stage}"
                        self.logger.error(error_msg)
                        return StageResult(success=False, data=None, error=error_msg)

                    self.logger.info(
                        "%s to stage: %s",
                        result.decision.value.title(),
                        result.next_stage,
                    )

                    # Simplified logic for both JUMP_TO and BRANCH_TO
                    current_stage_name = result.next_stage
                    if result.decision == StageDecision.BRANCH_TO:
                        # Process the branched stage and terminate
                        stage = self.stages[current_stage_name]
                        result = await stage.process(result.data)
                        self.state[current_stage_name] = result.data
                        metadata["execution_path"].append(current_stage_name)
                        current_stage_name = None
                    # For JUMP_TO, just update current_stage_name and continue normal flow
                    current_data = result.data
                    continue
                elif result.decision == StageDecision.TERMINATE:
                    self.logger.info("Pipeline terminating as per stage decision")
                    break

                current_data = result.data

            metadata["pipeline_end"] = datetime.now()
            duration = metadata["pipeline_end"] - metadata["pipeline_start"]
            self.logger.info(
                "Pipeline processing completed in %s seconds", duration.total_seconds()
            )
            return StageResult(success=True, data=current_data, metadata=metadata)

        except Exception as e:
            self.logger.error("Pipeline error: %s", str(e), exc_info=True)
            if current_stage_name:
                self.visualizer.update_stage_status(
                    current_stage_name,
                    "failed",
                    end_time=datetime.now(),
                    error=str(e),
                )
            metadata["pipeline_end"] = datetime.now()
            return StageResult(
                success=False,
                data=None,
                error=f"Pipeline error: {str(e)}",
                metadata=metadata,
            )
