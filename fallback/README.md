# Fallback: review a supplied candidate

Use this route if Copilot is unavailable or access troubleshooting takes more than five minutes. You can also switch here after an interrupted agent attempt. Preserve any useful earlier evidence and explain where you switched.

This is supplied course material, not output from your own agent session. Label your source **Supplied candidate**. The same rubric and maximum score apply.

## Proposed plan

1. Find the target and reject a cancelled target.
2. Validate the destination.
3. Check destination conflicts using the existing helper.
4. Update the target in place and return it.
5. Run the supplied checks.

Read `candidate_move.py` as a proposed change to `service.py`. Review the plan before copying the function. Compare the resulting file with your baseline. Investigate the requirements and add the two student checks required by IA 3.2. Correct problems manually, or use AI later if access returns. Explain a concrete decision to retain or revise part of this candidate.

Do not assume that supplied code is correct or that passing three smoke checks covers SPEC.md. No fabricated prompt, transcript or agent approval is required for this route.
