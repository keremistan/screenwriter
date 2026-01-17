def main():
    writer_prompt = """
    Look at state. If it's REVISION_REQUIRED, ignore your previous internal "plan" and prioritize the critiques.
    Find the entry in the critiques array that matches the current target_ref.
    Re-generate only the specific field requested, while maintaining consistency with the non-rejected fields (the "Source of Truth").
    """

def orchestrator_agent():
    '''when a phase is finished, human approval is needed to commence to the next phase'''
    # receive new draft
    #  validate json format
    #  lint-check static information; names, etc.
    #  pass to validator for narrative consistency check
    #  pass to critique agent for narrative quality check
    pass

def validator_agent():
    '''it validates the narrative consistency'''
    pass

def critique_agent():
    '''it critiques the narrative quality'''
    pass

def writer_agent():
    # submit new draft
    pass

def transition_rewriter_agent():
    '''rewrites if any dependencies of a content block became STALE'''
    pass

def summarizer_agent():
    '''it summarizes for significant events, emotional shifts and open threads. Not for brevity.'''

    # todo: how/when to update the state with summaries?
    pass


if __name__ == "__main__":
    main()
