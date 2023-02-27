import pytest
from unittest.mock import patch
from ppt_nlp import backend
import openai

@pytest.fixture
def mock_openai():
    with patch.object(openai, "Completion") as mock_completion:
        yield mock_completion

def test_summarization(mock_openai):
    # Mock the OpenAI API response
    mock_openai.create.return_value = {
        "choices": [{"text": "This is the summarization."}]
    }

    # Call the function and check the output
    question = "What is the meaning of life?"
    expected_summarization = "This is the summarization."
    assert backend.summarization(question) == expected_summarization

    # Check that the OpenAI API was called with the correct prompt
    mock_openai.create.assert_called_with(
        prompt="What is the meaning of life?'tl;dr:",
        temperature=0,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        model="text-davinci-002",
    )

def test_summarization_error(mock_openai):
    # Mock an error from the OpenAI API
    mock_openai.create.side_effect = openai.ErrorObject("API connection error")

    # Call the function and check that it returns None
    question = "What is the meaning of life?"
    assert backend.summarization(question) == None