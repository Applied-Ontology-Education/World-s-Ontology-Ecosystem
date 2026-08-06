from day4.exercise import ZebraExercise


def run_experiment(exercise: ZebraExercise) -> list[dict]:
    """Execute every experiment declared in exercise.json."""
    results = []
    configuration = exercise.configuration
    print(f"Starting: {configuration.title}", flush=True)
    print(f"Model: {exercise.model_id}", flush=True)

    for experiment in configuration.experiments:
        print(f"\n=== {experiment.name} ===", flush=True)
        print(experiment.learning_question, flush=True)

        for stage in exercise.stages_for(experiment):
            session = exercise.start(experiment, stage)
            hypothesis = session.hypothesize()
            critique = None

            if experiment.use_critic:
                critique = session.criticize(hypothesis)
                while (
                    critique.revision_required
                    and session.revision_count < experiment.max_revisions
                ):
                    hypothesis = session.revise(hypothesis, critique)
                    critique = session.criticize(hypothesis)

            results.append(session.finish(hypothesis, critique))

    exercise.complete()
    return results
