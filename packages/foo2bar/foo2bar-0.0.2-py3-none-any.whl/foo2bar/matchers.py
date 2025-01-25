"""
This module describes which statements we would like to isolate before replacing them.

The global_statement_matcher is a matcher that matches all global statements that contain an assignment.
Out of these statements, we are interested in the first occurence of a variable name in a given scope.
From this first occurence, we would like to save the name of the variable, the type of the variable if it is explicitly annotated, and the value assigned to the variable.
In addition, we would like to save the trailing line comment associated with the assignment.

However, if the trailing line comment contains the phrase "no param", the full statement will be ignored.
"""

import re
from libcst import matchers as m, metadata
from .providers import FirstAssignInScopeProvider

assign_name = m.Name(
    # Save the name of the variable
    value=m.SaveMatchedNode(m.DoNotCare(), "name"),
    # We care only about first occurence of a variable name in a given scope
    metadata=m.MatchMetadata(FirstAssignInScopeProvider, True),
)

# Save the type of the variable when explicitly annotated
assign_type = m.Annotation(annotation=m.SaveMatchedNode(m.DoNotCare(), "annotation"))

# Save the value node assigned to the variable to replace it later
assign_value = m.SaveMatchedNode(m.DoNotCare(), "value")

# A comment containing "no param" should not be saved
no_param = m.MatchRegex(re.compile(r".*no param.*", re.IGNORECASE))
# Save the comment if it does not contain "no param"
comment = m.Comment(value=m.SaveMatchedNode(m.DoesNotMatch(no_param), "comment"))
# If no comment is present, save None
no_comment = m.SaveMatchedNode(None, "comment")

# Match an assignment statement, be it annotated or not
assign_matcher = m.Assign(
    targets=[m.AssignTarget(target=assign_name)], value=assign_value
)
ann_assign_matcher = m.AnnAssign(
    target=assign_name, annotation=assign_type, value=assign_value
)

statement_matcher = m.SimpleStatementLine(
    body=[m.OneOf(assign_matcher, ann_assign_matcher)],
    trailing_whitespace=m.OneOf(
        m.TrailingWhitespace(comment=comment),
        m.TrailingWhitespace(comment=no_comment),
    ),
)

def _test():
    import libcst as cst
    from pathlib import Path
    from node_converter import resolve_scope_name
    code = cst.parse_module(Path("test_data/test_script.py").read_text())
    wrapper = metadata.MetadataWrapper(code)
    matches = m.extractall(wrapper, statement_matcher)
    print([type(m["scope"]) for m in matches])
    
    
if __name__ == "__main__":
    _test()