function SlackResponseStylePrompts(has_slack_thread_context: bool): seq<string>
  decreases
{
  if has_slack_thread_context then
    ["slack_response_style"]
  else
    []
}

method SlackResponseStylePromptsMethod(has_slack_thread_context: bool) returns (result: seq<string>)
  requires true
  ensures result == SlackResponseStylePrompts(has_slack_thread_context)
{
  if has_slack_thread_context {
    result := ["slack_response_style"];
  } else {
    result := [];
  }
}
