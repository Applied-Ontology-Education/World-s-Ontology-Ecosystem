from naas_abi_core.engine.Engine import Engine
from naas_abi_core.engine.context import get_default_model_registry

from day4 import ABIModule
from day4.exercise import ZebraExercise, load_exercise_configuration
from day4.workflows.ExercisePlumbing import AgentRuntime, RunArtifacts
from day4.workflows.StudentExerciseWorkflow import run_experiment


def main():
    engine = Engine()
    engine.load()
    registry = get_default_model_registry()
    assert registry is not None, "Model registry is not initialized"

    configuration = load_exercise_configuration()
    artifacts = RunArtifacts(log_filename=configuration.output.csv)
    for model_id in ABIModule.get_instance().configuration.agent_models:
        chat_model = registry.get_chat_model(model_id)
        exercise = ZebraExercise(
            configuration,
            AgentRuntime(chat_model),
            artifacts,
            model_id=model_id,
        )
        run_experiment(exercise)


if __name__ == "__main__":
    main()
