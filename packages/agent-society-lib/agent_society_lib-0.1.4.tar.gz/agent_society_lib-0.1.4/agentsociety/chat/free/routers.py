from agentsociety.chat.intent.intent_router import IntentRouter, CategoricalIntentContext
from enum import Enum


class YesNoForCompletion(Enum):
    Yes = 1
    No = 2


yes_no_refinement_completion_examples = {
    YesNoForCompletion.Yes: ["Yes", "I am done", "Yes I am done gathering information", "Yes the step is complete", "Yes this is enough", "Done", "It's done", "Complete"],
    YesNoForCompletion.No: ["No", "no" "It's not done yet", "Not complete", "Not enough information", "I need more time", "I want to keep on interviewing"]
}

YES_NO_COMPLETION_ROUTER = None

def get_yes_no_completion_router() -> IntentRouter:
    global YES_NO_COMPLETION_ROUTER

    if YES_NO_COMPLETION_ROUTER is None:
        context = CategoricalIntentContext(YesNoForCompletion, yes_no_refinement_completion_examples)
        YES_NO_COMPLETION_ROUTER = IntentRouter(context, top_n=1)
    return YES_NO_COMPLETION_ROUTER


class SimplificationCheckResult(Enum):
    Ok = 1
    ReSimplify = 2
    ReDraft = 3

simplification_check_result_examples = {
    SimplificationCheckResult.Ok: ["Ok", "Looks good", "The simplification looks good", "Okay", "Everything okay"],
    SimplificationCheckResult.ReDraft: ["re-draft", "re draft", "start over with drafting", "draft again"],
    SimplificationCheckResult.ReSimplify: ["re-simplify", "re simplify", "start over with simplification", "simplify again"]
}

SIMPLIFICATION_CHECK_RESULTS = None

def get_simplification_check_results_router() -> IntentRouter:
    global SIMPLIFICATION_CHECK_RESULTS

    if SIMPLIFICATION_CHECK_RESULTS is None:
        context = CategoricalIntentContext(SimplificationCheckResult, simplification_check_result_examples)
        SIMPLIFICATION_CHECK_RESULTS = IntentRouter(context)
    return SIMPLIFICATION_CHECK_RESULTS


class FormalizationFailedChoices(Enum):
    ReFormalize = 1
    ReSimplify = 2
    ReDraft = 3


formalization_failed_choices_examples = {
    FormalizationFailedChoices.ReDraft: ["Restart with drafting", "re-draft", "start over with drafting", "draft", "draft again", "Draft the MILP again"],
    FormalizationFailedChoices.ReSimplify: ["Re-simplify", "Restart simplification", "start over with simplification", "simplify", "simplify again", "Simplify the MILP again"],
    FormalizationFailedChoices.ReFormalize: ["try-again", "re-formalize", "try formalization again", "formalize", "Formalize the MILP again"]
}

FORMALIZATION_FAULT_CHOICES_ROUTER = None

def get_formalization_fault_choices_router() -> IntentRouter:
    global FORMALIZATION_FAULT_CHOICES_ROUTER

    if FORMALIZATION_FAULT_CHOICES_ROUTER is None:
        context = CategoricalIntentContext(FormalizationFailedChoices, formalization_failed_choices_examples)
        FORMALIZATION_FAULT_CHOICES_ROUTER = IntentRouter(context)
    return FORMALIZATION_FAULT_CHOICES_ROUTER


class TestCaseDraftChecker(Enum):
    restart = 1
    ok = 2


test_case_draft_exmaples = {
    TestCaseDraftChecker.restart: ["restart", "restart writing test case", "restart drafting"],
    TestCaseDraftChecker.ok: ["ok", "proceed", "test case okay", "okay"]
}

TEST_CASE_DRAFT_CHECKER = None

def get_test_case_draft_router() -> IntentRouter:
    global TEST_CASE_DRAFT_CHECKER
    if TEST_CASE_DRAFT_CHECKER is None:
        context = CategoricalIntentContext(TestCaseDraftChecker, test_case_draft_exmaples)
        TEST_CASE_DRAFT_CHECKER = IntentRouter(context, top_n=1)
    return TEST_CASE_DRAFT_CHECKER
