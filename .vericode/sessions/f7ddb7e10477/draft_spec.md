This PR introduces a feature in the PostHog Slack app to provide concise responses when replying in Slack threads. A new response style is applied only for Slack threads, offering short, skimmable answers instead of lengthier web app responses. The new behavior is conditionally included based on a context flag indicating a Slack thread. The changes are validated through automated tests ensuring these new responses only appear when appropriate.

Notes from formalizer:
- No description; spec inferred from diff only.
