The `_slack_response_style_prompts` function generates a list of prompts specifically designed for Slack responses, emphasizing conciseness and skimmability compared to web app responses. If the configuration indicates that the request originates from a Slack thread, a specific prompt guiding the format of the response is returned. If not, an empty list is returned.

Notes from formalizer:
- No description; spec inferred from diff only.
- The PR description specifies that the Slack bot should generally provide shorter answers, which is captured in the specification, but the details in the code diff regarding bullet points may need more clarification on quantities and structure.
