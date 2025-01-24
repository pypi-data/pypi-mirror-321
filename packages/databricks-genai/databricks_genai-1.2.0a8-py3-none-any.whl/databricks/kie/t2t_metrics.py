"""Implementation of task specific Text2Text metrics."""

from typing import Callable, List

from databricks.agents.evals import metric
from mlflow.evaluation import Assessment
from mlflow.metrics import MetricValue, bleu, rougeL

from databricks.kie.eval_utils import PrimitiveTypes, fuzzy_match, normalized_match  # pylint: disable=ungrouped-imports
from databricks.kie.t2t_schema import InstructionType
from databricks.kie.text_utils import normalize_text

CLASSIFICATION_MATCH_NAME = "classification_match"
FUZZY_MATCH_WITH_TARGET_NAME = "fuzzy_match_with_target"
TOKENS_OVERLAP_WITH_TARGET_NAME = "tokens_overlap_percentage_with_target"
ROUGE_L_SCORE_WITH_TARGET_NAME = "rouge_L_score_with_target"
BLEU_SCORE_WITH_TARGET_NAME = "bleu_score_with_target"

# CLASSIFICATION METRICS


def is_classification_match(request: PrimitiveTypes, prediction: PrimitiveTypes, target: PrimitiveTypes) -> Assessment:
    """Normalized (+ exact) matching check between prediction and target."""
    if type(prediction) != type(target):  # pylint: disable=unidiomatic-typecheck
        return Assessment(name=CLASSIFICATION_MATCH_NAME,
                          value=False,
                          rationale="Prediction and target are not the same type")

    # request is unused in this metric, but needs to be passed in
    match_assessment: Assessment = normalized_match(request, prediction, target)
    return Assessment(name=CLASSIFICATION_MATCH_NAME,
                      value=match_assessment.value,
                      rationale=match_assessment.rationale)


# SUB-SPAN EXTRACTION METRICS


def fuzzy_match_score_with_target(request: PrimitiveTypes, prediction: PrimitiveTypes,
                                  target: PrimitiveTypes) -> Assessment:
    """Fuzzy string matching check between prediction and target."""
    if type(prediction) != type(target):  # pylint: disable=unidiomatic-typecheck
        return Assessment(name=FUZZY_MATCH_WITH_TARGET_NAME,
                          value=False,
                          rationale="Prediction and target are not the same type")

    # request is unused in this metric, but needs to be passed in
    match_assessment: Assessment = fuzzy_match(request, prediction, target)
    return Assessment(name=FUZZY_MATCH_WITH_TARGET_NAME,
                      value=match_assessment.value,
                      rationale=match_assessment.rationale)


def token_overlap_percentage_with_target(
        request: PrimitiveTypes,  # pylint: disable=unused-argument
        prediction: PrimitiveTypes,
        target: PrimitiveTypes) -> Assessment:
    """Token overlap check between prediction and target. Best for keyword extraction."""
    if not isinstance(prediction, str) or not isinstance(target, str):
        return Assessment(name=TOKENS_OVERLAP_WITH_TARGET_NAME,
                          value=0.0,
                          rationale="Prediction and target are not strings")

    prediction_tokens = normalize_text(prediction).split()
    target_tokens = normalize_text(target).split()
    overlap = len(set(prediction_tokens) & set(target_tokens)) / len(set(prediction_tokens))
    return Assessment(name=TOKENS_OVERLAP_WITH_TARGET_NAME,
                      value=int(overlap * 100),
                      rationale=f"{int(overlap * 100)}% of tokens in prediction overlap with the target")


def rouge_l_score_with_target(
        request: PrimitiveTypes,  # pylint: disable=unused-argument
        prediction: PrimitiveTypes,
        target: PrimitiveTypes) -> Assessment:
    """RougeL score check between prediction and target."""

    if not isinstance(prediction, str) or not isinstance(target, str):
        return Assessment(name=ROUGE_L_SCORE_WITH_TARGET_NAME,
                          value=0.0,
                          rationale="Prediction and/or target are not strings")
    prediction = normalize_text(prediction)
    target = normalize_text(target)
    rouge_calc: MetricValue = rougeL().eval_fn([prediction], [target])
    rouge_score = rouge_calc.scores[0]
    return Assessment(name=ROUGE_L_SCORE_WITH_TARGET_NAME, value=rouge_score, rationale=f"Rouge L score: {rouge_score}")


# SUMMARIZATION METRICS


def bleu_score_with_target(request: PrimitiveTypes, prediction: PrimitiveTypes, target: PrimitiveTypes) -> Assessment:  # pylint: disable=unused-argument
    """We use BLEU to calculate the score for the prediction and target."""
    if not isinstance(prediction, str) or not isinstance(target, str):
        return Assessment(name=BLEU_SCORE_WITH_TARGET_NAME,
                          value=0.0,
                          rationale="Prediction and/or target are not strings")
    if len(prediction.split()) < 4 or len(target.split()) < 4:
        return Assessment(
            name=BLEU_SCORE_WITH_TARGET_NAME,
            value=0.0,
            rationale="Prediction and/or target have less than 4 tokens, which isn't enough to calculate a BLEU score")
    prediction = normalize_text(prediction)
    target = normalize_text(target)
    blue_calc: MetricValue = bleu().eval_fn([prediction], [target])
    bleu_score = blue_calc.scores[0]
    return Assessment(name=BLEU_SCORE_WITH_TARGET_NAME,
                      value=bleu_score,
                      rationale=f"Bleu score with prediction and target: {bleu_score}")


# METRIC CREATION


def create_metric(fn: Callable[[PrimitiveTypes, PrimitiveTypes, PrimitiveTypes], float], name: str):
    """Helper function to create an mlflow metric."""

    @metric(name=name)
    def wrapper(request, response, expected_response):
        return fn(request, response, expected_response)

    return wrapper


CLASSIC_METRICS = {
    InstructionType.classification: [create_metric(is_classification_match, CLASSIFICATION_MATCH_NAME)],
    InstructionType.subspan_extraction: [
        create_metric(fuzzy_match_score_with_target, FUZZY_MATCH_WITH_TARGET_NAME),
        create_metric(token_overlap_percentage_with_target, TOKENS_OVERLAP_WITH_TARGET_NAME),
        create_metric(rouge_l_score_with_target, ROUGE_L_SCORE_WITH_TARGET_NAME),
    ],
    InstructionType.summarization: [
        create_metric(rouge_l_score_with_target, ROUGE_L_SCORE_WITH_TARGET_NAME),
        create_metric(bleu_score_with_target, BLEU_SCORE_WITH_TARGET_NAME),
    ],
}


def create_classic_metrics(task_type: InstructionType) -> List[metric]:
    """Create an mlflow metric given a task type."""
    return CLASSIC_METRICS.get(task_type, [])
