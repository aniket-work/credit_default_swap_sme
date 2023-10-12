from model_add import LlamaCPPInvocationLayer

def initialize_model():
    """
    Initializes the PromptModel for answering questions.

    Returns:
        PromptModel: Initialized PromptModel.
    """
    return PromptModel(
        model_name_or_path="model/mistral-7b-instruct-v0.1.Q4_K_S.gguf",
        invocation_layer_class=LlamaCPPInvocationLayer,
        use_gpu=False,
        max_length=1000
    )
