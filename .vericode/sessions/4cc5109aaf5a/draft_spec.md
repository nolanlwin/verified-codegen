This specification defines the expected behavior for generating Slack response style prompts based on the context in which a request originates. If the request comes from a Slack thread, the method should return a specific set of prompts that guide a concise response format. Instead, if the request does not come from a Slack thread, an empty list is returned. The method depends on the context indicated by the `slack_thread_context` attribute from the configuration. This approach separates Slack-specific responses from the general web app responses, as per user feedback, which highlighted the need for brevity in Slack interactions.

Notes from formalizer:
- The method and function names were updated to avoid starting with an underscore, which is not permitted in Dafny.
- All postconditions are appropriately placed on the method only, complying with Dafny rules.
- Clarified the functionality of the prompt to ensure it aligns with the provided intent in the PR description.
