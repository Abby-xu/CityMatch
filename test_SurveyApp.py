# Author: Yibo Wang
# Date: 11/15/2024
# Description: Test functions of SurveyApp
import pytest
from unittest.mock import patch, MagicMock, mock_open
from SurveyApp import SurveyApp

@pytest.fixture
def app():
    """Fixture to provide a SurveyApp instance for testing."""
    return SurveyApp()


def test_local_css(app):
    """Test the local_css method."""
    mock_file_content = "body {color: red;}"
    file_name = "style.css"

    # Mock the open function to return a file-like object with mock_file_content
    with patch("builtins.open", mock_open(read_data=mock_file_content)) as mock_file:
        # Mock the st.markdown function
        with patch("streamlit.markdown") as mock_markdown:
            app.local_css(file_name)

            # Assert the open function was called with the correct file name
            mock_file.assert_called_once_with(file_name)

            # Assert st.markdown was called with the correct formatted content
            mock_markdown.assert_called_once_with(
                '<style>{}</style>'.format(mock_file_content),
                unsafe_allow_html=True
            )

def test_set_background(app):
    with patch("streamlit.markdown") as mock_markdown:
        app.set_background()
        mock_markdown.assert_called_once()

def test_display_header(app):
    with patch("streamlit.title") as mock_title, \
         patch("streamlit.markdown") as mock_markdown, \
         patch("streamlit.image") as mock_image:
        with patch("PIL.Image.open", MagicMock()):
            app.display_header()
            mock_title.assert_called_once_with("City Match")
            mock_markdown.assert_called()
            mock_image.assert_called_once()

def test_get_survey_responses(app):
    with patch("streamlit.markdown"), \
         patch("streamlit.radio", side_effect=["Yes", "No"]), \
         patch("streamlit.selectbox", side_effect=["High", "Medium", "Low", "None"]), \
         patch("streamlit.success"), \
         patch("streamlit.write"):
        app.get_survey_responses()
        assert app.option_list == [1, 0, 3, 2, 1, 0]

def test_show_submit_button(app):
    with patch("streamlit.button", return_value=True), \
         patch("streamlit.progress") as mock_progress, \
         patch("streamlit.spinner"), \
         patch("streamlit.success") as mock_success:
        app.show_submit_button()
        mock_progress.assert_called()
        mock_success.assert_called_once_with("Submitted")

def test_run(app):
    with patch.object(app, "set_background"), \
         patch.object(app, "local_css"), \
         patch.object(app, "display_header"), \
         patch.object(app, "get_survey_responses"), \
         patch.object(app, "show_submit_button"):
        app.run()
        app.set_background.assert_called_once()
        app.local_css.assert_called_once_with("style.css")
        app.display_header.assert_called_once()
        app.get_survey_responses.assert_called_once()
        app.show_submit_button.assert_called_once()
