episodic_memory = []

def store_episode(query, observations, final_response):

    episode = {

        "query": query,

        "observations": observations,

        "final_response": final_response
    }

    episodic_memory.append(episode)


def get_memory():

    return episodic_memory