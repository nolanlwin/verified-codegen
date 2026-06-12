This specification defines a function `SlackResponseStyleSpec` that generates a response style for Slack threads, emphasizing brevity and skimmability. The behavior is contingent upon whether the request is from a Slack thread as indicated by the `slack_thread_context` parameter. The `SlackResponseStyle` method serves as the implementation of this specification with an exact match on the defined behavior in its `ensures` clause. The function prioritizes concise responses, discourages lengthy prose, and describes an approach to structure responses in Slack.

Notes from formalizer:
- No explicit description for the focused symbol; inferred from the PR description and code diff.
- The conflict between 'a single sentence for simple questions' and 'when there is actual information to convey, use bullet points' suggests ambiguity in the exact format of responses.
- The description mentions this styling only applies to Slack threads, aligning with the code logic based on `slack_thread_context`; no similar behavior defined for the web.
- Code priorities articulated in the PR description around simplicity and skimming may not be fully encapsulated in the formalization and need explicit mapping.
