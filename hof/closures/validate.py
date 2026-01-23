# THE TOOL FACTORY
def rule(predicate, error_message):
    """
    I don't validate data. 
    I manufacture a function that validates data.
    """
    def validator(value):
        if not predicate(value):
            raise ValueError(error_message)
        return value
    return validator

# MANUFACTURING NEW TOOLS
# These are not results; they are new FUNCTIONS created at runtime.
must_be_long = rule(lambda x: len(x) >= 3, "Too short")
must_be_adult = rule(lambda x: x >= 18, "Too young")
must_be_email = rule(lambda x: "@" in x, "Invalid email")

# USING THE TOOLS
must_be_long("Jo")  # Raises ValueError: Too short
