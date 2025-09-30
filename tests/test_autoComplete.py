from playwright.sync_api import Page
from pages.autocomplete_page import AutoComplete

def test_default_functionality(page: Page):
    run = AutoComplete(page)
    run.load_page("https://jqueryui.com/autocomplete/#default")
    run.default_functionality()