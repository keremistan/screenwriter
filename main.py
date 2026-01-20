from typing_extensions import Literal, TypedDict
from langgraph.graph import START, END, StateGraph


def main():
    writer_prompt = """
    Look at state. If it's REVISION_REQUIRED, ignore your previous internal "plan" and prioritize the critiques.
    Find the entry in the critiques array that matches the current target_ref.
    Re-generate only the specific field requested, while maintaining consistency with the non-rejected fields (the "Source of Truth").
    """


def validator_agent():
    """it validates the narrative consistency"""
    pass


def transition_rewriter_agent():
    """rewrites if any dependencies of a content block became STALE"""

    # constrained rewriting, anchored in beat sheet - when scene X should be rewritten because scene X-1 changed, then scene X needs to adjusted while maintaining consistency with scene X-1 and beat sheet.
    #  If that is not possible, emit BLOCKER signal
    #    then the next step is to update the beat sheet

    """
    sample blocker control signal
    {
        status: REWRITING_FAILED,
        issue_severity: BLOCKER,
        feedback: ,
        target_scope: 
    }
    """

    pass


def summarizer_agent():
    """it summarizes for significant events, emotional shifts and open threads. Not for brevity."""

    # todo: how/when to update the state with summaries?
    pass


class ScreenplayState(TypedDict):
    # content
    genre: str
    title: str
    logline: str
    setting: str
    beat_sheet: list[str]

    # writing metadata
    critique_feedback: str
    state: Literal["NOT_STARTED_YET", "IN_DRAFT", "FINISHED"]
    status: Literal[
        "FEEDBACK_REQUIRED",  # writing_agent has finished
        "REVISION_REQUIRED",  # critique_agent wants improvement
        "APPROVED",  # critique_agent approved
    ]
    phase: Literal[
        "GENRE",  # starting phase
        "TITLE",
        "LOGLINE",
        "SETTING",
        "BEAT_SHEET",
    ]


def orchestrator_agent():
    """when a phase is finished, human approval is needed to commence to the next phase"""
    # receive new draft
    #  validate json format
    #  lint-check static information; names, etc.
    #  pass to validator for narrative consistency check
    #  pass to critique agent for narrative quality check
    pass


def critique_agent(state: ScreenplayState):
    """it critiques the narrative quality"""

    """
    transitioning between phases:
    1. there can be a list phases and every time, this agent signals 'APPROVED' orchestrator can move to the next phase.
    """

    pass


def writer_agent(state: ScreenplayState):
    # submit new draft
    pass


if __name__ == "__main__":
    graph = StateGraph(Screenplay)

    graph.add_node("orchestrator_agent", orchestrator_agent)
    graph.add_node("critique_agent", critique_agent)
    graph.add_node("writer_agent", writer_agent)

    graph.add_edge(START, "orchestrator_agent")
    graph.add_edge("orchestrator_agent", END)
