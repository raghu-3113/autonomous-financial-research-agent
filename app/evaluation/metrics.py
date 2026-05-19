def calculate_tool_count(observations):

    return len(observations)


def calculate_observation_coverage(observations):

    filled = 0

    for obs in observations:

        if obs["output"]:

            filled += 1

    if len(observations) == 0:

        return 0

    return round(
        (filled / len(observations)) * 100,
        2
    )


def calculate_response_length(response):

    return len(response.split())


def calculate_verification_status(
    verification_text
):

    verification_text = verification_text.lower()

    # Strong negative checks
    if (
        "unsupported claims identified"
        in verification_text
    ):

        return "Warning"

    elif (
        "hallucinations detected"
        in verification_text
    ):

        return "Risk"

    # Positive checks
    elif (
        "no unsupported claims"
        in verification_text
        and
        "no hallucinations"
        in verification_text
    ):

        return "Passed"

    else:

        return "Passed"
    
def calculate_tool_success_rate(
    observations
):

    if len(observations) == 0:

        return 0

    success_count = 0

    for obs in observations:

        if obs.get("status") == "success":

            success_count += 1

    return round(
        (success_count / len(observations)) * 100,
        2
    )